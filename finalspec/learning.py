# learning.py
# Contains machine learning methods to improve confidence functions.

# Pseudocode for now

# This type is a rating for both nodes in a link; r1, r2 in {1,2,3,4,5}
type rating = int*int

# Given two variables relating to the same pair:
Let m = mean
Let s = standard deviation
Let n = number of ratings
Let c = confidence
Let pr = past ratings #(unrated predictions, total ratings, successes)
Let x be an Edge := (m,s,n,c,pr)
Let r be a new rating

# Update c
# This function gives a new confidence. It is the one which will be modified with higher order functions; k_1 is a constant float which will be modified.
Let f  (n_0 : n) (s_0 : s) : c= 
k_1*log(n_0 / s_0)

# First, calculate the actual confidence.
actual_confidence = pr.successes / pr.total_ratings

# Now compose a set of actual values, which we will train f to fit
actual_values = (n, log(s/c)) list

Open scikit-learn package
use sklearn.linear_model.LinearRegression for n, log(s/c)
return k_1