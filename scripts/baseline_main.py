from utils.tools import read_jsonl, answer2jsonl, check_jsonls
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def main(in_file, config="own", prompt_file="prompts/prompt.jsonl", out_dir="../baseline_results/", model_id=None):
    questions = read_jsonl(in_file)
    prompt = read_jsonl(prompt_file)
    scores = None
    if config == "own":
        from generation.own import run_own 
        answers, outputs = run_own(model_id, questions, prompt=prompt)
    elif config == "chatgpt":
        from generation.chatgpt import run_chatgpt
        answers, outputs = run_chatgpt(questions, prompt=prompt)
    elif config == "chatgpt-en":
        from generation.chatgpt_en import run_chatgpt_en
        answers, outputs = run_chatgpt_en(questions, prompt=prompt)
    elif config == "gpt3":
        from generation.gpt3 import run_gpt3
        answers, outputs = run_gpt3(questions, prompt=prompt)
    elif config == "gpt4":
        from generation.chatgpt import run_chatgpt
        answers, outputs = run_chatgpt(questions, prompt=prompt, model="gpt-4")
    elif config == "gpt4o":
        from generation.chatgpt import run_chatgpt
        answers, outputs = run_chatgpt(questions, prompt=prompt, model="gpt-4o")
    elif config == "student-majority":
        from generation.student import run_student
        meta_data = read_jsonl(in_file.replace('.jsonl', '_metadata.jsonl'))
        answers, outputs = run_student(questions, meta_data)
    out_file = os.path.basename(in_file).replace('.jsonl', '')
    out_file = out_file + "_" + config + ".jsonl"
    out_file = os.path.join(out_dir, out_file)
    
    answer2jsonl(answers, outputs, questions, out_file)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(allow_abbrev=False)

    parser.add_argument('--in-file', type=str, metavar='N',
                        default='../data/2022/116-A.jsonl', help='input jsonl file')
    parser.add_argument('--config', type=str, metavar='N',
                        choices=["chatgpt", "chatgpt-en", "gpt3", "gpt4", "gpt4o", "student-majority","own"],
                        default='own', help='baseline configuration')
    parser.add_argument('--out-dir', type=str, metavar='N',
                        default='../baseline_results/', help='baseline results output')
    parser.add_argument('--prompt-file', type=str, metavar='N',
                        default='prompts/prompt.jsonl', help='prompt file')
    parser.add_argument('--model-id', type=str, metavar='N',
                        default=None, help='prompt file')
    args = parser.parse_args()
    main(args.in_file, args.config, args.prompt_file, args.out_dir, args.model_id)
