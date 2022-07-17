import tkinter as tk
from tkinter import ttk
from pathlib import Path
import os
import subprocess

window = tk.Tk()
window.geometry('400x600')
window.title('MyDiary')
window.config(bg= "#FFFFFF")

font = ("Times bold", 14)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

add_image_menu = tk.PhotoImage(file=relative_to_assets("new.png"))
stat_image_menu = tk.PhotoImage(file=relative_to_assets("stat.png"))
game_image_menu = tk.PhotoImage(file=relative_to_assets("game.png"))
bin_image_menu = tk.PhotoImage(file=relative_to_assets("bin.png"))
setting_image_menu = tk.PhotoImage(file=relative_to_assets("setting.png"))
help_image_menu = tk.PhotoImage(file=relative_to_assets("help.png"))

def add_click():
    window.destroy()
    import hackathon_2

def game_click():
    subprocess.call(["C:/Users/HOME/PycharmProjects/pythonProject/build/CuteSimpleGame/CuteSimpleGame.exe"])

def show_menu_board():
    global show_menu, canvas_menu
    if show_menu:
        canvas_menu.place(x=0, y=0)#pack(side='left')
        canvas_menu.create_rectangle(0, 0, 200, 600, fill='#5d8c74')

        add_button_menu = tk.Button(canvas_menu, text='  Tạo mới', image = add_image_menu, font=('Inter', 10), bg='#5d8c74', fg='white', activebackground='#B4D6C5', compound="left", command=add_click, relief="flat")
        add_button_menu.place(x=10, y=10)

        stat_button = tk.Button(canvas_menu, text='   Thống kê', image = stat_image_menu, font=('Inter', 10), bg='#5d8c74', fg='white', activebackground='#B4D6C5', compound="left", command=lambda: print("stat clicked"), relief="flat")
        stat_button.place(x=10, y=60)

        game_button = tk.Button(canvas_menu, text='   Giải trí', image = game_image_menu, font=('Inter', 10), bg='#5d8c74', fg='white', activebackground='#B4D6C5', compound="left", command=game_click, relief="flat")
        game_button.place(x=10, y=110)

        bin_button = tk.Button(canvas_menu, text='   Thùng rác', image = bin_image_menu, font=('Inter', 10), bg='#5d8c74', fg='white', activebackground='#B4D6C5', compound="left", command=lambda: print("bin clicked"), relief="flat")
        bin_button.place(x=10, y=160)

        setting_button = tk.Button(canvas_menu, text='   Cài đặt', image = setting_image_menu, font=('Inter', 10), bg='#5d8c74', fg='white', activebackground='#B4D6C5', compound="left", command=lambda: print("setting clicked"), relief="flat")
        setting_button.place(x=10, y=210)

        help_button = tk.Button(canvas_menu, text='   Trợ giúp & Phản hồi', image = help_image_menu, font=('Inter', 10), bg='#5d8c74', fg='white', activebackground='#B4D6C5', compound="left", command=lambda: print("help clicked"), relief="flat")
        help_button.place(x=10, y=260)

        show_menu = False
    else:
        canvas_menu.place_forget()
        show_menu = True

menu_frame = tk.Frame(window, pady=5)
menu_frame.pack()
main_frame = tk.Frame(window, pady=5)
main_frame.pack()

canvas_heading = tk.Canvas(menu_frame, height=50, width=400)#, bd= 0, highlightthickness= 0, relief = "ridge")
heading_board = round_rectangle(canvas_heading, 1, 1, 399, 49, radius=20, fill="#C2E7D6")
canvas_heading.pack()

story_width = 150
canvas_story = tk.Canvas(main_frame, height=550, width=400)#, bd= 0, highlightthickness= 0, relief = "ridge")

story_canvas = []
story_title_canvas = []
story_title = ['Đăng kí thi Hackathon', 'Chờ đợi...', "Let's go", 'Mệt quá']
story_day = ['14/07/2022', '15/07/2022', '16/07/2022', '17/07/2022']
story_content = ['Được bạn bè mời vào nên tham gia thử cho biết.', 'Chờ đề thi lâu quá à...', 'Sẵn sàng xuất phát thôi nào!', 'Không ngờ thi hackathon lại mệt như vậy, nhưng mà vui lắm.']

for i in range(4):
    story_canvas.append(round_rectangle(canvas_story, 10, 10 + story_width*i, 380, 150 + story_width*i, radius=20, fill="#C2E7D6"))
    story_title_canvas.append(round_rectangle(canvas_story, 10, 10 + story_width*i, 380, 60 + story_width*i, radius=20, fill="#6C9581"))
    canvas_story.create_text(20, 25 + story_width * i, text=story_day[i], font=('Inter', 10), fill='white', anchor='w')
    canvas_story.create_text(20, 45 + story_width*i, text=story_title[i], font=('Inter', 11, 'bold italic'), fill='white', anchor='w')
    canvas_story.create_text(20, 75 + story_width * i, text=story_content[i], font=('Inter', 10), fill='black', anchor='w')

menu_image = tk.PhotoImage(file=relative_to_assets("menu.png"), width=40, height=40)
show_menu = True
canvas_menu = tk.Canvas(main_frame, height=600, width=180, bg='black')
menu_button = tk.Button(canvas_heading, image=menu_image, bg='#C2E7D6', activebackground='#C2E7D6',  command=show_menu_board, relief="flat")
menu_button.place(x=2, y=2)

acc_image = tk.PhotoImage(file=relative_to_assets("account.png"), width=42, height=41)
acc_button = tk.Button(canvas_heading, image=acc_image, bg='#C2E7D6', activebackground='#C2E7D6',  command=lambda: print("acc clicked"), relief="flat")
acc_button.place(x=345, y=2)

add_image = tk.PhotoImage(file=relative_to_assets("add.png"))
add_button = tk.Button(canvas_story, image=add_image, bg='white', activebackground='white',  command=add_click, relief="flat")
add_button.place(x=320, y=450)

# add a scrollbar
scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas_story.yview)
scrollbar.pack(side='right', fill='y')
canvas_story.config(scrollregion=canvas_story.bbox("all"), yscrollcommand=scrollbar.set)
canvas_story.pack()

window.mainloop()