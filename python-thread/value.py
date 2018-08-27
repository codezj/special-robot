from multiprocessing import Process, Value
import time

alive = Value('b', False)

def worker(alive):
	while alive.value:
		time.sleep(0.1)
		print("running")


if __name__=='__main__':
	p=Process(target=worker, args=(alive,))
	alive.value=True
	p.start()
	time.sleep(1)
	alive.value=False


	#p.process.signal(signal.SIGINT)  note: not SIGTERM