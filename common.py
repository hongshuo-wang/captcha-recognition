import random
import string
import time
import os

from captcha.image import ImageCaptcha, random_color
from createCaptcha import valid_code
from config import MyConfig

captcha_array = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
captcha_size = 4
#path = "datasets/validate/"
# path = "datasets/train/"
# path = "datasets/test/"
# path = MyConfig.DATASETS_TRAIN.value
path = MyConfig.DATASETS_TEST.value
# path = MyConfig.DATASETS_VALIDATE.value


img = ImageCaptcha()          #实例化ImageCaptcha类
number = 100 

if __name__ == "__main__":
    for i in range(number):
        if not os.path.exists(path):
            os.makedirs(path)
        # 彩色验证码生成
        # valid_str, image = valid_code()
        # image_path = path + valid_str + "_" + str(int(time.time())) + ".png"
        # image.save(image_path)

        # 纯色验证码生成
        captcha_text = "".join(random.sample(captcha_array, captcha_size))  #随机字符，固定数量 
        image_path = path + captcha_text + "_" + str(int(time.time())) + ".png"
        img.write(captcha_text, image_path)
        print(i)
