def bisiesto(x):  
  if((x % 400 == 0) or  
     (x % 100 != 0) and  
     (x % 4 == 0)):   
    print("Es Bisiesto!");    
  else:  
    print ("No es Bisiesto!")    
x = int(input("Ingrese un Año: "))   


bisiesto(x)  