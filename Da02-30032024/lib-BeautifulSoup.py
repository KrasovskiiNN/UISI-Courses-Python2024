# pip install bs4
# pip freeze

import requests
import bs4

result = ''

x = requests.get("https://mainfin.ru/currency/cb-rf/usd")
b = bs4.BeautifulSoup(x.text, 'html.parser')

courseValue = b.select('.current-course__value')

for a in courseValue:
    x = (a.getText().strip())
    result = result + x + "\n\n"
print('Курс доллара', x)

##########

result = ''

x = requests.get("https://www.anekdot.ru/")
b = bs4.BeautifulSoup(x.text, 'html.parser')

anekdotText = b.select('.text')

for a in anekdotText:
    text = (a.getText().strip())
    result = result + text + "\n\n"
print('Анекдот: ', result)