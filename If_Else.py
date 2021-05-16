temperature=int(input("What is the temperature outside?  "))

if temperature >80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#What is your grade?
score=int(input("What is your test score?  "))

#Determine the Grade
if score >=90:
        print('Your grade is an A')
else:
    if score>=80:
        print('Your grade is a B.')
    else:
        if score>=70:
            print('Your grade is a C.')
        else:
            if score >=60:
                print('Your grade is a D')
            else:
                print('Your grade is an F.')
                