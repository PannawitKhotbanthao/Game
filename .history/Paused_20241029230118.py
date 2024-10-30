def paused(gameDisplay, display_width, display_height, message, pause=False):
    largeText = pygame.font.SysFont("comicsansms", 100)
    TextSurf, TextRect = displayText.display_text(message, largeText, white)
    TextRect.center = ((display_width / 2), (display_height / 5))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        continueAction = None

        continueAction = buttons.button(gameDisplay, "Continue", 350, 250, 100, 50, green, bright_green, 'continue_game')
        buttons.button(gameDisplay, "Quit", 750, 250, 100, 50, red, bright_red)

        if continueAction == 'continueGame':  # เปลี่ยนเป็น ==
            pause = False

        pygame.display.update()
        clock.tick(15)
