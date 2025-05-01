import pandas as pd

for year in [18,19,20,21,22]:
    for letter in ["A","B","C","D","E","F"]:
        file = f"<MODEL_NAME>/20{year}/{year+94}-{letter}_own.jsonl"
        df = pd.read_json(file, orient='records', lines=True,dtype={"problem_id":str})
        # df["prediction"] = df["prediction"].apply(lambda x: x.replace("<|im_start|>system\n医師国家試験を解きます｡<|im_end|>\n<|im_start|>user\n問題: ﾋﾄｹﾞﾉﾑ･遺伝子解析研究の被験者に対する説明で必須でないのはどれか｡\na: 研究の目的\nb: 同意の自由\nc: 匿名化の方法\nd: 参加による不利益\ne: 研究成果還元の保証\n必ずa,b,c,d,eの中からちょうど1個選んでください｡\n答え:<|im_end|>\n<|im_start|>assistant\ne<|im_end|>\n<|im_start|>user\n問題: 57歳の男性｡下水処理場のﾏﾝﾎｰﾙ内で汚泥を外に搬出する作業を行っていたが､突然意識を失って倒れた｡さらに救助しようとして中に入った同僚も急激に意識を失って倒れた｡可能性が高いのはどれか｡2つ選べ｡\na: 酸素欠乏症\nb: 硫化水素中毒\nc: 一酸化炭素中毒\nd: 二酸化炭素中毒\ne: 二酸化窒素中毒\n必ずa,b,c,d,eの中からちょうど2個選んでください｡\n答え:<|im_end|>\n<|im_start|>assistant\na,b<|im_end|>\n<|im_start|>user\n問題: 28歳の女性｡妊娠30週｡子宮底長は22cmで､腹部超音波検査で羊水はほとんど認めない｡胎児で最も考えられるのはどれか｡\na: 食道閉鎖\nb: 心室中隔欠損\nc: 腎低形成\nd: 鎖肛\ne: 胎児水腫\n必ずa,b,c,d,eの中からちょうど1個選んでください｡\n答え:<|im_end|>\n<|im_start|>assistant\nc<|im_end|>\n","").split("assistant")[1].strip())
        # df["prediction"] = df["prediction"].apply(lambda x: x.split("<|im_end|>")[0].strip())

        def f(x):
            x = x.replace(",\n","")
            if "\n" in x:
                x = x.split("\n")
                if len(x) == 1:
                    return x.split(":")[0]
                else:
                    res = []
                    for item in x:
                        res.append(item.split(":")[0])
                    return ",".join(res)
            else:
                return x
            return x.split(".")[0]
        
        #Apply necessary postprocessing
        df["prediction"] = df["prediction"].apply(f)
        df["prediction"] = df["prediction"].apply(lambda x: x.split(":")[0])
        df["prediction"] = df["prediction"].apply(lambda x: x.replace(" ",""))
        # df["prediction"] = df["prediction"].apply(lambda x: x.split("<|end_of_text|>")[0])
        # df["prediction"] = df["prediction"].apply(lambda x: x.split("\n")[0])
        # df["prediction"] = df["prediction"].apply(lambda x: x.split(" ")[0])
        # if letter == "E":
        #     df["problem_id"] = pd.read_json(file.replace("own","gpt4"), orient='records', lines=True,dtype={"problem_id":str})["problem_id"]

        df["explanation"] = df["prediction"] #explanationカラムはAccuracy評価のためには不要.
        df.to_json(file, orient='records', force_ascii=False, lines=True)