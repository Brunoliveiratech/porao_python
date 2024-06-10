import time 
def contador(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer) 
        time.sleep(1) 
        t -= 1
  
  
t = 300
contador(t)