dataList = ["apple",100,99.99]
print(dataList)
print(dataList[0])
print(dataList[0:2])
print(len(dataList))
print(dataList[2])

dataList = ["apple",100,99.99]
dataList.remove("apple")
print(dataList)
dataList.insert(1,"Dell")
print(dataList)

dataList = ["apple",100,99.99]
print("apple" in dataList)
print("tesla" in dataList)
dataList.clear()
print(dataList)