"""
Output a list containing the arithmetic means of the numbers of each nested tuple in a given tuple of numbers tuples
"""

numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
print([sum(i)/len(i) for i in numbers])