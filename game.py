import pygame
from config import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, WHITE, BLACK, RED, GREEN

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
            self.screen.fill(WHITE)

            pygame.display.flip()

            self.clock.tick(FPS)
            
            if self.state.nextState:
                self.changeState(self.state.nextState)

        pygame.quit()

    def changeState(self):
        self.state = newState 
        