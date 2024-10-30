# background.py

import pygame
import os

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
