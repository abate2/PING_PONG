import pygame
pygame.init()

#colors 
black = (0, 0, 0)
white = (255, 255, 255)
screen_size = (800, 600)
player_width = 15
player_height = 90

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

#font and text
fuente = pygame.font.SysFont("Gothic Uralic", 28)
fuente2 = pygame.font.SysFont("Palladio Uralic", 20)
header_pong_center = fuente.render("PING PONG", True, white)

#score counter
score_player1 = 0
score_player2 = 0


#coordinates and speed of the player 1
player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0

#Coordinates and speed of the player 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0

#ball's coordinates
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3

game_over = False


while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      # player 1
      if event.key == pygame.K_w:
        player1_y_speed = -3
      if event.key == pygame.K_s:
        player1_y_speed = 3
      #player 2
      if event.key == pygame.K_UP:
        player2_y_speed = -3
      if event.key == pygame.K_DOWN:
        player2_y_speed = 3

    if event.type == pygame.KEYUP:
      #player 1
      if event.key == pygame.K_w:
        player1_y_speed = 0
      if event.key == pygame.K_s:
        player1_y_speed = 0
      #player 2
      if event.key == pygame.K_UP:
        player2_y_speed = 0
      if event.key == pygame.K_DOWN:
        player2_y_speed = 0
	
	#ball's boundaries in y axis
  if pelota_y > 590 or pelota_y < 10:
    pelota_speed_y *= -1

  #check if the ball goes out by the right side
  if pelota_x > 800:
    pelota_x = 400
    pelota_y = 300
    score_player1 += 1
    #if the ball goes out of the screen, reverse the direction
    pelota_speed_x *= -1
    pelota_speed_y *= -1
	
  #check if the ball goes out by the left side
  if pelota_x < 0:
    pelota_x = 400
    pelota_y = 300
    score_player2 += 1
    #If the ball goes out of the screen, reverse the direction
    pelota_speed_x *= -1
    pelota_speed_y *= -1

  # You modifies the coordinates to give movement to the players/ ball
  player1_y_coor += player1_y_speed
  player2_y_coor += player2_y_speed
  #Player's boundaries
  if player1_y_coor < 0 or player1_y_coor > 510:
  	player1_y_speed = 0
  if player2_y_coor < 0 or player2_y_coor > 510:
    player2_y_speed = 0
	
  #ball's movement
  pelota_x += pelota_speed_x
  pelota_y += pelota_speed_y

  screen.fill(black)
  # score counter
  header_pong_left = fuente2.render(f'Score Player1: {score_player1}', True, white)
  header_pong_right = fuente2.render(f"Score Player2: {score_player2}", True, white)
  title_center = screen.blit(header_pong_center, (320,10))
  title_left = screen.blit(header_pong_left, (10, 10))
  title_right = screen.blit(header_pong_right, (560, 10))
    
  #draw zone
  jugador1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor, player_width, player_height))
  jugador2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor, player_width, player_height))
  pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)
	#draw zone
  #collisions
  if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
    pelota_speed_x *= -1
  
  pygame.display.flip()
  clock.tick(50)
pygame.quit()

