import requests
import schedule
import datetime
import time
import os

def read_and_write_level():
    r = requests.get("https://www.pegelonline.nlwkn.niedersachsen.de/Pegel/Binnenpegel/ID/593")
    page_content = str(r.text)
    wasserstand = page_content[page_content.find("_0_Wasserstand_0")+18:page_content.find("_0_Wasserstand_0")+21]

    jetzt = datetime.datetime.now()

    aktuelle_zeit = jetzt.strftime("%H:%M:%S")
    aktuelles_datum = jetzt.strftime("%Y-%m-%d")
        
    zeile = aktuelles_datum + " " + aktuelle_zeit + ";" + wasserstand + "\n"
    
    csv_datei = open("aller_pegel.csv", "a")
    csv_datei.write(zeile)
    csv_datei.close()
    
def generate_and_move_plot():
	os.system("Rscript aller_auswertung.R")
	os.system("mv allerpegel_plot.jpg /var/www/html/img/")
    

schedule.every().hour.do(read_and_write_level)
schedule.every().day.at("07:00").do(generate_and_move_plot)

while True:
    schedule.run_pending()
    time.sleep(1)
