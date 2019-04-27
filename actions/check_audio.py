import os
from pygame import mixer
import time

from Voice import speakmodule
from MySqlite import mysqlite as sq

dirname = os.path.dirname(__file__)
#change this if you are using windows
path=r"C:/Users/Achal_pc/Desktop/VPDA-master/audio/"

filename=''

def check(msg):
	audio_path=sq.select(msg)
	if audio_path:
		#print(len(msg[0:]))
		#print(type(audio_path))
		mixer.init()
		mixer.music.load(audio_path)
		mixer.music.play()
		time.sleep(5)
			
	else:
		temp = path+msg+str(len(msg[0:]))+'.mp3'
		#print(len(msg[0:]))
		filename = os.path.join(dirname,temp) 
		flag= sq.insert(msg,filename)
		speakmodule.speak([msg],len(msg[0:]),mixer)
		time.sleep(3)
