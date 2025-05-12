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

## 🧑‍💻 Como usar

Após rodar o comando `python main.py`, o projeto será iniciado e a assistente virtual Stella começará a monitorar os comandos de voz. **Para interagir com a Stella**, basta falar algo como:

### Formato de Comando

1. **Fale "Stella" seguido do comando desejado**. Exemplos de comandos incluem:
   - **"Stella, qual a previsão do tempo?"**
   - **"Stella, qual é a minha localização?"**
   - **"Stella, me conta uma piada!"**
   - **"Stella, qual é o número aleatório?"**
   
A assistente irá responder a cada comando de forma vocal e, se necessário, executará ações como consultar APIs externas ou gerar respostas aleatórias.

### Exemplos de uso:

1. **Localização**
   - Comando: "Stella, qual a minha localização?"
   - Resposta: A assistente irá dizer algo como "Você está na cidade de [sua cidade]."

2. **Previsão do Clima**
   - Comando: "Stella, qual a previsão do tempo?"
   - Resposta: A assistente fornecerá a previsão do tempo para sua cidade, caso tenha configurado corretamente a chave API do OpenWeather.

3. **Piada**
   - Comando: "Stella, me conta uma piada."
   - Resposta: A assistente irá contar uma piada aleatória em português.

4. **Número Aleatório**
   - Comando: "Stella, me dê um número aleatório."
   - Resposta: A assistente gerará um número aleatório e responderá, por exemplo, "O número aleatório gerado é 7."

Agora a sua assistente virtual está pronta para ser utilizada! Você pode falar com ela a qualquer momento e ela irá responder conforme os comandos que você definir. Divirta-se e explore as funcionalidades de Stella! 😊🎙️

---

## 🏗️ Arquitetura

Stella foi projetada com uma arquitetura procedural para garantir facilidade de manutenção e expansão. A seguir, detalho a estrutura básica do projeto.

### Estrutura de Pastas

```plaintext
assistente/
├── audios/
│   └── 
├── main.py
├── requirements.txt
├── README.md
```

---

## 🚀 Expanda o seu assistente!

O projeto **Stella** é apenas a base para uma assistente virtual poderosa. Com a arquitetura modular que você encontrou, é muito fácil adicionar novas funcionalidades, integrações e inteligências ao sistema.

### O que você pode adicionar?

- **Integrações com outros serviços**: Você pode facilmente integrar com APIs de terceiros, como serviços de previsão do tempo, notícias, redes sociais, sistemas de automação residencial e muito mais.
  
- **Funções inteligentes**: Adicione funcionalidades que utilizam inteligência artificial, como reconhecimento de sentimentos, análise de textos ou até mesmo chatbots avançados.

- **Comandos personalizados**: Crie novos comandos para interagir com sistemas locais ou na web. Adicione qualquer tipo de funcionalidade que atenda às suas necessidades ou crie novas formas de interação com a Stella.

- **Melhorias contínuas**: Com a estrutura modular, você pode sempre melhorar e adicionar novas capacidades à assistente, deixando-a cada vez mais inteligente e interativa.

Esse é apenas o começo! O que você pode fazer com a Stella é ilimitado, e você tem total liberdade para customizar e expandir a inteligência conforme seu gosto e necessidade. Se tiver ideias interessantes, compartilhe com a comunidade e faça sua contribuição para que todos possamos aproveitar!

---

## 👨‍💻 Direitos Autorais

Este projeto é mantido por **Leonardo Alves Fernandes**.

- **Email**: [leonardoaf65572005@gmail.com](mailto:leonardoaf65572005@gmail.com)
- **Website**: [leonardo-alves.com](https://leonardo-alves.com)

Todos os direitos reservados.
