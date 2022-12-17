import os 
import csv 

pypoll_csv = os.path.join("/Users/jiaminli/Documents/DataBootCamp/Week3/python-challenge/PyPoll", "Resources","election_data.csv")

with open(pypoll_csv, "r") as read: 
    pypoll_read = csv.reader(read, delimiter = ",")
    csv_header = next(read)
    # for row in pypoll_read: 
    #     print(row)

# define variable 
    vote = []
    candidate = []
    diana = 0 
    charles = 0
    raymon = 0
    winner = ""

 
    for row in pypoll_read: 
    # find total vote 
        vote.append(row[0]) 
        total_vote = len(vote) 
     # set list for each candidate no duplication
        candidate.append(row[2]) 
        candidate = sorted(list(set(candidate)))
        
    # find each candidate vote num
        if row[2] == 'Diana DeGette':
            diana += 1 
        elif row[2] == 'Charles Casper Stockham':
            charles +=1
        elif row[2] == 'Raymon Anthony Doane':
            raymon += 1
    # find each candidate vote percentage 
    per_diana = round(diana / total_vote *100,3)
    per_charles = round(charles /total_vote *100,3)
    per_raymon = round(raymon / total_vote *100,3)

   
    # find winner by max(vote list)
    vote_won = [diana, charles, raymon]
    if diana == max(vote_won):
        winner = "Diana DeGette"
    elif charles == max(vote_won):
        winner = 'Charles Casper Stockham'
    elif raymon ==max(vote_won):
        winner = 'Raymon Anthony Doane'
# print in terminal 
print("Election Results")
print("-------------------------") 
print("Total Votes: " + str(total_vote))
print("-------------------------")
print(candidate[0] +" " +":"+" "  + str(per_charles)+"%"  + " " + "(" + str(charles) + ")"  )
print(candidate[1] +" " +":"+" "  + str(per_diana)+"%"  + " " + "(" + str(diana) + ")"   )
print(candidate[2] +" " +":"+" "  + str(per_raymon)+"%"  + " " + "(" + str(raymon) + ")"   )
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")

# print in txt 
f = open("pypoll.txt", "w")
f.write("Election Results"  + "\n" )
f.write("-------------------------" + "\n")
f.write("Total Votes: " + str(total_vote)  + "\n" )
f.write("-------------------------"  + "\n")
f.write(candidate[0] +" " +":"+" "  + str(per_charles)+"%"  + " " + "(" + str(charles) + ")"  + "\n" )
f.write(candidate[1] +" " +":"+" "  + str(per_diana)+"%"  + " " + "(" + str(diana) + ")"  + "\n" )
f.write(candidate[2] +" " +":"+" "  + str(per_raymon)+"%"  + " " + "(" + str(raymon) + ")"  + "\n" )
f.write("-------------------------"  + "\n")
f.write("Winner: " + str(winner)  + "\n")
f.write("-------------------------"  + "\n")

    # print(total_vote)
    # print(candidate)
    # print(diana)
    # print(charles)
    # print(raymon)
    # print(per_diana)
    # print(per_charles)
    # print(per_raymon)
    # print(winner)
  
