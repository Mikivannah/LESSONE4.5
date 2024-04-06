# ЭТО БАЗА ДЛЯ ЛЮБОЙ ИГРЫ
import pygame
pygame.init()

window_size = (800, 600) # переменная . которая принимает  значение размера игрового окна
screen = pygame.display.set_mode(window_size) #где pygame.display.set_mode( переменная окна с размерами) структура  создающая окно
pygame.display.set_caption("Тестовый проект") # заголовок окна

# Мы начинаем создавать "тело игрового цикла" это то что играет

run = True        # переменная  которая запискает игровой цикл


while run:   # создаем цикл WHILE RUN , КОТОРЫЙ БУДЕТ РАБОТАТЬ ПОКА RUN ПЕРЕЙДЕТ В ЛОЖЬ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0)) # кол -во красного , кол во голубго , кол-во зеленый
    pygame.display.flip() # будем обновлять экран


pygame.quit()