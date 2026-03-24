# This program gets three test scores and displays
# their average. It congratulates the user if the
# average is a high score.
# The HIGH_SCORE named constant holds the value that is
# considered a high score.
HIGH_SCORE = 95
# Get the three test scores.
test1 = int(input('Enter the score for test 1: ' ))
test2 = int(input('Enter the score for test 2: ' ))
test3 = int(input('Enter the score for test 3: ' ))
# Calculate the average test score.
average = (test1 + test2 + test3) / 3
# Print the average.
print(f'The average score is {average}.')
# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')

# Named constants to represent the base hours and
# the overtime multiplier.
BASE_HOURS = 40 # Base hours per week
OT_MULTIPLIER = 1.5 # Overtime multiplier
# Get the hours worked and the hourly pay rate.
hours = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))
# Calculate and display the gross pay.
if hours > BASE_HOURS:
    overtime_hours = (hours - BASE_HOURS)
    overtime_pay = (overtime_hours * pay_rate * OT_MULTIPLIER)
    gross_pay = (BASE_HOURS * pay_rate + overtime_pay)

else:
    # Calculate the gross pay without overtime.
    gross_pay = (hours * pay_rate)
    # Display the gross pay.
print('The gross pay is ',gross_pay)
#loan_qualifier. This program determines wheter a bank customer qualifies for a loan
MIN_SALARY=30000.0  #the minimum annual salary
MIN_YEARS=2         #the minimum years on the job
#Get the customer's annual salary
salary=float(input('Enter your annual salary: '))
#get the number of years on the current job
years_on_job=int(input('Enter the number of years employed:  '))
#Determine whether the customer qualifies.
if salary>=MIN_SALARY:
    if years_on_job>=MIN_YEARS:
        print('You qualify for the loan')
    else:
        print('You must have been employed for at least ',MIN_YEARS,' years to qualify')
else:
    print('You must earn at least $ ',MIN_SALARY,' per year to qualify')
##2#2#2#2 this program determines wheter a bank customer qualifies for a loan.

years_on_job=int(input('Enter your number of years employed'))
if salary>=MIN_SALARY and years_on_job>=MIN_YEARS:
    print ('you qualify for the loan')
else:print(' you do not qualify for this loan.')
#3#3#3#3#3#3
if salary >= MIN_SALARY or years_on_job >= MIN_YEARS:
    print('You qualify for the loan.')
else:
    print('You do not qualify for this loan.')    
#greader
#This program gets a numreic test score from the user and displays the corresponding letter grade.
#Nmaed constants to represent the grade thresholds
A_score=90
B_score=80
C_score=70
D_score=60
#get a test score from the user
score=int(input('Enter your test score: '))
#determine the grade
if score>=A_score:
    print('your grade is A')
else:
    if score>=B_score:
        print('Your grade is B')
    else:
        if score>=C_score:
            print('Your grade is C ')
        else:
            if score>=D_score:
                print('Your grade is D ')
            else:print('Your grade is F ')
#elif conditional
if score>=A_score:
    print('Your grade is A ')
elif score>=B_score:
    print('Your grade is B')
elif score>=C_score:
    print('Your grade is C ')
elif score>=D_score:
    print('your grade is D ')
else:print ('your grade is F')    



































