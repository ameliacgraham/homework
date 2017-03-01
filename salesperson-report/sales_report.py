"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

# salespeople = []
# melons_sold = []

# f = open("sales-report.txt")
# for line in f:
#     # remove trailing whitespace
#     line = line.rstrip()
#     entries = line.split("|")
#     # salesperson is the data that is at the 0 index for each line
#     salesperson = entries[0]
#     # melons is the data that is at the 2nd index for each line
#     melons = int(entries[2])

#     if salesperson in salespeople:

#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)

# # instead of saving to empty lists, it would be better to add the salespeople
# # to a dictionary


# for i in range(len(salespeople)):
#     print "{} sold {} melons".format(salespeople[i], melons_sold[i])


def sales_by_salesperson(filename):
    opened_file = open(filename)
    sales_by_salespeople = {}
    for line in opened_file:
        entries = line.rstrip().split("|")
        salesperson = entries[0]
        melons_sold = int(entries[2])
        if salesperson not in sales_by_salespeople.keys():
            sales_by_salespeople[salesperson] = {"melons sold": melons_sold}
        else:
            sales_by_salespeople[salesperson]["melons sold"] += melons_sold




        # sales_by_salespeople[salesperson] = {"melons sold": melons_sold}
    return sales_by_salespeople


def print_sales_by_person(sales_by_salespeople):
    for person in sales_by_salespeople:
        print "{} sold {} melons".format(person, sales_by_salespeople[person]["melons sold"])

get_sales = sales_by_salesperson("sales-report.txt")
print_sales_by_person(get_sales)

