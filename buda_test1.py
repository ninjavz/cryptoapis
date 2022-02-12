import requests # install requests with `pip install requests`
import time

def getprice():
  c_precio = 0
  c_moneda = 1
  #url = 'https://www.buda.com/api/v2/markets/eth-btc/ticker'
  url = 'https://www.buda.com/api/v2/markets/btc-usdc/ticker'
  response = requests.get(url)
#  print(response)
  jsonresp = (response.json())
#  print(jsonresp)
  ticker=jsonresp['ticker']
  print(ticker)
  pricebtc=ticker['last_price']
  print(pricebtc)

  print("Moneda: ", pricebtc[c_moneda])
  print("Precio: ", pricebtc[c_precio])

# Defining main function
def main():
    print("Hey there")
    while (1):
      getprice()
      time.sleep(30)

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
