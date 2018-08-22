from multiprocessing import Queue
import threading

class Job(object):
	def __init__(self,priority,description):
		self.priority=priority
		self.description=description
		print('job: ', description)
		return

	def __cmp__(self,other):
		return cmp(self.priority,other.priority)


q=Queue.PriorityQueue()

q.put(Job(3, 'level 3 job'))
q.put(Job(1, 'level 1 job'))
q.put(Job(10, 'level 10 job'))



def process_job(q):
	while True:
		next_job=q.get()
		print("for: ", next_job.description)
		q.task_done()


workers=[threading.Thread(target=process_job,args=())]
