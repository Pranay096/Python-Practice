#strings are immutable 
a = "pranay!!!!!!! pranay!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("pranay", "tanvi"))
print(a.split())
b = "pranaUPP"
print(b.capitalize()) # Capitalize method turn
# only first character into uppercase and the rest into lower case.The string has no effect if the first letter is already upper case
c = "pranay"
print(c.center(50))
print(len(c.center(50)))
print(len(c))
print(a.count("pranay"))
print(a.endswith("!!"))
print(a.title())
print(a.istitle())
d = "Pranay"
print(d.swapcase())
print(a.startswith("pranay"))
print(a.find("a"))
# print(a.index["as"))
print(a.isalnum())
print(a.isalpha())
print(a.isprintable())
print(a.translate("spanish"))