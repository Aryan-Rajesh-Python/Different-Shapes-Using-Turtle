import turtle
from turtle import Turtle,Screen
tortoise=Turtle()
screen=Screen()
def different_shapes():
    n=int(input("Enter the number of sides: "))
    for i in range(n):
        a=(360/n)
        tortoise.forward(100)
        tortoise.left(a)
    screen.exitonclick()
while(True):
    choice=input("Do you want to continue drawing the shapes: ")
    if(choice=="yes"):
        different_shapes()
    else:
        print("Thank you for using our application!")
        break