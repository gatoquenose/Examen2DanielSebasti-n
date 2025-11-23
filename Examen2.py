class MiClase:
    def __init__(self, Valencia, Tempo, Tonos, listaCanciones, listaBailabilidad):
        self.Valencia = Valencia
        self.Tempo = Tempo
        self.Tonos = Tonos
        self.listaCanciones = listaCanciones
        self.listaBailabilidad = listaBailabilidad

    def ObtieneValencia(self, numero): # Verifica los digitos impares de un número
        
        numero_str = str(numero)
        digitos_impares = []
        for digit in numero_str:
            numero_entero = int(digit)
            if numero_entero % 2 != 0: 
                digitos_impares.append(numero_entero)

        return len(digitos_impares)

    def DivisibleTempo(self, numero): # Obtiene divisores de la variable numero
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return divisores

    def ObtieneMasBailable(self, lista): # Obtiene el número mayor de una lista
        if not lista:
            return None


        mayor = lista[0]
        for elemento in lista:
            if elemento > mayor:
                mayor = elemento

        return mayor

    def VerificaListaCanciones(self, lista): # Verifica si la lista de canciones es válida, != none
        for song in lista:
            if song is None:
                return False
        return True


################################################################################################
# Ejemplo de ejecución
objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])

print(objeto.ObtieneValencia(1234567))       # Esperado: 4
print(objeto.DivisibleTempo(10))             # Esperado: [1, 2, 5, 10]
print(objeto.ObtieneMasBailable([0.8, 0.9, 0.7]))  # Esperado: 0.9
print(objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]))  # Esperado: True
