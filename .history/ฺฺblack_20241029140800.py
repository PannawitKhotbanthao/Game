import pygame
import os

กำ
display_width = 1200
display_height = 600

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

# Load GIF frames for animated background
backImg_frames = []
frame_folder = 'BG'  # Folder containing separated frames

# Load each frame image into the list and scale to display size
for filename in sorted(os.listdir(frame_folder)):
    frame = pygame.image.load(os.path.join(frame_folder, filename))
    frame = pygame.transform.scale(frame, (display_width, display_height))
    backImg_frames.append(frame)

# Animation settings for background
frame_index = 0
background_fps = 10  # Adjust this to control the animation speed of the background

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display the current frame as background
    screen.blit(backImg_frames[frame_index], (0, 0))

    # Update to the next frame
    frame_index = (frame_index + 1) % len(backImg_frames)  # Loop back to the first frame if it reaches the end

    # (Add game objects or player controls here if needed)

    # Update the display
    pygame.display.flip()

    # Control the frame rate for background animation
    clock.tick(background_fps)

# Quit Pygame
pygame.quit()
