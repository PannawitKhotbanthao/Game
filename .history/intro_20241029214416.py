import pygame
import cv2
import displayText
import buttons

clock = pygame.time.Clock()

def game_intro(gameDisplay, display_width, display_height, sound):
    # โหลดวิดีโอด้วย OpenCV
    video_path = 'images/messi.mp4'  # ใส่ path ของไฟล์วิดีโอที่ต้องการ
    video_capture = cv2.VideoCapture(video_path)

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    bright_red = (255, 128, 0)
    bright_green = (0, 255, 128)

    intro = True

    def play_video_background():
        # อ่านเฟรมจากวิดีโอ
        ret, frame = video_capture.read()
        if ret:
            # แปลงสีจาก BGR (OpenCV) เป็น RGB (Pygame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # หมุนเฟรม 90 องศาและ 180 องศาให้ได้วิดีโอแนวนอนและถูกต้อง
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            frame = cv2.rotate(frame, cv2.ROTATE_180)  # หมุน 180 องศาเพื่อให้ไม่กลับหัว
            # แปลงเป็น Surface ของ Pygame
            frame_surface = pygame.surfarray.make_surface(frame)
            # ปรับขนาด Surface ให้พอดีกับขนาดหน้าจอ
            frame_surface = pygame.transform.scale(frame_surface, (display_width, display_height))
            gameDisplay.blit(frame_surface, (0, 0))
        else:
            # รีเซ็ตวิดีโอให้เล่นซ้ำเมื่อถึงเฟรมสุดท้าย
            video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        introAction = None

        # แสดงวิดีโอเป็นพื้นหลัง
        play_video_background()

        # แสดงชื่อเกม
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = displayText.display_text("Football Game", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        # ปุ่ม Go และ Cancel
        introAction = buttons.button(gameDisplay, "Go", 400, 450, 100, 50, green, bright_green, 'close_intro')
        buttons.button(gameDisplay, "Cancel", 800, 450, 100, 50, red, bright_red, 'close_game')

        # ตรวจสอบการกดปุ่ม
        if introAction == 'close_intro':
            intro = False

        pygame.display.update()
        clock.tick(30)  # ตั้งอัตราเฟรมสำหรับการแสดงวิดีโอ

    # ปิดการจับภาพเมื่อสิ้นสุดการใช้งาน
    video_capture.release()
