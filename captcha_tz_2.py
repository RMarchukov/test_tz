class Captcha2:
    binance = "https://accounts.binance.com/ru/register?ref=18502050"
    tg_channel = "@LampMarket"
    user = "Roma"
    rules = "url"

    def get_true_res(self):
        text = f'Привет, {self.user}! У нас не задают глупые вопросы, ответы на которые можно элементарно нагуглить.' \
               'Но задают и обсуждают любые другие вопросы о майнинге.😉 Также обрати внимание на шапку группы, ' \
               'там много' \
               'различных полезных ссылок и информации для майнеров.Рекомендуемая криптобиржа️' \
               f'{self.binance} - возможно лучшая криптобиржа на данный момент. Много разных монет, действительно ' \
               f'маленькие комиссии,' \
               'голосование за добавление новых монет, конкурсы и т.д. Рекомендуем, сами там торгуем.👍 ' \
               'Другие биржи, боты, полезные сервисы и проверенных партнёров смотрите в шапке группы. Объявления о' \
               'купле/продаже в группе запрещены. Для публикации такого у нас есть отдельный канал.'
        button1 = self.rules
        button2 = "good"
        return {"text": text, "button1": button1, "button2": button2}


test = Captcha2()
data = test.get_true_res()
print(data)
text = data['text']
print(text)
answer = int(input("Turn 1(button1) or 2(button2): "))
if answer == 1:
    print(data['button1'])
elif answer == 2:
    print(data['button2'])
