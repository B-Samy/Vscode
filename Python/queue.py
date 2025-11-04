from collections import deque


queue = deque()

queue.append(10)
queue.append(20)

print(f'Queue {queue}')

# dequeue 


print('Deque', queue.popleft())
print('queue after dequeue', queue)




