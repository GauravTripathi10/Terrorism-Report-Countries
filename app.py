import numpy as np
import csv
import matplotlib.pyplot as plt

file_obj=open('terrorismData.csv',encoding='utf-8')
data=csv.DictReader(file_obj,skipinitialspace=True)

killed=[]
wounded=[]
countries=[]

for row in data:
    killed.append(row['Killed'])
    wounded.append(row['Wounded'])
    countries.append(row['Country'])

np_killed=np.array(killed)
np_wounded=np.array(wounded)
np_country=np.array(countries)

# Masking the number of killed to replace the empty value
mask1=(np_killed=='')
# print(mask)
np_killed[mask1]='0.0' #for killed
# print(np_killed)

# Masking the number of wounded to replace the empty value
mask2=(np_wounded=='')
np_wounded[mask2]='0.0'   #for wounded

np_killed=np.array(np_killed, dtype=float) # to convert string to float
np_wounded=np.array(np_wounded, dtype=float) # to convert string

killed_wounded=np_killed+np_wounded  #total number of killed and wounded

# Masking for countries:
mask_India=(np_country=='India')
mask_United_States=(np_country=='United States')
mask_Japan=(np_country=='Japan')
mask_Italy=(np_country=='Italy')
mask_Russia=(np_country=='Russia')

#for value only for sepecified country
ans_India=killed_wounded[mask_India]
ans_United_States=killed_wounded[mask_United_States]
ans_Japan=killed_wounded[mask_Japan]
ans_Italy=killed_wounded[mask_Italy]
ans_Russia=killed_wounded[mask_Russia]

#Sum for all countries

sum_India=np.sum(ans_India)
sum_United_States=np.sum(ans_United_States)
sum_Japan=np.sum(ans_Japan)
sum_Italy=np.sum(ans_Italy)
sum_Russia=np.sum(ans_Russia)

catlog_country=['India','United States','Japan','Italy','Russia']
values=[sum_India,sum_United_States,sum_Japan,sum_Italy,sum_Russia]

print(sum_India,sum_United_States,sum_Japan,sum_Italy,sum_Russia)
# Bar Graph
plt.figure(figsize=(10,6))
plt.bar(catlog_country,values,color='blue')
plt.xlabel('country')
plt.ylabel('Total Attacks')
plt.title("Terrorsim Attacks in Different countries")
plt.show()


# PI Chart:

colors=['green','gold','skyblue','lightcoral','lightsteelblue']
explode=(0.1,0,0,0,0)

plt.figure(figsize=(10,6))
plt.pie(
    values,labels=catlog_country,colors=colors,explode=explode,
    autopct='%1.1f%%',shadow=True,startangle=140
)

plt.title("Countries Terrorism Attacks")
plt.show()








