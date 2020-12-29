import threading
import sys
from time import sleep
import os
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(4. / 100)


#print(usage)
def banner():
    os.system("clear")
    print('''\033[31m 
    ██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗   ██╗    ██████╗ ██╗██████╗ ████████╗██╗  ██╗██████╗  █████╗ ██╗   ██╗
    ██║  ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝    ██╔══██╗██║██╔══██╗╚══██╔══╝██║  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝
    ███████║███████║██████╔╝██████╔╝ ╚████╔╝     ██████╔╝██║██████╔╝   ██║   ███████║██║  ██║███████║ ╚████╔╝ 
    ██╔══██║██╔══██║██╔═══╝ ██╔═══╝   ╚██╔╝      ██╔══██╗██║██╔══██╗   ██║   ██╔══██║██║  ██║██╔══██║  ╚██╔╝  
    ██║  ██║██║  ██║██║     ██║        ██║       ██████╔╝██║██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║   ██║   
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝        ╚═╝       ╚═════╝ ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝
               ~                  ~
     *                   *                *       *
                  *               *
  ~       *                *         ~    *
              *       ~        *              *   ~
                  )         (         )              *
    *    ~     ) (_)   (   (_)   )   (_) (  *
           *  (_) # ) (_) ) # ( (_) ( # (_)       *
              _#.-#(_)-#-(_)#(_)-#-(_)#-.#_
  *         .' #  # #  #  # # #  #  # #  # `.   ~     *
           :   #    #  #  #   #  #  #    #   :
    ~      :.       #     #   #     #       .:      *
        *  | `-.__                     __.-' | *
           |      `````"""""""""""`````      |         *
     *     |         | ||\ |~)|~)\ /         |
           |         |~||~\|~ |~  |          |       ~
   ~   *   |                                 | *
           |      |~)||~)~|~| ||~\|\ \ /     |         *
   *    _.-|      |~)||~\ | |~|| /|~\ |      |-._
      .'   '.      ~            ~           .'   `.  *
      :      `-.__    { MARISSA !!}      __.-'      :
       `.         `````"""""""""""`````         .'
         `-.._                             _..- ''')
banner()
slowprint('\033[00m           \033[01m\033[33m                            Wish You a Happy Birthday Dear Marissa! \033[00m\033[00m\n')
slowprint('\033[00m           \033[01m\033[33m                            Marissa is more priceless than the most beautiful diamond.\n'
          '                                                          You are not only strong and wise, but kind and thoughtful as well for Max. \n'
          '                                                             Your birthday is the perfect opportunity to show you much always.\n'
          '                                                              I care and how grateful I am to have you in my life My Marissa. \033[00m\033[00m\n')

import datetime

#asking the user to input their birthdate
birthDate = input("Enter your birth date Marissa :)) (dd/mm/yyyy)\n>>> ")
birthDate = datetime.datetime.strptime(birthDate, "%d/%m/%Y").date()
print("Your birthday is on "+ birthDate.strftime("%d") + " of " + birthDate.strftime("%B, %Y"))

currentDate = datetime.datetime.today().date()

#some calculations here
age = currentDate.year - birthDate.year
monthVeri = currentDate.month - birthDate.month
dateVeri = currentDate.day - birthDate.day

#Type conversion here
age = int(age)
monthVeri = int(monthVeri)
dateVeri = int(dateVeri)

# some decisions
if monthVeri < 0 :
    age = age-1
elif dateVeri < 0 and monthVeri == 0:
    age = age-1


#lets print the age now
print("Marissa is {0:d} old :)".format(age))