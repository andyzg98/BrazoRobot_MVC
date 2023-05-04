class BrazoVista:
    def __init__(self):
        pass

    def leer_angulos(self):
        angulos = []
        for i in range(3):
            angulo = input("Ingrese el ángulo del motor {}: ".format(i+1))
            angulos.append(int(angulo))
        return angulos

    def mostrar_estado(self, angulos):
        print("Ángulos de los motores: ", angulos)
