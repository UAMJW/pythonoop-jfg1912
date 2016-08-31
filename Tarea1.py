class auto:
	def __init__(self):
		
		self.dinero = 5
		self.precioxlitro = 2
		self.kmxlitro = 5
		self.gasolina = 0
		self.estado_encendido = False
	
	def encender(self, estado):
		if estado == 1:
			if self.gasolina > 0:
				self.estado_encendido = True
				return True
			else:
				self.estado_encendido = False		
				return False
		else:
			self.estado_encendido = False
	def cuenta_x(self):
		
		return "Tu saldo es:%s"%self.dinero

	def cargar_gasolina(self, litros):
		self.litros = litros
		self.cuenta = self.litros*self.precioxlitro
		self.dinero = self.dinero-self.cuenta	
		if self.dinero > 0:
			self.gasolina = a.litros
			self.km_disponibles = self.gasolina*self.kmxlitro
			return True
		else:
			return False
	def avanzar(self, cuadras):
		if self.estado_encendido:
			if cuadras <= self.km_disponibles:
				return True
			else:
				return False
		else:
			return False
a = auto()
if a.encender(1):
	print "Encendido!"
else:
	print a.cuenta_x()
	print "Precio x Litro:", a.precioxlitro, "KM x Litro:", a.kmxlitro
	litros = input("Litros:")
	if a.cargar_gasolina(litros):
		print "Se cargaron:", a.litros, "Litros!"
		print "Tu nuevo saldo es:", a.dinero
		if a.encender(1):
			av = input("KM A AVANZAR? ::> ")
			if a.avanzar(av):
				print "Tienes", a.km_disponibles, "KM para recorrer"
				a.km_disponibles -= av
				print "Vamos a avanzar", av, "km"
				print "Te quedan %sKM"%a.km_disponibles, "ahora"
			else:
				print "No te alcanzan los KM o prende el carro!"
		else:
			print "El auto no se ha encendido..."
	else:
		print "No te alcanza el $"