import pygame
import sys
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
sound = pygame.mixer.Sound("sounds/sound.wav")

# กำหนดสี
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# ฟังก์ชันแสดงหน้าจอเริ่มต้น
def start_screen():
    while True:
        screen.blit(startImg, (0, 0))  # แสดงภาพพื้นหลัง

        # สร้างฟอนต์และแสดงข้อความ
        font = pygame.font.Font(None, 74)
        title_text = font.render("Football Game", True, white)
        screen.blit(title_text, (display_width // 2 - title_text.get_width() // 2, display_height // 2 - 100))

        # ปุ่ม Start
        start_button = pygame.Rect(display_width // 2 - 100, display_height // 2, 200, 50)
        pygame.draw.rect(screen, green, start_button)
        start_text = font.render("Start", True, black)
        screen.blit(start_text, (display_width // 2 - start_text.get_width() // 2, display_height // 2 + 5))

        # ปุ่ม Exit
        exit_button = pygame.Rect(display_width // 2 - 100, display_height // 2 + 100, 200, 50)
        pygame.draw.rect(screen, red, exit_button)
        exit_text = font.render("Exit", True, black)
        screen.blit(exit_text, (display_width // 2 - exit_text.get_width() // 2, display_height // 2 + 105))

        pygame.display.update()

        # ตรวจจับเหตุการณ์การคลิกปุ่ม
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return  # เริ่มเกมเมื่อกดปุ่ม Start
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

# ฟังก์ชันแสดงพื้นหลังของเกม
def game_background():
    screen.blit(backImg, (0, 0))

# ฟังก์ชันสำหรับเกม
def main_game():
    # ตำแหน่งลูกบอลและผู้เล่น
    ball_x, ball_y = display_width // 2, display_height // 2
    ball_speed_x, ball_speed_y = 0, 0
    gravity = 0.3

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

        # อัปเดตหน้าจอ
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# เรียกใช้หน้าจอเริ่มต้น
start_screen()

# เรียกใช้เกมหลัก
main_game()
