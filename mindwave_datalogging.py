#!/usr/bin/python
import mindwave
import time
import datetime


#create a tsv file_name of YMD of today's date
time_stamp = time.time()
file_name = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d') + '.tsv'
f = open(file_name,'a')

#connect the mindwave
headset = mindwave.Headset('/dev/tty.MindWaveMobile-DevA', '771C')
headset.disconnect()  #clear any previous activity
headset.connect()

while 1 :
  #getting the data
  meditation_data = headset.meditation
  attention_data  = headset.attention

  #printing data to screen
  print( "attention average :   {0}".format(meditation_data))
  print( "meditation average:   {0}\r\n".format(attention_data))

  #create raw and formatted timestamp
  time_stamp = time.time()
  date_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')

  #writing data and timestamp to tab-separated-value file
  f.write(str(time_stamp) + "\t" + str(meditation_data).rstrip("\r\n") + "\t" + str(attention_data).rstrip("\r\n") + "\t"  + str(date_stamp) + "\n")
  f.closed
  time.sleep(1)
  f = open(file_name,'a')

