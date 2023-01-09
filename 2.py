class stormtrooper:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print("Se ha registrado el Stormtrooper correctamente")
    def clasificador(self, legion, cohorte, siglo, escuadra, trooper):
        print(legion," - ",cohorte,siglo,escuadra,trooper)
    def __str__(self):
        cadena=str(self.nombre)+","+self.rango
        return cadena
        
pepe = stormtrooper("pepe", "general")
juan = stormtrooper("juan", "coronel")
felipe = stormtrooper("akbar", "almirante")
tropas = [pepe, juan, felipe]
print(tropas[0], tropas[1], tropas[2])