class stormtrooper:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print("Se ha registrado el Stormtrooper correctamente")
    def clasificador(self, legion, cohorte, siglo, escuadra, trooper):
        print(legion," - ",cohorte,siglo,escuadra,trooper)
    
        
pepe = stormtrooper("pepe", "general").clasificador("TK", 5, 6, 7, 9)
juan = stormtrooper("juan", "coronel").clasificador("TK", 5, 6, 8, 9)
felipe = stormtrooper("akbar", "almirante").clasificador("TK", 5, 5, 8, 9)

