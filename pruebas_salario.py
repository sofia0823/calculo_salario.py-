from calculo_salario import calcular_salario

def ejecutar_pruebas():
    print("=" * 60)
    print("        EJECUCIÓN DE CASOS DE PRUEBA")
    print("=" * 60)

    casos = [
        # (ID, técnica, horas, categoria, esperado)
        ("CB-01", "Camino Básico", 40, 5, "Error: Categoría inválida"),
        ("CB-02", "Camino Básico", -2, 2, "Error: Las horas no pueden ser negativas"),
        ("CB-03", "Camino Básico", 38, 1, 4560000.0),
        ("CB-04", "Camino Básico", 45, 2, 7437500.0),
        ("CB-05", "Camino Básico", 40, 3, 8800000.0),
        ("CO-01", "Cobertura Condición", 44, 1, 5040000.0),
        ("CO-02", "Cobertura Condición", 40, 2, 6800000.0),
        ("PE-01", "Partición Equivalencia", 20, 1, 2400000.0),
        ("PE-02", "Partición Equivalencia", 44, 3, 9680000.0),
        ("VL-01", "Valores Límite", 0, 1, 0.0),
        ("VL-02", "Valores Límite", 41, 2, 7012500.0),
    ]

    aprobados = 0
    fallidos = 0

    for id_caso, tecnica, horas, cat, esperado in casos:
        try:
            resultado = calcular_salario(horas, cat)
            if isinstance(esperado, float) and abs(resultado - esperado) < 0.01:
                estado = "✅ APROBADO"
                aprobados += 1
            else:
                estado = "❌ FALLIDO"
                fallidos += 1
        except ValueError as e:
            if isinstance(esperado, str) and esperado in str(e):
                estado = "✅ APROBADO"
                aprobados += 1
            else:
                estado = "❌ FALLIDO"
                fallidos += 1

        print(f"{id_caso} | {tecnica} | h={horas}, cat={cat} | {estado}")

    print("\n" + "=" * 60)
    print(f"RESUMEN: {aprobados} aprobados | {fallidos} fallidos")
    print("=" * 60)

if __name__ == "__main__":
    ejecutar_pruebas() 