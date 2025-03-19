# script to illustrate usage of tuples

#1
fruits = ("banana", "mango", "orange", "lemon", "apple")
vegetables = ("carrot", "potato", "peas")
poultry = ("chicken", "turkey", "duck")

fvp = fruits + vegetables + poultry
print("\n",fvp,)

#2
fvp = list(fvp)
print("\n",fvp)
print(type(fvp))

#3
fvpBorders = fvp[1:-1]
print("\n",fvpBorders)

#4
fvp3Wide = fvp[0:3] + fvp[-3:]
print("\n",fvp3Wide)

#5
fvp = ()

#6
print("\nList contains",len(fvp),"elements.\n",)