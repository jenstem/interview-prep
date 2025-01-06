# Create a Queue with Queue Module - FIFO Queue w Queue Class


import queue as q

customQueue = q.Queue(maxsize=3)
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.qsize())