""" 
We are given a set of grades from a class final. We are to write a program that displays the number of final tests submitted, the class average, and the percentage above the class average.
We will sum up the total of tests submitted. We will add the total scores together and divide them by the total number of tests submitted to calculate average. We will then take average test scores and 
and see how many tests were above the average score. We will then calculate the percentage of tests that scored above the average. 



"""


"""
number of tests sumbmitted = sum of all finals
total = 24


class average = total of all scores / number of tests submitted
1998 sum of all points / 24 tests = 83.25 % class average


number of tests above the grade point average = number of tests > class average
test score > class avegerage ( we add it them up)


percent of number of tests above class average = ((number of tests>class average) / number of tests submitted))
13 (number of tests above the class average)  / 24 (total tests sumbmitted) = 54.17 % scored above the class average



"""


def enter_score ():
    grades = [78,67,56,99,80,83,82,91,94,95,77,88,85,92,91,79,88,82,81,86,94,93,92,45]
    scores = int(input("How many grades were submitted? : "))
    for i in range(scores):
        return grades

def calc_average(grades):
    total=0
    for student_score in grades:
        total=total+student_score
    average= total/len(grades)
    print("The class average is ", average)
    return average

def above_average(grades, average_score):
    above_average_amount=0
    for student_score in grades:
        if student_score > average_score:
            above_average_amount = above_average_amount + 1
            print("The number of grades above the average is now ", above_average_amount)
    return above_average_amount

def percent_above_average(above_average_amount, grades):
    for above_average_amount in above_average:
        if above_average_amount==13:
            percent_above_avergage= above_average_amount/len(grades)
    print("The percent of grades above average is ", percent_above_average)
    return percent_above_average

grades = enter_score()
average_score = calc_average(grades)
above_average_amount = above_average(grades, average_score)
percent_above_average = percent_above_average(average_score, grades)