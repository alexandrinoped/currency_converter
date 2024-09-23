import xmltodict

def coins_name():
  with open("coins.xml", "rb") as coins_file:
    dic_coins = xmltodict.parse(coins_file)

  coins = dic_coins["xml"]
  return coins

def conversions_available():  
  with open("conversions.xml", "rb") as conversios_file:
    dic_conversions = xmltodict.parse(conversios_file)

  conversions = dic_conversions["xml"]
  dic_conversions_available = {}
  for par_conversion in conversions:
    source_currency, destination_currency = par_conversion.split("-")
    if source_currency in dic_conversions_available:
      dic_conversions_available[source_currency].append(destination_currency)
    else:
      dic_conversions_available[source_currency] = [destination_currency]
  return dic_conversions_available