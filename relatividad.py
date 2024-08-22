import pygame
import math

# Inicializamos Pygame
pygame.init()

# Dimensiones de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Contracción de la Longitud")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Longitud original del objeto
original_length = 200

# Función para calcular la longitud contraída
def contracted_length(v, L0):
  c = 299792458  # Velocidad de la luz
  gamma = 1 / math.sqrt(1 - (v/c)**2)
  L = L0 / gamma
  return L

# Bucle principal del juego
running = True
velocity = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aumentamos la velocidad gradualmente
    velocity += 0.01

    # Calculamos la longitud contraída
    new_length = contracted_length(velocity, original_length)

    # Limpiamos la pantalla
    screen.fill(black)

    # Dibujamos el objeto
    pygame.draw.rect(screen, white, [width/2 - new_length/2, height/2, new_length, 20])

    # Actualizamos la pantalla
    pygame.display.flip()

pygame.quit()
