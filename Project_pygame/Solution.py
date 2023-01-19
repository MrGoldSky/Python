import pygame
import time
from time import strftime, gmtime
import random
import sqlite3

WIDTH = 500
HEIGHT = 460

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
collor_score = pygame.Color(220, 20, 60)
collor_snake = pygame.Color(124, 252, 0)
collor_apple = pygame.Color(255, 0, 0)

snake_speed = 10
snake_position = [100, 50]

body_of_snake = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
    ]

apple_position = [
    random.randrange(1, (WIDTH // 10)) * 10,
    random.randrange(1, (HEIGHT // 10)) * 10
    ]
spawning_of_fruit = True

last_direction = "DOWN"
now_direction = last_direction

score = 0
game_run = True


def display_score():  
    score_font_style = pygame.font.SysFont("times new roman", 35)
    score_surface = score_font_style.render("Очки: " + str(score), True, black)
    score_rectangle = score_surface.get_rect()
    display_screen.blit(score_surface, score_rectangle)


def game_over():
    game_over_font_style = pygame.font.SysFont("times new roman", 50)
    game_over_surface = game_over_font_style.render(
        "Очки: " + str(score), True, collor_score
    )
    game_over_rectangle = game_over_surface.get_rect()
    game_over_rectangle.midtop = (WIDTH / 2, HEIGHT / 4)
    display_screen.blit(game_over_surface, game_over_rectangle)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    insert_score(score)
    quit()


def connect_to_db():
    try:
        con = sqlite3.connect("Project_pygame//base//db.sqlite")
        cur = con.cursor()
        return con, cur
    except BaseException:
        print("Ошибка подключения к БД")


def insert_score(score):
    con, cur = connect_to_db()
    try:
        result = cur.execute(f"""INSERT 
                             INTO pygame(result, time) 
                             VALUES({int(score)},'{strftime("%Y-%m-%d %H:%M:%S", gmtime())}')
                             """)
        con.commit()
        con.close()
        return result
    except BaseException as exception:
        print("Ошибка заполнения БД (score, time)")
        print(exception)


if __name__ == "__main__":
    pygame.init()
    display_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Змейка")
    game_clock = pygame.time.Clock()

    while game_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    now_direction = "UP"
                if event.key == pygame.K_DOWN:
                    now_direction = "DOWN"
                if event.key == pygame.K_LEFT:
                    now_direction = "LEFT"
                if event.key == pygame.K_RIGHT:
                    now_direction = "RIGHT"

        if now_direction == "UP" and last_direction != "DOWN":
            last_direction = "UP"
        if now_direction == "DOWN" and last_direction != "UP":
            last_direction = "DOWN"
        if now_direction == "LEFT" and last_direction != "RIGHT":
            last_direction = "LEFT"
        if now_direction == "RIGHT" and last_direction != "LEFT":
            last_direction = "RIGHT"

        if last_direction == "UP":
            snake_position[1] -= 10
        if last_direction == "DOWN":
            snake_position[1] += 10
        if last_direction == "LEFT":
            snake_position[0] -= 10
        if last_direction == "RIGHT":
            snake_position[0] += 10

        body_of_snake.insert(0, list(snake_position))
        if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
            score += 1
            spawning_of_fruit = False
            snake_speed += 0.2
        else:
            body_of_snake.pop()

        if not spawning_of_fruit:
            apple_position = [
                random.randrange(1, (WIDTH // 10)) * 10,
                random.randrange(1, (HEIGHT // 10)) * 10
            ]
        spawning_of_fruit = True
        display_screen.fill(white)

        for position in body_of_snake:
            pygame.draw.rect(display_screen, collor_snake, pygame.Rect(position[0], position[1], 10, 10))
            pygame.draw.rect(display_screen, collor_apple, pygame.Rect(apple_position[0], apple_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > WIDTH - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > HEIGHT - 10:
            game_over()

        for block in body_of_snake[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()
        display_score()
        pygame.display.update()
        game_clock.tick(snake_speed)
    
    pygame.quit()
