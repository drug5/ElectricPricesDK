from urllib.request import urlopen
from datetime import date
from datetime import timedelta
import json

today = date.today()
tomorrow = today + timedelta(days = 2)
url = "https://api.energidataservice.dk/dataset/Elspotprices?start="+str(today)+"&end="+str(tomorrow)+"&filter={\"PriceArea\":\"DK1\"}&sort=HourDK%20asc"

print(url)
response = urlopen(url)
data_json = json.loads(response.read())

for d in data_json['records']:
  UnitPrice = d['SpotPriceDKK']/1000
  Tax = UnitPrice * 0.25
  Total = UnitPrice + Tax
  RoundUP = str(round(Total, 2))
  split = d['HourDK'].split("T")
  print(split[0], split[1], RoundUP)
