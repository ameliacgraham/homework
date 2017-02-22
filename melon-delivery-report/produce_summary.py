day_summaries = ["um-deliveries-20140519.txt", "um-deliveries-20140520.txt", "um-deliveries-20140521.txt"]

def melon_summary(list_of_summaries):
    count = 1
    for day_summary in list_of_summaries:
        new_file = open(day_summary)
        print "Day %i" % (count)
        count += 1
        for line in new_file:
            line = line.rstrip()
            words = line.split('|')

            melon_name = words[0]
            melon_count = words[1]
            amount = words[2]
            print "Delivered {} {} for total of ${}".format(melon_count, melon_name, amount)
    new_file.close()

melon_summary(day_summaries)