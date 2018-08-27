from multiprocessing import Process
import time
import os

def task(n):
	print('pid: %s ppid:%s'  %(os.getpid(),os.getppid()))
	time.sleep(n)


if __name__=='__main__':
	p=Process(target=task,args=(15,),name='process1')
	p.start()
	p.terminate()

	print(p.is_alive())
	print('main pid : %s ppid: %s' %(os.getpid(), os.getppid()))
	p.name='xxxxxx'
	print(p.name)