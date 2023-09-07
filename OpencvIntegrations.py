# Import
import pygame
import cv2
import numpy as np
from PIL import Image
from pathlib import Path

# Initialize
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")

# Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)  # height

# Main loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
#     window.fill((0,0,0))

    # OpenCV
    success, img = cap.read()
    imgRGB = None  # Initialize imgRGB with a default value
    if img is not None:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
    if imgRGB is not None:
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        frame = pygame.transform.flip(frame, True, False)
        window.blit(frame, (0, 0))

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)
    exit()
