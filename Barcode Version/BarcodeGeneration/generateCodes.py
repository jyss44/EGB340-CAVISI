import barcode
from barcode.writer import ImageWriter

products = [
    ('Bread', '0614074001629'),
    ('Milk', '0815473010377'),
    ('Baked Beans', '0692991705059'),
    ('Pasta', '0085164000011'),
    ('Juice', '0048500001745'),
    ('Cheese', '0046100000915')
]

def genFilename(name):
    return name

def generateBarcode(item):
    name = item[0]
    number = item[1]
    tag = genFilename(name)

    UPC = barcode.get_barcode_class('EAN13')
    upc = UPC(number, writer=ImageWriter())

    upc.save(tag)


# Generate codes
for item in products:
    generateBarcode(item)