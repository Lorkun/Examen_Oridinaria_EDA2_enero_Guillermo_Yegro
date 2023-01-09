class artefactosvaliosos:
    def __init__(self, peso, nombre, precio, fecha):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha = fecha
        print("Se ha creado correctamente el artefacto")
    def __str__(self):
        cadena=str(self.peso)+","+self.nombre+","+str(self.precio)+","+str(self.fecha)
        return cadena
    def __gt__(self, persona):
        return self.fecha > persona.fecha
    
tesoro = artefactosvaliosos(1, 'lecheazul', 15, 25)
kaiber = artefactosvaliosos(0.5, "Cristal Kaiber", 100000000, 0)
womprat = artefactosvaliosos(15, 'Womprat', 22, 17)

