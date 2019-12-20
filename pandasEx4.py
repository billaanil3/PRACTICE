import pandas as pd
import matplotlib.pyplot as plt
import _tkinter

names = ['Bob','Jessica','Mery','John','Merl']
births = [968,155,77,578,973]

BabyDataSet = list(zip(names,births))
print "---------",BabyDataSet
df = pd.DataFrame(data = BabyDataSet , columns = ['Names','Births'])
print df
df.to_csv('births1880.csv',index = False,header = True)

read_data = pd.read_csv("births1880.csv")
print read_data


