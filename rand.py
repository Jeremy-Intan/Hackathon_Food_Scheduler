from random import randint

probability = [[1,1,1,1,1,1,1,31,31,31],
               [1,1,1,1,1,11,21,21,21,21],
               [10,10,10,10,10,10,10,10,10,10],
               [31,31,31,1,1,1,1,1,1,1],
               [31,31,31,1,1,1,1,1,1,1],
               [31,31,31,1,1,1,1,1,1,1],
               [31,31,31,1,1,1,1,1,1,1],
               [10,10,10,10,10,10,10,10,10,10]]

def randNew(hour):
    outHour = []
    
    for i in range(0, len(probability[hour])):
        outHour.append(0);
        
    x = randint(1, 100)
    for i in range(0, len(probability[hour])):
        if x <= probability[hour][i]:
            outHour[i] = 1
            break
        else:
            x = x - probability[hour][i]

    return outHour
for i in range(0, 10):
    for i in range(0, 8):
        print(randNew(i))     
    
