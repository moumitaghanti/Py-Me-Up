
# Modules
import os
import csv

filename = os.path.join( "election_data.csv")
output_file= os.path.join( "election_data_out.csv")
header = [] 

rows = [] 
total = 0
cnt = 0
win_id = 0
total_change=0
country = []
candidates =[]
vote_counts =[]

maxvote = 0


with open(filename, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader) 
    for row in csvreader:
        cnt = cnt+1
        candidate = row[2]
        # If the candidate has votes then add to vote total for that candidate
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        # Else create new spot in list for candidate
        else:
            candidates.append(candidate)
            vote_counts.append(1)   
            
    #Printing the results     
    print("Election Results")
    print("----------------------------")
    print("Total Votes:   "+str(cnt))
    print("----------------------------")
    len_can = int(len(candidates))
    for i in range(len_can):
        percent_votes= '{:.3f}'.format(round(float((vote_counts[i]/cnt)*100),3))
        print(candidates[i]+":    "+ str(percent_votes)+"%   ("+str(vote_counts[i])+")")
        if vote_counts[i] > maxvote:
           maxvote = vote_counts[i]
           win_id = i
    print("----------------------------")       
    print("Winner:"+candidates[win_id]) 
    print("----------------------------")      
# printing in file
with open(output_file, 'w') as filewriter:
    filewriter.write(f"Election Results:\n")
    filewriter.write("-------------------------------------------------------\n")
    filewriter.write(f"Total Votes: {cnt}\n")
    filewriter.write("-------------------------------------------------------\n")
    for i in range(len_can):
        percent_votes='{:.3f}'.format(round(float((vote_counts[i]/cnt)*100),3))
        filewriter.write(f"{candidates[i]} : {percent_votes}% ({vote_counts[i]} )\n")
    filewriter.write("-------------------------------------------------------\n")
    filewriter.write(f"Winner: {candidates[win_id]}\n")   
    filewriter.write("-------------------------------------------------------\n")     
    filewriter.write("")

    filewriter.close()    
    
   