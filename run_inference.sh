model="gpt3.5-turbo"
# dataset="multiarith"
dataset="aqua"
python main.py --method=zero_shot_cot --model=${model} --dataset=${dataset}