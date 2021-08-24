from colorama import Fore, Style, init; init()
import os, threading

class Color:
    def __init__(self):
        # Styles
        self.invisible = '\033[30;40;196m'
        self.underline = '\033[4m'
        self.bright =  '\033[1;4m'
        self.reset =   '\033[0m'

        # Colors
        self.white     = self.rgb(255, 255, 255)
        self.magenta = self.rgb(249, 53, 248) 
        self.yellow  = self.rgb(216, 235, 52)
        self.orange  = self.rgb(255, 99, 71)
        self.blue_m  = self.rgb(88, 5, 255)
        self.green   = self.rgb(0, 255, 0)
        self.red     = self.rgb(255, 0, 0)

    def rgb(self, r: int, g: int, b: int):
        return '\033[38;2;<r>;<g>;<b>m'.replace('<r>', str(r)).replace('<g>', str(g)).replace('<b>', str(b))

    def fade(self, text: str):
        final = ''
        for char in text:
            final += f'{self.rgb(200, 60, len(final) + 12)}{char}'
        
        return final

class Console:
    def __init__(self):
        self.locker = threading.Semaphore(value= 1)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __lock_print(self, text: str, past: str, color: Fore):
        self.locker.acquire()
        print(f'[{color}{past}{Fore.RESET}] {text}.')
        self.locker.release()

    def __format_text(self, text: str):
        return text.replace('->', f'{Fore.LIGHTCYAN_EX}->{Fore.RESET}').replace(':', f'{Fore.YELLOW}:{Fore.RESET}').replace('Error', f'{Fore.RED}Error{Fore.RESET}').replace('Invalid', f'{Fore.MAGENTA}Invalid{Fore.RESET}').replace('"', f'{Fore.BLUE}"{Fore.RESET}').replace('killed', f'{Fore.LIGHTRED_EX}killed{Fore.RESET}')

    def loader_banner(self):
        self.clear()
        print(Style.BRIGHT + Fore.WHITE + '''
         _    _ _                     _           
        | |  | | |                   | |          
        | |__| | |     ___   __ _  __| | ___ _ __ 
        |  __  | |    / _ \ / _` |/ _` |/ _ \ '__|
        | |  | | |___| (_) | (_| | (_| |  __/ |   
        |_|  |_|______\___/ \__,_|\__,_|\___|_|    github.com/Its-Vichy/HBot
        ''' + Style.RESET_ALL + Fore.RESET)
    
    def cnc_banner(self):
        self.clear()
        print(Style.BRIGHT + Fore.WHITE + '''
         _    _ ____        _   
        | |  | |  _ \      | |  
        | |__| | |_) | ___ | |_ 
        |  __  |  _ < / _ \| __|
        | |  | | |_) | (_) | |_ 
        |_|  |_|____/ \___/ \__|    github.com/Its-Vichy/HBot
        ''' + Style.RESET_ALL + Fore.RESET)
    
    def print_success(self, text: str):
        self.__lock_print(self.__format_text(text), 'SUCCESS', Fore.LIGHTGREEN_EX)
    
    def print_info(self, text: str):
        self.__lock_print(self.__format_text(text), 'INFO', Fore.LIGHTYELLOW_EX)