# import pygame  # Importa a biblioteca pygame
# import time  # Para controlar o tempo de execução

# # Inicializa o mixer do pygame
# pygame.mixer.init()

# # Solicita ao usuário o nome do arquivo MP3
# arquivo_mp3 = input("Digite o caminho do arquivo MP3: ")

# # Carrega o arquivo de áudio
# pygame.mixer.music.load(arquivo_mp3)

# # Reproduz o áudio
# pygame.mixer.music.play()

# print("Reproduzindo áudio... Pressione Ctrl+C para parar.")

# # Aguarda enquanto o áudio está sendo reproduzido
# while pygame.mixer.music.get_busy():
#     time.sleep(1)  # Espera 1 segundo para evitar consumo excessivo de CPU

import pygame
pygame.init()
pygame.mixer.music.load('/PythonExercicios/ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()