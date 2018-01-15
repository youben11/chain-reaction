import pygame
from algorithms import *
from sys import exit
from random import randint
from os import environ

#COLORS to be used for the players
COLOR = {1: (255,0,0), 2: (0,255,0), 3: (0,0,255), 4: (255,255,0),\
        5: (255,0,255), 6: (0,255,255), 7: (128,128,128), 8: (255,255,255),}
#PADDING
PADD = 10
#LEFT BUTTON MOUSE
LEFT = 1
#FRAME PER SECOND
FPS = 90
#Screen size on startup
SIZE_X = 800
SIZE_Y = 600
#player
MAX_PLAYER = 8
MIN_PLAYER = 1
#row
MAX_ROW = 10
MIN_ROW = 3
#column
MAX_COLUMN = 15
MIN_COLUMN = 3

def drawBoard(surface, board, n, m, player):
    surface.fill((0,0,0))
    width = surface.get_width() - PADD * 2
    height = surface.get_height() - PADD * 2
    color = COLOR[player]
    l_width = 2
    #draw vertical lines
    for i in range(PADD,width + PADD * 2, width / m):
        pygame.draw.line(surface, color, (i, PADD),\
                        (i, height + PADD),l_width)
    #draw horizontal lines
    for j in range(PADD,height + PADD * 2, height / n):
        pygame.draw.line(surface, color, (PADD, j),\
                        (i, j),l_width)#width + PADD ~= i
    #draw cells
    for i in range(n):
        for j in range(m):
            drawCell(surface, board, n, m, i, j)

def drawCell(surface, board, n, m, i, j):
    cell = board[i][j]
    pawns = cell[1]
    if pawns == 0:
        #nothing to do
        return
    width = (surface.get_width() - PADD * 2) / m
    height = (surface.get_height() - PADD * 2) / n
    base_x = PADD + width * j
    base_y = PADD + height * i
    color = COLOR[cell[0]]

    if pawns % 2 == 1:
        pygame.draw.circle(surface, color,\
                (base_x + width / 2, base_y + height / 2),\
                width / 10)
        pawns -= 1
    if pawns == 2:
        pygame.draw.circle(surface, color,\
                (base_x + width / 5, base_y + height / 5),\
                width / 10)
        pygame.draw.circle(surface, color,\
                (base_x + width * 4/5 , base_y + height * 4/5),\
                width / 10)

def initGame(surface):
    width = surface.get_width()
    height = surface.get_height()
    player = 2
    row = 5
    column = 5
    #selection texts
    font = pygame.font.Font("ressources/Lato-Black.ttf", width / 25)
    text = font.render("Select number of players", True, (255,255,255), (0,0,0))
    surface.blit(text,(width * 1/10, height * 1/5))
    text = font.render("Select number of rows", True, (255,255,255), (0,0,0))
    surface.blit(text,(width * 1/10, height * 2/5))
    text = font.render("Select number of columns", True, (255,255,255), (0,0,0))
    surface.blit(text,(width * 1/10, height * 3/5))
    #increment and decrement button
    font = pygame.font.Font("ressources/Lato-Black.ttf", width / 20)
    inc = font.render("+", True, (255,255,255), (0,0,0))
    dec = font.render("-", True, (255,255,255), (0,0,0))
    rect_inc_players = surface.blit(inc,(width * 9/10, height * 1/5))
    rect_dec_players = surface.blit(dec,(width * 7/10, height * 1/5))
    rect_inc_rows = surface.blit(inc,(width * 9/10, height * 2/5))
    rect_dec_rows = surface.blit(dec,(width * 7/10, height * 2/5))
    rect_inc_columns = surface.blit(inc,(width * 9/10, height * 3/5))
    rect_dec_columns = surface.blit(dec,(width * 7/10, height * 3/5))
    #start text
    font = pygame.font.Font("ressources/Lato-Black.ttf", width / 15)
    start = font.render("START", True, (255,255,255), (0,0,0))
    rect_start = surface.blit(start,((surface.get_width() - start.get_width()) / 2,\
                        surface.get_height() * 5.0/6))
    pygame.display.flip()

    font = pygame.font.Font("ressources/Lato-Black.ttf", width / 25)
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            if rect_start.collidepoint(event.pos):
                break
            #nb_player
            if rect_inc_players.collidepoint(event.pos):
                if player in range(MIN_PLAYER, MAX_PLAYER):
                    player += 1
            if rect_dec_players.collidepoint(event.pos):
                if player in range(MIN_PLAYER + 1, MAX_PLAYER + 1):
                    player -= 1
            #nb_row
            if rect_inc_rows.collidepoint(event.pos):
                if row in range(MIN_ROW,MAX_ROW):
                    row += 1
            if rect_dec_rows.collidepoint(event.pos):
                if row in range(MIN_ROW + 1, MAX_ROW + 1):
                    row -= 1
            #nb_column
            if rect_inc_columns.collidepoint(event.pos):
                if column in range(MIN_COLUMN, MAX_COLUMN):
                    column += 1
            if rect_dec_columns.collidepoint(event.pos):
                if column in range(MIN_COLUMN + 1, MAX_COLUMN + 1):
                    column -= 1
        #update numbers
        nb_player = font.render("%d   " % player, True,(255,255,255),(0,0,0))
        rect_nb_player = surface.blit(nb_player,(width * 8/10, height * 1/5))
        nb_row = font.render("%d   " % row, True,(255,255,255),(0,0,0))
        rect_nb_row = surface.blit(nb_row,(width * 8/10, height * 2/5))
        nb_column = font.render("%d   " % column, True,(255,255,255),(0,0,0))
        rect_nb_column = surface.blit(nb_column,(width * 8/10, height * 3/5))

        pygame.display.flip()

    return (player, row, column)

def gamePlay(surface, board, n, m, player):
    players = range(1,player + 1)
    p = 0
    winner = 0
    move_counter = 0
    #play against computer
    COMPUTER = 2
    if player == 1:
        computer_mode = True
        players.append(COMPUTER)
    else:
        computer_mode = False

    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        #QUIT
        quit_events = pygame.event.get(pygame.QUIT)
        if len(quit_events) != 0:
            pygame.quit()
            exit()
        player = players[p]
        drawBoard(surface, board, n, m, player)
        #display the changes before blocking on select()
        pygame.display.flip()
        #select a cell
        if computer_mode and player == COMPUTER:
            i, j = select_computer(board, n, m, COMPUTER)
        else:
            i, j = select(surface, board, n, m, player)
        put(board, n, m, i, j, player)
        #winners and loosers
        to_remove = []
        for player in players:
            if move_counter >= len(players):
                if loose(board, n, m, player):
                    to_remove.append(player)
                elif win(board, n, m, player):
                    winner = player
        if winner != 0:
            break
        for r in to_remove:
            players.remove(r)
        #next player, next move
        p = (p + 1) % len(players)
        move_counter = move_counter + 1

    #The winneeer!
    drawBoard(surface, board, n, m, winner)
    font = pygame.font.Font("ressources/Lato-Black.ttf", m * 4)
    wins = font.render("Player %d wins !" % winner, True, COLOR[winner], (0,0,0))
    surface.blit(wins,((surface.get_width() - wins.get_width()) / 2,\
                        surface.get_height() / 3))
    pygame.display.flip()


def select(surface, board, n, m, nb):
    width = (surface.get_width() - PADD * 2) / m
    height = (surface.get_height() - PADD * 2) / n

    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        #QUIT
        quit_events = pygame.event.get(pygame.QUIT)
        if len(quit_events) != 0:
            pygame.quit()
            exit()
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            x = event.pos[0]
            y = event.pos[1]
            i = (y - PADD) / height
            j = (x - PADD) / width
            if possible(board, n, m, i, j, nb):
                return (i,j)

def select_computer(board, n, m, player):
    pos = []
    for i in range(n):
        for j in range(m):
            if possible(board, n, m, i, j, player):
                pos.append((i, j))
    rand = randint(0, len(pos) - 1)
    choice = pos[rand]
    return choice


def chainReaction():
    environ["SDL_VIDEO_CENTERED"] = '1'
    pygame.init()
    pygame.display.set_caption("Chain Reaction")

    while True:
        #screen for initGame()
        screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
        player, row, column = initGame(screen)
        #screen for the rest of the game
        screen = pygame.display.set_mode((column * 50, row * 50))
        board = newBoard(row, column)
        gamePlay(screen, board, row, column, player)
        #play again or quit
        font = pygame.font.Font("ressources/Lato-Black.ttf", row * 3)
        again = font.render("Play again", True, (255,255,255), (0,0,0))
        quit = font.render("Quit", True, (255,255,255), (0,0,0))
        rect_again = screen.blit(again,((screen.get_width() - again.get_width()) / 2,\
                            screen.get_height() * 2.0/3))
        rect_quit = screen.blit(quit,((screen.get_width() - quit.get_width()) / 2,\
                            screen.get_height() * 5.0/6))
        pygame.display.flip()

        clock = pygame.time.Clock()
        while True:
            clock.tick(FPS)
            event = pygame.event.poll()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                if rect_again.collidepoint(event.pos):
                    break
                if rect_quit.collidepoint(event.pos):
                    pygame.quit()
                    exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()
