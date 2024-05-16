import csv
import os


count = 0
election_result = {}
winner_count = 0
winner_name = ""
csvFilename = os.path.join("Resources","election_data.csv")
with open(csvFilename) as PollData:
    data = csv.reader(PollData,delimiter=",")
    next(PollData)
    for eachRow in data:
        count = count + 1
        candidate_name = eachRow[2]
        if candidate_name not in election_result:
            election_result[candidate_name] = 1
        else:
            election_result[candidate_name] = election_result[candidate_name] + 1

print("Election Results")
print("-------------------------")
print("Total Votes: {}".format(count))
print("-------------------------")
for name in election_result.keys():
    print("{}: {:.3%} ({})".format(name,election_result[name]/count, election_result[name]))
    if election_result[name] > winner_count:
        winner_name = name
        winner_count = election_result[name]

print("-------------------------")
print("Winner: {}".format(winner_name))
print("-------------------------")


with open('election_result_analysis.txt', 'w') as textOutFile:
    textOutFile.write("Election Results Analysis\n")
    textOutFile.write("-------------------------\n")
    textOutFile.write("Total Votes: {}\n".format(count))
    textOutFile.write("-------------------------\n")
    for name in election_result.keys():
        textOutFile.write("{}: {:.3%} ({})\n".format(name,election_result[name]/count, election_result[name]))
    textOutFile.write("-------------------------\n")
    textOutFile.write("Winner: {}\n".format(winner_name))
    textOutFile.write("-------------------------\n")