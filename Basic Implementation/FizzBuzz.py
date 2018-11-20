"""
https://www.lintcode.com/problem/fizz-buzz/description
"""
"""
9. Fizz Buzz
Given number n. Print number from 1 to n. But:

when number is divided by 3, print "fizz".
when number is divided by 5, print "buzz".
when number is divided by both 3 and 5, print "fizz buzz".

"""

class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        result = []
        for x in range(1, n+1):
            if x%3 ==0 and x%5==0:
                result.append("fizz buzz")
            elif x%3 == 0:
                result.append("fizz")
            elif x%5 == 0:
                result.append("buzz")
            else:
                result.append(str(x))
        return result