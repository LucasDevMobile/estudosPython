#faca um programa q reproduza o audio de um mp3

import pygame
pygame.init   #inicia o pygame
pygame.mixer.music.load ('meuarquivo.mp3')  #puxa o arquivo mp3 q esta na mesma pasta do exercicio
pygame.mixer.music.play   #da play na musica
pygame.event.wait ()     # espera a musica acabar


