import pygame

def draw_start_button(screen, ):
    pygame.draw.rect(screen, (0, 255, 0), start_button_rect)
    pygame.draw.rect(screen, (255, 255, 255), start_button_rect, 2)
    font = pygame.font.Font(None, 36)
    text = font.render("Start", True, (255, 255, 255))
    text_rect = text.get_rect(center=start_button_rect.center)
    screen.blit(text, text_rect)
