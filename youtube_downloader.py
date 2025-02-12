'''
Entrada: Nenhum parâmetro é passado, a URL é solicitada via input.
Saída: O vídeo é baixado e salvo na mesma pasta onde o script for executado.
"""
'''
from pytubefix import YouTube

url = input("Insira o link do vídeo que deseja baixar: ")

ytb = YouTube(url)

print("Baixando", ytb.title)

resolution = ytb.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

resolution.download()

print("Download concluído!")
