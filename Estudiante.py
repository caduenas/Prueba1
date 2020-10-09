class Estudiante():
    def __init__(self,nombre,codigo):
        self.__Nombre=nombre
        self.__Codigo=codigo
    def getName(self):
        return self.__Nombre
    def setName(self,newName):
        self.__Nombre = newName
        return self.__Nombre

Carlos=Estudiante(str(input("Escriba el nombre del estudiante")),str(input("Escriba el codigo del estudiante")))
print(Carlos.getName())
print(Carlos.setName(input("Nuevo nombre")))