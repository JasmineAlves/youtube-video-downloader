# Youtube Video Downloader
Script em Python que utiliza a biblioteca `pytubefix` para baixar vídeos do YouTube de forma simples e eficiente. 

## 📚 | Funcionalidades
- Download automático do vídeo na melhor qualidade disponível (formato MP4).
- Interface via terminal, onde o usuário apenas insere o link do vídeo.
- Biblioteca confiável (`pytubefix`) para manipulação e download de vídeos do YouTube.

## 🔧 | Requisitos 
- Python (versão 3.6 ou superior)
- Biblioteca `pytubefix` instalada na máquina. 

Caso ainda não tenha a biblioteca `pytubefix` instalada, utilize o seguinte comando para instalá-la:

    pip install pytubefix


## 🖥️ | Funcionamento
1. O script solicita ao usuário um link de vídeo do YouTube;
2. Ele cria um objeto `YouTube` com base no link informado;
3. Obtém o melhor resolução possível no formato MP4;
4. Realiza o download do vídeo no mesmo diretório que o script foi executado;
5. Exibe uma mensagem confirmando o download.

## 📄 | Documentação
- [pytubefix](https://pytubefix.readthedocs.io/en/latest/)
