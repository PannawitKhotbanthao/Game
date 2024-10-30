# video_loader.py

# video_loader.py

import cv2
import pygame

def load_and_resize_video(video_path, display_width, display_height):
    # โหลดวิดีโอด้วย OpenCV
    video_capture = cv2.VideoCapture(video_path)

    def get_next_frame():
        # อ่านเฟรมจากวิดีโอ
        ret, frame = video_capture.read()
        if ret:
            # หมุนเฟรม 90 องศาเป็นแนวตั้ง
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            # ปรับขนาดเฟรมให้ตรงกับขนาดหน้าจอ
            frame = cv2.resize(frame, (display_width, display_height))
            # แปลงสีจาก BGR (OpenCV) เป็น RGB (Pygame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # แปลงเป็น Surface ของ Pygame
            backImg = pygame.surfarray.make_surface(frame)
            return backImg
        else:
            # รีเซ็ตวิดีโอให้เล่นซ้ำเมื่อถึงเฟรมสุดท้าย
            video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
            return None

    return get_next_frame, video_capture

