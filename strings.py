#string quotes 
from pickletools import string4


st="python's good"
st1='python is "good"'
st2=''' 
Hello,Katha

You are a very beautiful person.Nice face.
And have a good heart as well.May God bless you and your fam.

Love ,
Katha :)

'''
print(st) 
print(st1)
print(st1[-1])#0=1st,1=2nd, -1=last,-2=2nd last...
print(st2)

#printing certain interval
name="Rebecca"
print(name[1:-1])
print(name[:])

#formatted string
fn='Sooka'
ln='Pooka'
print(f'{fn}[{ln}]is a coder')

#inbuilt methods
string4='Peru'
string5='mY tuMMY fill with Yum'
print(string4.upper())
print(string4.lower())
print(len(string4))
print(string4.find("P"))
print(string4.find("Lulu"))#returns -1 since doesn't exists
print(string4.replace('Pe','R e'))
print(string4.replace('Le','Re'))
print(string5.title())
print('Pe' in string4)




