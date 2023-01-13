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
        [`sudo nano /etc/hosts`]

    2.  Head to the crontab by typing the command
        [`sudo crontab -e`]

    3.  Navigate to the end of the file and add the command
        [`@reboot python3 <filepath>`]

        <!-- Which in my case is -->
        [@reboot python3 /Users/mbp16/Desktop/Projects/Raw_codes/website_blocker/blockapp.py]
        
        <!-- Then ^X to exit, Y to save. -->

    4.You need to provide administrative rights to your terminal
        and you can do so by using the command (<sudo> before calling the program)
        [`sudo python3 blockapp.py`] 



##### Windows Users
    To run it as a system file. (from the )

    1. Rename the blockapp.py to blockapp.pyw
    
    2. On lines 22 & 36, make sure that the `<host_path_mac>` is changed to `<host_path_windows>` 

    3.  Naigate to `<Task Scheduler>` from the windows menu.

    4.  Click on `<Create Basic Task>` on the right hand pane.

    5.  Type the name of you want to give it.

    6.  On `<configure for>` choose your windows version.

    7.  Check the `<run with the highest privileges>` to enable adminstrative rights.

    8. To to `<Triggers>` from the top tabs, click on <New>.

    9. On `<Begin the task>`, Choose `<At startup>` and click `<OK>`

    10. Navigate to `<Actions>` from the top tabs, on `<Actions>`, choose `<Start a program>`, click on Browse and choose the file (blockapp.pyw)

    11. Navigate to `<Conditions>` from the top tabs and uncheck `<Start the program if the computer is on AC power>`

    12. Click `<OK>`



## Author
Boateng Jephthah Agyenim
