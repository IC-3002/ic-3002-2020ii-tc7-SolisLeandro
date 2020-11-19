def aux_encontrar_ruta(arr,rutaArr,x,y,guiaPar):
    print("-----")
    print("x="+str(x)+" lenX="+str(len(arr[0])-1)+" y="+str(y)+" lenY="+str(len(arr)-1)+" guiaPar="+str(guiaPar))
    
    rutaArr[y][x]=1
    if(x==len(arr[0])-1 and y==len(arr)-1):
        print("finnn")
        return True
    
    if(guiaPar):
        if(x==len(arr[0])-1):   #ir si o si abajo
            if(arr[y+1][x]==0):     #ver si puedo ir abajo
                print("abajo")
                aux_encontrar_ruta(arr,rutaArr,x,y+1,True)
                return rutaArr
        else:
            if(arr[y][x+1]==0):     #ver si puedo ir a la derecha
                print("derecha")
                final=aux_encontrar_ruta(arr,rutaArr,x+1,y,False)
                print(final)
                if(final==False):
                    if(y<len(arr)-1):
                        if(arr[y+1][x]==0):
                            print("Segundo x="+str(x)+" lenX="+str(len(arr[0])-1)+" y="+str(y)+" lenY="+str(len(arr)-1)+" guiaPar="+str(guiaPar))
                            print("abajo")
                            aux_encontrar_ruta(arr,rutaArr,x,y+1,True)
                        else:
                            print("back")
                            rutaArr[y][x]=0
                            return False
                return rutaArr
            elif(arr[y+1][x]==0):
                print("abajo")
                final=aux_encontrar_ruta(arr,rutaArr,x,y+1,True)
                print(final)
                if(final==False):
                    if(x<len(arr[0])-1):
                        if(arr[y][x+1]==0):
                            print("Segundo x="+str(x)+" lenX="+str(len(arr[0])-1)+" y="+str(y)+" lenY="+str(len(arr)-1)+" guiaPar="+str(guiaPar))
                            print("derecha")
                            aux_encontrar_ruta(arr,rutaArr,x+1,y,False)
                        else:
                            print("back")
                            rutaArr[y][x]=0
                            return False
                return rutaArr
    else:
        if(y==len(arr)-1):   #ir si o si derecha
            if(arr[y][x+1]==0):     #ver si puedo ir derecha
                print("derecha")
                aux_encontrar_ruta(arr,rutaArr,x+1,y,False)
                return rutaArr
        else:
            if(arr[y+1][x]==0):     #ver si puedo ir a la abajo
                print("abajo")
                final=aux_encontrar_ruta(arr,rutaArr,x,y+1,True)
                print(final)
                if(final==False):
                    if(x<len(arr[0])-1):
                        if( arr[y][x+1]==0):
                            print("Segundo x="+str(x)+" lenX="+str(len(arr[0])-1)+" y="+str(y)+" lenY="+str(len(arr)-1)+" guiaPar="+str(guiaPar))
                            print("derecha")
                            aux_encontrar_ruta(arr,rutaArr,x+1,y,False)
                        else:
                            print("back")
                            rutaArr[y][x]=0
                            return False
                return rutaArr
            elif(x<len(arr[0])-1 and arr[y][x+1]==0):
                print("derecha")
                final=aux_encontrar_ruta(arr,rutaArr,x+1,y,False)
                print(final)
                if(final==False):
                    if(y<len(arr)-1):
                        if( arr[y+1][x]==0):
                            print("Segundo x="+str(x)+" lenX="+str(len(arr[0])-1)+" y="+str(y)+" lenY="+str(len(arr)-1)+" guiaPar="+str(guiaPar))
                            print("abajo")
                            aux_encontrar_ruta(arr,rutaArr,x,y+1,True)
                        else:
                            print("back")
                            rutaArr[y][x]=0
                            return False
                return rutaArr

    #bactraking
    print("back")
    rutaArr[y][x]=0
    return False
        
    

def encontrar_ruta(C):
    rutaArr=[]
    for i in C:
        tempArr=[]
        for e in i:
            tempArr.append(0)
        rutaArr.append(tempArr)
    imprimirMatriz(C)
    return aux_encontrar_ruta(C,rutaArr,0,0,True)
    
def imprimirMatriz(arr):
    for i in arr:
        for e in i:
            print (str(e)+" ",end="")
        print("")
            
imprimirMatriz(encontrar_ruta([[0,0,0,0],[0,0,0,1],[0,1,1,0],[0,0,0,0]]))