import numpy as np 
import random 
import pandas as pd 
import matplotlib.pyplot as plt

# arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# print(arr1)


# sum = np.sum(arr1)
# print(sum)

# mean = np.mean(arr1)
# print(mean)


# standardDeviation = np.std(arr1)
# print(standardDeviation)

#   b. Find the indices of elements greater than 10 in the array.  


# indices = (arr1>10)
# print(indices)


# 2. Create a 2D NumPy array of shape 4 X 4 with numbers ranging from 1 to 16.  

# arr2 = np.arange(16).reshape(4,4)
# print(arr2)

print(end="\n")

# transpose = arr2.T
# print(transpose)


# rowise = arr2 + 5
# print(f"After adding rowise to arr2 {rowise}")


# columnwise = arr2 + np.array([5,5,5,5])
# print(f'After adding ccolumn wise {columnwise}')



# 3. Create two 3 X 3 arrays filled with random integers between 1 and 20.  


# arr3 = np.random.randint(1,20,(3,3))
# print(f"Random integar array 3 x 3 array of 1 is {arr3}")

# print(end="\n")

# arr4 = np.random.randint(1,20,(3,3))
# print(f"Random integar array 3 x 3 array of 2 is {arr4}")


#   a. Perform element-wise addition, subtraction, and multiplication.  

# addition = arr3 + arr4
# print(f"The addition of two array of arr3 + arr4 is {addition}")


# subtraction = arr3 - arr4
# print(f"The subtraction of two array of arr3 - arr4 is {subtraction}")


#   b. Compute the dot product of the two arrays.  

# mulitplication = arr3 * arr4
# dotproduct = sum(mulitplication)

# print(f"The dot product of two array is {dotproduct}")



# 4. Reshape a 1D array of size 12 into a 3 X 4 2D array and slice the first two rows and last two columns. 


# arr5 = np.arange(12).reshape(3,4)
# print(arr5)

# print(f"First two rows and last two columns {arr5[:2,-2:]}")




# Assignment 2 - Working with Pandas

# data = pd.DataFrame({
#       'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
#       'Age': [24, 27, 22, 32, 29],
#       'Department': ['HR', 'Finance', 'IT', 'Marketing', 'HR'],
#       'Salary': [45000, 54000, 50000, 62000, 47000]
#   })

# print(data.head())






# summary 
# summary = data[['Age','Salary']].describe()
# print(summary)

# Avg salary 

# Hr_department = data[data['Department'] == 'HR']
# avg_sal = Hr_department['Salary'].mean()
# print(f'The average Salary of Hr department is {avg_sal}')



# New column 

# new_column  = data['Bonus'] = data['Salary'] * 0.1
# print(new_column) 


# filterData Frame 

# filtered_dataframe = data[(data['Age'] >= 25) & (data['Age'] <= 30)]
# print(filtered_dataframe)


# Average salary 

# avgSal = data.groupby('Department')['Salary'].mean()
# print(avgSal)


# Sorting order 

# sorting_value = data.sort_values(by='Salary', ascending=True)
# print(sorting_value)


#Assignment 3 - Working with Matplotlib

# x = [1, 2, 3, 4, 5]
# y = [10, 15, 25, 30, 50]


# plt.plot(x, y )
# plt.show()


# plt.plot(x,y , color='green' , label="Test" )
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.title("Simply x vs y graph")
# plt.legend()
# plt.grid()
# plt.show()



# 2. Create a bar graph to represent the marks scored by students in a subject:  
  
# students = ['John', 'Jane', 'Alice', 'Bob']
# marks = [75, 85, 60, 90]


# plt.bar(students , marks , color='green'  , label='Marks vs Students')
# plt.xlabel('Students')
# plt.ylabel('Marks')
# plt.title("Students Marks")
# plt.legend()
# plt.grid()
# plt.show()

# 3. Create a pie chart to represent the percentage distribution of a company’s revenue from different regions:  
  
# regions = ['North America', 'Europe', 'Asia', 'Others' ]
# revenue = [45, 25, 20, 10]
# explode = [0.1, 0, 0, 0]  


# plt.pie(revenue, labels=regions , autopct='.%1.1f%%' , explode=explode )
# plt.title("Company revenue")

# plt.show()




# 4. Generate a histogram to show the frequency distribution of randomly generated integers between 1 and 100 (sample size = 1000).  


# histogram = np.random.randint(1,101 , 1000)
# plt.hist(histogram , label='Frequency' , bins=10 , color='g' , edgecolor='white' )
# plt.xlabel("Sample size")
# plt.ylabel('Frequency')
# plt.show()