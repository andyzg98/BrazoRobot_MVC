 # Importar las clases del modelo, vista y controlador
from modelo import BrazoModelo
from vista import BrazoVista
from controlador import BrazoControlador 

# Crear una instancia del modelo, vista y controlador
modelo = BrazoModelo()
vista = BrazoVista()
controlador = BrazoControlador(modelo, vista)

# bucle infinito  principal del programa
while True:
    # Mostrar el estado actual del brazo robótico
    controlador.mostrar_estado()

    # Leer los nuevos ángulos del usuario por teclado
    controlador.actualizar_estado()
  
  
'''# Creamos el modelo, la vista y el controlador 
#modelo = clase modelo para aceder a sus atributos y metodos 
modelo= BrazoModelo()
vista= BrazoVista()
controlador= BrazoControlador()
# Ejecutamos el controlador 
controlador.mostrar_estado()
# Escribimos un nuevo dato en el archivo 
vista.leer_angulos()
vista.mostrar_estado()

#new_data = "25.6" new_data=str(aleatorio) controller.set_data(new_data)
# Obtenemos el dato actualizado 
controlador.actualizar_estado()
'''