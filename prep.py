# Create a Queue with Queue Module - FIFO Queue w Multiprocessing

from multiprocessing import Queue

customQueue = Queue(maxsize=3)
customQueue.put(1)
print(customQueue.get())