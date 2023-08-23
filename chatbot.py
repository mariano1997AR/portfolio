

def main():
    salir = False
    preguntas = ['hola','como estas tu?','que estas haciendo?','salir']
    while(salir == False):
        cadena = input("")
        
        if(cadena.lower() == preguntas[0]):
            print("hola soy mariano")
        
        if(cadena.lower() == preguntas[1]):
            print("yo estoy bien")
            
        if(cadena.lower() == preguntas[2]):
            print("Estoy leyendo algo nuevo")
            
        if(cadena.lower() == preguntas[3]):
            print('..... estas saliendo de chatbot 0.1')
            salir = True
        

main()