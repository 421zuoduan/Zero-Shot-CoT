model="gpt3.5-turbo"
# dataset="multiarith"
dataset="gsm8k"
python zero_cot.py --method=zero_shot_cot --model=${model} --dataset=${dataset}