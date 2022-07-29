import pandas as pd
XYZ_web ={'Day':[1,2,3,4,5,6],'Visitors':[1000,2000,3000,4000,5000,6000],'Bounce_rate':[20,20,23,50,34,10]}

df=pd.DataFrame(XYZ_web)
print(df)

"""Slicing"""
print("Slicing: ")
print("Head: ")
print(df.head(2))
print("Tail: ")
print(df.tail(2))

"""Merging"""
print("Merging: ")
df1=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},index=[2001,2002,2003,2004])
df2=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},index=[2005,2006,2007,2008])
merge=pd.merge(df1,df2,on="HPI")
print(merge,"\n")

"""Joining"""
print("Joining: ")
df1=pd.DataFrame({"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},index=[2001,2002,2003,2004])
df2=pd.DataFrame({"Low_Tier_HPI":[50,45,67,34],"Unemployment":[50,45,45,67]},index=[2001,2003,2004,2004])
join = df1.join(df2)
print(join,"\n")

# """Changing Index and Column Heading"""
# print("Changing Index:")
# import pandas as pd
# df=({"Day":[1,2,3,4],"Visitors":[200,100,230,300],"Bounce_Rate":[20,45,60,10]})
# df=df.set_index("Day", inplace=True)
# print(df,"\n")
#
# print("Conver Column Heading")
# df=df.rename(columns={"Visitors":"Users"})
# print(df)

"""Concatenation"""
print("Concatenation:")
import pandas as pd
df1=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"US_GDP_Thousands":[50,45,45,67]},index=[2001,2002,2003,2004])
df2=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"US_GDP_Thousands":[50,45,45,67]},index=[2005,2006,2007,2008])
concat =pd.concat([df1,df2])
print(concat,"\n")

"""Python for Statistics"""
print("Statistics mean:")
from statistics import mean

print(mean([1,2,2,2,1,3,4,1,5]),"\n")
print("Statistics median:")
from statistics import median
print(median([1,1,1,2,2]),"\n")

print("Statistics mode:")
from statistics import mode
print(mode([1,1,1,2,2]),"\n")

print("Statistics variance:")
from statistics import variance
print(variance([1,1,1,2,2]),"\n")

s




