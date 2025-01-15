model="gpt3.5-turbo"
dataset="gsm8k"
# dataset="multiarith"
python ccot_basedon_auto.py --method=contrast_cot --model=${model} --dataset=${dataset}