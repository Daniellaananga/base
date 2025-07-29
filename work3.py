from colorama import Fore, Style
print(Fore.BLUE + "enter two numbers" + Style.RESET_ALL)
a=float(input(Fore.GREEN + "Enter First Number :" + Style.RESET_ALL))
b=float(input(Fore.GREEN + "Enter Second Number :" +Style.RESET_ALL))
c=a*b
print(Fore.YELLOW + "The multiplication of the two numbers entered is :", c)