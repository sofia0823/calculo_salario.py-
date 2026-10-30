def calcular_salario(horas_trabajadas: float, categoria: int) -> float:
    """
    Calcula el salario de un empleado según horas trabajadas y categoría.
    
    Tarifas:
        Categoría 1: 120000 COP por hora
        Categoría 2: 170000 COP por hora
        Categoría 3: 220000 COP por hora
    
    Horas extras (> 40): recargo del 25 % sobre la tarifa base.
    
    Args:
        horas_trabajadas: Cantidad de horas laboradas (debe ser ≥ 0)
        categoria: Nivel del empleado, valores válidos: 1, 2 o 3
    
    Returns:
        Salario total en pesos colombianos
    
    Raises:
        ValueError: Si la categoría no es 1, 2, 3 o si las horas son negativas
    """
    # Definición de tarifas por categoría
    tarifas = {
        1: 120000,
        2: 170000,
        3: 220000
    }

    # Validación de categoría
    if categoria not in tarifas:
        raise ValueError(
            f"Categoría inválida: {categoria}. "
            "Debe ser 1, 2 o 3."
        )

    # Validación de horas trabajadas
    if horas_trabajadas < 0:
        raise ValueError(
            "Las horas trabajadas no pueden ser negativas."
        )

    # Obtener tarifa base según la categoría
    tarifa_base = tarifas[categoria]

    # Cálculo del salario con o sin horas extras
    if horas_trabajadas > 40:
        horas_normales = 40
        horas_extras = horas_trabajadas - 40
        salario = (
            horas_normales * tarifa_base +
            horas_extras * tarifa_base * 1.25
        )
    else:
        salario = horas_trabajadas * tarifa_base

    return salario


# Bloque principal para ejecución interactiva
if __name__ == "__main__":
    print("=" * 50)
    print("    SISTEMA DE CÁLCULO DE SALARIOS")
    print("=" * 50)
    print("Tarifas:")
    print("  Categoría 1 → $120.000 / hora")
    print("  Categoría 2 → $170.000 / hora")
    print("  Categoría 3 → $220.000 / hora")
    print("* Horas > 40 → recargo del 25 %")
    print("=" * 50)

    try:
        # Entrada de datos
        horas = float(input("Ingrese las horas trabajadas: "))
        categoria = int(input("Ingrese la categoría (1, 2 o 3): "))

        # Cálculo
        salario_total = calcular_salario(horas, categoria)

        # Salida formateada
        print("\n" + "-" * 50)
        print(f"✅ El salario total es: ${salario_total:,.2f} COP")
        print("-" * 50)

    except ValueError as error:
        print(f"\n❌ Error: {error}")