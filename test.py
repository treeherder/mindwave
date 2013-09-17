import mindwave, time

headset = mindwave.Headset('/dev/tty.MindWave')
time.sleep(2)
headset.connect()
