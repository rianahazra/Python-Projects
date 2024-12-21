import time
print(time.gmtime(0))
time.sleep(3)
print(time.time())
print(time.ctime(time.time()))
print(time.localtime(time.time()))
print(time.gmtime(time.time()))
