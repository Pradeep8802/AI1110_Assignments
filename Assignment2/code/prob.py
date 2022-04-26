'''ICSE 2019 Grade 12
Name:I Sai Pradeep
Roll number: AI21BTECH11013

Question 1(ix):
Two balls are drawn from an urn containing 3 white,5 red and 2 black balls, one by one without replacement. 
What is the probability that at least one ball is red?
'''
Pr_1 = 1/2     # Probability that the ball drawn in the first draw is not red
Pr_2 = 4/9     # Probability that the ball drawn in the second draw is not red,given that ball drawn in the first draw is not red 
Pr_3=Pr_1*Pr_2 # Probability that none of the balls drawn is red
Pr_4=1-Pr_3    # Probability that aleast one of the balls drawn is red
#Output:
print("probability that at least one of the balls drawn is red is ",Pr_4)
