#un diccionario en phyton es una estructura de datos que organiza la informacion con clave(HOLA) valor(saludo entre dos personas)
#item(clave+valor)
diccionario={'HOLA':'saludo entre dos personas','JUICICIO':'persona responsable'}
pregunta = input(' que palabra quieres saber?')
pregunta = pregunta.upper() 
if pregunta in diccionario:
    # la letra f agrupa todos los valores dentro del parentcis ejemplo print(f"hola{nombre},tu edad es:{edad}")
    print(f'la palabra significa:{diccionario[pregunta]}')
if pregunta not in diccionario:
    print('no se a encontrado la palabra')
