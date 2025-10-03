import pandas as pd
data={'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
      'Age':[27, 24, 22, 32],   
      'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
      'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
      'Salary':[10000, 8000, 12000, 9000]}
df=pd.DataFrame(data)
print(df)
print("Employees whose salary is greater than 9000:")
print(df[df['Salary'] > 9000])
filtered=df[(df['Salary'] > 9000) & (df['Age'] > 23)]
print("Employees whose salary is greater than 9000 and age is greater than 23:")
print(filtered)