import pandas as pd
data={
    "name":['Alice', 'Bob', 'Charlie'],
    "age":[25, 30, 35],
    "city":['New York', 'Los Angeles', 'Chicago']

}
df=pd.DataFrame(data)
print(df)
df.to_csv('people.csv',index=False)