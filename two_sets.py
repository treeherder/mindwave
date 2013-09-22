import mindwave, time

h1 = mindwave.Headset('/dev/tty.MindWaveMobile-DevA', '9402')
h2 = mindwave.Headset('/dev/tty.MindWaveMobile-DevA-1', '771c')
time.sleep(2)

h1.connect()
h2.connect()

while True:
    print "Attention 1: %s, Meditation 1: %s" % (h1.attention, h1.meditation)
    print "Attention 2: %s, Meditation 2: %s" % (h2.attention, h2.meditation)
