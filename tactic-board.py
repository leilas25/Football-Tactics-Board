import pygame
import os
from utils import scale_image, blit_rotate_center, blit_text_center

pygame.init()

# Constants
BOARD_IMAGE = "images/tactic-board.jpg"
TEAM1_IMAGE = "images/passing(1).png"
TEAM2_IMAGE = "images/passing.png"
PLAYER_SIZE = 40
TEAM_SIZE = 11
WIDTH, HEIGHT = 900, 600  # Adjust as needed

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Football Tactics Board")

# Helper to load and scale images
def load_image(path, size):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.smoothscale(img, (size, size))

# Classes
class PlayerIcon:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.dragging = False

    def draw(self, win):
        win.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
                mouse_x, mouse_y = event.pos
                self.offset_x = self.rect.x - mouse_x
                self.offset_y = self.rect.y - mouse_y
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y

class TacticsBoard:
    def __init__(self):
        self.board_img = pygame.transform.smoothscale(
            pygame.image.load(BOARD_IMAGE), (WIDTH, HEIGHT)
        )
        self.team1_img = load_image(TEAM1_IMAGE, PLAYER_SIZE)
        self.team2_img = load_image(TEAM2_IMAGE, PLAYER_SIZE)
        self.players = []
        self.init_players()

    def init_players(self):
        # Team 1 (left side)
        for i in range(TEAM_SIZE):
            x = WIDTH // 4
            y = int(HEIGHT * (i + 1) / (TEAM_SIZE + 1))
            self.players.append(PlayerIcon(self.team1_img, x, y))
        # Team 2 (right side)
        for i in range(TEAM_SIZE):
            x = 3 * WIDTH // 4
            y = int(HEIGHT * (i + 1) / (TEAM_SIZE + 1))
            self.players.append(PlayerIcon(self.team2_img, x, y))

    def draw(self, win):
        win.blit(self.board_img, (0, 0))
        for player in self.players:
            player.draw(win)

    def handle_event(self, event):
        for player in self.players:
            player.handle_event(event)

def main():
    clock = pygame.time.Clock()
    board = TacticsBoard()
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            board.handle_event(event)

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()