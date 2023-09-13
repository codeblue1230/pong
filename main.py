import pygame
import random

pygame.init() # Initialize pygame
pygame.display.set_caption("Pong") # Makes Pong get displayed in the upper left of window
screen_width, screen_height = 1000, 700 # Variables for the size of the game screen
screen = pygame.display.set_mode((screen_width, screen_height)) # Set screen size using variables from line above, define the screen variable
clock = pygame.time.Clock() # Create clock object to be used later to control fram rate

rect_color = (255, 0, 0) # Variable holding rectangle color as red
rect_width, rect_height = 20, 110 # Define rectangle width and height
center_rect_Y = (screen_height - rect_height) / 2 # Define the y-axis position of the rectangles to center them vertically

ball_color = (255, 255, 255) # Variable holding ball color as white
center_ball_X, center_ball_Y = screen_width / 2, screen_height / 2 # Variable to center ball
ball_radius = 8 # Radius of the ball stored here


class Player: # Create player class
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.move = 5

    def draw_player(self): # method to draw each player on the screen
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move_player(self): # method to move each player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.x == 20: # Move player 1 Up
            self.y -= self.move
        if keys[pygame.K_s] and self.x == 20: # Move player 1 Down
            self.y += self.move
        if keys[pygame.K_UP] and self.x != 20: # Move player 2 Up
            self.y -= self.move
        if keys[pygame.K_DOWN] and self.x != 20: # Move player 2 Down
            self.y += self.move


class Ball: # Create Ball class
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.y_move = random.choice([-1, 1]) * 3
        self.x_move = random.choice([-1, 1]) * 3
    
    def draw_ball(self): # method to draw the ball on the screen
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move_ball(self): # method to move the ball
        self.x += self.x_move
        self.y += self.y_move
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.y_move *= -1


# Main game loop
def play():

    # Instantiate Player Objects
    player1 = Player(20, center_rect_Y, rect_width, rect_height, rect_color)
    player2 = Player(screen_width - 40, center_rect_Y, rect_width, rect_height, rect_color)

    # Instantiate Ball Object
    ball = Ball(center_ball_X, center_ball_Y, ball_radius, ball_color)

    running = True
    while running:
        for event in pygame.event.get(): # Loop through all events
            if event.type == pygame.QUIT: # If conditional to check if user closes program
                running = False # Break the loop if program gets closed

        screen.fill((0, 0, 0)) # Fill the screen with background color of black

        player1.draw_player() # Draw player 1 on screen
        player2.draw_player() # Draw player 2 on screen
        ball.draw_ball() # Draw ball on screen

        player1.move_player() # Move player 1 
        player2.move_player() # Move player 2
        ball.move_ball() # Move the ball in a random direction off the starts

        pygame.display.flip() # Update the display

        clock.tick(60) # Set max screen fps to 60

    pygame.quit() # Quit the game once loop is broken

play() # Call function to start the game