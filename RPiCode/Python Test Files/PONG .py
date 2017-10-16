import pygame, sys
from pygame.locals import *

FPS = 200

#Global Variables
WINDOWWIDTH = 400
WINDOWHEIGHT = 300
LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 20

BLACK = (0  ,0  ,0  )
WHITE = (255,255,255)

def drawArena():
    DISPLAYSURF.fill((0,0,0))
    #Draw Outline
    pygame.draw.rect(DISPLAYSURF, WHITE, ((0,0),(WINDOWWIDTH,WINDOWHEIGHT)), LINETHICKNESS*2)
    #Draw Centre line
    pygame.draw.line(DISPLAYSURF, WHITE, ((WINDOWWIDTH/2),0),((WINDOWWIDTH/2),WINDOWHEIGHT), (LINETHICKNESS/4))

def drawPaddle(paddle):
    #Stops paddle moving too low
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    #Stops paddle moving too high
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    #Draws paddle
        pygame.draw.rect(DISPLAYSURF, WHITE, paddle)

def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)

def moveBall(ball, ballDirX, ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY
    return ball

def checkEdgeCollision(ball, ballDirX, ballDirY):
    if ball.top == (LINETHICKNESS) or ball.bottom == (WINDOWHEIGHT - LINETHICKNESS):
        ballDirY = ballDirY * -1
    if ball.left == (LINETHICKNESS) or ball.right == (WINDOWWIDTH - LINETHICKNESS):
        ballDirX = ballDirY * -1
    return ballDirX, ballDirY

def checkHitBall(ball, paddle1, paddle2, ballDirX):
    if ballDirX == -1 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
        return -1
    elif ballDirX == 1 and paddle2.left == ball.right and paddle2.top < ball.top and paddle2.bottom > ball.bottom:
        return -1
    else:
        return 1

def checkPointScored(paddle1, ball, score, ballDirX):
    if ball.left == LINETHICKNESS:
        return 0
    elif ballDirX == -1 and paddle1.right == ball.left and paddle1.top and paddle1.bottom > ball.bottom:
        score += 1
        return score
    elif ball.right == WINDOWWIDTH - LINETHICKNESS:
        score += 5
        return score
    else:
        return score

def artificialIntelligence(ball, ballDirX, paddle2):
    if ballDirX == -1:
        if paddle2.centery < (WINDOWHEIGHT/2):
            paddle2.y += 1
        elif paddle2.centery > (WINDOWHEIGHT/2):
            paddle2.y -= 1
    elif ballDirX == 1:
        if paddle2.centery < ball.centery:
            paddle2.y += 1
        else:
            paddle2.y -= 1
    return paddle2

def displayScore(score):
    resultSurf = BASICFONT.render('Score = %s' %(score), True, WHITE)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = (WINDOWWIDTH - 150, 25)
    DISPLAYSURF.blit(resultSurf, resultRect)
    
def main():
    pygame.init()
    global DISPLAYSURF
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Pong')
 
    #Initiate and set starting variables
    ballX = WINDOWWIDTH/2 - LINETHICKNESS/2
    ballY = WINDOWHEIGHT/2 - LINETHICKNESS/2
    playerOnePosition = (WINDOWHEIGHT - PADDLESIZE) /2
    playerTwoPosition = (WINDOWHEIGHT - PADDLESIZE) /2
    score = 0

    ballDirX = -1
    ballDirY = -1

    #Create rectangles for ball and paddles
    paddle1 = pygame.Rect(PADDLEOFFSET,playerOnePosition, LINETHICKNESS,PADDLESIZE)
    paddle2 = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, playerTwoPosition, LINETHICKNESS,PADDLESIZE)
    ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)

    #Draws the starting position of the Arena
    drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)

    pygame.mouse.set_visible(0)     

    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                paddle1.y = mousey

        drawArena()
        drawPaddle(paddle1)
        drawPaddle(paddle2)
        drawBall(ball)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()
