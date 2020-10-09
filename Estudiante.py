class Estudiante():
    def __init__(self,nombre,codigo):
        self.__Nombre=nombre
        self.__Codigo=codigo
    def getName(self):
        return self.__Nombre


Carlos=Estudiante("Carlos","12")
print(Carlos.getName())
