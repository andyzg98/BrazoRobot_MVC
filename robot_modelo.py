class BrazoModelo: #creo mi clase principal  #metodo contructor 
    def __init__(self):
      #atributo de brazo 
        self.angulos = [0, 0, 0] # ángulos de los tres motores
#metodo modoficar 
    def set_angulo(self, motor, angulo):
        self.angulos[motor] = angulo
#metodo  obtener 
    def get_angulo(self, motor):
        return self.angulos[motor]
