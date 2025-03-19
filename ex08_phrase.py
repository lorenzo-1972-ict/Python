phrase1 = """
        azerty uiop qsdfg hjklm wxcvbn
        """
phrase2 = "azerty uiop \nqsdfg hjklm \nwxcvbn\n"

phrase3 = "azerty uiop \nqsdfg hjklm \twxcvbn\n"

print(phrase1)
print(phrase2)
print(phrase3)
print(str.split(phrase1))

s = slice (2,-5)
print(phrase3[s])

print(phrase3[10])