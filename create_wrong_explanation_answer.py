import spacy
import random

# 加载模型
nlp = spacy.load("en_core_web_lg")

# 输入文本
# text = "Shawn started with 5 toys. If he got 2 toys each from his mom and dad, then that is 4 more toys. 5 + 4 = 9."
# text = "There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29."
# text = "Michael started with 58 golf balls. After losing 58 - 23 = 35 on tuesday, he had 58 - 35 = 23. After losing 2 more, he had 23 - 2 = 21 golf balls."
text = "Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. So she has 23 - 15 dollars left. 23 - 15 is 8."

# 处理文本
doc = nlp(text)

# 提取对象片段（数字、方程、人物）
objects = []
for ent in doc.ents:
    if ent.label_ in ["CARDINAL", "PERSON", "DATE"]:  # 提取数字、人物等
        objects.append(ent.text)
for token in doc:
    if token.text in ["+", "-", "*", "/", "="]:  # 提取方程符号
        if token.i > 0 and token.i < len(doc) - 1:
            equation = f"{doc[token.i - 1].text} {token.text} {doc[token.i + 1].text}"
            objects.append(equation)

# 随机打乱对象片段
random.shuffle(objects)

# 构建不连贯桥梁对象的推理
shuffled_text = text
for obj in objects:
    shuffled_text = shuffled_text.replace(obj, "___", 1)  # 用占位符替换对象

# 输出结果
print("原始文本:", text)
print("提取的对象片段:", objects)
print("打乱后的文本:", shuffled_text)