from queue import Queue
q = Queue(maxsize=5)
print(q.qsize())
q.put('Chef')
q.put('Lawyer')
q.put('Dentist')
q.put('Teacher')
q.put('Architect')

print(q.qsize())

print("\nFull: ", q.full()) 
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())
print(q.qsize())

