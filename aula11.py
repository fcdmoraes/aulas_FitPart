class Tempo(object):
	def __init__(self, hora=0, minuto=0, seg=0):
		self.hora = hora
		self.min = minuto
		self.seg = seg
		self.update()

	def __repr__(self):
		return "{:02}:{:02}:{:02}".format(self.hora, self.min, self.seg)

	def update(self):
		while self.seg >= 60:
			self.seg -= 60
			self.min += 1
		while self.min >= 60:
			self.min -= 60
			self.hora += 1
		while self.hora >= 24:
			self.hora -= 24

	def em_seg(self):
		return self.hora*60*60 + self.min*60 + self.seg

	def __add__(self, other):
		soma = Tempo()
		soma.hora = self.hora + other.hora
		soma.min = self.min + other.min
		soma.seg = self.seg + other.seg
		soma.update()
		return soma

if __name__ == '__main__':
	t1 = Tempo(hora=15, minuto=20, seg=40)
	print(t1)

	t2 = Tempo(seg=180)
	print(t2)

	print(t1.hora)
	print(t1.em_seg())

	t3 = Tempo(minuto = 45)

	print((t1+t2+t3).em_seg())



# t1 = Tempo(hora=15, minuto=20, seg=40)
# print(t1)