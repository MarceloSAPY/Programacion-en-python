def agregarNombreyApellido(nombre, apellido):
    
    c = open("nombrecompleto.txt","a")
    c.write(nombre + " " + apellido + "\n")
    c.close()

agregarNombreyApellido("Diego","Saavedra")
agregarNombreyApellido("Juan","Martinez")
agregarNombreyApellido("Pedro","Lara")
agregarNombreyApellido("Maria","Sarango")