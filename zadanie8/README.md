Moduł pickle służy do peklowania obiektów, czyli serializacji obiektów i deserializacji.<br /> 

Funkcja dumps przekształca obiekt w bajty  <br />
Przykład <br />
import pickle <br />
dane = { 'imie':'adam', 'nazwisko':'nowak', 'ocena':3.0 } <br />
print('dane:', dane) <br />
#Funkcja dumps () tworzy ciąg znaków reprezentujący wartość obiektu w bajtach <br /> <br />
dane_string = pickle.dumps(dane) <br />
print('serializacja:', dane_string ) <br />
ODPOWIEDŹ : <br />
dane: {'imie': 'adam', 'nazwisko': 'nowak', 'ocena': 3.0} <br />
serializacja: <br /> b'\x80\x03}q\x00(X\x04\x00\x00\x00imieq\x01X\x04\x00\x00\x00adamq\x02X\x08\x00\x00\x00nazwiskoq\x03X\x05\x00\x00\x00nowakq\x04X\x05\x00\x00\x00ocenaq\x05G@\x08\x00\x00\x00\x00\x00\x00u.'<br /> 

Funkcja loads sluzy do deseralizacji  inaczej mówiąc jest to odwrotność do seralizacji odwraca strumien bajtów w obiekt. <br />
Przykład  <br />
dane_de = pickle.loads(dane_string) <br />
print('deserializacja:', dane_de <br />
Odpowiedź <br /> 
deserializacja: {'imie': 'adam', 'nazwisko': 'nowak', 'ocena': 3.0} <br />


CSV-format przechowywania danych w plikach tekstowych  <br />
Wykorzystywane funkcje <br /> 
Funkcja csv.reader() tworzy iterator czytający kolejne wiersze z danych typu csv do listy.  <br />
Funkcja csv.DictReader() można porównać do csv.reader() , tyle że linie tłumaczone do słownika.<br />
Funkcja csv.writer() funkcja zwraca obiekt ,do którego możemy zapisać kolejne wiersze metoda writerow().<br />
#pisanie pliku csv ze slownika za pomoca programu cvc <br />
import csv<br />
from google.colab import files<br />
wb = files.upload()<br />
with open('pracownicy_file2.csv', mode='w') as csv_file:<br />
    fieldnames = ['dane', 'stanowisko', 'miesiac']<br />
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)<br />

    writer.writeheader()
    writer.writerow({'dane': 'arek kowalik', 'stanowisko': 'ksiegowy', 'miesiac': 'Grudzien'}) <br />
    writer.writerow({'dane': 'bartek Nowaks', 'stanowisko': 'IT', 'miesiac': 'Marzec'})<br />


#Analizowanie plików CSV za pomocą Pandas biblioteki<br />
#pandas.read otwiera analizuje i odczytuje plik csv oraz zapisuje dane w DateFrame<br />
import pandas<br />
from google.colab import files<br />
wb = files.upload()<br />
df = pandas.read_csv('pandascsv.csv')<br />
print(df)<br />
 


