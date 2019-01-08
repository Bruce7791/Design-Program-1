# My design program that uses Turtle graphics to create various designs and art. 
# OOP style pseudoclasses and static methods.
# This version of the design program has been optimized for speed.
# Original code for optimization from https://stackoverflow.com/questions/16119991/how-to-speed-up-pythons-turtle-function-and-stop-it-freezing-at-the-end

# ==============================================================================================================================
# Modules

import turtle
from turtle import Turtle
from turtle import *
import random


# ==============================================================================================================================
# Classes

class Spiral_Square:

    def __init__(self):
        pass

    @staticmethod
    def spiralSquare1():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Warped Wood")
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(90.05)
        screen.update()

    @staticmethod
    def spiralSquare2():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Square Spiral")
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(91)
        screen.update()

    @staticmethod
    def spiralSquare3():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Spikey Swirl")
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(191)
        screen.update()

    @staticmethod
    def spiralSquare4():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Star Spiral")
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(491)
        screen.update()

    @staticmethod
    def spiralSquare5():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Round and Round")
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(591)
        screen.update()

    @staticmethod
    def spiralSquare6():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Pentagon Spiral")
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(791)
        screen.update()

    @staticmethod
    def spiralSquare7():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Spikey Star")
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(891)
        screen.update()

    @staticmethod
    def spiralSquare8():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Colorful Spiral")
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(1191)
        screen.update()

    @staticmethod
    def spiralSquare9():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Candy Cane Star")
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(1291)
        screen.update()

    @staticmethod
    def spiralSquare10():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Thread Spiral")
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(143)
        screen.update()

    @staticmethod
    def spiralSquare11():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Neon Focus")
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(443.05)
        screen.update()


    @staticmethod
    def spiralSquare12():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Color Explosion")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(190)
        screen.update()

    @staticmethod
    def spiralSquare13():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Radiating Color Wheel")
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(90.05)
            ninja.right(490.05)
        screen.update()

    @staticmethod
    def spiralSquare14():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Many Layers")
        t=Turtle()
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(555)
            ninja.forward(x)
            ninja.right(555)
            ninja.forward(x)
            ninja.right(255)
        screen.update()

    @staticmethod
    def spiralSquare15():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Bold Complexity")
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(555)
            ninja.forward(x)
            ninja.right(555)
            ninja.forward(x)
            ninja.right(855)
        screen.update()

    @staticmethod
    def spiralSquare16():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Mandala")
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(555)
            ninja.forward(x)
            ninja.right(555)
            ninja.forward(x)
            ninja.right(1255)
        screen.update()

    @staticmethod
    def spiralSquare17():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Circle Spiral")
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.circle(200)
            ninja.back(x)
            ninja.right(0.5)
        screen.update()

    @staticmethod
    def spiralSquare18():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Expanding Circle Spiral")
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.circle(200)
            ninja.back(x)
            ninja.right(20)
        screen.update()

    @staticmethod
    def spiralSquare19():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Pendulum Spiral")
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.circle(20)
            ninja.back(x)
            ninja.right(2)
        screen.update()

    @staticmethod
    def spiralSquare20():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Center of the Spiral")
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.circle(1000)
            ninja.back(x)
            ninja.right(1)
            ninja.forward(x)
            ninja.left(10)
            ninja.back(x)
        screen.update()

    @staticmethod
    def spiralSquare21():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Supernova Spiral")
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.circle(250)
            ninja.back(x)
            ninja.right(1)
            ninja.forward(x)
            ninja.left(10)
            ninja.back(x)
        screen.update()

    @staticmethod
    def spiralSquare22():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Odd Symbol")
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.circle(250)
            ninja.back(x)
            ninja.right(10)
            ninja.forward(x)
            ninja.left(100)
            ninja.back(x)
        screen.update()

    @staticmethod
    def spiralSquare23():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Amazing Color Ball")
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.circle(250)
            ninja.back(x)
            ninja.right(0.05)
            ninja.forward(x)
            ninja.left(100)
            ninja.back(x)
        screen.update()

    @staticmethod
    def spiralSquare24():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Golden Weaving Circles")
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.circle(250)
            ninja.backward(x)
            ninja.right(0.05)
            ninja.forward(x)
            ninja.right(100)
            ninja.backward(x)
            ninja.right(100)
        screen.update()

    @staticmethod
    def spiralSquare25():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Wonderful Mess")
        screen.tracer(18, 2)
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        t.hideturtle()
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.circle(250)
            ninja.circle(25)
            ninja.backward(x)
            ninja.right(0.05)
            ninja.forward(x)
            ninja.right(791)
            ninja.backward(x)
            ninja.right(591)
        screen.update()

    @staticmethod
    def spiralSquare26():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Stained Glass Ripple")
        t=Turtle()
        t.screen.bgcolor('gray')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.circle(500)
            ninja.circle(25)
            ninja.backward(x)
            ninja.circle(100)
            ninja.right(500)
            ninja.forward(x)
            ninja.circle(500)
            ninja.right(0.5)
            ninja.backward(x)
            ninja.right(991)
        screen.update()

    @staticmethod
    def spiralSquare27():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("TV Test Pattern")
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        colors = ['deep pink', 'DarkViolet', 'deep sky blue', 'SaddleBrown', 'DarkGreen', 'OrangeRed']
        colors2 = ['red', 'blue']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(225)
            ninja.dot(100)
            ninja.pencolor(colors2[x % 2])
            ninja.circle(150)
        screen.update()
                   
    @staticmethod
    def spiralSquare28():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Dots")
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        colors = ['deep pink', 'DarkViolet', 'deep sky blue', 'SaddleBrown', 'DarkGreen', 'OrangeRed']
        colors2 = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        colors3 = ['green', 'yellow', 'red', 'purple', 'black', 'white']
        for x in range(5000):
            ninja.penup()
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(425)
            ninja.forward(x)
            ninja.dot(50)
            ninja.down()
            ninja.pencolor(colors2[x % 6])
            ninja.dot(25)
            ninja.pencolor(colors3[x % 6])
            ninja.dot(12.5)
        screen.update()

    @staticmethod
    def spiralSquare29():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Jackson Pollock")
        t=Turtle()
        t.screen.bgcolor('gray68')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['firebrick', 'DodgerBlue', 'LemonChiffon', 'MidnightBlue', 'OliveDrab', 'SaddleBrown']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(random.randint(438, 448))
            ninja.right(random.randint(138, 148))
            ninja.backward(x)
            ninja.forward(x)
        screen.update()

    @staticmethod
    def spiralSquare30():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Disease Vector")
        t=Turtle()
        t.screen.bgcolor('gray68')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['deep pink', 'DarkViolet', 'deep sky blue', 'SaddleBrown', 'DarkGreen', 'OrangeRed']
        colors2 = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        colors3 = ['green', 'yellow', 'red', 'purple', 'black', 'white']
        colors4 = ['firebrick', 'DodgerBlue', 'LemonChiffon', 'MidnightBlue', 'OliveDrab', 'SaddleBrown']
        for x in range(5000):
            ninja.penup()
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(random.randint(438, 448))
            ninja.right(random.randint(138, 148))
            ninja.right(random.randint(38, 48))
            ninja.backward(x)
            ninja.forward(x)
            ninja.dot(random.randint(1, 25))
            ninja.pencolor(colors2[x % 6])
            ninja.dot(random.randint(1, 25))
            ninja.pencolor(colors3[x % 6])
            ninja.dot(random.randint(1, 25))
            ninja.pencolor(colors4[x % 6])
            ninja.dot(random.randint(1, 25))
        screen.update()
            
    @staticmethod
    def spiralSquare31():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("The Mother of all Spirals")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('hot pink')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        colors3 = ['green', 'yellow', 'red', 'purple', 'black', 'white']
        colors4 = ['firebrick', 'DodgerBlue', 'LemonChiffon', 'MidnightBlue', 'OliveDrab', 'SaddleBrown']
        for x in range(5000):
            a = [91, 191, 891 ]
            b = a[x%3]
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(b)
            ninja.right(b)
            ninja.forward(x)
            ninja.pencolor(colors3[x % 6])
            ninja.dot(10)
            ninja.pencolor(colors4[x % 6])
            ninja.circle(10)
        screen.update()
              
# ==============================================================================================================================
# Spiral Square functions

def spiral_square():
    print("\nSPIRAL DESIGNS")
    print("\nA collection of 31 algorithms that produce different spiral designs")
    print("\nSelect a design.")
    print("\n1. Warped Wood")
    print("2. Square Spiral")
    print("3. Spikey Swirl")
    print("4. Star Spiral")
    print("5. Round and Round")
    print("6. Pentagon Spiral")
    print("7. Spikey Star")
    print("8. Colorful Spiral")
    print("9. Candy Cane Star")
    print("10. Thread Spiral")
    print("11. Neon Focus")
    print("12. Color Explosion")
    print("13. Radiating Color Wheel")
    print("14. Many Layers")
    print("15. Bold Complexity")
    print("16. Mandala")
    print("17. Circle Spiral")
    print("18. Expanding Circle Spiral")
    print("19. Pendulum Spiral")
    print("20. Center of the Spiral")
    print("21. Supernova Spiral")
    print("22. Odd Symbol")
    print("23. Amazing Color Ball")
    print("24. Golden Weaving Circles")
    print("25. Wonderful Mess")
    print("26. Stained Glass Ripple")
    print("27. TV Test Pattern")
    print("28. Dots")
    print("29. Jackson Pollock")
    print("30. Disease Vector")
    print("31. The Mother of all Spirals")
    
    choice = input("\nEnter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31): ")

    if choice == '1':
        Spiral_Square.spiralSquare1()

    elif choice == '2':
        Spiral_Square.spiralSquare2()

    elif choice == '3':
        Spiral_Square.spiralSquare3()

    elif choice == '4':
        Spiral_Square.spiralSquare4()

    elif choice == '5':
        Spiral_Square.spiralSquare5()

    elif choice == '6':
        Spiral_Square.spiralSquare6()

    elif choice == '7':
        Spiral_Square.spiralSquare7()

    elif choice == '8':
        Spiral_Square.spiralSquare8()

    elif choice == '9':
        Spiral_Square.spiralSquare9()

    elif choice == '10':
        Spiral_Square.spiralSquare10()

    elif choice == '11':
        Spiral_Square.spiralSquare11()

    elif choice == '12':
        Spiral_Square.spiralSquare12()

    elif choice == '13':
        Spiral_Square.spiralSquare13()

    elif choice == '14':
        Spiral_Square.spiralSquare14()

    elif choice == '15':
        Spiral_Square.spiralSquare15()

    elif choice == '16':
        Spiral_Square.spiralSquare16()

    elif choice == '17':
        Spiral_Square.spiralSquare17()

    elif choice == '18':
        Spiral_Square.spiralSquare18()

    elif choice == '19':
        Spiral_Square.spiralSquare19()

    elif choice == '20':
        Spiral_Square.spiralSquare20()

    elif choice == '21':
        Spiral_Square.spiralSquare21()

    elif choice == '22':
        Spiral_Square.spiralSquare22()

    elif choice == '23':
        Spiral_Square.spiralSquare23()

    elif choice == '24':
        Spiral_Square.spiralSquare24()

    elif choice == '25':
        Spiral_Square.spiralSquare25()

    elif choice == '26':
        Spiral_Square.spiralSquare26()

    elif choice == '27':
        Spiral_Square.spiralSquare27()

    elif choice == '28':
        Spiral_Square.spiralSquare28()

    elif choice == '29':
        Spiral_Square.spiralSquare29()

    elif choice == '30':
        Spiral_Square.spiralSquare30()

    elif choice == '31':
        Spiral_Square.spiralSquare31()

    
    
# ==============================================================================================================================
# Main Global Menu

while True:
    print("\nWelcome to Bruce's Turtle Graphics Design Program 1.0")
    print("\n1. Spiral Designs")
    print("\n2. About this program")

    choice = input("\nEnter choice(1/2): ")

    if choice == '1':
        spiral_square()

    elif choice == '2':
        a = """\nA Turtle graphics design program I came up with"""
        print(a)

    while True:
        answer = input('\nRun Turtle Graphics Design Program again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print('Goodbye')
        break





