from subprocess import check_output, Popen
from sys import argv
from time import sleep
from math import pow

syntax_string: str = 'Syntax: python3 main.py [target network] [-r (recursive: optional)]'

try:
    target_network = argv[1]
except:
    print(syntax_string)
try:
    recursive = (lambda: True if argv[2] == '-r' else False)()
except:
    recursive = False
    


def calc_meters(rssi: int) -> float:
    # calc with exponential regression model from field testing
    return round(0.0990201415 * pow(0.9190093419, rssi+10), 2)

def get_signal_strength(command: str, target_network: str) -> list:
    # giant space is 19 characters long and with signal strength included 22
    result = list()
    for line in command.splitlines():
        if target_network in line:
            result.append(int(((line[line.index(target_network):line.index(target_network)+len(target_network)+22]))[len(target_network)+19:len(line)]))
    return result

# main function
def main() -> None:
    sleep(3)
    command_output = check_output(['airport', '-s']).decode()
    for index, ap in enumerate(get_signal_strength(command_output, target_network)):
        print(f'AP #{index+1} Distance: {calc_meters(ap)} meters')
    if get_signal_strength(command_output, target_network) == []:
        print('No Data')

if not recursive: {main() | exit(0)}

# mainloop
while True:
    try:
        main()
        print('\n')
    except KeyboardInterrupt:
        quit()


