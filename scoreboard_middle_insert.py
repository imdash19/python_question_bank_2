# A scoreboard stores [10,30]. 
# Take a score as input and insert it between the two values. 
# Print updated list.

scores = [10, 30]

score = int(input())

scores.insert(1, score)

print(scores)
