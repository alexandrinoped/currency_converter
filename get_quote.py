import requests

def get_currency_quote(source_currency, destination_currency):
  link = f"https://economia.awesomeapi.com.br/last/{source_currency}-{destination_currency}"
  recovery = requests.get(link)

  quote = recovery.json()[f"{source_currency}{destination_currency}"]["bid"]
  return quote