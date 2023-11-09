import cv2  # OpenCV
import numpy as np #NumPy

def THL():

        #Rastreamos la imagen y la almacenamos en una variable llamada "img"
        img = cv2.imread("imagenes/motor1.jpg")
        cv2.imshow("Original" ,img)
        cv2.waitKey(0)

        ################PROCEDIMIENTO DE FILTRADO DE IMAGEN ORIGINAL#######################
        
        
        #Se pasa la imagen a escala de grises
        iGris = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        cv2.imshow("Imagen en escala de grises",iGris)
        cv2.waitKey(0)



        #Se le aplica deteccion  de borde por Canny
        iBordes = cv2.Canny(iGris,100,200)
        cv2.imshow("Bordes de las imagen",iBordes)
        cv2.waitKey(0)
        ############################################################################


        #aplicamos la funcion HoughLine de openCV
        lineas = cv2.HoughLines ( iBordes, 1 , np.pi/180 , 145)
        #print(np.array(lineas))

        #Recorrer los resultados
        for i in range(0,len(lineas)):
        #Obtener los valores de rho(distancia)
                rho=lineas[i][0][0]
                #print("r: ", rho)

                #y de theta(angulo)
                theta = lineas[i][0][1]
                #print("theta: ",theta)

                #Gurardar el valor del cos(theta)
                a = np.cos(theta)
                #print("a: ",a)

                #Guardar el valor del sen(theta)
                b = np.sin(theta)
                #print("b: ",b)

                #Guardar el valor de r cos(theta)
                x0 = a * rho
                #print("x0: ",x0)

                #Guardar el valor de  r sen(theta),>>>todo se esta haciendo de forma parametrica<<< 
                y0 = b * rho
                #print("y0: ", y0)

        
                #Ahora todo se  recorrera desde 1000 a - 1000 pixeles(esto puede variar dependiendo del tamaño de la imagen )
                pixeles = 1000
                x1 = int(x0 + pixeles*(-b))
                #print("valor x1: ", x1)
                y1 = int(y0 + pixeles*(a))
                #print("valor y1: ", y1 )
                x2 = int(x0 - pixeles*(-b))
                #print("valor x1: ", x1 )
                y2 = int(y0 - pixeles*(a))
                #print("valor y2: ", y2 )

                #Generar  las lineas para mostrarlas en la linea original
                #un print para motrar las cordenadas que  se usaran para dibujar.
                print("({},{})  ({},{})".format(x1,y1, x2,y2))
                cv2.line(img , (x1,y1),(x2,y2),(0,0,255),1)
        

              
                cv2.imshow("Resultado",img)#Se muestra  el resultado final optenido 
                cv2.waitKey(0)
def THC():
        #Buscamos la imagen y la almacenamos en una variable llamada "img"
        img = cv2.imread('imagenes/motor2.png', cv2.IMREAD_COLOR) 
        cv2.imshow('Original', img)
        cv2.waitKey(0)

        ################PROCESO DE FILTRADO DE IMAGEN ORIGINAL########################
        #Convertir a escala de grises
        iGris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        cv2.imshow('Gris', iGris) # grigio es en italiano, pero no se asusten, no tiene Coreanovirus
        cv2.waitKey(0)
        
        iBorrosa = cv2.blur(iGris, (10, 10)) 
        cv2.imshow('Borrosa', iBorrosa)
        cv2.waitKey(0)

        #############################################################################

        # Aplicar la tranfromada de Hough para detección de círculos
        detectarCiculos = cv2.HoughCircles(iBorrosa, cv2.HOUGH_GRADIENT, 1, 20, param1 =30, param2 =30, minRadius =96, maxRadius = 96)   
       
        # Convertir los parámetros el círculo a, b, y r en enteros.
        dcirculos = np.uint16(np.around(detectarCiculos)) 
  
        # Ahora si se recorren todos los círculos detectados
        for pt in dcirculos[0, :]: 
                a, b, r = pt[0], pt[1], pt[2] 
  
        # Dibujar la circunferencia
                cv2.circle(img, (a, b), r, (0, 255, 100), 4) 
        
        # Para ver los datos de los circulos encontrados.
               
                
  
        # Dibujar un círculo pequeño alrededor del centro
                cv2.circle(img, (a, b), 1, (0, 0, 255), 4)


        # Ir mostradndo las ciculos encontrados.
                #print("Centro ({:}, {:}), radio = {:}".format(a, b, r))
                cv2.imshow("Detección de circunferencias", img) 
                cv2.waitKey(0)       

#Seleccion de metodo
print("Seleccione la opcion: \n 1:Tranformada de  Hough linial \n 2:Tranformada de  Hough circular")
op = input("Se selecciona la opcion: ")
match op :
        case"1":
                #Trnaformada de Hough Linial
                THL()
        case"2":
                #Tranformada de Hough Cicrular
                THC()
