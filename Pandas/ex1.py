import pandas as pd

s1 = pd.Series([1,2])
s2 = pd.Series(['Anil', 'Billa'])
df = pd.DataFrame([s1, s2])
# print df
dframe = pd.DataFrame([[1,2],['Ankush', 'Sid']], index=['r1','r2'], columns=['c1', 'c2'])
# print dframe
dframe = pd.DataFrame({
        "c1": [1, "Ashish"],
        "c2": [2, "Sid"]})
# print dframe

#--------------Read CSV------------
df = pd.read_csv('/home/anil/Desktop/Expense Contracts List.csv')
# print df
# print df.head()
# print df.shape
# print df.iloc[0:5,:]
# print df.iloc[:,:]
# df.iloc[5:,:5]
# print df.describe()
# print df.rank()
# print df.corr()



data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        # 'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df = pd.DataFrame(data)
# print df[['Name', 'Age']]
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
df['Address'] = address
print df
