a=input("Write your first sentence!: ")
b=input("write your second sentence!: ")
print("> > > I will make a long sentence for you!: " ,a,b)

p=a.split(" ")
q=b.split(" ")
print("> > > I will split your long sentence into a list of words!: " ,p+q)

WORDCOUNT=len(p)
WORDCOUNT2=len(q)
print("> > > i will calculate the total numbers of words in your sentence!: " ,WORDCOUNT,WORDCOUNT2)

e = sorted((a).split(),key=str.lower)
f = sorted((b).split(),key=str.lower)
print("> > > I will sort the words from first sentence in alphabetical order and print sentence")
print("> > > I will sort the words from second sentence in alphabetical order and print sentance")

Dictionary ={}
for I in range (len(p+q)):
    Dictionary[I] = (p+q)[I]
print("> > > I will display your Dictionary!: ",Dictionary)
