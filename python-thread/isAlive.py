from multiprocessing import Process
import time

n=100

def task():
	global n
	time.sleep(5)
	n=0

if __name__=='__main__':
	p=Process(target=task)
	p.start()
	print(p.is_alive())
	p.join(4)
	print(p.is_alive())
	print('main',n)