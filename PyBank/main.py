# Will need to import the CSV function so can call functions to read file
# Need to import the CSV file that needs to be analyzed. Make sure have pathway correct
# Have to total the number of months being analyzed
# Calculate the total revenue in column 2 (if excel file)
# Will need to have formula take current month revenue - last month revenue to get change per month
    # will then need to average all change per months 
# Will need to use a max function to identify greatest increase in change per months
    # Must return date and amount
# Will need to use a min function to identify greatest decrease in change per months
    # Must return date and amount
# To finish export answers to a text file.     

# Import Dependencies. 
import csv
import os

months = []
total_revenue = 0
revenue = []
rev_chg = []

# Import and read the CSV File.
csvPath = os.path.join("..", "PyBank", "budget_data.csv")

with open(csvPath, "r", newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")

# Skip the header.
    next(csvReader)

# Identifies the months and revenue in the csv file. Then uses len to return number of elements for months and then sums total revenue.    
    for row in csvReader:
        months.append(row[0])
        revenue.append(int(row[1]))
        total_months = len(months)   # returns the number of elements in the list
        total_revenue += int(row[1])     
        
# Compares current month and prior month to get change. Then calculate average change and identify max and min.
    for i in range(1,len(revenue)):
        
        rev_chg.append(revenue[i] - revenue[i - 1])
        avg_rev_chg = sum(rev_chg)/total_months

        max_rev_chg = max(rev_chg)

        min_rev_chg = min(rev_chg)

        max_rev_chg_date = str(months[rev_chg.index(max(rev_chg))])
        min_rev_chg_date = str(months[rev_chg.index(min(rev_chg))])

# Print results in terminal.
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Change: ${round(avg_rev_chg)}")
print(f"Greatest Increase in Profits: {max_rev_chg_date} (${round(max_rev_chg)})")
print(f"Greatest Decrease in Profits: {min_rev_chg_date} (${round(min_rev_chg)})")

# Display resutls in a txt file. 
txtPath = os.path.join("..", "PyBank", "budget_data.txt")

with open(txtPath,"w") as txtfile:
    txtfile.writelines(f"Financial Analysis" + "\n")
    txtfile.writelines(f"----------------------------" +"\n")
    txtfile.writelines(f"Total Months: {total_months}" + "\n")
    txtfile.writelines(f"Total Revenue: ${total_revenue}" + "\n")
    txtfile.writelines(f"Average Change: ${round(avg_rev_chg)}" + "\n")
    txtfile.writelines(f"Greatest Increase in Profits: {max_rev_chg_date} (${round(max_rev_chg)})" + "\n")
    txtfile.writelines(f"Greatest Decrease in Profits: {min_rev_chg_date} (${round(min_rev_chg)})")









   



