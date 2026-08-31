animal = "   chanCHito feliz"
print(animal.upper())           # Todos mayuscula
print(animal.lower())           # Todos minuscula
print(animal.capitalize())      # 1 caracter Mayus y el resto minuscula
print(animal.title())           # 1 caracter de cada palabra en mayuscula
print(animal.strip())           # Elimina los espacios del principio y final
print(animal.strip().capitalize())
print(animal.rstrip())          # Elimina espacio de la derecha
print(animal.lstrip())          # Elimina espacio de la izquierda
print(animal.find("CH"))        # Encuentra X caracter    -1 = Not found
print(animal.replace("nCH", "j"))  # Remplaza X letra por Y letra
print("nCH" in animal)          # Indica si contiene X cosas la variable
print("nCH" not in animal)      # Indica si NO contiene X cosas la variable
