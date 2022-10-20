from urllib.request import urlopen
from datetime import date
from datetime import timedelta
import re
import json

#In Denmark transport fees are more expensive in some hours.
transportCheap = 0.39
transportExp = 1.03
highFeeHours = ["17","18","19"]

today = date.today()
tomorrow = today + timedelta(days = 2)
url = "https://api.energidataservice.dk/dataset/Elspotprices?start="+str(today)+"&end="+str(tomorrow)+"&filter={\"PriceArea\":\"DK1\"}&sort=HourDK%20asc"

print(url)
response = urlopen(url)
data_json = json.loads(response.read())

for d in data_json['records']:
  unitPrice = d['SpotPriceDKK']/1000
  tax = unitPrice * 0.25
  total = unitPrice + tax
  roundUP = str(round(total,2))
  time = re.sub(r'^.*?T','',d['HourDK'])
  specific = re.sub(':.*','',time)
  split = d['HourDK'].split("T")
  if specific not in highFeeHours:
    price = total + transportCheap
    unitTax = price * 0.25
    unitTotal = price + unitTax
    print(split[0], split[1]+' Low fee! Price is '+str(unitTotal))
  if specific in highFeeHours:
    price = total + transportExp
    unitTax = price * 0.25
    unitTotal = price + unitTax
    print(split[0], split[1]+' HIGH FEE! Price is '+str(unitTotal))
  #print(split[0], split[1], roundUP)
