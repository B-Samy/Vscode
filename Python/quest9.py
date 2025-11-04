def case_count(s):

    upper_case = 0
    lower_case = 0

    for char in s:
        if char.isupper():
            upper_case+=1
        elif char.islower():
            lower_case+=1

    return upper_case , lower_case

n = input("Enter the string :")
upper , lower = case_count(n)


print(f"The total upper case is {upper} \n The total lower case is {lower}")