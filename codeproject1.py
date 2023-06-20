import random

print('How much time do you have in your day to do work?')
total = input()
totalint = (int(total))
print("You have "+ total +" hours to compete your tasks")
print('How many tasks do you have to do?')
numtask = input()
print("You need to do " + numtask +" number of tasks in " + total + " hours")
tasks = []
times = []
ans = "yes"
print("Do you have a new task?")
ans = input()

while ans != "no":
    print("What is the task?")
    task = input()
    tasks.append(task)
    print("How much time will it take to complete this task?")
    time = input()
    times.append(time)
    print("Do you have a new task?")
    ans = input()
    
print(tasks)
print(times)
resettimes = [eval(i) for i in times]
totaltasks = len(times)
sum = 0 

for x in resettimes:
    sum = sum + x 
print(sum)


settimes = set()
settasks = set()
for x in times:
        settimes.add(x)
for x in tasks:
        settasks.add(x)

def randomize():
    # print(settimes)
    # print(settasks)
    order = []
    ordertime = []
    while len(order) < totaltasks: 
        x = settasks.pop()
        order.append(x)
        y = settimes.pop()
        while (tasks.index(x)!= times.index(y)):
            settimes.add(y)
            y = settimes.pop()
        ordertime.append(y)   
    print(order)
    print(ordertime)
    print("")
    for x in times:
        settimes.add(x)
    for x in tasks:
        settasks.add(x)

    
if sum > totalint:
    print("You do not have the time to do all of these tasks")
    exit()
else:
    print("Yes you can complete these tasks in the time")
print("First option:")

randomize()


print("Second option: ")

randomize()


print("Third option")
randomize()

# print("Fourth option")
# randomize()

# print("Fifth option")
# randomize()


    

        
            






    
    
    
