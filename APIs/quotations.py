import requests
import json

quotations = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL")

quotations = quotations.json()
dollar_quotation = quotations['USD']['bid']
euro_quotation = quotations['EUR']['bid']

print()
print("  Hello, World!")
print("  Hello, APIs!")
print("  This is one of my first codes in python and the first time I use an API")
print("  The goal of this program is to print the quotation of a few currencys in BRL")
print()
print("*--------------------|--------------|---------*")
print("| Currency           | *** to BRL   |   $$$   |")
print("|--------------------|--------------|---------|")
print("| Dollar quotation   | USD to BRL   |", dollar_quotation, " |")
print("|--------------------|--------------|---------|")
print("| Euro quotation     | EUR to BRL   |", euro_quotation, " |")
print("|____________________|______________|_________|")
