import os

import time

try:

    import requests

    from bs4 import BeautifulSoup

    from sty import fg, bg, ef, rs

except ImportError:

  print("Installing requirements to run.".capitalize)

  lis = ('requests', 'bs4', 'sty')

  for i in lis:

    os.system(f'py -m pip install {i}')

  print(fg(0, 255, 51) + " Yay! , You have everything Ready" + fg.rs)
  print(fg.red + " ~ This code was written by @xMRV001 " + fg.rs)

headers = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'cmc-language=en; gtm_session_first=%222023-01-03T16%3A37%3A48.661Z%22; gtm_session_last=%222023-01-03T16%3A37%3A48.667Z%22; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22185787f087b72-0607a7c97fc1124-26021151-1327104-185787f087c5b5%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg1Nzg3ZjA4N2I3Mi0wNjA3YTdjOTdmYzExMjQtMjYwMjExNTEtMTMyNzEwNC0xODU3ODdmMDg3YzViNSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22185787f087b72-0607a7c97fc1124-26021151-1327104-185787f087c5b5%22%7D; _ga=GA1.2.2043623356.1672763870; _gid=GA1.2.1725174147.1672763870; _fbp=fb.1.1672763877854.1965783308; _tt_enable_cookie=1; _ttp=SJHxWQy444rqa6avI3nxLu_Jp_Z; cmc_gdpr_hide=1',
'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}



BTC = print(fg.yellow + " 1 => Bitcoin - BTC " + fg.rs)

ETH = print(fg.grey + " 2 => Ethereum - ETH " + fg.rs)

USDT = print(fg.green + " 3 => Tether - USDT " + fg.rs)

other =  print(fg.red + 'PS: if you want other currecny please type it full name.' + fg.rs)

userinput = input(fg(165,198,255) + 'Choose number or if you want other currency type it here please : ' + fg.rs)

if userinput == '2' or userinput == 'ethereum' or userinput == 'eth':

    url1 = "https://coinmarketcap.com/currencies/ethereum/"

    eth = requests.get(url1, headers=headers)

    soup1 = BeautifulSoup(eth.text, 'html.parser')

    price1 = soup1.find('div', class_='priceValue')

    print(fg.grey + 'Ethereum price now' + ' ' + price1.text + fg.rs)


elif userinput == '1' or userinput == 'bitcoin' or userinput == 'btc':

    url2 = "https://coinmarketcap.com/currencies/bitcoin/"

    btc = requests.get(url2, headers=headers)

    soup2 = BeautifulSoup(btc.text, 'html.parser')

    price2 = soup2.find('div', class_='priceValue')

    print(fg.yellow + 'Bitcoin price now' + ' ' + price2.text + fg.rs)


elif userinput == '3' or userinput == 'Tether' or userinput == 'USDT':

    url3 = "https://coinmarketcap.com/currencies/tether/"

    usdt = requests.get(url3, headers=headers)

    soup3 = BeautifulSoup(usdt.text, 'html.parser')

    price3 = soup3.find('div', class_='priceValue')

    print(fg.green + 'Tether price now' + ' ' + price3.text + fg.rs)


elif userinput != '3' or userinput != '2' or userinput != '1':

    url4 = f"https://coinmarketcap.com/currencies/{userinput}/"

    newinput = requests.get(url4, headers=headers)

    soup4 = BeautifulSoup(newinput.text, 'html.parser')

    price4 = soup4.find('div', class_='priceValue')

    print(f'{fg(255,0,0)}  {userinput} price now' + ' ' + price4.text + fg.rs)
    
inf = input(fg.magenta + "You want always ON MODE ? Y / N : " + fg.rs)

print(fg.cyan + "  PS: it get you the price every 2 seconds" + fg.rs)

if inf == "n" or inf == "N":

    print("Closing..")

    exit()

elif inf == "y" or inf == "Y":

    ask = input(fg.li_yellow + "Currency name please : " + fg.rs)

    while True:

        getit = f"https://coinmarketcap.com/currencies/{ask}/"

        gogetit = requests.get(getit, headers=headers)

        gowithsoup = BeautifulSoup(gogetit.text, 'html.parser')

        gotprice = gowithsoup.find('div', class_='priceValue')

        print(f'{fg(255,0,0)}  {ask} price now' + ' ' + gotprice.text + fg.rs)

        time.sleep(2)
