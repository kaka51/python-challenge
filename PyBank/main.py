import os 
import csv 
pybank_csv = os.path.join("/Users/jiaminli/Documents/DataBootCamp/Week3/python-challenge/PyBank", "Resources", "budget_data.csv")
#pybank_csv = "PyBank/Resources/budget_data.csv"

with open(pybank_csv, "r") as read: 
    pybank_read = csv.reader(read, delimiter = ",")
    #print(pybank_read) # won't print anything. 
    csv_header = next(read)
    #print(f"Header: {csv_header}")
    #for row in pybank_read:
    #    print(row)

    
    month = []
    net = []
    for row in pybank_read: 
        # to calculate month
        month.append(row[0])
        total_months = len(month)
        # to calculate profit and loss 
        net.append(int(row[1]))
        total_net = sum(net)

    # to calculate averge change 
    change = []
    for x in range(1, len(net)):
        change.append(((net[x])-(net[x-1])))
    change_average = round(sum(change) / len(change),2)
    # to calculate the greatest value & month
    greatest_increase = max(change)
    greatest_decrease = min(change)
    increase_month = month[change.index(max(change))+1]
    decrease_month = month[change.index(min(change))+1]

    # print in terminal 
    print("Financial Analysis")  
    print("----------------------------") 
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(total_net))
    print("Average Change: "+ "$" + str(change_average))
    print("Greatest Increase in Profits: " + str(increase_month) + " " + "(" + "$" + str(greatest_increase)+")")
    print("Greatest Decrease in Profits: " + str(decrease_month) + " "+ "(" + "$" + str(greatest_decrease)+")")
   
    # print in txt
    f = open("pybank.txt", "w")
    f.write("Financial Analysis"+ "\n")  
    f.write("----------------------------"+ "\n") 
    f.write("Total Months: " + str(total_months)+ "\n")
    f.write("Total: " + "$" + str(total_net)+ "\n")
    f.write("Average Change: "+ "$" + str(change_average)+ "\n")
    f.write("Greatest Increase in Profits: " + str(increase_month) + " " + "(" + "$" + str(greatest_increase)+")"+ "\n")
    f.write("Greatest Decrease in Profits: " + str(decrease_month) + " "+ "(" + "$" + str(greatest_decrease)+")"+ "\n")



    #print(total_months)
    #print(total_net)
    #print(round(change_average,2))
    #print(greatest_increase)
    #print(greatest_decrease)
    #print (increase_month)
    #print (decrease_month)

  
 
   