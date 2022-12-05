import os
import itertools
path = os.getcwd()
file_name = path + r'\result.txt'
file = open(file_name,'w')
teamA = ['大明','大花','大寶','大頭']
teamB = ['小明','小花','小寶','小頭']
combinationA = itertools.combinations(teamA,2)
combinationB = itertools.combinations(teamB,2)
products = itertools.product(combinationA,combinationB)
count = 0
for i in products:
    count = count + 1
    file.write(str(i)+'\n')
    print(i)
print("共",count,"種組合")