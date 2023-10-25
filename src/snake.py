import sys
import random
import pygame

# Inicializar Pygame
pygame.init()

# Configurar la ventana del juego
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Snake")

# Configurar el reloj del juego
reloj = pygame.time.Clock()

# Configurar la serpiente
TAMANO_SERPIENTE = 20
serpiente = [pygame.Rect(ANCHO_VENTANA // 2, ALTO_VENTANA // 2, TAMANO_SERPIENTE, TAMANO_SERPIENTE)]
direccion_serpiente = "derecha"

# Configurar la comida
TAMANO_COMIDA = 20
comida = pygame.Rect(random.randint(0, ANCHO_VENTANA - TAMANO_COMIDA), random.randint(0, ALTO_VENTANA - TAMANO_COMIDA), TAMANO_COMIDA, TAMANO_COMIDA)

# Inicializar el estado del juego
game_over = False

# Función para mostrar un mensaje de "Game Over"
def mostrar_game_over():
    fuente = pygame.font.Font(None, 36)
    texto_game_over = fuente.render("Game Over - Presiona R para reiniciar", True, (255, 255, 255))
    rectangulo_game_over = texto_game_over.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))
    ventana.blit(texto_game_over, rectangulo_game_over)
    pygame.display.flip()

# Bucle del juego
while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # Manejar la entrada del jugador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_RIGHT] and direccion_serpiente != "izquierda":
            direccion_serpiente = "derecha"
        elif teclas[pygame.K_LEFT] and direccion_serpiente != "derecha":
            direccion_serpiente = "izquierda"
        elif teclas[pygame.K_UP] and direccion_serpiente != "abajo":
            direccion_serpiente = "arriba"
        elif teclas[pygame.K_DOWN] and direccion_serpiente != "arriba":
            direccion_serpiente = "abajo"

        # Mover la serpiente
        if direccion_serpiente == "derecha":
            nueva_cabeza = pygame.Rect(serpiente[-1].x + TAMANO_SERPIENTE, serpiente[-1].y, TAMANO_SERPIENTE, TAMANO_SERPIENTE)
        elif direccion_serpiente == "izquierda":
            nueva_cabeza = pygame.Rect(serpiente[-1].x - TAMANO_SERPIENTE, serpiente[-1].y, TAMANO_SERPIENTE, TAMANO_SERPIENTE)
        elif direccion_serpiente == "arriba":
            nueva_cabeza = pygame.Rect(serpiente[-1].x, serpiente[-1].y - TAMANO_SERPIENTE, TAMANO_SERPIENTE, TAMANO_SERPIENTE)
        elif direccion_serpiente == "abajo":
            nueva_cabeza = pygame.Rect(serpiente[-1].x, serpiente[-1].y + TAMANO_SERPIENTE, TAMANO_SERPIENTE, TAMANO_SERPIENTE)

        # Comprobar colisiones con la pared
        if (
            nueva_cabeza.left < 0
            or nueva_cabeza.right > ANCHO_VENTANA
            or nueva_cabeza.top < 0
            or nueva_cabeza.bottom > ALTO_VENTANA
        ):
            game_over = True

        # Comprobar colisiones con la serpiente
        if nueva_cabeza in serpiente:
            game_over = True

        # Comprobar si la serpiente ha comido la comida
        if nueva_cabeza.colliderect(comida):
            comida.x = random.randint(0, ANCHO_VENTANA - TAMANO_COMIDA)
            comida.y = random.randint(0, ALTO_VENTANA - TAMANO_COMIDA)
        else:
            serpiente.pop(0)

        # Agregar la nueva cabeza a la serpiente
        serpiente.append(nueva_cabeza)

        # Borrar la pantalla
        ventana.fill((0, 0, 0))

        # Dibujar la serpiente y la comida
        for segmento in serpiente:
            pygame.draw.rect(ventana, (255, 255, 255), segmento)
        pygame.draw.rect(ventana, (255, 0, 0), comida)

        # Actualizar la pantalla
        pygame.display.flip()

        # Limitar la velocidad de fotogramas
        reloj.tick(10)

    # Mostrar "Game Over" si el juego ha terminado
    while game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    # Reiniciar el juego
                    serpiente = [pygame.Rect(ANCHO_VENTANA // 2, ALTO_VENTANA // 2, TAMANO_SERPIENTE, TAMANO_SERPIENTE)]
                    direccion_serpiente = "derecha"
                    comida.x = random.randint(0, ANCHO_VENTANA - TAMANO_COMIDA)
                    comida.y = random.randint(0, ALTO_VENTANA - TAMANO_COMIDA)
                    game_over = False

        mostrar_game_over()

