import sys
import requests
import json

# run it as: python find_address.py ${CEP}

if __name__ == "__main__":
    address = requests.get("https://cep.awesomeapi.com.br/json/" + sys.argv[1])
    address = address.json()
    print()
    print("  The information for the given CEP (" + sys.argv[1] + "):")
    print("_________________________________________")
    print("|             |")
    print("| CEP         | ", address['cep'])
    print("| Address     | ", address['address'])
    print("| City        | ", address['city'])
    print("| District    | ", address['district'])
    print("|_____________|__________________________")
    print()
