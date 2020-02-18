# -*- coding: utf-8 -*-
# 避免相对引入
from __future__ import absolute_import

from flask import Flask

# 跳转v1
import v1
from v1 import logs

import threading
import time
from threading import Thread
from threading import Timer

#timer_interval = 10

#def statistics():
#	stcs = logs.info+"|    "+repr(logs.eNBConnected)+"           "+"|    "+repr(logs.UEConnected)+"        "+"    |    "+repr(logs.UEAttached)+"         "+"   |    "+repr(logs.s1uBearer)+"            |"+"\n"\
#                        +"|----------------|-----------------|-----------------|-----------------|\n"
#	print(stcs)
	#print("???????????????????????????????????????????????????????????????????????????????????????????????????????????????/1")
	#print(logs.eNBConnected,logs.UEConnected,logs.UEAttached,logs.s1uBearer)
	#print("???????????????????????????????????????????????????????????????????????????????????????????????????????????????/2")
	#global timer
	#timer = threading.Timer(10.0, statistics)
	#timer.start()	
#	global timer
#	if timer != None:
#		timer.finished.wait(10)
#		timer.function()  
#	else:
#		timer = threading.Timer(10.0, statistics)
#		timer.start()
#def LoopLog():
	#tmr = Timer(timer_interval , statistics)
	#tmr.start()
	#while(True):
		#time.sleep(0.1)
#	time.sleep(0.1)
#	while True:
#		try:
#			time_remaining = time_interval - time.time()%time_interval
#			#statistics()
#			time.sleep(time_remaining)
#			statistics()
#		except (Exception ):
#			#print(e)
#			pass

#timer = threading.Timer(10.0, statistics)

def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        v1.bp,
        url_prefix='/namf-comm/v1')
    return app

if __name__ == '__main__':
	create_app().run(host='0.0.0.0',port=5001,debug=True)
