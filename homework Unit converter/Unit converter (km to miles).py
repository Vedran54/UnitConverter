#!/usr/bin/env python
# -*- coding: utf-8 -*-

print ("Welcome to BV Unit converter! Transfer kilometers to miles in an easy way!")

x = "no"
while True:

    km = int(raw_input("Please enter the number of kilometers You wish to convert: "))
    miles = km * 0.621371
    print miles
    y = raw_input("Do You want to do another conversion? Please enter Yes or No: ").lower()
    if x == y:
        break

print "Thank you for playing! See You next time!"




