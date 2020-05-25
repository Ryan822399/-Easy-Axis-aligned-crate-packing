#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 23:43:07 2020
[Easy] Axis-aligned crate packing

Description
You have a 2-dimensional rectangular crate of size X by Y, and a bunch of boxes, each of size x by y. The dimensions are all positive integers.

Given X, Y, x, and y, determine how many boxes can fit into a single crate if they have to be placed so that the x-axis of the boxes is aligned with the x-axis of the crate, and the y-axis of the boxes is aligned with the y-axis of the crate. That is, you can't rotate the boxes. The best you can do is to build a rectangle of boxes as large as possible in each dimension.

For instance, if the crate is size X = 25 by Y = 18, and the boxes are size x = 6 by y = 5, then the answer is 12. You can fit 4 boxes along the x-axis (because 6*4 <= 25), and 3 boxes along the y-axis (because 5*3 <= 18), so in total you can fit 4*3 = 12 boxes in a rectangle.

Examples
fit1(25, 18, 6, 5) => 12
fit1(10, 10, 1, 1) => 100
fit1(12, 34, 5, 6) => 10
fit1(12345, 678910, 1112, 1314) => 5676
fit1(5, 100, 6, 1) => 0

@author: ryanhennes
"""
#Original Problem
def fit1(X, Y, x, y):
    #use floor division to determine if the boxes can fit
    xRemainder = X // x
    yRemainder = Y // y
    return (xRemainder * yRemainder)

print("Original Solutions")
print(fit1(25, 18, 6, 5))
print(fit1(10, 10, 1, 1))
print(fit1(12, 34, 5, 6))
print(fit1(12345, 678910, 1112, 1314))
print(fit1(5, 100, 6, 1))


"""
Optional bonus fit2
You upgrade your packing robot with the latest in packing technology: turning stuff. You now have the option of rotating all boxes by 90 degrees, so that you can treat a set of 6-by-5 boxes as a set of 5-by-6 boxes. You do not have the option of rotating some of the boxes but not others.

fit2(25, 18, 6, 5) => 15
fit2(12, 34, 5, 6) => 12
fit2(12345, 678910, 1112, 1314) => 5676
fit2(5, 5, 3, 2) => 2
fit2(5, 100, 6, 1) => 80
fit2(5, 5, 6, 1) => 0
Hint: is there an easy way to define fit2 in terms of fit1?

Note that this is not the maximum possible number of boxes you could get if you rotated them independently. For instance, if you're fitting 3-by-2 boxes into a 5-by-5 crate, it's possible to fit 4 by varying the orientations, but fit2(5, 5, 3, 2) is 2, not 4. Handling the general case is much more complicated, and beyond the scope of today's challenge.
"""
#Bonus 1
def fit2(X, Y, x, y):

    bestArrangement = fit1(X, Y, x, y)  #storing original box arrnagment for comparison
    arr2 = fit1(X, Y, y, x) #rotating the boxes by 90 degrees
    if(bestArrangement < arr2):
       bestArrangement = arr2
    return bestArrangement

print("Bonus 1 Solutions")
print(fit2(25, 18, 6, 5))
print(fit2(12, 34, 5, 6))
print(fit2(12345, 678910, 1112, 1314))
print(fit2(5, 5, 3, 2))
print(fit2(5, 100, 6, 1))
print(fit2(5, 5, 6, 1))
    
    
    