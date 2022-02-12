import requests # install requests with `pip install requests`

def getmarkets():
  url = 'https://www.buda.com/api/v2/markets'
  response = requests.get(url)
  jsonresp = (response.json())
#  print(jsonresp)
  marketlist = jsonresp['markets']
  for mark in marketlist:
    print(mark)

# Defining main function
def main():
    print("Hey there")
    getmarkets()

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
