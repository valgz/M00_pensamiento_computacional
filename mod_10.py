#CONSTANTE
IMPUESTO = 0.05

def calcula_subtotal(prices, copies):
    indice = 0
    subtotales = []
    while indice < len(prices):
        n_elemento = prices[indice] * copies[indice]
        subtotales.append(n_elemento)
        indice += 1
    return subtotales

def calcula_tasa_impuesto(prices):
    indice = 0
    tasas = []
    while indice < len(prices):
        n_elemento = prices[indice] * IMPUESTO
        tasas.append(n_elemento)
        indice += 1
    return tasas

def calcula_total(subtotal, fee, copies):
    indice = 0
    totales = []
    while indice < len(subtotal):
        n_elemento = (fee[indice] * copies[indice]) + subtotal[indice]
        totales.append(n_elemento)
        indice += 1
    return totales