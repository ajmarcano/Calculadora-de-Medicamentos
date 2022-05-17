def main():
    while True:
        def wait_input(): #Pantalla que aparece despues de calcular tu medicamento, "Si" va a repetir el programa, "No" va a terminarlo
            wait_input = input("¿Desea calcular otro medicamento? Si / No: \n")
            if wait_input == "Si" or wait_input == "si":
                return(True)
            elif wait_input == "No" or wait_input == "no":
                return(False)

        try: #Primera pantalla, elige el medicamento que vas a calcular colocando el numero del medicamento
            pregunta = input("¿Qué medicamento desea calcular? \
                        \n1. Amoxicilina \
                        \n2. Azitromicina \
                        \n3. Cefalexina \
                        \n4. Difenhidramina \
                        \n5. Ibuprofeno al 2% \
                        \n6. Ibuprofeno al 4% \
                        \n7. Metronidazol \
                        \n")


            pregunta_int = int(pregunta)

        except: 
            print("¡Debes escribir un número!") #Si no introducen un numero crea esta excepcion y repite el programa
            continue
            
        peso = input("¿Cuál es el peso del paciente? ")
        
        try:
            class Medicamentos(): #Clase principal donde se guardan todos los medicamentos como objetos y contiene el algoritmo para calcular la dosis de acuerdo al peso del paciente
                def __init__(self, nombre, dosis, ml, mg, frecuencia, horas):
                    self.nombre = nombre
                    self.dosis = dosis
                    self.ml = ml
                    self.mg = mg
                    self.frecuencia = frecuencia #cada 8, 12 o 24 horas
                    self.horas = horas #Divide la dosis final en 1, 2 o 3 dependiendo de la frecuencia en la que se toma el medicamento
            
                def Calc_Peso(self):
                    dosis = float(peso) * self.dosis * self.ml / self.mg / self.horas
                    dosis_redon = "{:.1f}".format(dosis)
                    print("La dosis de " + self.nombre + " es " + str(self.dosis) + "mg por kg = " \
                        + str(dosis_redon) + "cc cada " + str(self.frecuencia) + " horas\n")


            Amoxicilina = Medicamentos("Amoxicilina", 80, 5, 500, 8, 3)
            Azitromicina = Medicamentos("Azitromicina", 10, 10, 200, 24, 1)
            Cefalexina = Medicamentos("Cefalexina", 50, 5, 500, 8, 3)
            Ibuprofeno_al_2 = Medicamentos("Ibuprofeno al 2%", 10, 100, 2000, 8, 1)
            Ibuprofeno_al_4 = Medicamentos("Ibuprofeno al 4%", 10, 100, 4000, 8, 1)
            Difenhidramina = Medicamentos("Difenhidramina", 1.25, 5, 12.5, 6, 1)
            Metronidazol = Medicamentos("Metronidazol", 30, 5, 125, 8, 3)

            if pregunta_int == 1:
                Amoxicilina.Calc_Peso()
                if wait_input() == True:
                    continue
                else:
                    quit()
            elif pregunta_int == 2:
                Azitromicina.Calc_Peso()
                if wait_input() == True:
                    continue
                else:
                    quit()
            elif pregunta_int == 3:
                Cefalexina.Calc_Peso()
                if wait_input() == True:
                    continue
                else:
                    quit()
            elif pregunta_int == 4:
                Difenhidramina.Calc_Peso()
                if wait_input() == True:
                    continue
                else:
                    quit()
            elif pregunta_int == 5:
                Ibuprofeno_al_2.Calc_Peso()
                if wait_input() == True:
                    continue
                else:
                    quit()
            elif pregunta_int == 6:
                Ibuprofeno_al_4.Calc_Peso()
                if wait_input() == True:
                    continue
                else:
                    quit()
            elif pregunta_int == 7:
                Metronidazol.Calc_Peso()
                if wait_input() == True:
                    continue
                else:
                    quit()

        except Exception as e:
            print("¡Debes escribir un número!\n")
            continue

if __name__ == "__main__":
   main()
