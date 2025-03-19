# script to illustrate the usage of tuple

#1
family = ()

#2
brothers = ("Charles", "Andrew", "Edward")
sisters = ("Ann",)

#3
siblings = brothers + sisters
print("\nMy siblings: ", siblings,"")

#4
print("\nI have", len(brothers),"brothers and", len(sisters),"sisters")

#5
parents = ("Albert", "Elizabeth")
print("\nMy parents:", parents)

siblings += parents

family = siblings
print("\nMy family:", family,"\n")

#6
l1 = len(brothers)
l2 = len(sisters)
l3 = len(parents)

tupleFamily1 = family[0:l1]
tupleFamily2 = (family[l1:l1+l2])
tupleFamily3 = family[l1+l2:]

print(tupleFamily1)
print(tupleFamily2)
print(tupleFamily3)