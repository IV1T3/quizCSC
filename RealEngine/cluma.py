import pygame, sys
from pygame.locals import *


def init(width, height, fullscreen, backgroundColor = (0,0,0) ):
    global screen
    global clock
    global screenColor

    screenColor = backgroundColor
    
    pygame.init()
    pygame.font.init()
    
    if fullscreen:
        flags = pygame.DOUBLEBUF | pygame.FULLSCREEN
    else:
        flags = pygame.DOUBLEBUF
        
    screen = pygame.display.set_mode((width, height), flags)
    pygame.display.set_caption("Quiz")
    clock = pygame.time.Clock()


def drawWords(position, words, fontSize = 23, fontColor = (255,255,255)):
    """Funktion, um Woerter zu schreiben"""

    global screen

    font = pygame.font.Font(None, fontSize)
    screen.blit(font.render(words, False, fontColor), position)

def drawCircle(m, r, color):
    global screen
    screen.lock()
    pygame.draw.circle(screen, color, m, r)
    screen.unlock()
        
def drawLine(point1, point2, color):
    global screen
    screen.lock()
    pygame.draw.line(screen, color, point1, point2)
    screen.unlock()

def drawRect(x, y, width, height, color):
    global screen
    screen.lock()
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
    screen.unlock()

def drawTriangle(point1, point2, point3, color):
    global screen
    pointlist = []
    pointlist.append(point1)
    pointlist.append(point2)
    pointlist.append(point3)
    screen.lock()
    pygame.draw.polygon(screen, color, pointlist)
    screen.unlock()

def draw():
    global screen
    global clock
    global screenColor

    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT or ((keys[K_LALT] or keys[K_RALT]) and keys[K_F4]) or keys[K_ESCAPE]:
            destruct()
            sys.exit()

            
    # Pygame aktuallisiert den Bildschirm
    pygame.display.flip()

    # Es wird gewartet, damit mit der Computer sich nicht ueberarbeitet
    clock.tick(30)
    screen.fill(screenColor)



def destruct():
    """Close the window"""
    pygame.quit()

