import pygame
import sys
import time

# Инициализация pygame
pygame.init()

# Установка размеров окна
WIDTH = 1000
HEIGHT = 600
BG_COLOR = (0, 128, 0)  # Ярко зеленый цвет
BALL_COLOR = (255, 255, 0)  # Желтый цвет


# Создание класса для ракетки
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 100
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def move(self, dy):
        self.y += dy
        self.rect.y = self.y


# Создание класса для мяча
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.dx = 5
        self.dy = 5
        self.rect = pygame.Rect(self.x, self.y, 2 * self.radius, 2 * self.radius)
        self.initial_speed = 15

    def draw(self):
        pygame.draw.circle(screen, BALL_COLOR, (self.x + self.radius, self.y + self.radius), self.radius)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y

        if self.rect.colliderect(player_paddle.rect) or self.rect.colliderect(enemy_paddle.rect):
            self.dx *= -1
        if self.y < 0 or self.y > HEIGHT - 2 * self.radius:
            self.dy *= -1


# Создание объектов игры
player_paddle = Paddle(10, HEIGHT // 2)
enemy_paddle = Paddle(WIDTH - 20, HEIGHT // 2)

ball = Ball(WIDTH // 2, HEIGHT // 2)

# Создание окна игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Загрузка музыки
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1)

# Переменные для счета и времени
player_score = 0
enemy_score = 0
start_time = time.time()


# Загрузка изображения
image = pygame.image.load('background_image.png')

# Установка позиции изображения на экране
image_rect = image.get_rect()
image_rect.center = (WIDTH // 2, HEIGHT // 2)

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_paddle.move(-15)
    if keys[pygame.K_DOWN]:
        player_paddle.move(15)

    enemy_paddle.rect.centery = ball.rect.centery

    ball.move()
    # Здесь вставляем код для отображения изображения
    screen.fill(BG_COLOR)
    screen.blit(image, image_rect)

    player_paddle.draw()
    enemy_paddle.draw()
    ball.draw()

    if player_score == 21 or enemy_score == 21:
        font = pygame.font.Font(None, 72)
        if player_score == 21:
            text = font.render("Player wins!", True, (255, 255, 255))
        else:
            text = font.render("Enemy wins!", True, (255, 255, 255))

        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(text, text_rect)
        pygame.display.flip()

        time.sleep(3)  # Пауза перед выходом из игры
        pygame.quit()
        sys.exit()

    if ball.x > WIDTH:  # Если мяч ушел за пределы экрана (возвращаем мяч и увеличиваем счет)
        ball.x = WIDTH // 2
        ball.y = HEIGHT // 2
        ball.dx = -ball.initial_speed
        player_score += 1

    if ball.x < 0:
        ball.x = WIDTH // 2
        ball.y = HEIGHT // 2
        ball.dx = ball.initial_speed
        enemy_score += 1

    elapsed_time = int(time.time() - start_time)

    screen.fill(BG_COLOR)
    player_paddle.draw()
    enemy_paddle.draw()
    ball.draw()

    font = pygame.font.Font(None, 36)
    player_text = font.render(f"Игрок: {player_score}", True, (255, 255, 255))
    enemy_text = font.render(f"Противник: {enemy_score}", True, (255, 255, 255))
    time_text = font.render(f"Time: {elapsed_time}", True, (255, 255, 255))

    screen.blit(player_text, (10, 10))
    screen.blit(enemy_text, (WIDTH - enemy_text.get_width() - 10, 10))
    screen.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
