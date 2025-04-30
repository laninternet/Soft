# © Okmeque1 Software - See https://github.com/GamerSoft24/Software/tree/Main/LICENSE for more information.
import cv2
from ffpyplayer.player import MediaPlayer
from tkinter import messagebox
class VideoPlayer:
    def __init__(self):
        self.pause = False
    def videoplayer(self, file_name):
        player = MediaPlayer(file_name)
        video = cv2.VideoCapture(file_name)
        fps = video.get(cv2.CAP_PROP_FPS)
        end_frame = video.get(cv2.CAP_PROP_FRAME_COUNT)
        while video.isOpened():
            
            if self.pause is False:
                audio_frame, val = player.get_frame()
                ret, frame = video.read()
                if not ret:
                    break
                cv2.imshow(f"{file_name} - Okmeque1 Video Player - © Okmeque1 Software - Press F1 to view controls", frame)
            key = cv2.waitKeyEx(int(1000/fps))
            if key == ord(' '):
                    self.pause = not(self.pause)
                    player.set_pause(self.pause)
            elif key == ord('q'):
                    print("Exiting...")
                    break
            elif key == 7340032:
                    self.pause = not(self.pause)
                    messagebox.showinfo("Okmeque1 Video Player","This program can play any video format supported by the Open Computer Vision Module.\nKey Controls:\nQ = Quit\nSPACEBAR = Pause/Play\nLeft/Right Arrow = Back/Forward 5 seconds\nDown/Up Arrow = Volume Down/Up")
                    self.pause = not(self.pause)
            elif key == 2424832:
                skip_frames = cv2.CAP_PROP_POS_FRAMES - (fps * 5)
                current_frame = video.get(cv2.CAP_PROP_POS_FRAMES)
                video.set(cv2.CAP_PROP_POS_FRAMES,current_frame - (fps*5)) 
                player.seek(-5.0, relative=True)
            elif key == 2555904:
                skip_frames = min(cv2.CAP_PROP_POS_FRAMES + (fps * 5), end_frame)
                current_frame = video.get(cv2.CAP_PROP_POS_FRAMES)
                video.set(cv2.CAP_PROP_POS_FRAMES, current_frame + (fps*5))
                player.seek(5.0, relative=True)
        print(fps)
        player.close_player()
        video.release()
        cv2.destroyAllWindows()
