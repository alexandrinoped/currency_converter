import customtkinter
from pickup_coins import coins_name,conversions_available
from get_quote import get_currency_quote


# criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("500x500")

dic_conversions_available = conversions_available()

# criar os botões, textos e outros elementos
title = customtkinter.CTkLabel(window, text="Conversor de moedas", font=("Georgia",20))
text_currency_origin = customtkinter.CTkLabel(window, text="Selecione a moeda de origem")
text_currency_destination = customtkinter.CTkLabel(window, text="Selecione a moeda de destino")

def load_destination_currency(selected_currency):
  destination_currency_list = dic_conversions_available[selected_currency]
  destination_currency_field.configure(values=destination_currency_list)
  destination_currency_field.set(destination_currency_list[0])

source_currency_field = customtkinter.CTkOptionMenu(window, values=list(dic_conversions_available.keys()), command=load_destination_currency)
destination_currency_field = customtkinter.CTkOptionMenu(window, values=["Selecione uma moeda de origem"])

def convert_currency():
  source_currency = source_currency_field.get()
  destination_currency = destination_currency_field.get()
  if source_currency and destination_currency:
    quote = get_currency_quote(source_currency, destination_currency)
    text_currency_quote.configure(text=f"1 {source_currency} = {quote} {destination_currency}")

conversion_button = customtkinter.CTkButton(window, text="Converter", command=convert_currency)

list_coins = customtkinter.CTkScrollableFrame(window)

text_currency_quote = customtkinter.CTkLabel(window, text="")

available_currencies = coins_name()
for currency_code in available_currencies:
  currency_name = available_currencies[currency_code]
  text_coins = customtkinter.CTkLabel(list_coins, text=f"{currency_code}: {currency_name}")
  text_coins.pack()

# colocar todos os elementos na tela
title.pack(padx=10, pady=10)
text_currency_origin.pack(padx=10)
source_currency_field.pack(padx=10, pady=10)
text_currency_destination.pack(padx=10)
destination_currency_field.pack(padx=10, pady=10)
conversion_button.pack(padx=10, pady=10)
text_currency_quote.pack(padx=10, pady=10)
list_coins.pack(padx=10, pady=10)

# rodar a janela
window.mainloop()