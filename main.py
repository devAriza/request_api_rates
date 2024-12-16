import pandas as pd
import requests

"""
Consulta la API de tasas de VAT Comply 'https://api.vatcomply.com/rates', usando parámetros para obtener las tasas de cambio para una moneda base de 'USD' y la fecha '2024-01-21'.
Usando el DataFrame de pedidos y la tasa de cambio de la API, calcula el monto total vendido en USD, guardándolo como una variable llamada total_usd_sales.
Asegúrate de que la versión final del DataFrame de pedidos coincida con los requisitos detallados en el Libro de trabajo.
*La API de tasas de VAT Comply es de uso gratuito y no requiere registro/autenticación.

1. Solicitud de información sobre la tasa de cambio
* Realiza una solicitud GET a la API de VatComply para obtener información sobre la tasa de cambio.

2. Actualización del DataFrame de pedidos
Agrega información sobre la tasa de cambio y calcula el monto de cada pedido en USD.

3. Cálculo del monto total en USD para todos los pedidos
Suma todos los valores de pedidos en USD.
"""
orders = pd.read_csv('orders-2024-01-21.csv')
print(orders.head())
print(orders.shape)

# Params for request to API
param = {
    "base": "USD",
    "date": "2024-01-21",
}

# Get information from API and save dict with rates
request = requests.get('https://api.vatcomply.com/rates', params=param)
rates = request.json()['rates']
print(type(rates))

# Save exchange_rate for USD, GBP and EUR
orders["exchange_rate"] = orders["currency"].map(rates)

# Multiply amount * exchange_rate
orders["amount_usd"] = orders["amount"] * orders["exchange_rate"]

# Sum total from amount
sum_total = orders["amount_usd"].sum()
print(f'{sum_total:.2f}')