import csv
import os
month = 0
total = 0
prevProfitLoss = 0
TotalChangeProfitorLoss = 0
maxTotal = 0
maxMonth = ""
minMonth = ""
minTotal = 0
minTotal = 0
csvFilename = os.path.join("Resources","budget_data.csv")
with open(csvFilename) as BudgetData:
    data = csv.reader(BudgetData,delimiter=",")
    next(data)
    for eachrow in data:
        Month = eachrow[0]
        month = month + 1
        ProfitorLoss = int(eachrow[1])
        monthProfitorLoss = ProfitorLoss - prevProfitLoss
        TotalChangeProfitorLoss = TotalChangeProfitorLoss + int(monthProfitorLoss)
        avgProfitLoss = TotalChangeProfitorLoss/month
        if monthProfitorLoss > maxTotal:
            maxTotal = monthProfitorLoss
            maxMonth = Month
        if monthProfitorLoss < minTotal:
            minTotal = monthProfitorLoss
            minMonth = Month
        prevProfitLoss = ProfitorLoss
        total = ProfitorLoss + total
print("Financial Analysis")
print("----------------------------")
print("Total Months:", month)
print("Total: $",total)
print("Average Change: $",avgProfitLoss)
print("Greatest Increase in Profits: {} (${}) ".format(maxMonth, maxTotal))
print("Greatest Decrease in Profits: {} (${}) ".format(minMonth, minTotal))

with open('profit_or_loss_analysis.txt', 'w') as textOutFile:
    textOutFile.write("Financial Analysis\n")
    textOutFile.write("----------------------------\n")
    textOutFile.write("Total Months: {}\n".format( month))
    textOutFile.write("Total: ${}\n".format(total))
    textOutFile.write("Average Change: ${}\n".format(avgProfitLoss))
    textOutFile.write("Greatest Increase in Profits: {} (${})\n".format(maxMonth, maxTotal))
    textOutFile.write("Greatest Decrease in Profits: {} (${})\n".format(minMonth, minTotal))