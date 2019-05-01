import subprocess as s

def checkBios():
    band = False
    tt ="virtualbox"
    task = s.Popen("wmic bios get smbiosbiosversion", shell=True, stdout=s.PIPE)# se necesita shhel true por que vamos a interactuar con la shell o cmd
    text = task.stdout.read().split("\n")
    bios = text[1].lower()
    if(bios==tt):
        band = True
    return band


def checkProc():
    band = False
    tt = "vboxservice"
    tt1= "vboxtray"
    task = s.Popen("tasklist", shell=True, stdout=s.PIPE)#listamos todos los proceso
    data = task.stdout.read()#leemos los resultados
    data = str(data[390:])#leemos de la pocision 390 en adelante
    lista2 = []#creamos otra lista
    lista = data.split("\n")#asignamos cada valor separado por \n
    listaFinal = []
    for i in lista:#imprimimos cada valor de la lista
        #print(i)
        lista2.append(i.lower().split(".exe"))
    for i in lista2:
        #print(i[0])
        listaFinal.append(i[0])

    for i in listaFinal:
        #print(i)
        if(tt in i or tt1 in i):
            band = True
            break
    return band

if(checkBios() or checkProc()):
    print("vm found")
else:
    print("VM didn't found'")

tete = raw_input()