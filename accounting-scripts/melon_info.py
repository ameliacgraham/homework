"""
Prints out all the melons in our inventory
"""

from melons import melon_attributes

def print_melon(melons_file):
    for melon, attributes in melon_attributes.items():
        print melon.upper()
        for attributes, value in attributes.items():
            print "{}: {}".format(attributes, value)
        print

print_melon("melons.py")
