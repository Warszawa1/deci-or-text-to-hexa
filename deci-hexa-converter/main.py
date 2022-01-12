#Ejercicio Decimal, Hexadecimal y Texto
proceso_on = True

def OKI(n):
  try:
    n=int(n)
  except:
    n=OKI(input("Carácter no válido. Introduce un número: "))
  return n

def ns(n):
  while n!="S" and n!="N":
    n = input("Introduzca solo 'S' (sí) o 'N' (no): ").upper()
  return n

def DecimalAHexadecimal(decimal):
  hexadecimal = ""
  while decimal != 0:
    rem = CambiarDigitos(decimal % 16)
    hexadecimal = str(rem) + hexadecimal
    decimal = int(decimal/16)
  return f"Tu decimal en hexadecimal: {hexadecimal}"

def CambiarDigitos(digits):
  decimales = [ 10, 11, 12, 13, 14, 15]
  hexadecimales = ["A", "B", "C", "D", "E", "F"]
  if digits in decimales:
    return hexadecimales[decimales.index(digits)]
  return digits

def TextoAHexadecimal(texto):
  joined = []
  for i in lista_texto:
    hexec = hex(ord(i))
    joined.append(hexec)
    joined_texto = ' '.join(joined)
  print(f"Tu texto en hexadecimal: {joined_texto}")

while proceso_on:
  tipo = input("Qué quieres convertir a hexadecimal, texto 'T' o decimal 'D'? : ").upper()
  if tipo == 'D':
    decimal = OKI(int(input("Introduzca un número: ")))
    print(DecimalAHexadecimal(decimal))
            
  elif tipo == 'T':
    texto=input("Introduzca su texto aquí: ")
    lista_texto= list(texto)
    TextoAHexadecimal(texto)
    
  continua = ns(input("¿Desea continuar? (S/N): ").upper())
    
  if continua == "N":
    print("Fin del programa.")
    break
  elif continua == "S":
    proceso_on = True
  else:
    print("Carácter no válido. Se ha cerrado el programa.")
    break 