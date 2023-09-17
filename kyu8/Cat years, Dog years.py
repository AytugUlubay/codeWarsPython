"""Kata Task
I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that"""
def human_years_cat_years_dog_years(human_years):
    for i in range (1,human_years+1):
        if i== 1:
            c = 15
            d = 15
        elif i==2:
            c +=9
            d +=9
        else: 
            c+=4
            d+=5
    return[human_years,c,d]
