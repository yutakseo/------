temp = input().split(" ")
temp = temp[1]
numbs = input().split(" ")

loss_numbs = []
print(numbs)
for i in range(len(numbs)):
    if numbs[i] < temp:
        loss_numbs.append(numbs[i])
        
print(loss_numbs)