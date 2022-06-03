# ABOUT
    This is an app that blocks a user from accessing some websites termed distracting during working or studying hours.


### LIBRAIRIES USED
    - Datetime
        This is a module for providing classes to work with time and dates.
        https://docs.python.org/3/library/datetime.html

    - Time
        This is a module for providing time related functions
        https://docs.python.org/3/library/time.html


### HOW TO SET IT UP AND RUN

##### Mac/Linux Users
    To run it as a system file. (from the /etc/hosts file) 

    1.  To navigate to the file and view what is inside use
        [sudo nano /etc/hosts]

    2.  You need to provide administrative rights to your terminal
        and you can do so by using the command (<sudo> before calling the program)
        [sudo python3 blockapp.py] 

    3.  Head to the crontab by typing the command
        [sudo crontab -e]

    4.  Navigate to the end of the file and add the command
        [@reboot python3 <filepath>]
        Which in my case is
        [@reboot python3 ]




##### Windows Users






MAc users

sudo nano /etc/hosts
sudo crontab -e
@reboot python3 -filepath














## Author
Boateng Jephthah Agyenim