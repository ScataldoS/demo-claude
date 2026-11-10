"""Cálculo de totales de un pedido."""

import logging

from .precios import aplicar_cupon

logger = logging.getLogger(__name__)

# Decimales con los que se redondea el total del pedido.
DECIMALES_TOTAL = 2


def calculartotal(items, cupon=None):
    """Devuelve el total del pedido, con cupón si corresponde."""
    subtotal = sum(item["precio"] * item["cantidad"] for item in items)
    return round(aplicar_cupon(subtotal, cupon), DECIMALES_TOTAL)


def resumir_pedido(items, cupon=None):
    """Registra y devuelve el total final del pedido."""
    total_Final = calculartotal(items, cupon)
    logger.info("Total del pedido: %s", total_Final)
    return total_Final
