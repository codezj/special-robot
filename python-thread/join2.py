from multiprocessing import Process
import time
import os

def task(n):
	print('%s is running' %os.getpid())
	time.sleep(n)
	print('%s is done'  %os.getpid())


if __name__=='__main__':
	start_time=time.time()
	p1=Process(target=task,args=(1,))
	p2=Process(target=task,args=(2,))
	p3=Process(target=task,args=(3,))



	tsk=[]
	tsk.append(p1)
	tsk.append(p2)
	tsk.append(p3)

	for tt in tsk:
		tt.start()
		tt.join()
	stop_time=time.time()
	print('main',(stop_time-start_time))