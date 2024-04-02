import pygame
import sys
import random

# Initialiser Pygame
pygame.init()

# Définir la taille de l'écran
screen = pygame.display.set_mode((800, 600))

# Définir la couleur du serpent et de la pomme
snake_color = (0, 255, 0)
apple_color = (255, 0, 0)

# Créer le serpent et les pommes
snake = [pygame.Rect(400, 300, 20, 20)]
apple = pygame.Rect(random.randint(0, 780), random.randint(0, 580), 20, 20)

# Définir la direction initiale
direction = 'RIGHT'

# Initialiser le score
score = 0

# Boucle du jeu
while True:
    # Vérifier les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Déplacer le serpent
    if direction == 'UP':
        snake.insert(0, snake[0].copy().move(0, -20))
    elif direction == 'DOWN':
        snake.insert(0, snake[0].copy().move(0, 20))
    elif direction == 'LEFT':
        snake.insert(0, snake[0].copy().move(-20, 0))
    elif direction == 'RIGHT':
        snake.insert(0, snake[0].copy().move(20, 0))

    # Vérifier si le serpent a mangé une pomme
    if snake[0].colliderect(apple):
        apple.x = random.randint(0, 780)
        apple.y = random.randint(0, 580)
        score += 10  # Incrémenter le score de 10 points

    else:
        del snake[-1]

    # Vérifier si le serpent est sorti de l'écran
    if not 0 <= snake[0].x < 800 or not 0 <= snake[0].y < 600:
        pygame.quit()
        sys.exit()

    # Vérifier si le serpent a touché sa propre queue
    if snake[0] in snake[1:]:
        pygame.quit()
        sys.exit()

    # Remplir l'écran de noir
    screen.fill((0, 0, 0))

    # Dessiner le serpent et la pomme
    for part in snake:
        pygame.draw.rect(screen, snake_color, part)
    pygame.draw.rect(screen, apple_color, apple)

    # Afficher le score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255)) 
    screen.blit(score_text, (10, 10)) 

    # Mettre à jour l'écran
    pygame.display.flip()

    # Faire une pause
    pygame.time.wait(100)
