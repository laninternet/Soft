# © Okmeque1 Software - See https://github.com/GamerSoft24/Software/tree/Main/LICENSE for more information.
from ffpyplayer.player import MediaPlayer
from tkinter import messagebox
import cv2
import numpy as np #vyyyyyy
class VideoPlayer:
    def __init__(self):
        self.pause = False
    def format_converter(self,frame_tuple):# © fmascarich from matham/ffpyplayer github issues
                (ff_frame, frame_pts) = frame_tuple
                frame_size = ff_frame.get_size()
                mem_view = ff_frame.to_memoryview()
                if mem_view is None:
                    exit()
                frame = np.asarray(mem_view)
                img_frame = np.asarray(frame[0]).copy()
                img_frame = img_frame.reshape((frame_size[1], frame_size[0], 3), order='C')
                fixed_frame = img_frame.copy()
                # convert BGR to RGB
                fixed_frame[:,:,2] = img_frame[:,:,0]
                fixed_frame[:,:,0] = img_frame[:,:,2]
                return fixed_frame
    def videoplayer(self, file_name):
        player = MediaPlayer(file_name)
        video = cv2.VideoCapture(file_name)
        fps = video.get(cv2.CAP_PROP_FPS)
        end_frame = video.get(cv2.CAP_PROP_FRAME_COUNT)
        while True:
            
            if self.pause is False:
                frame, val = player.get_frame()
                if val == "eof" or frame is None:
                     print("Frame is empty or at end of video. Exiting...")
                else:
                     print("Frame contains data.")
                     img, t = frame
                     w = img.get_size()[0] 
                     h = img.get_size()[1]
                     arr = np.uint8(np.asarray(list(img.to_bytearray()[0])).reshape(h,w,3)) # h - height of frame, w - width of frame, 3 - number of channels in frame
                     if img is not None:
                        #img = self.format_converter(frame)
                        cv2.imshow("Okmeque1 Video Player - Press F1 for controls - © Okmeque1 Software",arr)
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
