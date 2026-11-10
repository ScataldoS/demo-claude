"""Cálculo de precios y cupones."""

# Porcentaje de descuento por cupón.
DESCUENTOS = {"PROMO10": 10, "VIP20": 20}

# Base para convertir un porcentaje en fracción.
PORCENTAJE_BASE = 100


def aplicar_cupon(subtotal, cupon):
    """Devuelve el subtotal con el cupón aplicado."""
    if cupon in DESCUENTOS:
        return subtotal - (subtotal * DESCUENTOS[cupon] / PORCENTAJE_BASE)
    return subtotal
