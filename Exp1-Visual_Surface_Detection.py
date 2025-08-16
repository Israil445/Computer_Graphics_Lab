import pygame
import sys

# -------------------------
# Constants and Configuration
# -------------------------
WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Sequence of shapes to draw
SEQUENCE = "RCT"

# -------------------------
# Shape Drawing Functions
# -------------------------
def draw_triangle(surface):
    points = [(10, 100), (50, 20), (100, 100)]
    pygame.draw.polygon(surface, GREEN, points)

def draw_circle(surface):
    pygame.draw.circle(surface, BLUE, (100, 100), 45)

def draw_rectangle(surface):
    pygame.draw.rect(surface, RED, (100, 100, 80, 80))  # (x, y, width, height)

# -------------------------
# Main Function
# -------------------------
def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Draw Shapes")

    # Fill background
    screen.fill(WHITE)

    # Draw shapes based on the sequence
    for shape in SEQUENCE:
        if shape == 'C':
            draw_circle(screen)
        elif shape == 'T':
            draw_triangle(screen)
        else:
            draw_rectangle(screen)

    # Update display
    pygame.display.flip()

    # Main loop to keep window open until closed
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False

    # Clean up
    pygame.quit()
    sys.exit()

# -------------------------
# Entry Point
# -------------------------
if __name__ == "__main__":
    main()
