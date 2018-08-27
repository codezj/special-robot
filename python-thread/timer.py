import threading

def fun_timer():
    print('hello timer')
    global timer
    timer = threading.Timer(60,fun_timer) #each 60 seconds run
    timer.start()



timer = threading.Timer(1,fun_timer)
timer.start()
