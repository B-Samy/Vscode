s = {1, 2, 3, 4, 5, 6}
s2 = {2, 3, 4, 5, 6, 7, 8, 9, 10}

# Intersection: Elements common to both sets
result_intersection = s.intersection(s2)
print("Intersection:", result_intersection)  # Output: {2, 3, 4, 5, 6}

# Union: All unique elements from both sets
result_union = s.union(s2)
print("Union:", result_union)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Difference: Elements in 's' but not in 's2'
result_difference = s.difference(s2)
print("Difference:", result_difference)  # Output: {1}


