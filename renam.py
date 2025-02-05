import os
import tkinter as tk

list_path = []
list_names = []
n_to_p = {}
start_num=-1
end_num=-1
goto=-1

ch = ''
def output(a):
    global ch
    ch = ch + a + "|"
    tx1.configure(text=ch)

def clear():
    global ch
    en1.delete(0, tk.END)
    en2.delete(0, tk.END)
    en3.delete(0, tk.END)
    ch = ''
    tx1.configure(text=ch)

def read():
    global filename, list_path, list_names, n_to_p

    filename = en0.get()
    try:
        list_path = os.listdir(filename)
    except FileNotFoundError:
        output("!FileNotFound")
    except OSError:
        output("!SyntaxError")
    else:
        output("ReadSuccess")
    filename += '\\'
    list_names = []
    n_to_p = {}
    
    for i in list_path:
        cnt_init = len(i)-1
        while i[cnt_init] != '.': cnt_init -= 1
        try: list_names.append(int(i[:cnt_init]))
        except ValueError:
            output("!FilenameNotAccepted"+"-"+i)
        n_to_p[list_names[len(list_names)-1]] = i
    list_names.sort()

def check():
    read()
    
    global filename, list_path, list_names, n_to_p
    try:
        the_previous_check = list_names[0]
    except IndexError:pass
    else:
        print(filename)
        for i in list_names[1:]:
            if i != the_previous_check + 1:
                path = filename + n_to_p[i]
                new_path = filename + str(the_previous_check + 1) + n_to_p[i][len(str(i)):]
                output(n_to_p[i] + "->" + str(the_previous_check + 1) + n_to_p[i][len(str(i)):])
                os.rename(path, new_path)
            the_previous_check += 1
        output("CheckFinish")

def move():
    read()

    global filename, list_path, list_names, n_to_p, start_num, end_num, goto
    def M2(i, cnt_move):
        path = filename + n_to_p[i]
        new_path = filename + "i" + str(cnt_move) + n_to_p[i][len(str(i)):]
        output(n_to_p[i] + "->" + str(cnt_move) + n_to_p[i][len(str(i)):])
        os.rename(path, new_path)
    
    try:
        start_num = int(en1.get())
        end_num = int(en2.get())
        goto = int(en3.get())
    except ValueError:output("!WrongNumber")
    else:
        start_num -= 1
        end_num -= 1
        goto -= 1
        clear()
        
        if start_num > end_num or end_num > int(list_names[-1]) or start_num <= 0 or end_num <= 0:
            output("!OutOfRange")
        else:
            if start_num <= goto and goto <= end_num:
                pass
            elif start_num > goto and end_num > goto:
                cnt_move = goto+1
                for i in list_names[start_num:(end_num+1)]:
                    M2(i, cnt_move)
                    cnt_move += 1
                for i in list_names[goto:(start_num-1+1)]:
                    M2(i, cnt_move)
                    cnt_move += 1
                for i in list_names[end_num+1:]:
                    M2(i, cnt_move)
                    cnt_move += 1
            else:
                goto += 1
                
                cnt_move = start_num+1
                for i in list_names[(end_num+1):(goto-1+1)]:
                    M2(i, cnt_move)
                    cnt_move += 1
                for i in list_names[start_num:(end_num+1)]:
                    M2(i, cnt_move)
                    cnt_move += 1
                for i in list_names[goto:]:
                    M2(i, cnt_move)
                    cnt_move += 1

            list_path = os.listdir(filename)
            for i in list_path:
                if i[0] == 'i':
                    path = filename + i
                    new_path = filename + i[1:]
                    os.rename(path, new_path)
            output("MoveFinish")


root = tk.Tk()
root.geometry("300x300")
root.title("文件处理")
root.attributes("-topmost",True)
root.resizable(False, False)

fr1 = tk.Frame(root)
fr1.place(relx=.5, rely=.5, y=-75, anchor='center')

font = ("宋体", 15, "bold")
la0 = tk.Label(fr1, text="路径：", font=font)
la0.grid(row=0, column=0)
en0 = tk.Entry(fr1, width=20)
en0.grid(row=0, column=1)
bt0 = tk.Button(fr1, text="读取", font=font, command=read)
bt0.grid(row=0, column=2)

la1 = tk.Label(fr1, text="从：", font=font)
la1.grid(row=1, column=0)
en1 = tk.Entry(fr1, width=10)
en1.grid(row=1, column=1)

la2 = tk.Label(fr1, text="到：", font=font)
la2.grid(row=2, column=0)
en2 = tk.Entry(fr1, width=10)
en2.grid(row=2, column=1)

la3 = tk.Label(fr1, text="移动到：", font=font)
la3.grid(row=3, column=0)
en3 = tk.Entry(fr1, width=10)
en3.grid(row=3, column=1)

bt1 = tk.Button(fr1, text="移动", font=font, command=move)
bt1.grid(row=4, column=0, sticky=tk.E)
bt2 = tk.Button(fr1, text="清空", font=font, command=clear)
bt2.grid(row=4, column=1)
bt3 = tk.Button(fr1, text="检查", font=font, command=check)
bt3.grid(row=4, column=2, sticky=tk.W)

tx1 = tk.Label(root, width=48, height=20, fg="black", font=("Arial", 7, "bold"), state=tk.DISABLED, anchor="nw", justify=tk.LEFT, wraplength=290)
tx1.place(x=0, y=150)

root.mainloop()





