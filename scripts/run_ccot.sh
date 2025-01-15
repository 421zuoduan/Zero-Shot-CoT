model="gpt3.5-turbo"
dataset="gsm8k"
# dataset="multiarith"
python ccot.py --method=contrast_cot --model=${model} --dataset=${dataset}