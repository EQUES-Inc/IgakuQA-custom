# IgakuQA-Custom / ローカルLLM用のIgakuQA

本リポジトリは、経済産業省及びNEDOによる生成AI開発力強化プロジェクト「GENIAC」により支援を受けた成果の一部である。

This work is based on results obtained from GENIAC (Generative AI Accelerator Challenge, a project to strengthen Japan’s generative AI development capabilities), a project implemented by the Ministry of Economy, Trade and Industry (METI) and the New Energy and Industrial Technology Development Organization (NEDO).


## 概要
商用モデルを対象として開発されたIgakuQAを, ローカルLLMの性能評価用にカスタマイズしたコードです.  

詳細な解説は(株)EQUESのテックブログ記事を参照ください.　　
[ローカルLLM用IgakuQAのアレンジ](https://zenn.dev/eques/articles/09ee047e54e5bb)

## IgakuQAからの主な変更点
- scripts/generation以下にown.pyを作成
- `bash scripts/run_all_evaluate.sh`などで以下を実行できるようにしました. 中身は以下の4ステップです.
    1. 推論を実行し, `11*-*_own.jsonl`に結果を保存.
    2. ファイル群を移動
    3. (optional) `baseline_results/modify.py`で余白とか余分なスペースとか諸々を綺麗にします.
    4. `scripts/evaluate_main.py`を用い, exact match(3-shot)で正解率を算出します.

## 環境構築
Singularityを利用するのが簡便です.
```
singularity build --fakeroot basic.sif basic.def
singularity shell --nv basic.sif
```

## 実行方法
1. `scripts/run_all_evaluate.sh` 中の設定を指定する.
2. `bash scripts/run_all_evaluate.sh` を実行する.

## 謝辞
このリポジトリは[IgakuQA](https://github.com/jungokasai/IgakuQA)のカスタマイズ版です.  
本家IgakuQAのREADMEは`README_IgakuQA_original.md`を参照ください. 

## その他

ローカルLLMの評価結果は以下の論文を参照ください。
```
Coming soon...
```

Please also consider citing IgakuQA.
```
@misc{jpn-med-exam_gpt4,
  author    = {Jungo Kasai and Yuhei Kasai and Keisuke Sakaguchi and Yutaro Yamada and Dragomir Radev},
  title     = {Evaluating {GPT}-4 and {ChatGPT} on {J}apanese Medical Licensing Examinations},
  year      = {2023},
  url       = {https://arxiv.org/abs/2303.18027},
}
```