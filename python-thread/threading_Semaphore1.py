import time
import threading

s1=threading.Semaphore(1)

def foo():
	s1.acquire()
	time.sleep(2)
	print("ok",time.ctime())
	s1.release()

for i in range(20):
	t1=threading.Thread(target=foo,args=())
	t1.start()