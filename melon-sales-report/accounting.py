SALESPERSON_INDEX = 0
INTERNET_INDEX = 1
DORKY_LINE_LENGTH = 80

def count_melons():
    file = open("orders-by-type.txt")
    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

    for line in file:
        data = line.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count
    file.close()
    return melon_tallies

def total_revenue(melon_tallies):
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        # print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)
        print "We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(melon_tallies[melon_type], melon_type, price, revenue)

def get_sales_generated():
    file = open("orders-with-sales.txt")
    sales = [0, 0]
    for line in file:
        items = line.split("|")
        if items[1] == "0":
            sales[0] += float(items[3])
        else:
            sales[1] += float(items[3])
    print "Salespeople generated ${:.2f} in revenue.".format(sales[1])
    print "Internet sales generated ${:.2f} in revenue.".format(sales[0])
    if sales[1] > sales[0]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"
    file.close()

print "*" * DORKY_LINE_LENGTH
melon_tallies = count_melons()
total_revenue(melon_tallies)
print "*" * DORKY_LINE_LENGTH
get_sales_generated()
print "*" * DORKY_LINE_LENGTH

