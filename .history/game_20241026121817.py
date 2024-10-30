import pygame
import sys
import time
import displayText
import Paused

# กำหนดขนาดหน้าจอ
display_width = 1200
display_height = 600

# เริ่มต้น pygame และตั้งค่าหน้าจอ
pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Football')
clock = pygame.time.Clock()

# โหลดภาพและเสียง
startImg = pygame.image.load('images/start.jpg').convert()
startImg = pygame.transform.scale(startImg, (display_width, display_height))

backImg = pygame.image.load('images/messi and cr7 wallpaper.jpg').convert()
backImg = pygame.transform.scale(backImg, (display_width, display_height))

ballImg = pygame.image.load('images/football.png')
goalLeftImg = pygame.image.load('images/goalLeft.png')
goalRightImg = pygame.image.load('images/goalRight.png')
ronaldoImg = pygame.image.load('images/ronaldo.png')
messiImg = pygame.image.load('images/messi.png')
sound = pygame.mixer.Sound("sounds/sound.wav")

# สีและฟอนต์
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# ฟังก์ชันแสดงหน้าจอเริ่มต้น
def start_screen():
    screen.blit(startImg, (0, 0))
    font = pygame.font.Font(None, 74)
    title_text = font.render("Football Game", True, white)
    screen.blit(title_text, (display_width // 2 - title_text.get_width() // 2, display_height // 2 - 100))

    # ปุ่ม Start
    start_button = pygame.Rect(display_width // 2 - 100, display_height // 2, 200, 50)
    pygame.draw.rect(screen, green, start_button)
    button_text = font.render("Start", True, black)
    screen.blit(button_text, (display_width // 2 - button_text.get_width() // 2, display_height // 2 + 5))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return  # เริ่มเกมเมื่อกดปุ่ม Start

# ฟังก์ชันแสดงพื้นหลังของเกม
def game_background():
    screen.blit(backImg, (0, 0))

# ฟังก์ชันสำหรับเกม
def main_game():
    # ตำแหน่งผู้เล่นและลูกบอล
    ball_x, ball_y = display_width // 2, display_height // 2
    ronaldo_x, ronaldo_y = display_width // 4, display_height - ronaldoImg.get_height()
    messi_x, messi_y = 3 * display_width // 4, display_height - messiImg.get_height()

    ball_speed_x, ball_speed_y = 0, 0
    gravity = 0.3

    score_left, score_right = 0, 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # อัพเดตตำแหน่งและความเร็วของลูกบอล
        ball_speed_y += gravity
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # การชนขอบของลูกบอล
        if ball_x <= 0 or ball_x >= display_width - ballImg.get_width():
            ball_speed_x = -ball_speed_x * 0.7
        if ball_y >= display_height - ballImg.get_height():
            ball_y = display_height - ballImg.get_height()
            ball_speed_y = -ball_speed_y * 0.7

        # วาดพื้นหลัง เกมผู้เล่น ประตู ลูกบอล
        game_background()
        screen.blit(goalLeftImg, (0, display_height - goalLeftImg.get_height()))
        screen.blit(goalRightImg, (display_width - goalRightImg.get_width(), display_height - goalRightImg.get_height()))
        screen.blit(ballImg, (ball_x, ball_y))
        screen.blit(ronaldoImg, (ronaldo_x, ronaldo_y))
        screen.blit(messiImg, (messi_x, messi_y))

        # อัพเดตหน้าจอ
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# เรียกใช้หน้าจอเริ่มต้น
start_screen()

# เรียกใช้เกมหลัก
main_game()
