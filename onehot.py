import torch
import common

def text2Vec(text):
    # 4列62行
    vec = torch.zeros(common.captcha_size, len(common.captcha_array))
    for i in range(len(text)):
        vec[i, common.captcha_array.index(text[i])] = 1
    return vec

def vec2Text(vec):
    vec = torch.argmax(vec, dim=1)
    text = ""
    for i in vec:
        text += common.captcha_array[i]
    return text

if __name__ == "__main__":
    vec = text2Vec("1GKS")
    text = vec2Text(vec)
    print(text)
    print(vec)
