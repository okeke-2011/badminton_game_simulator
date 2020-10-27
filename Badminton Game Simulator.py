#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random #library for generating various types of random numbers used in the game

def badminton_game_sim(p1_prob):
    P1_wins = 0   #Accumulator for Number of times Player 1 wins the game
    for game in range(100000):  #plays the game a hundred thousand times
        
        P1 = 0  #accumulator for the score of Player 1
        P2 = 0   #accumulator for the score of Player 2
        who_serves = 1   #determines who serves at each point in the game
        while P1 < 21 and P2 < 21:   #continues to run the loop as long as no one has won yet
            while who_serves == 1:  #continues to run this loop as long as Player 1 is serving
                if P1 == 21 or P2 == 21: #if either player has one do not run the loop
                    break
                else:
                    win = random.random() #generates a random value from 0 to 1
                    if win < p1_prob: #the range this value falls in corresponds to the probability of Player 1 winning
                        P1 += 1   
                        #print("P1: ",P1,"P2: ",P2)  
                    else:
                        P2 += 1  #if the probability does not happen it means that Player 2 scored
                        #print("P1: ",P1,"P2: ",P2)
                        who_serves = 2 #Player 2 will serve next
            while who_serves == 2:  #as long as Player 2 is serving, run this loop
                if P1 == 21 or P2 == 21:
                    break
                else:
                    win = random.random()
                    if win < 0.5:
                        P1 += 1
                        #print("P1: ",P1,"P2: ",P2)
                        who_serves = 1 #if Player 1 score while Player 2 is serving, he will serve next
                    else:
                        P2 += 1
                        #print("P1: ",P1,"P2: ",P2)
        #print("P1: ",P1,"   P2: ",P2)
        if P1 > P2:  #determines the player with the higher score i.e. the winner of the game
            #print("P1 wins")
            P1_wins += 1 #if the winner is Player 1 add to the accumulator which store Player 1's wins
        #else:
            #print("P2 wins")
    P_of_P1_wins = P1_wins/100000 #calculates probability that Player 1 will win based on number of times he won in the games played
    print("Probability that P1 wins:", round(P_of_P1_wins, 4))
    print("Probability that P2 wins:", round(1-P_of_P1_wins, 4))

badminton_game_sim(0.6)


# In[2]:


from scipy import stats

#Geometric Distribution
p = 0.3
n = 2
print("Probability of first success on the",n,"nd trial:",stats.geom.pmf(n,p),"\n")

#Binomial Distribution
p = 0.4
n = 100
k = 45
print("Probability of ",k,"successes in",n,"trials:",stats.binom.pmf(k,n,p))
print(stats.t.cdf(-2,9))

