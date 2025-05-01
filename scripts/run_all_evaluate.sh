MODEL_NAME=<MODEL_NAME>
MODEL_ID=<ORGANIZATION>/<MODEL_NAME>
OUT_DIR=baseline_results/${MODEL_NAME}

# #Inference
mkdir ${OUT_DIR}
mkdir ${OUT_DIR}/2018
mkdir ${OUT_DIR}/2019
mkdir ${OUT_DIR}/2020
mkdir ${OUT_DIR}/2021
mkdir ${OUT_DIR}/2022
cd scripts
python baseline_main.py --in-file ../data/2018/112-A.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2018/112-B.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2018/112-C.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2018/112-D.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2018/112-E.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2018/112-F.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2019/113-A.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2019/113-B.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2019/113-C.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2019/113-D.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2019/113-E.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2019/113-F.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2020/114-A.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2020/114-B.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2020/114-C.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2020/114-D.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2020/114-E.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2020/114-F.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2021/115-A.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2021/115-B.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2021/115-C.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2021/115-D.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2021/115-E.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2021/115-F.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2022/116-A.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2022/116-B.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2022/116-C.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2022/116-D.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2022/116-E.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
python baseline_main.py --in-file ../data/2022/116-F.jsonl --out-dir ../${OUT_DIR} --model-id ${MODEL_ID}
cd ..

mv ${OUT_DIR}/112-*_own.jsonl ${OUT_DIR}/2018
mv ${OUT_DIR}/113-*_own.jsonl ${OUT_DIR}/2019
mv ${OUT_DIR}/114-*_own.jsonl ${OUT_DIR}/2020
mv ${OUT_DIR}/115-*_own.jsonl ${OUT_DIR}/2021
mv ${OUT_DIR}/116-*_own.jsonl ${OUT_DIR}/2022

# Modification
#Do it manualy

#Evaluation
cd scripts
python evaluate_main.py --gold-file ../data/2018/112-A.jsonl  --pred-file ../${OUT_DIR}/2018/112-A_own.jsonl
python evaluate_main.py --gold-file ../data/2018/112-B.jsonl  --pred-file ../${OUT_DIR}/2018/112-B_own.jsonl
python evaluate_main.py --gold-file ../data/2018/112-C.jsonl  --pred-file ../${OUT_DIR}/2018/112-C_own.jsonl
python evaluate_main.py --gold-file ../data/2018/112-D.jsonl  --pred-file ../${OUT_DIR}/2018/112-D_own.jsonl
python evaluate_main.py --gold-file ../data/2018/112-E.jsonl  --pred-file ../${OUT_DIR}/2018/112-E_own.jsonl
python evaluate_main.py --gold-file ../data/2018/112-F.jsonl  --pred-file ../${OUT_DIR}/2018/112-F_own.jsonl

python evaluate_main.py --gold-file ../data/2019/113-A.jsonl  --pred-file ../${OUT_DIR}/2019/113-A_own.jsonl
python evaluate_main.py --gold-file ../data/2019/113-B.jsonl  --pred-file ../${OUT_DIR}/2019/113-B_own.jsonl
python evaluate_main.py --gold-file ../data/2019/113-C.jsonl  --pred-file ../${OUT_DIR}/2019/113-C_own.jsonl
python evaluate_main.py --gold-file ../data/2019/113-D.jsonl  --pred-file ../${OUT_DIR}/2019/113-D_own.jsonl
python evaluate_main.py --gold-file ../data/2019/113-E.jsonl  --pred-file ../${OUT_DIR}/2019/113-E_own.jsonl
python evaluate_main.py --gold-file ../data/2019/113-F.jsonl  --pred-file ../${OUT_DIR}/2019/113-F_own.jsonl

python evaluate_main.py --gold-file ../data/2020/114-A.jsonl  --pred-file ../${OUT_DIR}/2020/114-A_own.jsonl
python evaluate_main.py --gold-file ../data/2020/114-B.jsonl  --pred-file ../${OUT_DIR}/2020/114-B_own.jsonl
python evaluate_main.py --gold-file ../data/2020/114-C.jsonl  --pred-file ../${OUT_DIR}/2020/114-C_own.jsonl
python evaluate_main.py --gold-file ../data/2020/114-D.jsonl  --pred-file ../${OUT_DIR}/2020/114-D_own.jsonl
python evaluate_main.py --gold-file ../data/2020/114-E.jsonl  --pred-file ../${OUT_DIR}/2020/114-E_own.jsonl
python evaluate_main.py --gold-file ../data/2020/114-F.jsonl  --pred-file ../${OUT_DIR}/2020/114-F_own.jsonl

python evaluate_main.py --gold-file ../data/2021/115-A.jsonl  --pred-file ../${OUT_DIR}/2021/115-A_own.jsonl
python evaluate_main.py --gold-file ../data/2021/115-B.jsonl  --pred-file ../${OUT_DIR}/2021/115-B_own.jsonl
python evaluate_main.py --gold-file ../data/2021/115-C.jsonl  --pred-file ../${OUT_DIR}/2021/115-C_own.jsonl
python evaluate_main.py --gold-file ../data/2021/115-D.jsonl  --pred-file ../${OUT_DIR}/2021/115-D_own.jsonl
python evaluate_main.py --gold-file ../data/2021/115-E.jsonl  --pred-file ../${OUT_DIR}/2021/115-E_own.jsonl
python evaluate_main.py --gold-file ../data/2021/115-F.jsonl  --pred-file ../${OUT_DIR}/2021/115-F_own.jsonl

python evaluate_main.py --gold-file ../data/2022/116-A.jsonl  --pred-file ../${OUT_DIR}/2022/116-A_own.jsonl
python evaluate_main.py --gold-file ../data/2022/116-B.jsonl  --pred-file ../${OUT_DIR}/2022/116-B_own.jsonl
python evaluate_main.py --gold-file ../data/2022/116-C.jsonl  --pred-file ../${OUT_DIR}/2022/116-C_own.jsonl
python evaluate_main.py --gold-file ../data/2022/116-D.jsonl  --pred-file ../${OUT_DIR}/2022/116-D_own.jsonl
python evaluate_main.py --gold-file ../data/2022/116-E.jsonl  --pred-file ../${OUT_DIR}/2022/116-E_own.jsonl
python evaluate_main.py --gold-file ../data/2022/116-F.jsonl  --pred-file ../${OUT_DIR}/2022/116-F_own.jsonl
