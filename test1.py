import pyxel
import time
#import PyxelUniversalFont as puf

pyxel.init(200,200)

count=1

#pyxel.images[0].load(0,0,"assets/sample.png")
font = pyxel.Font("assets/k8x12.bdf")
#pyxel.text(10,50,"日本語の表示",7,font)

#writer = puf.Writer("misaki_gothic.ttf")

class app:
	def __init__(self):
		self.count=1
		pyxel.run(self.update, self.draw)

	def update(self):
		pass		

	def draw(self):
		self.count+=1
		now = time.strftime("%H:%M:%S")
		pyxel.cls(0)
		pyxel.text(10, 10,str(self.count), 7)
		pyxel.blt(50, 50, 0, 0, 0, 8, 8, 0)
		pyxel.text(10,50,"日本語の表示",7,font)
		pyxel.text(50, 80, str(now), 7)
		#writer.draw(25, 4, "日本語", 50, 16)


app()
