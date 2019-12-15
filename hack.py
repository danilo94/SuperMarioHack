from gerenciadorDeMemoria import *
from Enderecos import *
class hack(object):

    gerenciadorDeMemoria = None
    vidaAoPegarMoeda = None
    def __init__(self,nomeProcesso):
        self.gerenciadorDeMemoria = gerenciadorDeMemoria(nomeProcesso)
        self.vidaAoPegarMoeda = False
        self.fixarStatusMario = False
        pass




    def fixarStatusPenaMario(self):
        statusMarioAgora = self.gerenciadorDeMemoria.lerByte(STATUSMARIO)
        print(statusMarioAgora)
        if (statusMarioAgora != MARIO_PENINHA):
            self.gerenciadorDeMemoria.escreverByte(STATUSMARIO,MARIO_PENINHA.to_bytes(1,byteorder='little'))
        pass

    def valorfixoMoedas(self):
        valorPadraoDeMoedas = 99
        quantidadeAtualDemoedas = self.gerenciadorDeMemoria.lerByte(MOEDAS)
        if (quantidadeAtualDemoedas!=99):
            self.gerenciadorDeMemoria.escreverByte(MOEDAS,valorPadraoDeMoedas.to_bytes(1,byteorder='little'))
