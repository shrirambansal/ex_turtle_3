"""
Write a program to check whether a person is eligible for voting or not. (accept age from user)
"""
age = int(input("Enter the age : "))
if age >= 18:
    print("Eligible for voting...")
else:
    print("Not Eligible for voting...")
