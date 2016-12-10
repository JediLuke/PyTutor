# -----------------------------------------------------------------------------
## Python 101 script
## Author: Luke Taylor
# -----------------------------------------------------------------------------


# Introduction

# Last time, we compiled and ran the 'hello world' program. This time we shall
# build a slightly more complicated program.

# Before we jump into programming this time, we should try to understand a little
# bit about how computers work. Not that many people can even understand how a car
# works - even fewer understand how computers work. We shall start by learning how
# computers work - we'll get to the programming part really soon I promise!


# -----------------------------------------------------------------------------
## Theory & reading - 10 mins
# -----------------------------------------------------------------------------


# How computers work - the basics

# Computers are mankinds most incredible achievement. The capabilities of an
# every day computer are nothing short of outstanding. Other species on this
# planet show almost no capability to use even the most rudimentary tools, yet
# somehow we umans have developed the ability precisely refine the required minerals
# and combine them to form a universal machine of epic complexity.

# It's a long process to make a computer. We start with sand, and refine it
# into something called silicon (more-better sand). Then we mix in some tiny
# bits of metal, and you an get something called a transistor. Transistors
# are the building blocks of computers. Although they are very small, you can
# link transistors together, to form tiny electric circuits, that work
# in some pretty awesome ways.

# Some very smart people were playing around with transistors one day, and
# they build a circuit that, from the outside, looks something like this:

#                _______
#       --------|       |
#               |  AND  |--------
#       --------|_______|
#

# This circuit is called an 'AND gate'. It has two wires going into it, and
# one coming out. If we put a voltage signal on both wires going in, then we
# shall get an output signal coming out the other side. If only one wire, or
# if neither wire, has any signal/voltage applied to it, then we get no output.
# We use the numbers 0 and 1 to signify if a signal is present.

# Here is the first example:

#                _______
#       -- 1 ---|       |               ## First wire is a 1, AND,
#               |  AND  |--- 1 --       ## Second wire is also a 1
#       -- 1 ---|_______|               ## Therefore output = 1
#


# We could replace the diagram above with this writing if we wanted.
#
#       (1 AND 1) -> 1
#

# More examples:

#                _______
#       -- 1 ---|       |               ## Only one wire equals 1
#               |  AND  |--- 0 --       ## So no output signal
#       -- 0 ---|_______|               ## (1 AND 0) -> 0
#


#                _______
#       -- 0 ---|       |               ## Only one wire equals 1
#               |  AND  |--- 0 --       ## So output = 0
#       -- 0 ---|_______|               ## (0 AND 0) -> 0
#

# This is how the AND gate works, there are a few different types (XOR
# is used below), and we can chain them together to do complicated stuff.

#                _______
#       -- 0 ---|       |               
#               |  XOR  |--- 1 --    _______
#       -- 1 ---|_______|        |__|       |
#                                   |  AND  |--- 1 --
#                _______          __|       |
#       -- 1 ---|       |        |  |_______|
#               |  AND  |--- 1 --       
#       -- 1 ---|_______|
#

# The code to represent this circuit looks like
#
#       ((0 XOR 1)
#           AND
#        (1 AND 1)) -> 1

# We can see that by having different inputs, we can get different output. This
# is what writing computer code is!! By picking the right gates, combining them
# together, and putting in the right inputs, we can make anything we want come
# out the other side.

# Luckily we don't have to write out code like that. Some very smart people have
# done some great work to make writing programs easier. At first, they created
# shortcuts that required less typing. Then we created 'compilers' which could
# read code in 'languages' and translate it down to the 1's and 0's for us. This
# is how python works today, we feed our python code into the computer, it gets
# turned into a whole bunch of 1's and 0's by the compiler, which get run
# directly on the CPU.


# If this explanation was complicated, then don't worry, you don't really NEED to
# understand how computers work to write code - just like you don't really NEED
# to know how an engine works to drive a car. But it does help, and it makes it
# easier to figure things out when it gets more complicated later.



# -----------------------------------------------------------------------------
## Lesson 2
# -----------------------------------------------------------------------------


# This program lets us get input from the user, and uses that input to do some
# cool stuff. To get it to do that cool stuff, we need to be able to write a
# program that does more than just print things to the screen.


# REMEMBER - You can run this lesson in python. You should comment out code
# that you don't want to run right at that point in time.

# Let's start with a reminder, how to print things to screen
print ("Welcome to lesson2")
print ("------------------")
print ("This lesson is contained completely within the source code")
print ("of this file. Only run the file after reading the code.")


# To get user input, we can just type 'raw_input()'. I will explain why we need
# brackets soon, but for now, just put them in.
print ("Can you please enter your name?")
x = raw_input()


# The next thing we shall do is to answer the user. We shall print the name
# back out in a nice greetings.
greeting = "Nice to meet you, " + x
print (greeting)



# Put your version of the code under here
# # # # # # # # # # # # # # # # # #
