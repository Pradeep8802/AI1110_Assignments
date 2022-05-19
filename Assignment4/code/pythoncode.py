'''
Name: I Sai Pradeep
Roll number: AI21BTECH11013
'''
'''
Reference: Papoulis book
chapter 2
Example 2.20

'''
"""
Question Statement:
In a group of n people,(a)what is the probability that two or more persons will have the same birthday (month and date)?
(b)What is the probability that someone in that group will have birthday that matches yours? 
"""
def parta(n):
    a=1.0
    for i in range(n):
        a=a*(1-i/365.0)
    print("The probability that two or more persons will have the same birthday(month and date) is ",1-a)
def partb(n):
    b=1.0
    for i in range(1,n+1):
        b=b*(1-1/365.0)
    print("the probability that someone in that group will have birthday that matches yours is ",1-b)
n=int(input("Enter number of people in the group: "))
parta(n)
partb(n)
