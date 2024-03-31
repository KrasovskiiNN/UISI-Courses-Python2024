import requests, bs4, random

result = ''

x = requests.get("https://www.anekdot.ru/")
b = bs4.BeautifulSoup(x.text, 'html.parser')

anekdotText = b.select('.text')

jokes = [a.getText().strip() for a in anekdotText]

random_joke = random.choice(jokes)

print('Анекдот: ', random_joke)