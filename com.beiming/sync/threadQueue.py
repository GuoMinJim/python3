# Python 的 Queue模块中提供了同步的、线程安全的队列类
# 包括FIFO队列Queue LIFO 后入先出和优先级队列

import queue
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self,threadID,name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("开启线程：" + self.name)
        process_data(self.name, self.q)
        print("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)
threadList = ["Thread-1","Thread-2","Thread-3"]
nameList = ["one","Two","Three","Four","Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadsID = 1

# 創建新線程
for tName in threadList:
    thread = myThread(threadsID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadsID += 1
# 填充隊列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

#等待队里清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("运行结束 主线程退出")
