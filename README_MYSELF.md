# Code

安装环境

```
conda create --name ccot python=3.9
conda activate ccot
pip install torch==1.8.2+cu111 torchtext==0.9.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
pip install -r requirements.txt
pip install openai==1.7.0
pip install httpx==0.27.2
```

导入OPENAI_API_KEY

```
export OPENAI_API_KEY=...
```

运行程序

```
bash scripts/run_ccot.sh
```