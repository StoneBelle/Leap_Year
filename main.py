# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Coditionals:
#is the year evenly / 4? Y - Leap N - Not Leap
#is the year evenly / 100? Y - Not Leap N - Leap
#is the year evenly / 400? Y - Leap N - Not Leap

condition_a = year % 4
condition_b = year % 100
condition_c = year % 400
#print(condition_a, condition_b, condition_c)


if condition_a == 0:
    if condition_b == 0:
        if condition_c == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
