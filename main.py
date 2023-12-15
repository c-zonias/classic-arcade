import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

robot = pygame.image.load('robot.png')
coin = pygame.image.load('coin.png')
coin_width, coin_height = coin.get_size()

x = 400
y = 500
robot_width, robot_height = robot.get_size()
vel = 20

coin_x = random.randint(0, 800 - coin_width)
coin_y = 0
coin_vel = 20

score = 0
lives = 3

font = pygame.font.SysFont(None, 50)
start_text = font.render("Press SPACE to continue", True, (255, 255, 255))
text_rect = start_text.get_rect(center=(400, 300))

start_game = False
while not start_game:
    screen.fill((0, 0, 0))
    screen.blit(start_text, text_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start_game = True
            break

def display_score(score, lives):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score) + " Lives: " + str(lives), True, (255, 255, 255))
    screen.blit(text, (10, 10))

def display_game_over():
    font = pygame.font.SysFont(None, 100)
    text = font.render("Game Over", True, (255, 0, 0))
    text_rect = text.get_rect(center=(400, 300))
    screen.blit(text, text_rect)

def display_message(message):
  font = pygame.font.SysFont(None, 50)
  text = font.render(message, True, (255, 0, 0))
  text_rect = text.get_rect(center=(400, 500))
  screen.blit(text, text_rect)

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x - vel > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x + vel < 800 - robot_width:
        x += vel

    coin_y += coin_vel

    if coin_y > 600 - coin_height:
        coin_y = 0
        coin_x = random.randint(0, 800 - coin_width)
        lives -= 1

    if lives == 0:
        run = False

    if x < coin_x + coin_width and x + robot_width > coin_x and \
       y < coin_y + coin_height and y + robot_height > coin_y:

        score += 1
        coin_y = 0
        coin_x = random.randint(0, 800 - coin_width)

    
        if score % 5 == 0: 
            coin_vel += 5

  

    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    screen.blit(coin, (coin_x, coin_y))
    display_score(score, lives)
    pygame.display.update()

if score < 100:
  display_message("Congratulations there are not many things you can buy in finland with your money")

display_game_over()
pygame.display.update()
pygame.time.delay(2000)
pygame.quit()



