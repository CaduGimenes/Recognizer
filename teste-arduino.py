from pyfirmata import Arduino, util
import time

Uno = Arduino("COM6")

print('Olá Mundo!')

while True:
    Uno.digital[13].write(1)
    print('Led ligado')
    time.sleep(1)

    Uno.digital[13].write(0)
    print('Led desligado')
    time.sleep(1)