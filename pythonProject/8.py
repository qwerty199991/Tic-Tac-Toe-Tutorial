name = "Andrey_Sokolov"
first_name = name[:6]
last_name = name[7:]
funky_name = name[::2]
reversed_name = name[::-1]


print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


website = "http://google.com"
website2 = "http://wikipedia.com"
slice1 = slice(7, -4)
print(website[slice1])
print(website2[slice1])
