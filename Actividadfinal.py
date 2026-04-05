from abc import ABC, abstractmethod

class Dispositivo(ABC):

    def __init__(self, nombre, marca):
        self.nombre = nombre
        self.marca = marca

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Wifi:

    def __init__(self, red):
        self.red = red

    def conectar_wifi(self):
        return f"Conectado a la red WiFi: {self.red}"


class Bateria:

    def __init__(self, porcentaje):
        self.porcentaje = porcentaje

    def estado_bateria(self):
        return f"Batería al {self.porcentaje}%"


class DispositivoInteligente(Dispositivo, Wifi, Bateria):

    def __init__(self, nombre, marca, red, porcentaje, volumen):
        Dispositivo.__init__(self, nombre, marca)
        Wifi.__init__(self, red)
        Bateria.__init__(self, porcentaje)

        self._volumen = volumen  

   
    @property
    def volumen(self):
        return self._volumen

   
    @volumen.setter
    def volumen(self, nuevo_volumen):
        if 0 <= nuevo_volumen <= 100:
            self._volumen = nuevo_volumen
        else:
            print("Error: El volumen debe estar entre 0 y 100")

   
    def encender(self):
        return f"{self.nombre} se ha encendido correctamente."

    def __str__(self):
        return f"Dispositivo: {self.nombre} - Marca: {self.marca} - Volumen: {self._volumen}"



if __name__ == "__main__":

   
    dispositivo1 = DispositivoInteligente("Alexa", "Amazon", "Casa_Wifi", 80, 30)
    dispositivo2 = DispositivoInteligente("Google Home", "Google", "Oficina_Wifi", 60, 50)
    dispositivo3 = DispositivoInteligente("Echo Dot", "Amazon", "Habitacion_Wifi", 90, 20)

    
    print(dispositivo1.encender())
    print(dispositivo2.encender())
    print(dispositivo3.encender())

    print("\n--- Información de dispositivos ---")
    print(dispositivo1)
    print(dispositivo2)
    print(dispositivo3)

    print("\n--- Funciones adicionales ---")
    print(dispositivo1.conectar_wifi())
    print(dispositivo1.estado_bateria())

  
    print("\n--- Encapsulamiento ---")
    print("Volumen actual:", dispositivo1.volumen)

    dispositivo1.volumen = 70
    print("Nuevo volumen:", dispositivo1.volumen)

    dispositivo1.volumen = 150  