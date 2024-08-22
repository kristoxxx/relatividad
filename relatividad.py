import pygame
import math
import random

# Inicializamos Pygame
pygame.init()

# Dimensiones de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Viaje Espacial: Contracción de la Longitud")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Longitud original del objeto
original_length = 200

# Carga de fuentes
font = pygame.font.SysFont(None, 36)

# Generación de estrellas para el fondo
stars = [(random.randint(0, width), random.randint(0, height)) for _ in range(100)]

# Constante de la velocidad de la luz
c = 299792458  # Velocidad de la luz en metros por segundo

# Función para calcular la longitud contraída
def contracted_length(v, L0):
    gamma = 1 / math.sqrt(1 - (v/c)**2)
    L = L0 / gamma
    return L

# Bucle principal del juego
running = True
velocity = 0
velocity_increment = 1000000  # Incremento pequeño en la velocidad
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control de la velocidad con las teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        velocity += velocity_increment  # Aumenta la velocidad gradualmente
    if keys[pygame.K_DOWN] and velocity > 0:
        velocity -= velocity_increment  # Disminuye la velocidad gradualmente

    # Evitar que la velocidad supere la velocidad de la luz
    if velocity >= c:
        velocity = c - 1  # Ajuste para que no sea exactamente igual a c y evitar división por cero en gamma

    # Calculamos la longitud contraída
    new_length = contracted_length(velocity, original_length)

    # Limpiamos la pantalla
    screen.fill(black)

    # Dibujamos el fondo estrellado
    for star in stars:
        pygame.draw.circle(screen, white, star, 2)

    # Efecto de movimiento de las estrellas
    stars = [(x - 2 if x > 0 else width, y) for x, y in stars]

    # Dibujamos el objeto (nave espacial)
    pygame.draw.rect(screen, white, [width/2 - new_length/2, height/2 - 10, new_length, 20])

    # Mostrar la velocidad y la longitud contraída
    velocity_text = font.render(f'Velocidad: {velocity:.2f} m/s', True, white)
    length_text = font.render(f'Longitud: {new_length:.2f} px', True, white)
    screen.blit(velocity_text, (10, 10))
    screen.blit(length_text, (10, 50))

    # Actualizamos la pantalla
    pygame.display.flip()

pygame.quit()
