import numpy as np

#Analysis where is the housing market-- mean,median, standard deviation, Q1, Q2,Q3

#Mean
#Median
#Std
#Q1
#Q2
#Q3

studentMarks = [55,78,85,91,66,79,82,75,89,95,68,74,92,88,77,81,69,84,73,87]
studentMarks2 = [23,22,85,91,66,79,82,75,89,95,68,74,92,88,77,81,69,84,13,87]
print(f'Mean value is {np.mean(studentMarks)}')
print(f'Median values is {np.median(studentMarks)}')
#why is mean and median different and what does it imply?

testData = [1,2,3,4,5]
testData2 = [1,1,2,2,3,3,9,9,10,23,100]
print('mean1',np.mean(testData))
print('median1',np.median(testData))
print('std1',np.std(testData))
print("=========")
print('mean2',np.mean(testData2))
print('median2',np.median(testData2))
print('std2',np.std(testData2))

#what does high std mean and what does low std mean
print(f'Std:{np.std(studentMarks)}')
print(f'Std2:{np.std(studentMarks2)}')

#Q1,Q3

print(f'Q1{np.quantile(studentMarks, 0.25)}')
print(f'Q3{np.quantile(studentMarks,0.75)}')
