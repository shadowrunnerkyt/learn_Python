from json import dumps, loads
from os import system

try:
    import colorama
    from colorama import Fore,Back,Style
    colorama.init(autoreset=True)
except ImportError:
    pass

products = []

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = round(price,2)
    def to_dict(self):
        return {"name": self.name, "price": self.price}

def clear():
    system('clear')

def load_products():
    products_file = open("products.json","r+")
    products_json = products_file.read()
    #products_json = open("products.json","r").read()
    product_data = loads(products_json)
    for product in product_data:
        products.append(Product(product['name'], product['price']))
    products_file.close()
    return products

def add_product(name, price):
    new_product = Product(name, price)
    products.append(new_product)
    clear()
    
def list_products(products):
    for p in products:
        print("Product ({0:10}) : Price: ${1:.2f}".format(p.name, p.price))

def save_products(products):
    product_save_list = []
    for product in products:
        product_save_list.append(product.to_dict())
    products_file = open("products.json","w+")
    products_file.write(dumps(product_save_list))
    products_file.close()

clear()
products = load_products()

while True:
    print(Fore.RED + "----------" + Fore.RESET + "\nType '" + Fore.GREEN + "add" + Fore.RESET + "' to add a product")
    print("Type '" + Fore.GREEN + "quit" + Fore.RESET + "' to quit the program")
    print("Type '" + Fore.GREEN + "list" + Fore.RESET + "' to list all the products")
    command = input('Type a command: ')
    if command == "quit":
        save_products(products)
        clear()
        break

    if command == "add":
        product_name = str(input("Enter a name for your product: "))
        product_price = float(input("Enter a price for your new product: "))
        add_product(product_name, product_price)

    if command == "list":
        clear()
        list_products(products)
