# Given a dictionary of student scores, create a new dictionary that only includes students who scored above a certain threshold (e.g., 75).

scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}
new_scores= {}

for a,b in scores.items():
  if b > 75:
    new_scores[a]= b

new_scores
