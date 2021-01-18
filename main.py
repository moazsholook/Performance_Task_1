"""
This program simulates an election for the user, where the user is
asked n indefinite number of times which candidate the next vote is
for. the program then stores the information, and counts both the total votes of the election and total votes for each candidate. the
program then returns who the winner of the election is and their
percentage of the votes.
"""

mickey_votes = 0 
donald_votes = 0
minnie_votes = 0
goofy_votes = 0

print ()
print ("The presidential candidates are:")
print ("1. Mickey Mouse")
print ("2. Donald Duck")
print ("3. Minnie Mouse")
print ("4. Goofy")
print ("Type 0 to quit")


while True:
  try:    
    v=int(input("Vote? "))
    if v==3:
        minnie_votes+=1
    elif v == 0:
        break
    elif v==2:
        donald_votes+=1
    elif v==1:
        mickey_votes+=1
    elif v==4:
        goofy_votes+=1
    else:
        print ("invalid")
        continue
  except ValueError as ve:
    print("invalid")

total_votes = mickey_votes + donald_votes + minnie_votes + goofy_votes
print (f"The total number of votes is {total_votes}")
if mickey_votes>donald_votes and mickey_votes>minnie_votes and mickey_votes>goofy_votes:
    print("Mickey Mouse wins!")
    print ((mickey_votes/total_votes)*100, "% of the votes")
elif donald_votes>minnie_votes and donald_votes>goofy_votes and donald_votes>mickey_votes:
    print ("Donald Duck wins!")
    print ((donald_votes/total_votes)*100, "% of the votes")
elif minnie_votes>goofy_votes and minnie_votes>mickey_votes and minnie_votes>donald_votes:
    print("Minnie Mouse wins!")
    print ((minnie_votes/total_votes)*100, "% of the votes")
elif goofy_votes>mickey_votes and goofy_votes>minnie_votes and goofy_votes>donald_votes:
    print("Goofy wins!")
    print ((goofy_votes/total_votes)*100, "% of the votes")
