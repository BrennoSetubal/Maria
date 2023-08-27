import datetime
import wikipedia

wikipedia.set_lang('pt')


class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def saldacao():
        resposta = 'olá, senhor Breno'
        resposta2 = 'sejá bem-vindo'
        resposta3 = 'espero que esteja tudo bem com o senhor'
        return resposta, resposta2, resposta3

    @staticmethod
    def pegar_hora():
        now = datetime.datetime.now()
        resposta = f'São {now.hour} horas e {now.minute} minutos'
        return resposta

    @staticmethod
    def boas_vindas():
        resposta = 'olá, como você está ?' + 'está bem ?' + 'como posso ajudar ?'
        return resposta

    @staticmethod
    def bom_dia():
        resposta = 'olá, bom dia '
        return resposta

    @staticmethod
    def boa_tarde():
        resposta = 'olá, boa tarde '
        return resposta

    @staticmethod
    def boa_noite():
        resposta = 'olá, boa noite '
        return resposta

    @staticmethod
    def ta_bem():
        resposta = 'sim, estou'
        resposta1 = 'e você'
        return resposta, resposta1

    @staticmethod
    def obrigado():
        resposta = 'desponha'
        resposta1 = 'estarei a desposição'
        resposta2 = 'see , caso precisar'
        return resposta, resposta1, resposta2

    @staticmethod
    def como_esta():
        resposta = 'estou bem'
        resposta1 = ' e você'
        return resposta, resposta1

    @staticmethod
    def brasil():
        r = wikipedia.summary('Brasil')
        resposta = r[:200]
        return resposta

    @staticmethod
    def pegar_data():
        data = datetime.date.today()
        data_str = str(data)
        ano, mes, dia = data_str.split('-')
        meses = {
            '01': 'janeiro',
            '02': 'fevereiro',
            '03': 'março',
            '04': 'abril',
            '05': 'maio',
            '06': 'junho',
            '07': 'julho',
            '08': 'agosto',
            '09': 'setembro',
            '10': 'outubro',
            '11': 'novembro',
            '12': 'dezembro',
        }
        resposta_formatada = f'{dia} de {meses[mes]} de {ano}'

        return resposta_formatada
