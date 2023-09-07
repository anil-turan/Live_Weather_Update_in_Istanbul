import requests
from bs4 import BeautifulSoup
import subprocess
from time import sleep
CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''
def notify(title, text):
  subprocess.call(['osascript', '-e', CMD, title, text]) # osascript ile macosx için bildirim olayı tetiklenmektedir.
def getdata(url):
    r = requests.get(url)  # get request sorgusu ile web sitesinden sayfa bilgisi alınmaktadır.
    return r.text
while True: # Sonsuz döngü açılmıştır.
    htmldata = getdata("https://weather.com/en-IN/weather/today/l/a6ae974ab6d54e31d092094d11d3e04d41a1f81adefe6a49a939c2c1c4bf2696") #weather.com sitesi istanbul 07.09.2023 tarihli hava durumu bilgisine erişim linkidir. Bağlantı zaman içinde değişebilir güncellenmesi önerilir.
    soup = BeautifulSoup(htmldata, 'html.parser') #HTML yanıtını düzeneleyen hazır bir kütüphane fonksiyonudur.
    current_temp = soup.find_all("span",
                                 class_="CurrentConditions--tempValue--MHmYY") # weather.com sitesi span elemanları içerisinden özel bir sınıfı bulup sınıfından devamındaki sıcaklık bilgisi alınması için kullanılmaktaıdr.
    chances_rain = soup.find_all("div",
                                 class_="CurrentConditions--phraseValue--mZC_p") # weather.com sitesi div elemanları içerisinden özel bir sınıfı bulup sınıfından devamındaki hava olayı bilgisi alınması için kullanılmaktaıdr.
    weat_temp = str(current_temp).split(">")[1].split("<")[0] # Sıcaklık bilgisi split fonsiyonu ile ayrıklaştırılmaktadır.
    weat_cond = str(chances_rain).split(">")[1].split("<")[0] # Hava olalyı bilgisi split fonsiyonu ile ayrıklaştırılmaktadır.
    result = "Sıcaklık " + weat_temp + " ve " + weat_cond # mesaj bütünleştirilmektedir.
    #print(result)
    notify("Hava Durumu İstanbul", result) # MacOSX bildirimi için çağırılan fonksiyondur.
    sleep(300) # 5 dakika bekleme yapılması için sleep fonksiyonu çağırılmaktadır.

