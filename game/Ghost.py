import pygame


class Ghost(pygame.sprite.Sprite):

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        # asf
        return rect.move(0)
