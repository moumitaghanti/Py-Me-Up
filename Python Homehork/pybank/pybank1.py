
# Modules
import os
import csv

filename = os.path.join( "budget_data.csv")
output_file= os.path.join( "budget_data_out.csv")
header = [] 

rows = [] 
total = 0
cnt = 0
change = 0
total_change=0
profit_loss = []
date_rev =[]
maxrev = 0
minrev = 0

with open(filename, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader) 
    for row in csvreader:
        cnt = cnt+1
        total = total + float(row[1])
        #urrent_rev = float(row[1])
        profit_loss.append(row[1])
        date_rev.append(row[0])
         
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:   "+str(cnt))
    print("Total  :  $"+ str(round(total)))


    
    # determing the average change in revenue by checking the list
    for i in range(0,(cnt-1)):
        
        change = float(float(profit_loss[i+1])-float(profit_loss[i]))
        current_rev = change
        total_change = total_change + change
        if current_rev > maxrev:
            maxrev = current_rev
            date_max = i+1

        if current_rev < minrev:
            minrev = current_rev
            date_min = i+1  
    average_revenue_change = float(total_change/(cnt-1))
    print("the average change:  $"+ str(round(float(total_change/(cnt-1)),2)) )  
    #print("max rev:  "+str(maxrev))
    #print("min rev:  "+str(minrev))
#print("date max rev:  "+ date_rev[date_max])
#print("date min  rev:  "+ date_rev[date_min])    
print("Greatest Increase in Profits:"+date_rev[date_max]+" ($"+str(round(maxrev))+")")  
print("Greatest Increase in Profits:"+date_rev[date_min]+" ($"+str(round(minrev))+")")      

# printing in file
with open(output_file, 'w') as filewriter:
    filewriter.write(f"Financial Analysis:\n")
    filewriter.write("-------------------------------------------------------\n")
    filewriter.write(f"Total Months: {cnt}\n")
    filewriter.write(f"Total Revenue: {round(total)} USD\n")
    filewriter.write(f"Average Revenue Change: {round(average_revenue_change,2)} USD\n")
    filewriter.write(f"Greatest Increase in Revenue: {date_rev[date_max]} ({round(maxrev)} USD)\n")
    filewriter.write(f"Greatest Decrease in Revenue: {date_rev[date_min]} ({round(minrev)} USD)\n")
    filewriter.write("")

    filewriter.close()    