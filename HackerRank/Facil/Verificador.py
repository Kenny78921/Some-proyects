def verificador(ID):
    # Filtro 10 caracteres, que no sean repetidos y que todos sean alfanum
    if len(set(ID)) != 10 or ID.isalnum() == "False":
        return "Invalid"
    
    # Verificar los nums de repeticiones de A-Z y 0-9
    Mayusculas = sum(1 for c in ID if c.isupper())
    Numeros = sum(1 for c in ID if c.isdigit())
    if Mayusculas < 2 or Numeros < 3:
        return "Invalid"
    
    # Si pasa todos los filtros previos es valido
    return "Valid"
    
    
for x in range(int(input())):
    ID = input()
    print(verificador(ID))
