# ЭТО БАЗА ДЛЯ ЛЮБОЙ ИГРЫ
import pygame
pygame.init()

window_size = (800, 600) # переменная . которая принимает  значение размера игрового окна
screen = pygame.display.set_mode(window_size) #где pygame.display.set_mode( переменная окна с размерами) структура  создающая окно
pygame.display.set_caption("Тестовый проект") # заголовок окна

# Мы начинаем создавать "тело игрового цикла" это то что играет


image = pygame.image.load("picPython.png")
image_rect = image.get_rect()      # get- брать      rect- рамка

#speed = 3


run = True        # переменная  которая запискает игровой цикл


while run:   # создаем цикл WHILE RUN , КОТОРЫЙ БУДЕТ РАБОТАТЬ ПОКА RUN ПЕРЕЙДЕТ В ЛОЖЬ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX - 100
            image_rect.y = mouseY - 100

    # keys = pygame.key.get_pressed()  # задаем клавишу
    # if keys[pygame.K_LEFT]:          # если было нажатие на левую стрелку
    #     image_rect.x -= speed        #координата х уvtymibncz  на величину  speed
    # if keys[pygame.K_RIGHT]:         # если было нажатие на правую стрелку
    #     image_rect.x += speed        # координата х увеличится на величину  speed
    # if keys[pygame.K_UP]:  # если было нажатие на левую стрелку
    #     image_rect.y -= speed  # координата y уvtymibncz  на величину  speed
    # if keys[pygame.K_DOWN]:  # если было нажатие на правую стрелку
    #     image_rect.y += speed  # координата y увеличится на величину  speed






    screen.fill((0, 0, 0)) # кол -во красного , кол во голубго , кол-во зеленый
    screen.blit(image, image_rect)
    pygame.display.flip() # будем обновлять экран


pygame.quit()