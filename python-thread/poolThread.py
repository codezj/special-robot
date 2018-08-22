from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time,random,os

def task(n):
		print('%s is running' %os.getpid())
		time.sleep(random.randint(1,3))
		return n**2

def handle(res):
		print('handle res %s ' %res)


if __name__=='__main__':
	pool=ProcessPoolExecutor(2)
	for i in range(5):
		res=pool.submit(task,i).result()
		handle(res)


	pool.shutdown(wait=True)
	print('main')