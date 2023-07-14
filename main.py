from maths import Math
from physics import Physics
phy = Physics()
mth = Math()
import art
print(art.logo)
print("Welcome to our Math and Physics operation machine")
mth_or_phy = input("What operation would you like to carry out math or phycics\n> ")

if mth_or_phy == "math":
    print("You can add(+), subtract(-), mutiply(*), divide(/), and find the exponent of a number(^)")
    num1 = int(input("First num\n> "))
    ops = input("Enter the operation you want to carry out\n> ")
    num2 = int(input("Second num\n> "))
    if ops == "+":
        print(mth.add(num1, num2))
    if ops == "-":
        print(mth.minus(num1, num2))
    if ops == "*":
        print(mth.multiply(num1, num2))
    if ops == "/":
        print(mth.divide(num1, num2))
    if ops == "^":
        print(mth.exponent(num1, num2))

if mth_or_phy == "physics":
    print("You can calculate speed, potential energy, force")
    ops = input("What operation do you want to carry out: ").lower()
    if ops == "speed":
        num1 = int(input("distance\n> "))
        num2 = int(input("time\n> "))
        print(phy.calc_speed(num1, num2))
    if ops == "potential energy":
        num1 = int(input("mass\n> "))
        num2 = int(input("height\n> "))
        print(phy.calc_PE(num1, num2))
    if ops == "force":
        num1 = int(input("mass\n> "))
        num2 = int(input("acceleration\n> "))
        print(phy.calc_force(num1, num2))
    if ops == "velocity":
        num1 = int(input("initial velocity\n> "))
        num2 = int(input("acceleration\n> "))
        num3 = int(input("time\n> "))
        print(phy.pressure(num1, num2, num3))
    if ops == "pressure":
        num1 = int(input("force\n> "))
        num2 = int(input("acceleration\n> "))
        print(phy.pressure(num1, num2))
