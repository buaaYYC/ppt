import tkinter as tk
import tkinter.messagebox
import TextRank_generate_ppt
def G_interface():
    # 1.
    window = tk.Tk()
    # 2
    window.title("生成ppt")
    # 3、
    window.geometry('800x700')
    # 4 加载 wellcome image
    canvas = tk.Canvas(window, width=400, height=135, bg='gray')
    from PIL import  Image,ImageTk
    image = Image.open("span.jpg")
    image_file = ImageTk.PhotoImage(image)
    image = canvas.create_image(200, 0, image=image_file)
    canvas.pack()
    Label1 = tk.Label(window, text='Wellcome generate ppt ',font=('Arial', 16))
    Label1.pack()
    tk.Label(window, text='在类似于头条和知乎这样网页文章生成ppt效果好些', font=('Arial', 14)).place(x=120, y=600)
    # 第5步，信息
    tk.Label(window, text='网址:', font=('Arial', 14)).place(x=120, y=200)
    tk.Label(window, text='ppt 页数:', font=('Arial', 14)).place(x=120, y=300)
    # 第6步，输入框entry
    entry_usr_name = tk.Entry(window)
    entry_usr_name.place(x=240,y=200,width=400,height=40)
    entry__name = tk.Entry(window)
    entry__name.place(x=240,y=300,width=400,height=40)
    # 第8步，定义用户登录功能

    def hit_me():
        if "http" in entry_usr_name.get():
            TextRank_generate_ppt.textRank_ppt(entry_usr_name.get(),int(entry__name.get()))
            tkinter.messagebox.showinfo(title='Hi', message="ppt已经生成")
        else:
            tkinter.messagebox.showinfo(title='Hi', message="非法输入，请重新输入")
    # 第7步，添加按钮
    btn_login = tk.Button(window, text='start genrate ppt', command=hit_me)
    btn_login.place(x=120, y=400,height=40)
    btn_1 = tk.Button(window, text='退出', command=window.quit)
    btn_1.place(x=400, y=400,width=80,height=40)
    # 第10步，主窗口循环显示
    window.mainloop()
if __name__=="__main__":
    G_interface()