class FtpClient:
	def __init__(self,host,port):
		self.host=host
		self.port=port
		self.conn='xxx'

	def interactive(self):
		while True:
			cmd=input('>>: ').strip()
			if not cmd: continue
			cmd_l=cmd.split()
			print(cmd_l)
			if hasattr(self,cmd_l[0]):
				func=getattr(self,cmd_l[0])
				func(cmd_l)

	def get(self,cmd_l):
		print('getting....',cmd_l)

	def put(self,cmd_l):
		print('putting....',cmd_l)


client=FtpClient('1.1.1.1',23)
client.interactive()