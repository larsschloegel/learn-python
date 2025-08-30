print(True & True) 
print("1 True")

print(False & True)
print("2 False")

print(1 == 1 & 2 == 1)
print("3 False")

print("test" == "test")
print("4 True")

print(1 == 1 | 2 != 1)
print("5 False")
# tricky one bitweises or zuerst, Kettenverleichoperation, Vergleichsketter -> 1 == 3 != 1

print(True & 1 == 1)
print("6 True")

print("test" == "testing")
print("7 False")

print(1 != 0 & 2 == 1)
print("8 False")

print("test" != "testing")
print("9 True")

print("test" == 1)
print("10 False")

print(not(True & False))
print("11 True")

print(not(1 == 1 & 0 != 1))
print("12 True")

print()

