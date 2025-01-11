import math

name = input("What is your name: ").upper()
print(name,"Give the value for the solution, ")

a=float(input('enter the coefficient of x^2, a= '))
b=float(input('enter the coefficient of x, b = '))
c=float(input('enter the value of c = '))

gh = b**2 - 4*a*c

while True:
    
    print('the rooot of given qudratic euation is :')

    if a >0 and gh >0 :
        #for normal quadratic equation
        root1 = (-b + math.sqrt(gh))/ (2*a)
        root2 = (-b - math.sqrt(gh))/ (2*a)
        print("First root is : ",root1,"\n second root is: ",root2)
        break
    elif a == 0:
        #while a=0 denominator becomes zeero so the roots become indetminate form
        print("It doesnot have two quadtratic  roots \n The equation is not in quadratic from")
        #so the equation becomes a single powered x equation so it has only one root 
        answer = input("enter do you want to solve in simple equation form \n If yes press Y and if not press N: ").lower()
            
        if answer == "y":
            root = -c /b 
            print("the root is: ",root)
            break
        
        break
    elif gh == 0:
        root_1 = -b/ (2*a)
        root_2 = -b/ (2*a)
        print("First root is: ",root_1,"\n second root is: ",root_2)
        break
    
    if gh < 0:
        print("\n The given equation has imaginary solution")
        real_part = -b/(2*a)
        imaginary_part = math.sqrt(abs(gh))/(2*a) 
        print("Real part is : ",real_part,"\n Imaginary root is :",imaginary_part)
        print(f"first root is: {real_part} + {imaginary_part}i \n Second root is: {real_part}- {imaginary_part}i")
        #print the value with simple process :
        #print("first root is: ",real_part,"+", imaginary_part,"i","\n Second root is: ",real_part,"-",imaginary_part,"i")
        break
    



