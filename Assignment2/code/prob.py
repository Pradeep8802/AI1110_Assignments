''' 
ICSE 2019 Grade 12
Question 1(ix)
Name: I Sai Pradeep
Roll number: AI21BTECH11013
'''
#Question:
"""

Two balls are drawn from an urn containing 3 white, 5 red and 2 black balls, one by one without replacement. What is the probability that at least one ball is red?
"""

#Solution:
from math import comb
def main():
    Pr_1 = 1/5   # Probability that first ball drawn is Black
    Pr_2 = 3/10  # Probability that first ball drawn is White
    Pr_3 = 1/45  # Probability that first and the second balls drawn are Black
    Pr_4 = 1/15  # Probability that first ball drawn is Black and second ball drawn is White
    Pr_5= 1/15   # Probability that first ball drawn is White and second ball drawn is Black
    Pr_6 = 1/15  # Probability that first and the second balls drawn are White
   
#Output 
    print(f"The probability that atleast one of the balls drawn is Red is {1-prob(Pr_3,Pr_4,Pr_5,Pr_6)}")

    
def prob(Pr_3,Pr_4,Pr_5,Pr_6) -> float:
        """ Returns the probability that none of the balls drawn are Red"""
        return Pr_3+Pr_4+Pr_5+Pr_6

if __name__ == '__main__':
       main()
