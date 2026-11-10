"""Cálculo de precios y cupones."""

# Porcentaje de descuento por cupón.
DESCUENTOS = {"PROMO10": 10, "VIP20": 20}


def aplicar_cupon(subtotal, cupon):
    """Devuelve el subtotal con el cupón aplicado."""
    if cupon in DESCUENTOS:
        return subtotal - DESCUENTOS[cupon] / 100
    return subtotal
