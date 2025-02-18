import pygame
import time
import random
import textwrap

# Funktion til at læse citater fra en fil
def load_quotes(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines() if line.strip()]  # Fjerner tomme linjer

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Citater & Klokkeslæt")

pygame.mouse.set_visible(False)  # Skjuler musen
pygame.mouse.set_pos(0, screen.get_height())  # Flytter musen væk

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

font_time = pygame.font.Font(None, 80)  # Større font til klokken
font_quote = pygame.font.Font(None, 50)  # Større font til citater

quotes = load_quotes("citater.txt")  # Indlæs citater fra fil

def get_random_quote():
    return random.choice(quotes)

def draw_text_centered(surface, text, font, color, y, max_width):
    """ Tegner centreret tekst med linjeskift """
    wrapped_text = textwrap.wrap(text, width=max_width)  # Bryder teksten i flere linjer
    total_height = len(wrapped_text) * font.get_height()  # Beregner samlet højde

    y_start = y - total_height // 2  # Start Y-position, så teksten er centreret

    for line in wrapped_text:
        text_surface = font.render(line, True, color)
        text_x = (screen.get_width() - text_surface.get_width()) // 2  # Center X
        surface.blit(text_surface, (text_x, y_start))
        y_start += font.get_height()  # Gå ned til næste linje

current_quote = get_random_quote()
quote_timer = time.time()

running = True
while running:
    screen.fill(BLACK)

    # Tegn klokken, centreret i toppen
    current_time = time.strftime("%H:%M:%S")
    time_surface = font_time.render(current_time, True, WHITE)
    screen.blit(time_surface, ((screen.get_width() - time_surface.get_width()) // 2, 100))

    # Skift citat hvert 10. sekund
    if time.time() - quote_timer > 10:
        current_quote = get_random_quote()
        quote_timer = time.time()

    # Tegn citatet centreret på skærmen
    draw_text_centered(screen, current_quote, font_quote, YELLOW, screen.get_height() // 2, max_width=30)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Luk programmet med ESC
            running = False

    time.sleep(1)

pygame.quit()
