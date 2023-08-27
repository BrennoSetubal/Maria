import speech_recognition as sr
import pyttsx3
import comandos_main as cm
import webbrowser
engine = pyttsx3.init()


def falar(texto):
    engine.say(texto)
    engine.runAndWait()

def google():
    url = "https://www.google.com/"
    resposta = webbrowser.open(url)
    return resposta

def chat_gpt():
    url = "https://chat.openai.com/"
    resposta = webbrowser.open(url)
    return resposta

def email():
    url = "https://mail.google.com/"
    resposta = webbrowser.open(url)
    return resposta

# reconhecimento de voz
rec = sr.Recognizer()

with sr.Microphone() as mic:
    while True:
        rec.adjust_for_ambient_noise(mic)
        print("Pode falar agora!")
        audio = rec.listen(mic)

        try:
            texto = rec.recognize_google(audio, language="pt-BR")

            print(texto)

            if texto.lower() == 'oi mari':
                falar(cm.SystemInfo.saldacao())

            if texto.lower() == 'que horas são' or texto.lower() == 'me fale as horas':
                falar(cm.SystemInfo.pegar_hora())

            if texto.lower() == 'oi maria' or texto.lower() == 'olá maria' or texto.lower() == 'oi oi maria' or texto.lower() == 'ok maria':
                falar(cm.SystemInfo.boas_vindas())

            if texto.lower() == 'obrigado':
                falar(cm.SystemInfo.obrigado())

            if texto.lower() == 'bom dia':
                falar(cm.SystemInfo.bom_dia())

            if texto.lower() == 'boa tarde':
                falar(cm.SystemInfo.boa_tarde())

            if texto.lower() == 'boa noite':
                falar(cm.SystemInfo.boa_noite())

            if texto.lower() == 'você está bem' or texto.lower() == 'tudo bem':
                falar(cm.SystemInfo.ta_bem())

            if texto.lower() == 'como você está':
                falar(cm.SystemInfo.como_esta())
            if texto.lower() == 'qual é a data de hoje' or texto.lower() == 'que dia é hoje':
                falar(cm.SystemInfo.pegar_data())

            if texto.lower() == 'o que é o brasil' or texto.lower() == 'brasil' or texto.lower() == 'informações sobre o brasil':
                falar(cm.SystemInfo.brasil())

            if texto.lower() == 'abrir google' or texto.lower() == 'abra o google' or texto.lower() == 'maria abri o google' or texto.lower() == 'ok maria abri o e-mail':
                google()

            if texto.lower() == 'abrir chat gpt' or texto.lower() == 'abra o chat gpt' or texto.lower() == 'maria abri o chat gpt' or texto.lower() == 'ok maria abri o e-mail':
                chat_gpt()

            if texto.lower() == 'abrir e-mail' or texto.lower() == 'abra o e-mail' or texto.lower() == 'maria abri o e-mail' or texto.lower() == 'ok maria abri o e-mail':
                email()

            elif texto.lower() == 'feixar' or texto.lower() == 'dispensada' or texto.lower() == 'encerrar' or texto.lower() == 'fechar':
                break

        except sr.UnknownValueError:
            print("Não foi possível reconhecer a fala. Por favor, tente novamente.")
            falar("Não foi possível reconhecer a fala. Por favor, tente novamente.")
