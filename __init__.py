import PhotoBooth
import threading

booth 	= PhotoBooth.PhotoBooth()

try:

  threading.Thread(target=booth.sleep(), args=()).start()

except KeyboardInterrupt:
	print('KEYBOARD INTERRUPT\n')
except Exception as e:
	print(e)
finally:
	print('thanks for using our photo booth!')
	booth.destroy()
