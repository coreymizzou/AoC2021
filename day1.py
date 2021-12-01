part1 = 0
part2 = 0

#put input file of numbers into list
f = open('input.txt')
data = f.read().splitlines()
data = [int(i) for i in data]
window = []

#part 1 checks if next item in list is greater than current item
for i in range(len(data)-1):
    if(data[i+1] > data[i]):
        part1 = part1 + 1
print(part1)
        


#part 2 checks if sum of 3 consecutive items in list are greater than previous sum of 3 items
for i in range(len(data)-2):
    window.append([data[i] + data[i+1] + data[i+2]])
    
for x in range(len(window)-1):
    if (window[x+1] > window[x]):
        part2 = part2 + 1
            
print(part2)
