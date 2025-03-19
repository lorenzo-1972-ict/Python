# script to manipulate lists

lst = list()
emptyList = list()
print(len(emptyList))

emptyList = []
print(len(emptyList))

tes = [234,True,{"name":"Thomas","surname":"Dulcer"}, [34,56]]

print(tes[3])
print(tes[3][1])
print(len(tes),"\n")

######################################################################################

fruits = ['banana', 'orange', 'mango', 'lemon']
allFruits = fruits [0:4]
print(allFruits)
allFruits = fruits [0:]
print(allFruits,"\n")

allFruits = fruits [0:2:4]
print(allFruits)

allFruits = fruits.pop()
print(fruits)
print(allFruits,"\n")

allFruits= fruits.append(allFruits)
print(fruits)
print(allFruits,"\n")

orangeMango = fruits[1:3]
print(orangeMango)
orangeMangoLemon = fruits[1:]
print(orangeMangoLemon)
orangeLemon = fruits[:2]
print(orangeLemon,"\n")
reserveFruits = fruits[::-1]

######################################################################################

vegetables = ['tomato', 'potato', 'salade', 'ognons', 'carrot']
techno = ['html', 'css', 'js']
countries = ['Finland','Estonia']