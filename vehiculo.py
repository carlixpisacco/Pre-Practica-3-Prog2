
class Vehiculo:
    def __init__(self, marca:str, ruedas:int, color:str, enMarcha = False) -> None:
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.enMarcha = enMarcha

    def arrancar(self) -> bool:
        while True:
            print("¿Desea poner en marcha el vehículo?")
            print("1- Si")
            print("2- No")
            opc=int (input("Elija una opción:"))
            if opc == 1:
                self.enMarcha = True
                break
            elif opc == 2:
                break
            else:
                print("Ingrese una opción válida")

        return self.enMarcha

    def tipoVehiculo(self) -> str:
        if self.ruedas == 4:
            return "Automovil"
        else:
            return "Motocicleta"
        
    def mostrar(self) -> None:
        tipo_vehiculo = self.tipoVehiculo()
        estado = "en marcha" if self.enMarcha else "apagado"
        print(f"Marca del vehículo: {self.marca}")
        print(f"Cantidad de ruedas: {self.ruedas}")
        print(f"Tipo de vehículo: {tipo_vehiculo}")
        print(f"Color del vehículo: {self.color}")
        print(f"Estado: el vehículo se encuentra {estado}")

marca = input("Ingrese la marca de su vehículo: ")
ruedas = int(input("Ingrese la cantidad de ruedas de su vehículo: "))
color = input("Ingrese el color de su vehículo: ")

mi_vehiculo = Vehiculo (marca, ruedas, color)

mi_vehiculo.arrancar()
mi_vehiculo.mostrar()



        

    

    