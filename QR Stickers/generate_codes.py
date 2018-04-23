import pyqrcode

"""
Generates QR codes based on a list of item names and prices.
QR Codes saved to current directory as png files.
"""

"""
List of items.
Enter items to be turned into QR Codes here.
Format as [name, price]
"""
items = [['Bread', 1.50],
         ['Milk', 3.00],
         ['Pasta', 2.00],
         ['Cheese', 3.59],
         ['Juice', 4.49]
         ]

"""
Turns a number (int or float) to a price string. 
"""
def price2str(price):
    return '$' + str(price)

""" 
Turns an item into a formatted tag.
Item formatted as [Name, Price].
Returns tag formatted as <name>Name<\name><price>price<\price>
"""
def item2tag(item):
    name = item[0]
    price = item[1]
    tag = '<name>' + name + '<\name>' + '<price>' + price2str(price) + '<\price>'
    return tag

"""
Generates a filename based on an item.
Filename formatted as name.png
"""
def genFilename(item):
    name = item[0]
    return name + '.png'

# Write items to QR Codes.
for item in items:
    tag = item2tag(item) # Write tag
    filename = genFilename(item) # Generate filename

    qrCode = pyqrcode.create(tag)  # Create QR Code
    qrCode.png(filename, scale = 6) # Save to png file