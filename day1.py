count = 0
f = open('input.txt')
data = f.read().splitlines()
data = [int(i) for i in data]
window = []

for i in range(len(data)-2):
    window.append([data[i] + data[i+1] + data[i+2]])
    
for x in range(len(window)-1):
    if (window[x+1] > window[x]):
        count = count + 1
            
print(count)
