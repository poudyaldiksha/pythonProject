from inspect import cleandoc

import pandas as pd

file = open('university_towns.txt', 'r')
fileData = file.readlines()
print(fileData)


universityTowns = []
for line in fileData:
   if '[edit]' in line:
       state = line
   else:
       universityTowns.append([state,line])


print(universityTowns)
myDataframe = pd.DataFrame(universityTowns, columns=['State', 'Uni'])
print(myDataframe)

#Alabama[edit]\n-- Alabama
#Auburn (Auburn University)[1]\n - Auburn
def getUniversityAndCleanState(item):
    if '[edit]' in item:
        bracketIndex = item.find('[')
        cleanedValue = item[:bracketIndex]
        return cleanedValue
    elif '(' in item:
        openBracketIndex = item.find('(')
        closeBracketIndex= item.find(')')
        cleanedValued = item[openBracketIndex+1:closeBracketIndex]
        return cleanedValued
    else:
        return item

mappedDf = myDataframe.map(getUniversityAndCleanState)
print(mappedDf)

##Create a similar function to generate dtaframe

def getTownAndCleanState(item):
    if '[edit]'in item:
        bracketIndex = item.find('[')
        cleanedValue = item[:bracketIndex]
        return cleanedValue
    elif '(' in item:
        openBracketIndex = item.find('(')
        cleanedValued = item[:openBracketIndex-1]
        return cleanedValued
    else:
        return item

mappedDf2 = myDataframe.map(getTownAndCleanState)
print(mappedDf2)

mappedDf['City']= mappedDf2['Uni']
print(mappedDf)
mappedDf.to_csv('FinalUniversityData.csv')




# Task 17. What is the mean age of users?
valueCountOfage= users['age'].value_counts()
print(valueCountOfage.tail(10))
# Task 18. What is the age with least occurrence?
