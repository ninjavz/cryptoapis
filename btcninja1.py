from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
#import re

def start(bot, context):
    # Run bot and send description
    bot.message.reply_text("Hola, soy un bot!")

def help(bot, context):
    # Get help and instructions of the bot
    bot.message.reply_text("Sistema de ayuda, comandos aceptados:")
    bot.message.reply_text("/start Saludo")
    bot.message.reply_text("/help Esta Ayuda, lista de comandos")
    bot.message.reply_text("/coindeskbtc Dar precio de BTC en USD de Coindesk")
    bot.message.reply_text("/coinpaprikabtc Dar precio de BTC en USD de Coindesk")
    bot.message.reply_text("/budabtc Dar precio de BTC en USDC de Buda")
    bot.message.reply_text("/dog Foto de un perro")

def btc_price_binance():
    # Get the BTC price from Binance in USD
    print()

def btc_price_bitstamp():
    # Get the BTC price from Binance in USD
    print()

def btc_price_kucoin():
    # Get the BTC price from Binance in USD
    print()

def btc_price_coindesk(bot, context):
    # Get the BTC price from Binance in USD
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url).json()
    print(response)
    price=response["bpi"]["USD"]["rate_float"]
    roundprice=round(price,2)
    respuesta = "Precio de BTC en Coindesk: $ " + str(roundprice) + " USD"
    bot.message.reply_text(respuesta)
    return(roundprice)

def btc_price_buda(bot, context):
    # BTC price from buda.com in USDC
    url = 'https://www.buda.com/api/v2/markets/btc-usdc/ticker'
    response = requests.get(url).json()
    ticker = response['ticker']
    pricebtc=ticker['last_price']
    amount = pricebtc[0]
    pair = pricebtc[1]
    famount = float(amount)
    roundamount="{:.2f}".format(round(famount,2))
    respuesta = "Precio de BTC en Buda: $ " + roundamount + " " + pair
    print(respuesta)
    bot.message.reply_text(respuesta)
    return(roundamount)
    
def btc_price_banex(bot, context):
    # BTC price from Banexcoin
    print()

def btc_price_kraken(bot, context):
    # BTC price from Kraken
    print()

def btc_price_coinpaprika(bot, context):
    # BTC price rrom coinpaprika
    url = 'https://api.coinpaprika.com/v1/tickers/btc-bitcoin'
    response = requests.get(url).json()
    print(response)
    price=response["quotes"]["USD"]["price"]
    roundprice=round(price,2)
    respuesta = "Precio de BTC en Coinpaprika: $ " + str(roundprice) + " USD"
    bot.message.reply_text(respuesta)
    return(roundprice)

def btc_price_coinmarketcap(bot, context):
    # BTC price from Coinmarketcap
    print()

def btc_price(bot, context):
    # Get the medium price of BTC from X exchanges
    print()

def titanus(bot, context):
    bot.message.reply_text("La Tits siempre llega tarde!")

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def dog(bot, context):
    url = get_url()
    print(url)
    bot.message.reply_photo(photo=url)

def main():
    # Crear 2 threads, uno para comandos, el otro para automatizar
    # Automatizado debe mostrar precio BTC cada 12h, y dar alarmas si
    # algun exchange cambia mas de 10% en una hora o en 12 horas
    updater = Updater('5142533483:AAEfUidP2DONiitAbLKSiFBrNGPtnMWRoRY')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('dog',dog))
    dp.add_handler(CommandHandler('titanus',titanus))
    dp.add_handler(CommandHandler('budabtc', btc_price_buda))
    dp.add_handler(CommandHandler('coindeskbtc', btc_price_coindesk))
    dp.add_handler(CommandHandler('coinpaprikabtc', btc_price_coinpaprika))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

