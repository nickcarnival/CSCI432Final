# Python terminal colors


red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
white='\033[37m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'

def cprint(color, text):
    if color == 'r':
        print(red, text)
    elif color == 'g':
        print(green, text)
    elif color == 'b':
        print(blue, text)
    elif color == 'lb':
        print(lightblue, text)
    elif color == 'y':
        print(yellow, text)

    print(white)