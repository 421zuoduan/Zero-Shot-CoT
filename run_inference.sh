model="gpt3.5-turbo"
dataset="multiarith"
python main.py --method=zero_shot_cot --model=${model} --dataset=${dataset}