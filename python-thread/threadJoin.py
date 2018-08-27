import threading, time
def doWaiting():
	print('start waiting1: '+ time.strftime('%H:%M:%S') + "\n" )
	time.sleep(3)
	print('stop waitting1: '+ time.strftime('%H:%M:%S') + "\n")


def doWaiting1():
	print('start waiting2: '+ time.strftime('%H:%M:%S') + "\n" )
	time.sleep(8)
	print('stop waitting2: '+ time.strftime('%H:%M:%S') + "\n")


tsk=[]

thread1=threading.Thread(target=doWaiting)

thread1.start()

tsk.append(thread1)

thread2=threading.Thread(target=doWaiting1)

thread2.start()

tsk.append(thread2)

print('start join: '+ time.strftime('%H:%M:%S')+ "\n")


for tt in tsk:
	tt.join()
	print(tt.is_alive())
	# tt.join(2)

print('end join: '+ time.strftime('%H:%M:%S')+ "\n")





