# http://www.leancrew.com/all-this/2010/08/random-sampling-with-python/

import mindwave, time

P = 100

def s_avg(N):
  stream = []
  stream.append(N)
  if len(stream) > P:
    # Only average the last P elements of the stream
    del(stream[:1])
  elif len(stream) == 0:
    average = 0
  else:
    sum = 0
    for n in stream:
      sum = sum + n
      average = sum / len(stream)
  return (average)

headset = mindwave.Headset('/dev/tty.MindWaveMobile-DevA', '9402')
headset.disconnect()  #clear any previous activity
headset.connect()

while True:
 print( "attention average :   {0}\r\n".format(s_avg(headset.attention)))
 print( "meditation average:   {0}\r\n".format(s_avg(headset.meditation)))
