import os
try:
    import random
    import logging
    import threading
    from datetime import datetime
    import pyttsx3
    import speech_recognition as sr
    import pygame
    import requests
    from unidecode import unidecode
    from playsound3 import playsound
    import hashlib
    from rapidfuzz import fuzz
except ImportError as e:
    os.system('pip install pyttsx3 SpeechRecognition pygame requests unidecode playsound3 pyaudio rapidfuzz')
    input("\n\n[!] Reinstalei as dependências necessárias. Pressione Enter para continuar...")
    exit(1)

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    datefmt='%d/%m/%Y %H:%M:%S')

# Inicializa pygame e pyttsx3
pygame.mixer.init()
engine = pyttsx3.init()

# Hotwords
hotwords = ["stella", "stela", "estella", "estela", "istella", "istela", "cela", "tela", "is tela", "costela"]
def contem_hotword(fala):
    for hotword in hotwords:
        score = fuzz.partial_ratio(hotword, fala)
        if score >= 80:  # ajuste a sensibilidade aqui (de 70 a 90)
            return True
    return False

def tocar_audio(path):
    try:
        playsound(path)
        if os.path.exists(path):
            os.remove(path)
    except Exception as e:
        logging.error(f"Erro ao tocar áudio: {e}")

def criar_audio(nome, texto, velocidade=350):
    nome = hashlib.md5(nome.encode()).hexdigest()
    caminho = f"./audios/{nome}.mp3"
    if not os.path.exists(caminho):
        logging.info(f"Stella: {texto}")
        engine.setProperty('rate', velocidade)
        engine.save_to_file(texto, caminho)
        engine.runAndWait()
    tocar_audio(caminho)

def informar_localizacao():
    try:
        ip = requests.get('https://api.ipify.org/').text
        resposta = requests.get(f"http://ip-api.com/json/{ip}").json()
        cidade = resposta.get("city", "desconhecida")
        criar_audio("localizacao", f"Você está na cidade de {cidade}.")
    except:
        criar_audio("erro_localizacao", "Não foi possível obter sua localização.")

def obter_data():
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    criar_audio("data", f"Hoje é {data}.")

def obter_previsao_clima(cidade):
    chave_api = 'sua_chave_api_openweathermap'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br&units=metric"
    resposta = requests.get(url)
    dados = resposta.json()
    if dados["cod"] == 200:
        temp = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        criar_audio("clima", f"A previsão do tempo em {cidade} é de {temp} graus Celsius com {descricao}.")
    else:
        criar_audio("erro_clima", "Desculpe, não consegui obter a previsão do tempo.")

def obter_definicao(palavra):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/pt/{palavra}"
    resposta = requests.get(url)
    dados = resposta.json()
    if 'message' not in dados:
        definicao = dados[0]['meanings'][0]['definitions'][0]['definition']
        criar_audio("definicao", f"A definição de {palavra} é: {definicao}")
    else:
        criar_audio("erro_definicao", "Desculpe, não consegui encontrar a definição dessa palavra.")

def contar_piada():
    url = "https://v2.jokeapi.dev/joke/Any?lang=pt"
    resposta = requests.get(url)
    dados = resposta.json()
    if dados["type"] == "single":
        piada = dados["joke"]
    else:
        piada = f"{dados['setup']} - {dados['delivery']}"
    criar_audio("piada", piada, 250)

def dar_conselho():
    url = "https://api.adviceslip.com/advice"
    resposta = requests.get(url)
    dados = resposta.json()
    criar_audio("conselho", dados["slip"]["advice"])

def contar_curiosidade():
    url = "https://uselessfacts.jsph.pl/random.json?language=pt"
    resposta = requests.get(url)
    dados = resposta.json()
    criar_audio("curiosidade", dados["text"])

def obter_ip_publico():
    ip = requests.get('https://api.ipify.org/').text
    criar_audio("ip", f"Seu IP público é {ip}.", 200)

def obter_cidade():
    ip = requests.get('https://api.ipify.org/').text
    resposta = requests.get(f"http://ip-api.com/json/{ip}").json()
    cidade = resposta.get("city", "desconhecida")
    criar_audio("cidade", f"Você está na cidade de {cidade}.")

def frase_motivacional():
    url = "https://zenquotes.io/api/random"
    resposta = requests.get(url)
    dados = resposta.json()
    criar_audio("motivacional", dados[0]["q"])

def gerar_numero_aleatorio(x, y):
    numero = random.randint(x, y)
    criar_audio("numero", f"O número aleatório gerado é {numero}.")

respostas = {
    "erro": [
        "Desculpe, não entendi.",
        "Pode repetir, por favor?",
        "Não consegui executar esse comando.",
        "Desculpe, não consegui processar isso.",
        "Não sei como responder a isso.",
        "Desculpe, não tenho essa informação.",
        "Não consegui entender o que você disse.",
        "Desculpe, não consegui processar seu pedido.",
        "Desculpe, não consegui entender o que você disse."
    ]
}

def resposta_padrao():
    resposta = random.choice(respostas["erro"])
    criar_audio("erro", resposta, 450)

comandos_personalizados = {
    "localizacao": informar_localizacao,
    "data": obter_data,
    "clima": obter_previsao_clima,
    "definicao": obter_definicao,
    "piada": contar_piada,
    "conselho": dar_conselho,
    "curiosidade": contar_curiosidade,
    "ip": obter_ip_publico,
    "cidade": obter_cidade,
    "motivacional": frase_motivacional,
    "numero aleatorio": gerar_numero_aleatorio
}

historico = []
def executar(comando):
    """
    Executa o comando solicitado, se reconhecido.
    """
    for palavra, acao in comandos_personalizados.items():
        if palavra in comando:
            historico.append(comando)
            acao()
            return
    resposta_padrao()

def responde(fala):
    """
    Responde ao comando com áudio.
    """
    thread = threading.Thread(target=criar_audio, args=("feedback", "Processando seu comando...", 550))
    thread.start()
    thread.join()
    executar(fala)

def normalizar_fala(fala):
    """
    Normaliza a fala para comparação.
    """
    return unidecode(fala).lower()

def monitorar_microfone():
    """
    Monitora o microfone para comandos de voz.
    """
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            criar_audio("inicio", "Olá, eu sou a Stella! Pode falar comigo.")
            while True:
                logging.info("Aguardando comando...")
                audio = reconhecedor.listen(source)
                try:
                    fala = reconhecedor.recognize_google(audio, language="pt-BR")
                    fala = normalizar_fala(fala)
                    
                    if contem_hotword(fala):
                        logging.info(f"Comando detectado: {fala}")
                        responde(fala)
                except sr.UnknownValueError:
                    pass
                except sr.RequestError as e:
                    logging.error(f"Erro no reconhecimento: {e}")
        except Exception as e:
            logging.error(f"Erro ao acessar o microfone: {e}")

def main():
    """
    Função principal que inicia o monitoramento do microfone.
    """
    monitorar_microfone()

if __name__ == "__main__":
    main()