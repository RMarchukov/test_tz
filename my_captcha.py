from random import randint
from captcha.image import ImageCaptcha


captcha_length = 5


class Captcha:
    captcha_text = ""
    captcha_image = 0

    def __init__(self):
        image = ImageCaptcha(width=280, height=90)
        self.captcha_text = self.generate_captcha_text()
        self.captcha_image = image.generate(self.captcha_text)

    def generate_captcha_text(self):
        numbers = []
        for i in range(captcha_length):
            numbers.append(str(randint(0, 9)))
        self.captcha_text = "".join(numbers)
        return self.captcha_text

    def change_captcha(self):
        self.captcha_text = ""
        self.generate_captcha_text()
        return self.captcha_text
