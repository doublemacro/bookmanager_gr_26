"""
Creati o clasa cu numele
Item

Care are urmatoarele atribute:
content, de tipul string
count, de tipul integer
warehouse, care este initial None, si cand un warehouse apeleaza add_item(item), acest atribut warehouse primeste valoare, referinta catre warehouse.

Si clasa Warehouse, care are urmatoarele atribute:
location, de tipul string,
items, de tipul lista, [], o lista de iteme.
Warehouse are si o metoda:
add_item(item), cand este apelata aceasta metoda, se adauga acel item in lista de items a clasei
De ex:
item1 = Item("flowers", 30)
warehouse1 = Warehouse()
warehouse1.add_item(item1)
In acea metoda add_item, luati acel item, si setati proprietatea item.warehouse = self, ca sa faceti o legatura intre un item si un warehouse.
Creati metodele de __str__ pentru warehouse si Item, sa reflecte pentru warehouse, care sunt itemele din el, si pentru un item, acel __str__ sa printeze, de exemplu:
"Item that contains 'flowers', currently in warehouse 'wearhouse object here'
"""

class Item:
    def __init__(self, content: str, count: int):
        self.content = content
        self.count = count
        self.warehouse = None

    def __str__(self):
        return f"Item that contains '{self.content}', currently in warehouse '{self.warehouse}'"

    def __repr__(self):
        return f"Item('{self.content}', {self.count})"


class Warehouse:
    def __init__(self, location: str):
        self.location = location
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)
        item.warehouse = self

    def __str__(self):
        return f"Warehouse at location: {self.location}, with items: {self.items}"

item1 = Item('Content for item 1', 30)
item2 = Item('content for item 2', 15)
warehouse1 = Warehouse('Romania')
warehouse1.add_item(item1)
warehouse1.add_item(item2)
# print(warehouse1)


arr = ["mar", "para", "kiwi"]
var1 = ", ".join([f"{item.content}, {item.warehouse.location}" for item in warehouse1.items]) # -> "mar, para, kiwi"

print(var1)
var2 = [Item('Content for item 1', 30), Item('content for item 2', 15)]


