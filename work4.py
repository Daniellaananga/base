from colorama import Fore, Style, Back
print(Fore.CYAN + Back.LIGHTBLACK_EX + "HERE WE DO DIVISION" + Style.RESET_ALL)
print(Fore.CYAN + Back.LIGHTBLACK_EX + "YOU MUST ENTER TWO NUMBERS" + Style.RESET_ALL)
a=int(input(Fore.GREEN + "ENTER YOUR FIRST NUMBER :" + Style.RESET_ALL))
if a != 0: 
    print(Fore.MAGENTA + "NUMBER VALID" + Style.RESET_ALL)
else:
    print(Fore.RED + "ERROR : DIVISION BY 0!!!" + Style.RESET_ALL)
b=int(input(Fore.GREEN + "ENTER YOUR SECOND NUMBER :" + Style.RESET_ALL))
if b != 0:
    print(Fore.MAGENTA + "NUMBER VALID" + Style.RESET_ALL)
else:
    print(Fore.RED + "ERROR : DIVISION BY 0!!!" + Style.RESET_ALL)
c=a/b
print(Fore.LIGHTMAGENTA_EX +"FIRST NUMBER / SECOND NUMBER : ", c)