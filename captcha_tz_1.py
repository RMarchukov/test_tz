from random import randint


class Captcha1:

    def get_true_res(self):
        a = randint(0, 9)
        b = randint(0, 9)
        true_res = a + b
        return {"a": a, "b": b, "true_res": true_res}


test = Captcha1()
data = test.get_true_res()
print(data)
text = f"{data['a']} + {data['b']} some text"
print(text)
answer = int(input("Enter yor answer: "))
if answer == data["true_res"]:
    print("good")
else:
    print("kick")
