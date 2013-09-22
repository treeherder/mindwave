import mindwave, time

h1 = mindwave.Headset('/dev/tty.MindWaveMobile-DevA', '9402')
h2 = mindwave.Headset('/dev/tty.MindWaveMobile-DevA-1', '771c')
time.sleep(2)

h1.connect()
print "Connecting h1..."
while h1.status != 'connected':
    time.sleep(0.5)
    if h1.status == 'standby':
        h1.connect()
        print "Retrying connect..."
print "Connected h1."

h2.connect()
print "Connecting h2..."
while h2.status != 'connected':
    time.sleep(0.5)
    if h2.status == 'standby':
        h2.connect()
        print "Retrying connect..."
print "Connected h2."

while True:
    print "Attention 1: %s, Meditation 1: %s" % (h1.attention, h1.meditation)
    print "Attention 2: %s, Meditation 2: %s" % (h2.attention, h2.meditation)
