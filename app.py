import time as t
from datetime import datetime as dt    


# Creating the necessary instances for the various path and https.
host_temp = "hosts"
host_path = "\etc\hosts"
redirect = "127.0.0.1"
site_list = ["facebook.com", "youtube.com", "gmail.com", "freecoursesite.com", "www.facebook.com", "www.youtube.com", "www.gmail.com", "www.freecoursesite.com",
"https://mail.google.com/mail/u/0/#inbox"]


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours.....")
        with open(host_temp, "r+") as file:
            content = file.read()
            for websites in site_list:
                if websites in content:
                    pass
                else:
                    file.write(redirect + " " + websites + "\n")

        

    else:
        print("Time to sleep!")

    t.sleep(10)



































