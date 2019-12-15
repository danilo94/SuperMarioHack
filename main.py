from hack import *
from time import *
processo = "zsnesw.exe"

hackMario = hack(processo)


while True:
    hackMario.fixarStatusPenaMario()
    hackMario.valorfixoMoedas()
    sleep(0.5)
