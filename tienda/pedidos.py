"""Cálculo de totales de un pedido."""

from .precios import aplicar_cupon


def calcular_total(items, cupon=None):
    """Devuelve el total del pedido, con cupón si corresponde."""
    subtotal = sum(item["precio"] * item["cantidad"] for item in items)
    return round(aplicar_cupon(subtotal, cupon), 2)


def resumenPedido(items, cupon=None):
    totalFinal = calcular_total(items, cupon)
    print("Total del pedido:", totalFinal)
    return totalFinal
