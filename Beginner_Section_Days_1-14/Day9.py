'''
Day 9 topics:
-dictionaries
-nested lists

Project:
-Silent Auction
'''

'''
#test grades
student_scores = {"Jim": 62, "Joe": 74, "Kate": 96, "Aly": 83, "Alex": 55}
grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        grades[student] = 'A'
    elif score > 80:
        grades[student] = 'B'
    elif score > 70:
        grades[student] = 'C'
    elif score > 60:
        grades[student] = 'D'
    else:
        grades[student] = 'F'

print(grades)
'''

#Secret Auction
clear = "\n" * 100
other_bidders = True
bids = {"opening" : 0}
while(other_bidders):
    name = input("What is your name? ")
    bid = int(input("What is your bid?"))
    bids[name] = bid
    loop = input("Are there any other bidders? (y/n): ")
    if loop == 'n':
        other_bidders = False
    else:
        print(clear)

winner = 'opening'
#assuming no bids are the sake for simplicity
#todo add tie logic
for name in bids:
    if bids[name] > bids[winner]:
        winner = name


print("The winner of the auction is " + winner + " with a bid of $" + str(bids[winner]))