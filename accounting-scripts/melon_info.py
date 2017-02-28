"""
Prints out all the melons in our inventory
"""

from melons import melon_attributes

def print_melon(melons_info):
    for melon, attributes in melon_attributes.items():
        print melon.upper()
        for attributes, price in attributes.items():
            print "{}: {}".format(attributes, price)
        print


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])


print_melon("melons.py")
