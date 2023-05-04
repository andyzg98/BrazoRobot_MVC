class BrazoControlador:#creo mi clase 
  #constructor (atribitos)
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
#metodo o funcion 
    def actualizar_estado(self):
      #el la variable almaceno el atributo con el metodo leer angulo 
        angulos =self.modelo.leer_angulos()
       # for i in range(3):                       #self.modelo.set_angulo(i,angulos[i])
    #a la vista llamo metodo mostras 
        self.modelo.set_angulo(i,angulos[i]
self.vista.mostrar_estado(self.model.angulos)
