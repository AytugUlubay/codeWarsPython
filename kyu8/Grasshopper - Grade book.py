"""Grade book
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100."""
def get_grade(s1, s2, s3):
    x=(s1+s2+s3)/3
    x=(x//10)*10
    num={100:"A",90:"A",80:"B",70:"C",60:"D",50:"F",40:"F",30:"F",20:"F",10:"F",0:"F"}
    return num[x]
