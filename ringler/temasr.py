f= open("Temas.txt","r")

mensaje=f.read()

a=mensaje.split(",")

n=list(set(a))

archivo=open("lista.txt","w")

for i in range(len(n)):
    archivo.write(n[i])
    archivo.write(",")

archivo.close()
