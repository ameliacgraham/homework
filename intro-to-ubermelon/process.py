log_file = open("um-server-01.txt")

# Takes in a file
def sales_reports(log_file):
    # loops over each line in the file
    for line in log_file:
        # takes off whitespace character
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print line


sales_reports(log_file)
