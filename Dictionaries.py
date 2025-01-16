student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
print(student_scores)

for key in student_scores:
    if(student_scores[key]>=91) and (student_scores[key]<=100):
        print(key+": Outstanding")
    elif( student_scores[key]>=81) and (student_scores[key]<=90):
        print(key+": Exceeds Expectations")
    elif( student_scores[key]>=71) and (student_scores[key]<=80):
        print(key+": Acceptable")
    else:
        print(key + ": Fail")
        
