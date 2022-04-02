from turtle import back
import pygame
from colors import colors
from tetris import tetris
from Assets import constants
pygame.init()




#creating the display
screen = pygame.display.set_mode(constants.SIZE)

#setting up the title of the game
pygame.display.set_caption("Tetris")

#background music for the game
background_music = pygame.mixer.music
background_music.load(constants.BACKGROUND_MUSIC)
background_music.play(-1)
background_music.set_volume(0.07)



clock = pygame.time.Clock()
game = tetris(20,10)
counter = 0
pressing_down = False
#variable for the loop
done = False
while not done:
    if game.get_figure() is None:
        game.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0


    if counter % (constants.FPS // game.get_level() // 2) == 0 or pressing_down:
        if game.get_state() == "start":
            game.go_down()

    #keyboard input control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
            #reset the game
            if event.key == pygame.K_ESCAPE:
                game.__init__(20,10)
                background_music.rewind()
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            pressing_down = False
    #screen background
    screen.fill(constants.WHITE)

    for i in range(game.height):
        for j in range (game.width):
            pygame.draw.rect(screen, constants.GRAY, [game.get_x() + game.get_zoom() * j , game.get_y() + game.get_zoom() * i, game.get_zoom(), game.get_zoom(),],1)
            if game.get_field(i,j) > 0:
                pygame.draw.rect(screen,colors[game.get_field(i,j) ],
                [game.x + game.get_zoom() * j + 1, game.get_y() + game.get_zoom() *i +1, game.get_zoom() -2, game.get_zoom() - 1])
    
    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.get_color()],
                        [
                            game.x + game.get_zoom() * (j + game.figure.get_x()) + 1,
                            game.get_y() + game.get_zoom() * (i + game.figure.get_y()) + 1,
                            game.get_zoom() - 2 , game.get_zoom() - 2
                        ]
                    )
    font  =  pygame.font.SysFont('Calibri', 25, True, False)
    font1 =  pygame.font.SysFont('Calibri',65,True,False)
    text = font.render('Score: ' + str(game.get_score()),True,constants.BLACK)

    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

    screen.blit(text, [0, 0])
    if game.get_state() == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])
    
    pygame.display.flip()
    clock.tick(constants.FPS)

pygame.quit()