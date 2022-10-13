from urllib.request import urlopen
from datetime import date
from datetime import timedelta
import json

today = date.today()
tomorrow = today + timedelta(days = 1)
url = "https://api.energidataservice.dk/dataset/Elspotprices?start="+str(today)+"&end="+str(tomorrow)+"&filter={\"PriceArea\":\"DK1\"}"

response = urlopen(url)
data_json = json.loads(response.read())

print(url)

for d in data_json['records']:
  #print(d['HourDK'], d['SpotPriceDKK'])
  UnitPrice = d['SpotPriceDKK']/1000
  RoundUP = str(round(UnitPrice, 2))
  print(d['HourDK'], RoundUP)
