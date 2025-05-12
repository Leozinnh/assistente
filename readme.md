# Stella - Assistente Virtual em Python

Stella é uma assistente virtual simples e poderosa, construída em Python, que responde a comandos de voz e realiza diversas funções úteis, como fornecer informações sobre o clima, a localização, piadas e muito mais.

## 🚀 Funcionalidades

- **Localização**: Obtém sua localização atual com base no seu IP.
- **Data e Hora**: Fornece a data e hora atuais.
- **Clima**: Consulta a previsão do tempo.
- **Definições**: Obtém a definição de palavras.
- **Piadas**: Conta piadas aleatórias.
- **Conselhos**: Fornece conselhos aleatórios.
- **Curiosidades**: Conta curiosidades interessantes.
- **Número Aleatório**: Gera um número aleatório.
- **IP Público**: Mostra o seu IP público.

## 📥 Como instalar

### 1. Clone o repositório

Primeiro, clone o repositório para o seu computador.

```bash
git clone https://github.com/Leozinnh/assistente.git
```

### 2. Instale as dependências

Este projeto requer algumas dependências que você pode instalar usando o `pip`. Execute o seguinte comando para instalar todas as dependências necessárias:

```bash
pip install -r requirements.txt
```
```bash
pip install pyttsx3 SpeechRecognition pygame requests unidecode playsound3 pyaudio rapidfuzz
```
### 3. Configuração

- **API do OpenWeather** (OPCIONAL): Para obter a previsão do tempo, você precisará de uma chave API da [OpenWeatherMap](https://openweathermap.org/api). Substitua `'sua_chave_api_openweathermap'` no código pela sua chave de API.

- **Microfone**: Certifique-se de ter um microfone funcionando e configurado para que a assistente virtual possa reconhecer comandos de voz.

### 4. Teste o projeto

Depois de configurar tudo, basta rodar o seguinte comando para iniciar a assistente virtual:

```bash
python main.py
```