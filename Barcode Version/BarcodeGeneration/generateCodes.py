import barcode
from barcode.writer import ImageWriter

products = [
    ('Bread', '072945601345'),
    ('Milk', '070360002372'),
    ('Baked Beans', '039400015925'),
    ('Pasta', '076808001495')
]

def genFilename(name):
    return name + '.png'

def generateBarcode(item):
    name = item[0]
    number = item[1]
    tag = genFilename(name)

    UPC = barcode.get_barcode_class('upc')
    upc = UPC(number, writer=ImageWriter())

    upc.save(tag)


# Generate codes
for item in products:
    generateBarcode(item)