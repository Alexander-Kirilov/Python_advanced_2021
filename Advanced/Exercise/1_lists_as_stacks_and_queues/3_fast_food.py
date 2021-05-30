from collections import deque

quantity_of_food = int(input())
order_queue = deque()

for order in input().split():
    order_queue.append(int(order))

max_order = max(order_queue)

for i in range(len(order_queue)):
    order = order_queue.popleft()
    if order <= quantity_of_food:
        quantity_of_food -= order
    else:
        order_queue.appendleft(order)
        break

print(max_order)
if len(order_queue) == 0:
    print('Orders complete')
else:
    print('Orders left:', ' '.join([str(order) for order in order_queue]))
