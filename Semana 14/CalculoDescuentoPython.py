def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento de una compra.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


def main():
    # Primera compra con descuento por defecto (10%)
    compra1 = 100.0
    descuento1 = calcular_descuento(compra1)
    total1 = compra1 - descuento1
    print(f"Compra 1: ${compra1}")
    print(f"Descuento aplicado: ${descuento1}")
    print(f"Total a pagar: ${total1}\n")

    # Segunda compra con descuento personalizado (20%)
    compra2 = 250.0
    descuento2 = calcular_descuento(compra2, 20)
    total2 = compra2 - descuento2
    print(f"Compra 2: ${compra2}")
    print(f"Descuento aplicado: ${descuento2}")
    print(f"Total a pagar: ${total2}\n")


if __name__ == "__main__":
    main()
