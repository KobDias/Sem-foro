import time
from colorama import Fore

def luz(vermelho, amarelo, verde):
    while True:
        print(Fore.RED + "Vermelho")
        time.sleep(vermelho)

        print(Fore.YELLOW + "Amarelo")
        time.sleep(amarelo)

        print(Fore.GREEN + "Verde")
        time.sleep(verde)

luz(7, 2, 5)

# pip install colorama
