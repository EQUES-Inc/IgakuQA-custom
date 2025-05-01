import openai, string, mojimoji
openai.api_key = ""
import string, time
from utils.tools import check_jsonls
import threading
import pdb
import torch
from vllm import LLM, SamplingParams

from transformers import AutoTokenizer, AutoModelForCausalLM
import os
import wandb
from huggingface_hub import login
login()

def run_own(model_id,questions, prompt=None):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    llm = LLM(
        model=model_id,
        tensor_parallel_size=1,
        gpu_memory_utilization=0.9,
        max_model_len=8192
    )

    preds = []
    outputs = []
    for q_idx in range(len(questions)):
        question = questions[q_idx]
        print(question['problem_id'])
        chatgpt_input = create_input(prompt, question)
        print(chatgpt_input)
        # [{'role': 'system', 'content': '医師国家試験を解きます。'}, {'role': 'user', 'content': '問題: ヒトゲノム・遺伝子解析研究の被験者に対する説明で必須でないのはどれか。\na: 研究の目的\nb: 同意の自由\nc: 匿名化の方法\nd: 参加による不利益\ne: 研究成果還元の保証\n必ずa,b,c,d,eの中からちょうど1個選んでください。\n答え:'}, {'role': 'assistant', 'content': 'e'}, {'role': 'user', 'content': '問題: 57歳の男性。下水処理場のマンホール内で汚泥を外に搬出する作業を行っていたが、突然意識を失って倒れた。さらに救助しようとして中に入った同僚も急激に意識を失って倒れた。可能性が高いのはどれか。2つ選べ。\na: 酸素欠乏症\nb: 硫化水素中毒\nc: 一酸化炭素中毒\nd: 二酸化炭素中毒\ne: 二酸化窒素中毒\n必ずa,b,c,d,eの中からちょうど2個選んでください。\n答え:'}, {'role': 'assistant', 'content': 'a,b'}, {'role': 'user', 'content': '問題: 28歳の女性。妊娠30週。子宮底長は22cmで、腹部超音波検査で羊水はほとんど認めない。胎児で最も考えられるのはどれか。\na: 食道閉鎖\nb: 心室中隔欠損\nc: 腎低形成\nd: 鎖肛\ne: 胎児水腫\n必ずa,b,c,d,eの中からちょうど1個選んでください。\n答え:'}, {'role': 'assistant', 'content': 'c'}, {'role': 'user', 'content': '問題: 睡眠時無呼吸症候群による高血圧について、正しくないのはどれか。\na: 夜間高血圧となることが多い。\nb: 肥満患者では減量を推奨する。\nc: α遮断薬が第一選択薬である。\nd: 家庭血圧では早朝に高血圧となることが多い。\ne: 持続的気道陽圧法〈CPAP〉で降圧が期待される。\n必ずa,b,c,d,eの中からちょうど1個選んでください。\n答え:'}]
        done = False
        nb_trials = 0
        
        while not done:
            answer = own_problem(llm,tokenizer,chatgpt_input)
            if answer is None:
                done = False
                print('\nfailed')
            else:
                done = True
            
            if nb_trials == 3:
                explanation = 'NA'
                answer = 'NA'
                break
        preds.append(answer)
        outputs.append(answer)
    return preds, outputs

def create_input(prompt, question):
    # messages = [{"role": "system", "content": "医師国家試験を解きます。"}]
    messages = []
    for example in prompt:
        messages.extend(dict2problem(example))
    messages.extend(dict2problem(question, False))
    return messages

def dict2problem(dict_input, demo=True):
    problem = "問題: " + dict_input['problem_text']
    choices = dict_input['choices']
    answer = dict_input['answer']
    if len(choices) > 0:
        for choice, label in zip(choices, string.ascii_lowercase):
            problem = problem + '\n' + label + ': ' + choice
        problem = problem + "\n必ずa,b,c,d,eの中からちょうど{}個選んでください。".format(len(answer))
        problem = problem + "\n答え:"
    output = [{"role": "user", "content": problem}]
    if not demo:
        return output
    output.append({"role": "assistant", "content": ",".join(answer)})
    return output

def own_problem(llm,tokenizer,messages):
    sampling_params = SamplingParams(
        temperature=0.1, top_p=0.9, max_tokens=128, stop="<|eot_id|>"
    )
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    output = llm.generate(prompt, sampling_params)       
    answer = output[0].outputs[0].text
    pred = mojimoji.zen_to_han(answer).lower()
    return pred
