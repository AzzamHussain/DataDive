import pandas as pd
data={'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
      'Age':[27, 24, 22, 32],   
      'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
      'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
      'Salary':[10000, 8000, 12000, 9000]}
df=pd.DataFrame(data)
print(df)
print("Describe Statistics:")
print(df.describe())
print("shape:", df.shape)
print("columns:", df.columns)