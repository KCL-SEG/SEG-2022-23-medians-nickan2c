# hello first commit 
"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
while True:
        try:
            print("Enter a list of numbers separated by commas: ")
            numbers = [float(value) for value in input().split(",")]
            numbers.sort()
            n = len(numbers)
            if n % 2 == 1:
                Median = (numbers[n//2])
            else:
                Median =((numbers[n//2] + numbers[(n//2)-1])/2)
        except ValueError:
            print("Some input could not be converted to a number!")
            
print(numbers)
print(Median)

