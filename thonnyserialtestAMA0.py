import serial
from time import sleep,strftime, time
import matplotlib.pyplot as plt

plt.ion()
x = []
y = []

temp = 68


def write_temp(temp):	
	with open("/home/pi/Medella/temphum_log1.csv", "a") as log:
		log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(line)))
def graph(temp):
	y.append(test)
	x.append(time())
	plt.clf()
	plt.scatter(x,y)
	plt.plot(x,y)
	plt.draw()

if __name__ == '__main__':
    ser = serial.Serial('/dev/serial0',9600, timeout=1)
    ser.flush()

with open("/home/pi/Medella/temphum_log1.csv", "a") as log:

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            write_temp(line)
#           graph(temp) 
        sleep(10)

	
