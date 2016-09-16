import numpy as np
import time
import os
import random
import uuid
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#This is the laboratory streaming library
from pylsl import StreamInfo, StreamOutlet
#scikit-learn machine learning package
from sklearn import datasets
#to import pngs into plotter
import matplotlib.image as mpimg
from termios import tcflush, TCIFLUSH
import time,sys

def getRandomFile(path):
	files = os.listdir(path)
	index = random.randrange(0, len(files))
	return files[index]

#calibration and stream settings
warmup_trials = 10
trials_per_class = 60
perform_time = 3.5
wait_time = 1
pause_every = 30
pause_duration = 10
fontsize = 30

labels = []
markers = []

dir = 'images/'
for filename in os.listdir(dir):
	fname = os.path.join(dir, filename)
	labels.append(fname)
	markers.append(os.path.splitext(filename)[0])

matplotlib.rcParams.update({'font.size': fontsize})

info = StreamInfo(name='MotorImag-Markers', type='Markers', channel_count=1,
                  nominal_srate=0, channel_format='string',
                  source_id='t8u43t98u')
outlet = StreamOutlet(info)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_yticklabels([''])
ax.set_xticklabels([''])
plt.ion()
plt.show()

for trial in range(1, warmup_trials+trials_per_class*len(labels)+1):
	choice = random.choice(range(len(labels)))
	print "molecule index is", choice
	print "molecule path is", labels[choice]
	print "molecule label is", markers[choice]
	im = plt.imread(labels[choice])
	img = ax.imshow(im)
	plt.draw()
	accept = raw_input('Next? ')
	
	if trial == warmup_trials:
		#print "warmup trials are over"
		outlet.push_sample(['calib-begin'])
	if trial > warmup_trials:
		#print "this is a real trial"
		outlet.push_sample([markers[choice]])
		print "I just pushed sample", markers[choice]
		
		if trial % pause_every == 0:
			#print ('pause!')
			outlet.push_sample(['break-begin'])
			im = plt.imread('break.png')
			img = ax.imshow(im)
			plt.draw()
			accept = raw_input('Let\'s take a short break. ')
			time.sleep(pause_duration)
			tcflush(sys.stdin, TCIFLUSH)
			accept = raw_input('ready to continue?' )
			outlet.push_sample(['break-end'])

			
print "you're done! Good job!"
			
outlet.push_sample(['calib-end'])




