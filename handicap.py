def input_score():
    course_rating = input("What is the rating of your home course?")
    course_rating = float(course_rating)
    course_slope = input("What is the slope of your home course?")
    course_slope = float(course_slope)
    score1 = input("What is your first score?")
    score1 = int(score1)
    score2 = input("What is your second score?")
    score2 = int(score2)
    score3 = input("What is your third score?")
    score3 = int(score3)
    score4 = input("What is your fourth score?")
    score4 = int(score4)
    score5 = input("What is your fifth score?")
    score5 = int(score5)
    differential1 = (score1 - course_rating)*113/course_slope
    differential2 = (score2 - course_rating)*113/course_slope
    differential3 = (score3 - course_rating)*113/course_slope
    differential4 = (score4 - course_rating)*113/course_slope
    differential5 = (score5 - course_rating)*113/course_slope
    differential_use = min(differential1, differential2, differential3, differential4, differential5)
    differential_final = differential_use/1
    differential_final = float(differential_final)
    return differential_final

my_differential = input_score()

def handicap():
    global my_differential
    my_handicap = my_differential*0.96
    my_handicap = round(my_handicap)
    return my_handicap

final_handicap = handicap()
final_handicap = str(final_handicap)
print("Your handicap is: " + final_handicap)
    
