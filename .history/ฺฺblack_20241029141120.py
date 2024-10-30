import pygame
import os

# Display settings
display_width = 1200
display_height = 600

def load_background_frames(folder, width, height):
    """Load and scale background frames from a specified folder."""
    frames = []
    for filename in sorted(os.listdir(folder)):
        frame = pygame.image.load(os.path.join(folder, filename))
        frame = pygame.transform.scale(frame, (width, height))
        frames.append(frame)
    return frames

def display_background(screen, frames, frame_index):
    """Display a single frame of the background."""
    screen.blit(frames[frame_index], (0, 0))
    return (frame_index + 1) % len(frames)  # Update the frame index for looping

# Initialize Pygame and set up the display
pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

# Load GIF frames for animated background
frame_folder = 'BG'  # Folder containing separated frames
background_frames = load_background_frames(frame_folder, display_width, display_height)

# Animation settings
frame_index = 0
background_fps = 10  # Animation speed

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display the current frame as background
    frame_index = display_background(screen, background_frames, frame_index)

    # Update the display
    pygame.display.flip()

    # Control the frame rate for background animation
    clock.tick(background_fps)

# Quit Pygame
pygame.quit()

