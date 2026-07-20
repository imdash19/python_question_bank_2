# Take two scores for first game and two for second game. 
# Combine them into one scoreboard.

lst1= list(map(int, input().split()))
lst2= list(map(int, input().split()))

score= lst1 + lst2
print(score)
