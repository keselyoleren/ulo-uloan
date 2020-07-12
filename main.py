
import pygame
import random
import time
import sys

pygame.init()
class Game:
    def __init__(self):
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 102)
        self.kuning = (255, 255, 51)
        self.black = (0, 0, 0)
        self.red = (213, 50, 80)
        self.green = (0, 255, 0)
        self.blue = (50, 153, 213)
        self.dis_width = 600
        self.dis_height = 400
        self.font_style = pygame.font.SysFont("bahnschrift", 30)
        self.score_font = pygame.font.SysFont("comicsansms", 35)
        self.x1_change = 0
        self.y1_change = 0
        self.x1 = self.dis_width / 2
        self.y1 = self.dis_height / 2
        self.snake_block = 15
        self.game_over = False
        self.game_close = False
        self.foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
        self.foody = round(random.randrange(0, self.dis_height - self.snake_block) /10.0) * 10.0
        self.snake_speed = 5
        self.snake_list = []        
        self.length_of_snake = 1
        

    def on_message(self, message, color):
        message = self.font_style.render(message, True, color)
        self.display.blit(message, [self.dis_width/6 , self.dis_height/2])

    def score(self, score):
        self.value = self.score_font.render("Score: " + str(score), True, self.yellow)
        self.display.blit(self.value, [0,0])

    def our_snake(self, snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(self.display, self.green, [x[0], x[1], snake_block, snake_block])
    
    def on_init(self):
        self.display = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption("ulo uloan")
        pygame.display.update()

    def on_execute(self):
        self.on_init()

        while not self.game_over:
            while self.game_close == True:
                self.display.fill(self.black)
                self.on_message("Haha.. nubb !! press C-play Q-Quit", self.red)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_c:
                            app = Game()
                            app.on_execute()
                            
                            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x1_change = -self.snake_speed
                        self.y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        self.x1_change = self.snake_speed
                        self.y1_change = 0
                    elif event.key == pygame.K_UP:
                        self.y1_change = -self.snake_speed
                        self.x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        self.y1_change = self.snake_speed
                        self.x1_change = 0
            if self.x1 >= self.dis_width or self.x1 < 0 or self.y1 >= self.dis_height or self.y1 < 0:
                self.game_close = True

            self.x1 += self.x1_change
            self.y1 += self.y1_change
            self.display.fill(self.black)
            pygame.draw.rect(self.display, self.red, [self.foodx, self.foody, self.snake_block, self.snake_block])
            self.snake_head = []
            self.snake_head.append(self.x1)
            self.snake_head.append(self.y1)
            self.snake_list.append(self.snake_head)
            if len(self.snake_list) > self.length_of_snake:
                del self.snake_list[0]

            for a in self.snake_list[:-1]:
                if a == self.snake_head:
                    self.game_close = True
            
            self.our_snake(self.snake_block, self.snake_list)
            self.score(self.length_of_snake -1)

            pygame.display.update()

            if self.x1 == self.foodx and self.y1 == self.foody:
                self.foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
                self.foody = round(random.randrange(0, self.dis_height - self.snake_block) /10.0) * 10.0
                self.length_of_snake += 1


if __name__=="__main__":
    run = Game()
    run.on_execute()