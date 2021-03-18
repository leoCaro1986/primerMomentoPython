def averageStudent():
    average = 0
    averageNote = 0
    for j in range(1,6):
        while True:
            try:
                average =  float(input(f"Ingrese nota {j}: "))
                if average < 0:
                    print("Debes escribir un número positivo.")
                else:           
                    if average > 5:
                        print("Debes escribir una nota menor a 5")
                    else:
                        averageNote = averageNote + average
                        break
            except ValueError:
                print("Debes escribir un número.")
    averageNote = averageNote / 5
    return averageNote

def existData(program,listProgram):
    exists = False
    for i in listProgram:
        for l in i:
            if l == program:
                exists = True
    return exists            


def searchData(student,item):
        programDictionary= []
        # search_age = input("Provide age")
        for value in student:
            for valueList in value.values():
                if valueList == item:
                    programDictionary.append(value) 
        return programDictionary  
def countItem(result):
    item = 0
    for l in result:
        item+=1
    return item    

def countWomenProgram(result):
    women = 0
    for w in result:
        if w.get("sexo") == "m":
            women +=1
    return women

def countMenProgram(result):
    men = 0
    for w in result:
        if w.get("sexo") == "h":
            men +=1
    return men

numAlumnos = 0
listProgram = []
existsProgram = False
sw = 0  
edad =0
totalMatriculados =0
nombreValid = 0
promEdad = 0
opcion = 0
edadValid = 0
alumValid = 0
menuValid = 0
sexValid = 0
newStudent  = 0
countWomen=0
countMen = 0
student =[] 
studentCoverage = []
studenDic={}
coverageProgram = 0

while menuValid == 0:
    menu = input("¿Qué desea hacer? para finalizar semestre escriba (semestre) - para matricular estudiantes escriba (matricula) ")
    if menu == "Semestre" or menu == "semestre":
        menuValid = 1
        while True:
            try:
                numAlumnos = int(input("Ingrese número de alumnos: "))
                if numAlumnos < 0:
                    print("Debes escribir un número positivo.")
                else:
                    break
            except ValueError:
                print("Debes escribir un número.")
        for i in range(numAlumnos):
            nombreValid = 0
            while nombreValid == 0: 
                name = input("Ingrese nombre: ")
                if name.isalpha():
                    nombreValid = 1
                else:
                    print("El Nombre no debe contener numeros")
                    nombreValid = 0
            sw=0        
            while sw == 0:
                program = input("Ingrese programa academico: ")
                if program.isalpha():
                    sw = 1
                else:
                    print("El programa academico no contiene numeros")
                    sw = 0   
            existsProgram = existData(program,listProgram)
            if existsProgram == False:
                listProgram.append({program})
            sexValid = 0
            while sexValid == 0:
                sex = input("Ingrese sexo - m(mujer), h(hombre)")
                if sex == "m" or sex == "M":  
                    countWomen+=1
                    sexValid = 1
                elif sex == "h" or sex == "H":
                    countMen+=1
                    sexValid = 1
                else:
                    print("error ingrese una de las dos opcines")
                    sexValid = 0
            average =averageStudent()        
            student.append({"name":name, "program":program , "average":average, "sexo":sex}) 
        for item in listProgram:
            for b in item:
                coverageProgram = 0
                result = searchData(student,b)

                for item2 in result:    
                    aux = item2.get('program')
                    coverageProgram = coverageProgram + item2.get('average')
                    studentCoverage.append({"name":item2.get('name'), "program":item2.get('program') , "average":item2.get('average'), "sexo":item2.get('sexo')})
                coverageProgram = coverageProgram / countItem(result)
                print()
                print("El promedio de notas del programa: " + aux + " es " + str(coverageProgram))
                
                resultWomenProgram = countWomenProgram(result)
                print("La cantidad de mujeres del programa " + aux + " es " + str(resultWomenProgram))
                
                resultMenProgram = countMenProgram(result)
                print("La cantidad de hombres del programa: " + aux + " es " + str(resultMenProgram))
                print()
                for promStudent in studentCoverage:
                    print("El (la) estudiante " + promStudent.get('name') + "del programa "+promStudent.get("program") + ","+"Tiene un promedio de "+str(promStudent.get("average")) + " en sus notas.")
                    
                studentCoverage.clear()    
                print()
    else:
        if menu == "Matricula" or menu == "matricula":
            opcion = 0
            while True:
                nombreValid = 0
                while nombreValid == 0: 
                    name = input("Ingrese nombre: ")
                    if name.isalpha():
                        nombreValid = 1
                    else:
                        print("El Nombre no debe contener numeros")
                        nombreValid = 0
                while True:
                    try:
                        edad = int(input("Ingrese edad: "))
                        if edad < 0:
                            print("Debes escribir un número mayor a 0.")
                        else:
                            break
                    except ValueError:
                        print("Debes escribir un número.") 
                sexValid = 0
                promEdad = promEdad + edad
                while sexValid == 0:
                    sex = input("Ingrese sexo - m(mujer), h(hombre)")
                    if sex == "m" or sex == "M":  
                        countWomen+=1
                        sexValid = 1
                    elif sex == "h" or sex == "H":
                        countMen+=1
                        sexValid = 1
                    else:
                        print("error ingrese una de las dos opcines para sexo ")
                        sexValid = 0
                totalMatriculados +=1
                while True:
                    try:
                        newStudent=int(input("Si desea ingresar un nuevo estudiante presione 1 o cualquier tecla para salir!!"))  
                        if newStudent < 0:                                  
                            print("Debes escribir un número positivo.")
                        else:
                            break
                    except ValueError:
                        print("Debes escribir un número.")
                menuValid = 1
                if newStudent != 1:
                    break
            promEdad = promEdad /totalMatriculados
            print("El promedio de edad de los estudiantes matriculados es: " + str(promEdad))
            print("La cantidad de estudiantes matriculados es: " + str(totalMatriculados))
            print("El promedio de mujeres matriculadas es: " + str(countWomen))
            print("El promedio de hombres matriculados es: " + str(countMen))
        else:
            print("Error: Debe ingresar una de las dos opciones")
            menuValid = 0                 