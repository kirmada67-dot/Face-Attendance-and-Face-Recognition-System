import os.path
import datetime
import pickle

import tkinter as tk
import cv2
from PIL import Image, ImageTk
import face_recognition

import util
from test import test


class App:
    def __init__(self):
        self.main_window = tk.Tk()
        util.setup_window(self.main_window, title="Face Attendance System", size=(1200, 600))

        self.page_bg = "#e8f1fb"
        self.webcam_frame_bg = "#0c1116"
        self.panel_bg = "#0b4da0"
        self.panel_inner = "#ffffff"
        self.btn_primary = "#2f8fe8"
        self.btn_secondary = "#1976d2"
        self.btn_grey = "#6b7280"
        self.main_window.configure(bg=self.page_bg)

        self.left_frame = tk.Frame(self.main_window, bg=self.page_bg)
        self.left_frame.pack(side="left", fill="both", expand=True)

        self.webcam_margin = tk.Frame(self.left_frame, bg="#dff6ff")
        self.webcam_margin.pack(expand=True, fill="both", padx=40, pady=30)

        self.webcam_card = tk.Frame(self.webcam_margin, bg=self.webcam_frame_bg, bd=2, relief="flat")
        self.webcam_card.pack(expand=True, fill="both", padx=10, pady=10)

        self.right_frame = tk.Frame(self.main_window, bg=self.panel_bg, width=320)
        self.right_frame.pack(side="right", fill="y")

        title_strip = tk.Frame(self.right_frame, bg=self.panel_inner, height=80)
        title_strip.pack(fill="x")
        self.title_label = tk.Label(
            title_strip,
            text="Face Attendance",
            font=("Segoe UI", 20, "bold"),
            bg=self.panel_inner,
            fg=self.panel_bg
        )
        self.title_label.pack(pady=18)

        controls_frame = tk.Frame(self.right_frame, bg=self.panel_bg)
        controls_frame.pack(expand=True, fill="both", pady=20)

        self.login_button_main_window = util.get_button(
            controls_frame, 'Login', self.btn_primary, self.login
        )
        self.login_button_main_window.pack(pady=(10, 12), ipadx=10, ipady=6)

        self.logout_button_main_window = util.get_button(
            controls_frame, 'Logout', self.btn_secondary, self.logout
        )
        self.logout_button_main_window.pack(pady=(0, 12), ipadx=10, ipady=6)

        self.register_new_user_button_main_window = util.get_button(
            controls_frame, 'Register New User', self.btn_grey,
            self.register_new_user, fg='white'
        )
        self.register_new_user_button_main_window.pack(pady=(0, 12), ipadx=8, ipady=6)

        footer = tk.Frame(self.right_frame, bg=self.panel_bg, height=40)
        footer.pack(fill="x", side="bottom", pady=10)

        self.webcam_label = tk.Label(self.webcam_card, bg=self.webcam_frame_bg)
        self.webcam_label.pack(expand=True, fill="both", padx=12, pady=12)

        self.add_webcam(self.webcam_label)

        self.db_dir = './db'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

        self.log_path = './log.txt'

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)
            try:
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            except Exception:
                pass

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()

        if ret and frame is not None:
            self.most_recent_capture_arr = frame
            img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
            self.most_recent_capture_pil = Image.fromarray(img_)
            imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
            self._label.imgtk = imgtk
            self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)

    def login(self):

        label = test(
                image=self.most_recent_capture_arr,
                model_dir='/home/prem/PycharmProjects/PythonProject/Silent-Face-Anti-Spoofing/resources/anti_spoof_models',
                device_id=0
                )

        if label == 1:

            name = util.recognize(self.most_recent_capture_arr, self.db_dir)

            if name in ['unknown_person', 'no_persons_found']:
                util.msg_box('Ups...', 'Unknown user. Please register new user or try again.')
            else:
                util.msg_box('Welcome back !', 'Welcome, {}.'.format(name))
                with open(self.log_path, 'a') as f:
                    f.write('{},{},in\n'.format(name, datetime.datetime.now()))

        else:
            util.msg_box('Hey, you are a spoofer!', 'You are fake !')

    def logout(self):

        label = test(
                image=self.most_recent_capture_arr,
                model_dir='//home/prem/PycharmProjects/PythonProject/Silent-Face-Anti-Spoofing/resources/anti_spoof_models',
                device_id=0
                )

        if label == 1:

            name = util.recognize(self.most_recent_capture_arr, self.db_dir)

            if name in ['unknown_person', 'no_persons_found']:
                util.msg_box('Ups...', 'Unknown user. Please register new user or try again.')
            else:
                util.msg_box('Logging out', 'Goodbye, {}.'.format(name))
                with open(self.log_path, 'a') as f:
                    f.write('{},{},out\n'.format(name, datetime.datetime.now()))

        else:
            util.msg_box('Hey, you are a spoofer!', 'You are fake !')

    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        util.setup_window(self.register_new_user_window, title="Register New User", size=(900, 500))

        left = tk.Frame(self.register_new_user_window, bg=self.page_bg)
        left.pack(side="left", fill="both", expand=True)

        webcam_card = tk.Frame(left, bg=self.webcam_frame_bg, bd=2, relief="flat")
        webcam_card.pack(expand=True, fill="both", padx=20, pady=20)

        self.capture_label = tk.Label(webcam_card, bg=self.webcam_frame_bg)
        self.capture_label.pack(expand=True, fill="both", padx=12, pady=12)

        self.add_img_to_label(self.capture_label)

        right = tk.Frame(self.register_new_user_window, bg=self.panel_bg, width=300)
        right.pack(side="right", fill="y")

        tk.Label(right, text="Enter Username", font=("Segoe UI", 14, "bold"),
                 bg=self.panel_bg, fg="white").pack(pady=30)

        self.entry_text_register_new_user = util.get_entry_text(right)
        self.entry_text_register_new_user.pack(pady=10)

        util.get_button(
            right, 'Accept', self.btn_primary, self.accept_register_new_user
        ).pack(pady=15, ipadx=8, ipady=6)

        util.get_button(
            right, 'Cancel', self.btn_secondary, self.try_again_register_new_user
        ).pack(pady=8, ipadx=8, ipady=6)

    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        self.register_new_user_capture = self.most_recent_capture_arr.copy()

    def start(self):
        self.main_window.mainloop()

    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0, "end-1c")

        embeddings = face_recognition.face_encodings(self.register_new_user_capture)[0]

        file = open(os.path.join(self.db_dir, '{}.pickle'.format(name)), 'wb')
        pickle.dump(embeddings, file)

        util.msg_box('Success!', 'User was registered successfully !')

        self.register_new_user_window.destroy()


if __name__ == "__main__":
    app = App()
    app.start()