# The txt file is supplying all the melon delivery data for the sales reports function below
#log_file is storing the data to a variable so Python can access it from the variable, using it's open function
log_file = open("um-server-01.txt")

# Functions in python are defined using def, keyword, and a paramater with a colon
# the for-in statement accesses the lines in the txt file (stored in log_file)
# rstrip() removes white space to return only the data with no whitespace attached to data
# day stores each weekday information which is accessed by changing the if statement to reflect
# the desired day, in this case, "Tue" becomes "Mon" since that is what we want to print
def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


sales_reports(log_file)
