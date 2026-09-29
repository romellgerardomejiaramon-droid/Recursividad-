def preparar_fruta(estado):

    if estado == "Limpia y Seca":
        print("  -> La fruta ya está lista para comer.")
        return "Lista para comer"

    print(f"Estado actual de la fruta: [{estado}]")

    # Si la fruta está sucia, aplicamos recursividad anidada
    if estado == "Sucia":
        print("  1. Primero hay que lavar la fruta sucia...")
    
        fruta_lavada = preparar_fruta("Húmeda")

        print("  2. Ahora pasamos el resultado al proceso de secado...")
        
        fruta_final = preparar_fruta("Limpia y Seca")
        
        return "Fruta perfecta para comer"

    if estado == "Húmeda":
        print("  -> Fruta lavada con éxito.")
        return "Húmeda"

print("--- PREPARANDO UNA MANZANA PARA COMER ---")
resultado = preparar_fruta("Sucia")
print(f"\nResultado final: {resultado}")
