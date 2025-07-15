# check name function
def check_name(name):
    if (name == "sham"):
        name1="sham Praison"
        for n1 in name1[::-1]:
            print(n1)
        print("this is your first name")
        num = input("want to continue yes or no = ")
        if(num == "yes"):
            start()
        else:
            print("thank  your for using the app")
    else:
        print("this is your second name")
        num = input("want to continue yes or no = ")
        if(num == "yes"):
            start()
        else:
            print("thank  your for using the app")
        

# maths function
def maths_function():
    num1 = int(input("Enter the num1 = "))
    num2 = int(input("Enter the num2 = "))
    num4 = (input("enter the function to do = "))
    if(num4 == "subtraction"):
            num3 = num1-num2
            print("subtraction of two value",num3)
            num = input("want to continue yes or no = ")
            if(num == "yes"):
                start()
            else:
                print("thank  your for using the app")
    elif(num4 == "addition"):
            num3 = num1+num2
            print("addition of two value",num3)
            num = input("want to continue yes or no = ")
            if(num == "yes"):
                start()
            else:
                print("thank  your for using the app")
    elif(num4 == "multiplication"):
            num3 = num1*num2
            print("multiplication of two value",num3)
            num = input("want to continue yes or no = ")
            if(num == "yes"):
                start()
            else:
                print("thank  your for using the app")
    elif(num4 == "division"):
            num3 = num1/num2
            print("division of two value",num3)
            num = input("want to continue yes or no = ")
            if(num == "yes"):
                start()
            else:
                print("thank  your for using the app")
    else:
        print("please enter the correct function")
        maths_function()

#start function
def start():
    user = input("Enter the method want to execute = ")
    if (user == "maths"):
        maths_function()
    elif(user == "name"):
        check_name(input("Enter your name = "))
    else:
        print("please enter the correct method")
        start()



start()
