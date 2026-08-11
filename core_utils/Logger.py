from colorama import Fore, Style, init

class Logger:

    def __init__(self):
        init(autoreset=True)

    def Log_Error(self, Logs, Code):
        print(Style.BRIGHT+Fore.RED+ f'\nLog ---> {Logs}, \n Error Code --> {Code} \n')

    def Log_Success(self, Logs, Code):
        print(Style.BRIGHT+Fore.GREEN+ f'\nLog ---> {Logs}, \n Success Code--> {Code} \n')

    def Log_Debug(self, Logs, Code):
        print(Fore.YELLOW+ f'\n Log ---> {Logs}, \nDebug Code --> {Code} \n')

    def Log_Verbose(self, Logs, Code):
        print(Fore.BLUE+ f'\n Log ---> {Logs}, \nVerbose --> {Code} \n')



