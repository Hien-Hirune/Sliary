import tkinter as tk
from pathlib import Path

window = tk.Tk()
window.geometry('400x600')
window.title('MyDiary')
window.config(bg="#FFFFFF")

font=('Inter', 10, 'bold')

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

menu_frame = tk.Frame(window, pady=5)
menu_frame.pack()
main_frame = tk.Frame(window, pady=5)
main_frame.pack()

canvas_heading = tk.Canvas(menu_frame, height=50, width=400)
heading_board = round_rectangle(canvas_heading, 1, 1, 399, 49, radius=20, fill="#C2E7D6")
canvas_heading.pack()

def back_click():
    window.destroy()
    import hackathon
back_image = tk.PhotoImage(file=relative_to_assets("back.png"))
back_button = tk.Button(canvas_heading, image=back_image, bg='#C2E7D6', activebackground='#C2E7D6',  command=back_click, relief="flat")
back_button.place(x=10, y=10)

canvas_story = tk.Canvas(main_frame, height=550, width=400)
title_image = tk.PhotoImage(file=relative_to_assets("title.png"))
content_image = tk.PhotoImage(file=relative_to_assets("content.png"))
img_image = tk.PhotoImage(file=relative_to_assets("img.png"))
add_image = tk.PhotoImage(file=relative_to_assets("add.png"))
def next_click():
    canvas_mood.pack_forget()
    canvas_act.pack_forget()
    next_button.place_forget()
    date_label = tk.Label(canvas_heading, text='17/07/2022', font=('Inter', 12, 'bold'), bg='#C2E7D6', activebackground='#C2E7D6',
                            relief="flat")
    date_label.place(x=50, y=15)
    del_button = tk.Button(canvas_heading, text='Xoá', font=('Inter', 12), bg='#C2E7D6', activebackground='#C2E7D6',
                            relief="flat")
    del_button.place(x=280, y=10)
    save_button = tk.Button(canvas_heading, text='Lưu', font=('Inter', 12), bg='#C2E7D6', activebackground='#C2E7D6', relief="flat")
    save_button.place(x=340, y=10)
    canvas_story.pack()
    canvas_story.create_image(20, 0, anchor='nw', image=title_image)
    canvas_story.create_image(20, 90, anchor='nw', image=content_image)
    canvas_story.create_image(20, 460, anchor='nw', image=img_image)
    canvas_story.create_image(90, 465, anchor='nw', image=add_image)

next_image = tk.PhotoImage(file=relative_to_assets("next.png"))
next_button = tk.Button(canvas_heading, image=next_image, bg='#C2E7D6', activebackground='#C2E7D6',  command=next_click, relief="flat")
next_button.place(x=350, y=10)

canvas_mood = tk.Canvas(main_frame, height=200, width=400)
mood_board = round_rectangle(canvas_mood, 10, 1, 390, 170, radius=20, fill="white")
canvas_mood.pack()

canvas_act = tk.Canvas(main_frame, height=350, width=400)
act_board = round_rectangle(canvas_act, 10, 1, 390, 300, radius=20, fill="white")
canvas_act.pack()

mood_label = tk.Label(canvas_mood, text='Trạng thái', font=('Inter', 20, 'bold'), bg='white')
mood_label.place(x=130, y=10)

def awful_click():
    bad_button.config(state='disable')
    normal_button.config(state='disable')
    fun_button.config(state='disable')
    happy_button.config(state='disable')
awful_image = tk.PhotoImage(file=relative_to_assets("awful.png"))
awful_button = tk.Button(canvas_mood, image=awful_image, text='\nTệ', bg='white', fg='red', font=font, activebackground='white', activeforeground='red', compound='top',
                       command=awful_click, relief="flat")
awful_button.place(x=10, y=70)

def bad_click():
    awful_button.config(state='disable')
    normal_button.config(state='disable')
    fun_button.config(state='disable')
    happy_button.config(state='disable')
bad_image = tk.PhotoImage(file=relative_to_assets("bad.png"))
bad_button = tk.Button(canvas_mood, image=bad_image, text='\nBuồn', bg='white', fg='#c4ad47', font=font, activebackground='white', activeforeground='#c4ad47', compound='top',
                       command=bad_click, relief="flat")
bad_button.place(x=80, y=70)

def normal_click():
    awful_button.config(state='disable')
    bad_button.config(state='disable')
    fun_button.config(state='disable')
    happy_button.config(state='disable')
normal_image = tk.PhotoImage(file=relative_to_assets("normal.png"))
normal_button = tk.Button(canvas_mood, image=normal_image, text='\nBình thường', bg='white', fg='#99d9ea', font=font, activebackground='white', compound='top',
                       command=normal_click, relief="flat")
normal_button.place(x=150, y=70)

def fun_click():
    awful_button.config(state='disable')
    normal_button.config(state='disable')
    bad_button.config(state='disable')
    happy_button.config(state='disable')
fun_image = tk.PhotoImage(file=relative_to_assets("fun.png"))
fun_button = tk.Button(canvas_mood, image=fun_image, text='\nVui', bg='white', fg='#b5e61d', font=font, activebackground='white', compound='top',
                       command=fun_click, relief="flat")
fun_button.place(x=240, y=70)

def happy_click():
    awful_button.config(state='disable')
    normal_button.config(state='disable')
    fun_button.config(state='disable')
    bad_button.config(state='disable')
happy_image = tk.PhotoImage(file=relative_to_assets("happy.png"))
happy_button = tk.Button(canvas_mood, image=happy_image, text='\nHạnh phúc', bg='white', fg='#1bf5e6', font=font, activebackground='white', compound='top',
                       command=happy_click, relief="flat")
happy_button.place(x=310, y=70)

act_label = tk.Label(canvas_act, text='Hoạt động trong ngày', font=('Inter', 20, 'bold'), bg='white')
act_label.place(x=50, y=10)

def family_click():
    family_button.config(state='disable')
family_image = tk.PhotoImage(file=relative_to_assets("Family_onl.png"))
family_button = tk.Button(canvas_act, image=family_image, bg='white', activebackground='white',
                       command=family_click, relief="flat")
family_button.place(x=25, y=60)

def friend_click():
    friend_button.config(state='disable')
friend_image = tk.PhotoImage(file=relative_to_assets("Friend_onl.png"))
friend_button = tk.Button(canvas_act, image=friend_image, bg='white', activebackground='white',
                       command=friend_click, relief="flat")
friend_button.place(x=100, y=60)

def dating_click():
    dating_button.config(state='disable')
dating_image = tk.PhotoImage(file=relative_to_assets("Date_onl.png"))
dating_button = tk.Button(canvas_act, image=dating_image, bg='white', activebackground='white',
                       command=dating_click, relief="flat")
dating_button.place(x=175, y=60)

def exercise_click():
    exercise_button.config(state='disable')
exercise_image = tk.PhotoImage(file=relative_to_assets("Exercise_onl.png"))
exercise_button = tk.Button(canvas_act, image=exercise_image, bg='white', activebackground='white',
                       command=exercise_click, relief="flat")
exercise_button.place(x=245, y=60)

def sport_click():
    sport_button.config(state='disable')
sport_image = tk.PhotoImage(file=relative_to_assets("Sport_onl.png"))
sport_button = tk.Button(canvas_act, image=sport_image, bg='white', activebackground='white',
                       command=sport_click, relief="flat")
sport_button.place(x=320, y=60)

#row act 2
def sleep_click():
    sleep_button.config(state='disable')
sleep_image = tk.PhotoImage(file=relative_to_assets("Sleep_onl.png"))
sleep_button = tk.Button(canvas_act, image=sleep_image, bg='white', activebackground='white',
                       command=sleep_click, relief="flat")
sleep_button.place(x=22, y=140)

def eat_click():
    eat_button.config(state='disable')
eat_image = tk.PhotoImage(file=relative_to_assets("Eat_onl.png"))
eat_button = tk.Button(canvas_act, image=eat_image, bg='white', activebackground='white',
                       command=eat_click, relief="flat")
eat_button.place(x=89, y=140)

def relax_click():
    relax_button.config(state='disable')
relax_image = tk.PhotoImage(file=relative_to_assets("Relax_onl.png"))
relax_button = tk.Button(canvas_act, image=relax_image, bg='white', activebackground='white',
                       command=relax_click, relief="flat")
relax_button.place(x=168, y=140)

def movie_click():
    movie_button.config(state='disable')
movie_image = tk.PhotoImage(file=relative_to_assets("Movie_onl.png"))
movie_button = tk.Button(canvas_act, image=movie_image, bg='white', activebackground='white',
                       command=movie_click, relief="flat")
movie_button.place(x=240, y=140)

def read_click():
    read_button.config(state='disable')
read_image = tk.PhotoImage(file=relative_to_assets("Read_onl.png"))
read_button = tk.Button(canvas_act, image=read_image, bg='white', activebackground='white',
                       command=read_click, relief="flat")
read_button.place(x=317, y=140)

#row act 3
def game_click():
    game_button.config(state='disable')
game_image = tk.PhotoImage(file=relative_to_assets("Game_onl.png"))
game_button = tk.Button(canvas_act, image=game_image, bg='white', activebackground='white',
                       command=game_click, relief="flat")
game_button.place(x=97, y=230)

def shopping_click():
    shopping_button.config(state='disable')
shopping_image = tk.PhotoImage(file=relative_to_assets("Shopping_onl.png"))
shopping_button = tk.Button(canvas_act, image=shopping_image, bg='white', activebackground='white',
                       command=shopping_click, relief="flat")
shopping_button.place(x=169, y=230)

other_image = tk.PhotoImage(file=relative_to_assets("Other.png"))
other_button = tk.Button(canvas_act, image=other_image, bg='white', activebackground='white',
                       command=lambda: print("other clicked"), relief="flat")
other_button.place(x=249, y=230)

window.resizable(False, False)
window.mainloop()