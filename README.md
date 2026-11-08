# DoS-UDP-flood-tool
 # EDUCATIONAL PURPOSES ONLY
Prosty skrypt napisany w Pythonie w celach edukacyjnych, służący do demonstracji działania protokołu UDP oraz generowania ruchu sieciowego w ramach testu.

 Ostrzeżenie (Disclaimer)
Ten kod jest przeznaczony  wyłącznie do celów naukowych i testów we własnym, kontrolowanym środowisku (jeżeli chcesz przetestować router swój  `127.0.0.1`). Uruchamianie tego skryptu wobec cudzych sieci, serwerów lub urządzeń bez zgody jest nielegalne.  nie ponosze  żadnej odpowiedzialności za szkody wyrządzone przez oprogramowanie.
### Wszystkie zmiany jakie można dokonać ale wtedy skrypt staje sie o wiele bardziej destrukcyjny
-usunięcie time.sleep pozwoli na wysyłanie nieograniczaną ilość pakietów czyli wyśle tyle ile twój procesor da rade (pierwotnie ustawiłem ograniczenie dla niekumatych)
-zwiększenie objętości pliku wysylanego z 1kb(1024bajtów) można zmienić do 1.4kb(1436bajtów) jak coś wszystko powyżej 1.5kb jest fragmentowane i nie dziala to już tak dobrze jakbyśmy chcieli 
