import random
from itertools import combinations
import customtkinter as ctk
from PIL import Image
import pygame

# COLOR
BG_MAIN_COLOR = "#0D0D11"
BG_COLOR = "#1D2D50"
LINE_COLOR = "#A3B2CC"
BORDER_COLOR = "#9BA4B5"
BTN_COLOR = "#394867"
BTN_HOVER_COLOR = "#0C1E3F"
COMPUTER_WIN_COLOR = "#AD0707"
USER_WIN_COLOR = "#098BD3"
DRAW_COLOR = "#9BA4B5"
TEXT_COLOR = "#A3B2CC"

# FONT
SCORE_FONT = ("Roboto Slab", 17, "bold")
RESTART_FONT = ("Roboto Slab", 22, "normal")
FEEDBACK_FONT = SCORE_FONT
BOTTOM_TEXT = ("Roboto Slab", 12, "normal")


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=BG_MAIN_COLOR)
        self.title(" Amos' Tic Tac Toe")
        self.iconbitmap("files/images/logo.ico")
        self.resizable(False, False)
        app_width = 550
        app_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cor = int((screen_width / 2) - (app_width / 2))
        y_cor = int((screen_height / 2) - (app_height / 2))
        self.geometry("{}x{}+{}+{}".format(app_width, app_height, x_cor, y_cor))

        # MUSIC
        pygame.init()
        self.bg_music = pygame.mixer.Sound("files/sound/bg_music.mp3")
        self.bg_music.set_volume(0.5)
        self.bg_music.play(loops=-1)

        # VARIABLES
        self.win_boxes_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        self.all_boxes_list = [n for n in range(9)]

        self.computer_played_list = []
        self.user_played_list = []
        self.computer_score = 0
        self.user_score = 0
        self.play_switcher = 1

        self.turn_var = ctk.StringVar(value="Computer")
        self.win_var = ctk.BooleanVar(value=False)

        # LAYOUT DESIGN
        self.board_frame = ctk.CTkFrame(self)
        self.board_frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.85)
        for n in range(3):
            self.board_frame.columnconfigure(n, weight=1, uniform="a")
            self.board_frame.rowconfigure(n, weight=1, uniform="a")

        # RESTART BUTTON
        self.restart_btn = ctk.CTkButton(self, text="Restart", font=RESTART_FONT, fg_color=BG_COLOR,
                                         text_color=TEXT_COLOR, hover_color=BTN_HOVER_COLOR, command=self.restart_game)
        self.restart_btn.place(relx=0.695, rely=0.03)

        # SCORE LABELS
        self.user_score_label = ctk.CTkLabel(self, text=f"Your Score: {self.user_score}", text_color=TEXT_COLOR,
                                             font=SCORE_FONT)
        self.user_score_label.place(relx=0.05, rely=0.005)

        self.computer_score_label = ctk.CTkLabel(self, text=f"Computer's Score: {self.computer_score}",
                                                 text_color=TEXT_COLOR, font=SCORE_FONT)
        self.computer_score_label.place(relx=0.05, rely=0.045)

        # FEEDBACK LABEL
        self.feedback_label = ctk.CTkLabel(self, text="", font=FEEDBACK_FONT, anchor="center",
                                           text_color=BG_MAIN_COLOR)
        self.feedback_label.pack(side="top", pady=22)

        # BOTTOM LABEL
        # SCORE LABELS
        self.bottom_label = ctk.CTkLabel(self, text="Designed by Amos @PythonDecorator", fg_color=BG_MAIN_COLOR,
                                         font=BOTTOM_TEXT, text_color=BTN_COLOR)
        self.bottom_label.pack(side="bottom")

        # LINES
        Lines(self)

        # IMAGE
        image_o = Image.open("files/images/o.png")
        image_x = Image.open("files/images/x.png")
        self.ctk_img_o = ctk.CTkImage(dark_image=image_o, light_image=image_o, size=(80, 84))
        self.ctk_img_x = ctk.CTkImage(dark_image=image_x, light_image=image_x, size=(89, 87))

        # BUTTONS
        self.button_list = []
        for box_number in range(1, 10):
            self.create_button(box_number, command=self.play_game)

        self.play_game(user_choice=11)

    def restart_game(self):
        """To restart, the play switcher is responsible for switching play from computer to user"""
        self.play_switcher += 1
        for button in self.button_list:
            button.configure(text=" ", image=None, state="normal")

        self.all_boxes_list = [n for n in range(9)]
        self.computer_played_list = []
        self.user_played_list = []

        if self.play_switcher % 2:
            self.turn_var.set(value="Computer")
            self.feedback_label.configure(text="", fg_color=BG_MAIN_COLOR)
        else:
            self.turn_var.set(value="User")
            self.feedback_label.configure(text=" Your Turn ", fg_color=LINE_COLOR)

        self.win_var.set(value=False)
        self.play_game(user_choice=11)

    def play_game(self, user_choice):
        """All the game logic happens here, computer first tries to play to win while also blocking the user from
        winning when the user have played two or more moves"""
        # USER'S TURN
        user_choice = user_choice - 1
        if not self.win_var.get() and self.turn_var.get() == "User" and user_choice != 10:
            self.button_list[user_choice].configure(text="", image=self.ctk_img_o, fg_color=BTN_COLOR, state="disabled")
            self.all_boxes_list.remove(user_choice)
            self.user_played_list.append(user_choice + 1)

            # DETECTS USER WIN
            if len(self.user_played_list) >= 3:
                all_possible_combinations = list(combinations(self.user_played_list, 3))
                all_possible_list = [[x[0], x[1], x[2]] for x in all_possible_combinations]

                for win_boxes in self.win_boxes_list:
                    for i in range(len(all_possible_list)):
                        if sorted(all_possible_list[i]) == win_boxes:
                            self.user_score += 1
                            self.user_score_label.configure(text=f"Your Score: {self.user_score}")
                            self.feedback_label.configure(text=" You Win! ", fg_color=USER_WIN_COLOR)
                            self.win_var.set(value=True)

            # SETS TURN TO  COMPUTER
            if not self.win_var.get():
                self.turn_var.set(value="Computer")

        # COMPUTER'S TURN
        if self.turn_var.get() == "Computer" and self.all_boxes_list:
            computer_choice = random.choice(self.all_boxes_list)

            # ARTIFICIAL INTELLIGENCE: PLAYS FOR COMPUTER TO WIN AND TRIES TO BLOCK USER FROM WINNING
            # TRIES TO WIN ON THE FORTH MOVE
            if len(self.computer_played_list) == 3:
                computer_played_list = self.computer_played_list[:2], self.computer_played_list[1:3], \
                    self.computer_played_list[:: 2]
                available_boxes_list = [x + 1 for x in self.all_boxes_list]
                for win_boxes_ in self.win_boxes_list:
                    for n in available_boxes_list:
                        for k in range(3):
                            if sorted(computer_played_list[k] + [n]) == win_boxes_:
                                computer_choice = n - 1
                                self.computer_score += 1
                                self.computer_score_label.configure(text=f"Computer's Score: {self.computer_score}")
                                self.feedback_label.configure(text=" Computer Wins! ", fg_color=COMPUTER_WIN_COLOR)
                                self.win_var.set(value=True)
                                break

            # TRIES TO WIN ON THE THIRD MOVE
            if len(self.computer_played_list) == 2:
                available_boxes_list = [x + 1 for x in self.all_boxes_list]
                for win_boxes in self.win_boxes_list:
                    for n in available_boxes_list:
                        if sorted(self.computer_played_list + [n]) == win_boxes:
                            computer_choice = n - 1
                            self.computer_score += 1
                            self.computer_score_label.configure(text=f"Computer's Score: {self.computer_score}")
                            self.feedback_label.configure(text=" Computer Wins! ", fg_color=COMPUTER_WIN_COLOR)
                            self.win_var.set(value=True)
                            break

            # BLOCKS USER THIRD MOVE FROM WINNING
            if not self.win_var.get() and len(self.user_played_list) == 2:
                for win_boxes in self.win_boxes_list:
                    if self.user_played_list[0] in win_boxes and self.user_played_list[1] in win_boxes:
                        win_boxes.remove(self.user_played_list[0])
                        win_boxes.remove(self.user_played_list[1])
                        if win_boxes[0] - 1 in self.all_boxes_list:
                            computer_choice = win_boxes[0] - 1

            # BLOCKS USER FORTH MOVE FROM WINNING
            # if not self.win_var.get() and len(self.user_played_list) == 3:
            #     user_played_list = self.user_played_list[:2], self.user_played_list[1:3], \
            #         self.computer_played_list[:: 2]
            #     available_boxes_list = [x + 1 for x in self.all_boxes_list]
            #     for win_boxes_ in self.win_boxes_list:
            #         for n in available_boxes_list:
            #             for k in range(3):
            #                 if sorted(user_played_list[k] + [n]) == win_boxes_:
            #                     computer_choice = n - 1

            self.button_list[computer_choice].configure(text="", image=self.ctk_img_x, fg_color=BTN_COLOR,
                                                        state="disabled")
            self.all_boxes_list.remove(computer_choice)
            self.computer_played_list.append(computer_choice + 1)

            # SETS TURN TO USER
            self.turn_var.set(value="User")

            # CHECKS FOR COMPUTER WIN AFTER ALL MOVES
            if len(self.computer_played_list) == 5:
                all_possible_combinations_ = list(combinations(self.computer_played_list, 3))
                all_possible_list_ = [[x[0], x[1], x[2]] for x in all_possible_combinations_]
                for win_boxes in self.win_boxes_list:
                    for i in range(len(all_possible_list_)):
                        if sorted(all_possible_list_[i]) == win_boxes:
                            self.computer_score += 1
                            self.computer_score_label.configure(text=f"Computer's Score: {self.computer_score}")
                            self.feedback_label.configure(text=" Computer Wins! ", fg_color=COMPUTER_WIN_COLOR)
                            self.win_var.set(value=True)

        # CHECKS FOR A DRAW
        if not self.win_var.get() and not self.all_boxes_list:
            self.feedback_label.configure(text=" Draw! ", fg_color=DRAW_COLOR)
            self.win_var.set(value=True)

    def create_button(self, box_number, image=None, command=None):
        button = ctk.CTkButton(self.board_frame, text=" ", image=image, border_width=5, fg_color=BTN_COLOR,
                               compound="left", hover_color=BTN_HOVER_COLOR, border_color=BORDER_COLOR)
        if command is not None:
            button.configure(command=lambda: command(box_number))
        if box_number < 4:
            button.grid(column=box_number - 1, row=0, sticky="news", padx=20, pady=30)
        elif box_number < 7:
            button.grid(column=box_number - 4, row=1, sticky="news", padx=20, pady=30)
        else:
            button.grid(column=box_number - 7, row=2, sticky="news", padx=20, pady=30)
        self.button_list.append(button)


class Lines(ctk.CTkCanvas):
    def __init__(self, parent: App):
        super().__init__(parent.board_frame, background=BG_COLOR, highlightthickness=0)
        self.parent = parent
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        # HORIZONTAL LINES
        self.create_line((50, 50, 1200, 50), fill=LINE_COLOR, width=13, capstyle="round")
        self.create_line((50, 425, 1200, 425), fill=LINE_COLOR, width=13, capstyle="round")
        self.create_line((50, 850, 1200, 850), fill=LINE_COLOR, width=13, capstyle="round")
        self.create_line((50, 1220, 1200, 1220), fill=LINE_COLOR, width=13, capstyle="round")

        # VERTICAL LINES
        self.create_line((415, 20, 415, 1250), fill=LINE_COLOR, width=13, capstyle="round")
        self.create_line((830, 20, 830, 1250), fill=LINE_COLOR, width=13, capstyle="round")


if __name__ == "__main__":
    app = App()
    app.mainloop()
