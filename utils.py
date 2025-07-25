import pygame

def scale_image(img, size):
    """Scale an image to a (width, height) tuple."""
    return pygame.transform.smoothscale(img, size)

def blit_rotate_center(win, image, center, angle):
    """Blit an image rotated around its center."""
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    win.blit(rotated_image, new_rect.topleft)

def blit_text_center(win, font, text, color=(200, 200, 200)):
    """Draw text centered on the window."""
    render = font.render(text, True, color)
    win.blit(
        render,
        (
            win.get_width() // 2 - render.get_width() // 2,
            win.get_height() // 2 - render.get_height() // 2,
        ),
    )