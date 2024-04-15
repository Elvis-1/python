import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';

Application logs are useful in analysing interactions with an application and may may also be used to detect suspicious activities

A log file is provided as a string array where each entry represents a money transfer in the form "sender_user_id recipient_user_id amount". Each of the values is separated by a space

 sender_user_id and recipient_user_id both consist only of digits, are at most 9 digits long and start with non-zero digit

amount consists only of digits, is at most 9 digits long and starts with non zero digit.

Logs are given in no particular order. Write a function that returns an array of strings denoting user_id's  of suspicious users who were involved in at least threshold number of log entries. The id's should be ordered ascending by numeric value.

Example
logs = ["88 99 200","88 99 300", "99 32 100", "12 12 15"];
threshold = 2



Find the number of strings of a given length that can be formed under the following rules.
 Each letter is a vowel, that is, it is in the set{a,e,i,o,u},
 The letter a may only be followed by the letter e
 An e may only be followed by an a or an i
 An i may not be next to another i
 The letter o may only be followed by an i or a u
 The letter u may only be followed by an a

#
# Complete the 'countPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def countPerms(n):
# Write your code here



5. K- Subarrays
A K-subarray of an array is:AboutDialoga subarray (a contiguous element)
the sum of the elements is evenly divisible by k(sum modulo k = 0)

Given an array of integers determine the number of k-subarrays it contains

Example
k = 5
nums = [5,10,11,9,5]

The 10 k-subarrays are {5},{5,10} etc