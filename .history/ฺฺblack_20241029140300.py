import pygame
import random
import time
import Things
import intro
import buttons
import displayText
import Paused
import sys
import os

# Display settings
display_width = 1200
display_height = 600

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
sound = pygame.mixer.Sound("sounds/sound.wav")   
pygame.mixer.music.load('sounds/music.mp3')
#pygame.mixer.music.play(-1)

# Load GIF frames for animated background
backImg_frames = []
frame_folder = 'images/campnu_frames/'  # Folder containing separated frames

# Load each frame image into the list and scale to display size
for filename in sorted(os.listdir(frame_folder)):
    frame = pygame.image.load(os.path.join(frame_folder, filename))
    frame = pygame.transform.scale(frame, (display_width, display_height))
    backImg_frames.append(frame)

# Animation settings for background
frame_index = 0
background_fps = 10  # Adjust this to control the animation speed of the background

# Load images for players and goals
ballImg = pygame.image.load('images/football.png')
goalLeftImg = pygame.image.load('images/goalLeft.png')
goalRightImg = pygame.image.load('images/goalRight.png')
boyFirstLeftNormalImg = pygame.image.load('images/ronaldo.png')
boyFirstRightNormalImg = pygame.image.load('images/ronaldo.png')
boyFirstLeftKickImg = pygame.image.load('images/ronaldo_kick.png')
boyFirstRightKickImg = pygame.image.load('images/ronaldo_kick.png')
boySecondLeftNormalImg = pygame.image.load('images/messi.png')
boySecondRightNormalImg = pygame.image.load('images/messi.png')
boySecondLeftKickImg = pygame.image.load('images/messi_kick.png')
boySecondRightKickImg = pygame.image.load('images/messi_kick.png')
boyFirstLeftVictoryImg = pygame.image.load('images/ronaldo_action.png')
boySecondRightVictoryImg = pygame.image.load('images/messi_action.png')

pygame.display.set_caption('Football')
pygame.display.set_icon(ballImg)

# Define colors and other settings
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
goal_width = goalLeftImg.get_rect().size[0]
goal_height = goalLeftImg.get_rect().size[1]

# Initialize positions and other variables
gravityAcceleration = 0.3
horizontalAcceleration = 0
verticalSpeed = [0, 0]
horizontalSpeed = [0, 0]
ball_x, ball_y = 600, 300

boyGravityAcceleration = 0.3
boy_x, boy_y = display_width / 2, display_height - boyFirstRightNormalImg.get_rect().size[1]
boySecond_x, boySecond_y = display_width / 4, display_height - boySecondRightNormalImg.get_rect().size[1]

score_left = 0
score_right = 0

def goal(x1, y1, x2, y2):
    screen.blit(goalLeftImg, (x1, y1))
    screen.blit(goalRightImg, (x2, y2))

def ball(x, y):
    screen.blit(ballImg, (x, y))

def firstBoy(type, x, y):
    if type == 'normal left':
        screen.blit(boyFirstLeftNormalImg, (x, y))
    elif type == 'normal right':
        screen.blit(boyFirstRightNormalImg, (x, y))
    elif type == 'kick left':
        screen.blit(boyFirstLeftKickImg, (x, y))
    elif type == 'kick right':
        screen.blit(boyFirstRightKickImg, (x, y))

def secondBoy(type, x, y):
    if type == 'normal left':
        screen.blit(boySecondLeftNormalImg, (x, y))
    elif type == 'normal right':
        screen.blit(boySecondRightNormalImg, (x, y))
    elif type == 'kick left':
        screen.blit(boySecondLeftKickImg, (x, y))
    elif type == 'kick right':
        screen.blit(boySecondRightKickImg, (x, y))

intro.game_intro(screen, display_width, display_height, sound)

crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            # Add movement controls for players as in original code
            pass

    # Display the current frame as background
    screen.blit(backImg_frames[frame_index], (0, 0))
    frame_index = (frame_index + 1) % len(backImg_frames)

    # Draw goals and ball
    goal(0, display_height - goal_height, display_width - goal_width, display_height - goal_height)
    ball(ball_x, ball_y)

    # Display score
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = displayText.display_text(f"{score_left} | {score_right}", largeText)
    TextRect.center = (display_width / 2, 20)
    screen.blit(TextSurf, TextRect)

    pygame.display.flip()
    clock.tick(background_fps)

pygame.quit()
sys.exit()
