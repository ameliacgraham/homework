melon_cost = 1.00

def read_customer_info(file, melon_cost):
    """
    Input: file, output: underpaying customers
    """
    new_file = open(file)
    for line in new_file:
        line = line.rstrip()
        
        words = line.split('|')
        customer_name = words[1]
        customer_melons = int(words[2])
        customer_paid = float(words[3])
        # calculates how much the customer should have paid
        customer_expected = (customer_melons * melon_cost)
        if customer_expected > customer_paid:
            print customer_name, "paid {}, expected {}".format(customer_paid, customer_expected)

read_customer_info("customer-orders.txt", melon_cost)
