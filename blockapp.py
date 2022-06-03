# Importing modules to be used
import time as t 
from datetime import datetime as dt    


# Creating the necessary instances for the various path and https.
host_temp = "hosts" # temp file to check if program works
host_path_mac = "\etc\hosts"  # True path to the file running the program on mac[ absolute path]
host_path_windows = "" # True path to the file running the program on windows[ absolute path]

redirect = "127.0.0.1"   # site to redirect the websites to if searched
site_list = ["facebook.com", "youtube.com", "gmail.com", "freecoursesite.com", "www.facebook.com", "www.youtube.com", "www.gmail.com", "www.freecoursesite.com",
"https://mail.google.com/mail/u/0/#inbox", "www.twitter.com", "twitter.com", "netflix.com", "www.netflix.com", "www.yahoo.com", "yahoo.com"]   # lists of websites to block

# Creating a loop to run the neccesary commands
while True:
    # calling a time range for working hours.
    if dt(dt.now().year, dt.now().month, dt.now().day, 9, 30) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours.....")

        # opening the file from the file path, reading and performing operations on it
        with open(host_temp, "r+") as file:
            content = file.read()

            # reading through the lines and appending the sites that are not in the file
            for websites in site_list:
                if websites in content:
                    pass

                else:
                    file.write(redirect + " " + websites + "\n")

        

    else:  # Calls to time outside the working hours
        with open(host_temp, "r+") as file:
            contents = file.readlines() # Reading the lines in the file and not word by word
            file.seek(0) # Places the cursor back to the start of the file

            # 
            for lines in contents:
                if not any(website in lines for website in site_list):
                    file.write(lines)
            file.truncate()  # Deletes all that prints after the first print

        print("Time to sleep!")

    t.sleep(20)



































