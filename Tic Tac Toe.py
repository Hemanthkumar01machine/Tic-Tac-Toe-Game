import tkinter 
from tkinter import *
import pyttsx3
from tkinter import messagebox as msg

class Tictactoe:
    def __init__(self):
        plr_x_lbl=0
        plr_o_lbl=0
        plr_draw_lbl=0
        plr_match_lbl=0
    def outline(self):

        self.instructions=["Fill The Name In The Respective Column.(Name Should Be Of 2-15 Characters)","Click On Submit Button.","Start Playing.","At First Player X Will Start And Then Player O And So on.","If Any Player Won Then The Next Player Has To Start The Game At First.","Results Can Be Viewed In The Result Box.","Reset = Only The Scores Will Be Cleared Name Will Be Remains Same","New Game = Both Name Of The Players And The Scores Will BE Cleared Starts As Fresh","Clear Name = Will Clear The Name"]

        main_screen=Tk()
        main_screen.title("Tic Tac Toe")
        main_screen.geometry("1350x700+0+0")
        main_screen.config(background="powder blue")

        name_game=Label(main_screen,text="Tic Tac Toe",foreground="dark blue",background="yellow",font=("jokerman",50))
        name_game.place(x=500,y=5)

        main_frame=LabelFrame(main_screen,text="Gaming Is just A Relaxiation",background="powder blue")
        main_frame.place(x=10,y=100,width=1320,height=570)

        game_frame=LabelFrame(main_frame,text="Concentration Leads To Success",border=6,foreground="blue",background="powder blue",font=("courier new",15,"bold")).place(x=15,y=11,width=605,height=515)

        plr_det_frame=LabelFrame(main_frame,text="Player's Details",border=6,foreground="red",background="powder blue",font=("gabriola",25,"bold")).place(x=630,y=-8,width=350,height=318)
        
        result_frame=LabelFrame(main_frame,text="Game Results",border=6,background="powder blue",foreground="#005D8D",font=("monotypecorsiva",20,"bold")).place(x=630,y=320,width=480,height=206)

        game_settings=LabelFrame(main_frame,text="Settings",border=8,background="powder blue",foreground="#C200DF",font=("msmincho",22)).place(x=1115,y=320,width=180,height=206)
        
        plr_det_lbl=Label(plr_det_frame,text="Enter Player's Name's",font=("curlzmt",18,"bold"),foreground="Yellow",background="blue").place(x=690,y=165)

        instruction_frame=LabelFrame(main_frame,text="Instructions For Playing",border=6,background="powder blue",foreground="brown",font=("pristina",22)).place(x=990,y=5,width=305,height=305)

        scroll_x=Scrollbar(instruction_frame,orient="horizontal")
        scroll_x.place(x=1010,y=388,width=290,height=20)
        sentence=Listbox(instruction_frame,font=("segoescript",14),xscrollcommand=scroll_x.set)
        sentence.place(x=1010,y=168,width=290,height=220)

        for sen in range(len(self.instructions)):
            if sen<6:
                sentence.insert(sen,"Step "+str(sen+1)+" : "+self.instructions[sen]+"\n")
            else:
                sentence.insert(sen,"    "+self.instructions[sen])
        
        scroll_x.config(command=sentence.xview)

        self.plr_start=0
        self.plr_start_checking=0
        self.plr_x_win=0
        self.plr_o_win=0
        self.plr_draw=0
        self.plr_match=0

        def result():
            global plr_x_lbl
            global plr_o_lbl
            global plr_draw_lbl
            global plr_match_lbl
            plr_x_lbl=Label(result_frame,text=int(self.plr_x_win),background="white",foreground="black",font=("arial",20))
            plr_x_lbl.place(x=1080,y=480)
            plr_o_lbl=Label(result_frame,text=int(self.plr_o_win),background="white",foreground="black",font=("arial",20))
            plr_o_lbl.place(x=1080,y=520)
            plr_draw_lbl=Label(result_frame,text=int(self.plr_draw),background="white",foreground="black",font=("arial",20)).place(x=875,y=560)
            plr_match_lbl=Label(result_frame,text=int(self.plr_match),background="white",foreground="black",font=("arial",20)).place(x=895,y=600)

        self.name_no=1
        def name():
            global name_no
            if self.name_no%2==0:
                name=self.plr_x.get()
                self.name_no+=1
                player_lbl=Label(game_frame,text="Player X : "+name+"'s "+"Turn",font=("chaparralprolight",20,"bold"),bg="blue",foreground="red").place(x=50,y=570,width=550)
            else:
                name=self.plr_o.get()
                self.name_no+=1
                player_lbl=Label(game_frame,text="Player O : "+name+"'s "+"Turn",font=("chaparralprolight",20,"bold"),bg="red",foreground="blue").place(x=50,y=570,width=550)

        def result_name_back_frame():
            plrs_lbl_frame=Frame(background="powder blue").place(x=800,y=475,width=280,height=80)


        def name_submit_fn():
            if len(self.plr_x.get())>1 and len(self.plr_o.get())>1 and len(self.plr_x.get())<=15 and len(self.plr_o.get())<=15:
                self.plr_start+=1
                ######
                result_name_back_frame()
                plr_x_name_lbl_result=Label(result_frame,text=self.plr_x.get()+" = ",background="powder blue",foreground="purple",font=("pristina",27,"bold")).place(x=800,y=475)
                plr_y_name_lbl_result=Label(result_frame,text=self.plr_o.get()+" = ",background="powder blue",foreground="purple",font=("pristina",27,"bold")).place(x=800,y=513)
                msg.showinfo("Data Saved","Your Name Has Been Saved You Can Start Playing")
                self.name_no=0
                name()
            else:
                msg.showwarning("Warning","Name Of The Players Should Be\nAtleast Of 2 Characters and Atmost Of 15 character")
                
        def clr_name_fn():
            self.plr_x.set("")
            self.plr_o.set("")


        def onclick(btn):
            x=self.plr_x.get()
            o=self.plr_o.get()
            global player_value
            if x=="" or o=="":
                msg.showwarning("Warning","Please Fill The Player's Name First")
                reset()
            else:
                if self.plr_start!=0:
                    if btn["text"]==" " and self.player_value==True:
                        btn["text"]="X"
                        btn["background"]="dark green"
                        self.player_value=False
                        checking()
                    elif btn["text"]==" " and self.player_value==False:
                        btn["text"]="O"
                        btn["background"]="red"
                        self.player_value=True
                        checking()
                else:
                    msg.showinfo("Warning","Click The Submit Button Before Starting")
        self.plr_x=StringVar()
        plr_x_lbl=Label(plr_det_frame,text="Player X :",font=("courier",18,"bold"),foreground="red",background="lime").place(x=655,y=210)
        plr_x_entry=Entry(plr_det_frame,textvariable=self.plr_x,font=("gigi",20,"bold"),width=14)
        plr_x_entry.place(x=800,y=207)

        self.plr_o=StringVar()
        plr_o_lbl=Label(plr_det_frame,text="Player O :",font=("courier",18,"bold"),foreground="red",background="lime").place(x=655,y=260)
        plr_o_entry=Entry(plr_det_frame,textvariable=self.plr_o,font=("gigi",20,"bold"),width=14)
        plr_o_entry.place(x=800,y=257)
        
        name_submit=Button(plr_det_frame,text="Submit",foreground="dark red",background="orange",width=9,height=-3,font=("arial",15,"bold"),command=name_submit_fn).place(x=745,y=307)
        
        name_clear=Button(plr_det_frame,text="Clear Name",foreground="orange",background="dark red",width=9,height=-3,font=("arial",15,"bold"),command=clr_name_fn).place(x=745,y=367)

        game_bd=Frame(main_frame,border=4,bg="magenta").place(x=38,y=43,width=550,height=371)

        self.player_value=True
        self.btn=StringVar()

        def reset():
            btn00["text"]=" "
            btn01["text"]=" "
            btn02["text"]=" "
            btn10["text"]=" "
            btn11["text"]=" "
            btn12["text"]=" "
            btn20["text"]=" "
            btn21["text"]=" "
            btn22["text"]=" "

            btn00.configure(background="black")
            btn01.configure(background="black")
            btn02.configure(background="black")
            btn10.configure(background="black")
            btn11.configure(background="black")
            btn12.configure(background="black")
            btn20.configure(background="black")
            btn21.configure(background="black")
            btn22.configure(background="black")

        def result_placing():
            plr_x_lbl_result=Label(result_frame,text="Player X  : ",font=("arialblack",20,"bold"),foreground="black",background="powder blue").place(x=660,y=480)
            plr_o_lbl_result=Label(result_frame,text="Player O : ",font=("arialblack",20,"bold"),foreground="black",background="powder blue").place(x=660,y=520)
            draw_lbl_result=Label(result_frame,text="Draw Matches = ",font=("arialblack",20,"bold"),foreground="black",background="powder blue").place(x=660,y=560)
            matches_lbl_result=Label(result_frame,text="Matches Played = ",font=("arialblack",20,"bold"),foreground="black",background="powder blue").place(x=660,y=600)
            result()

        def speech_(namesay):
            if namesay=="X":
                namesayings=self.plr_x.get()
                sayings="Player X "+namesayings+" Won"
            elif namesay=="O":
                namesayings=self.plr_o.get()
                sayings="Player O "+namesayings+" Won"
            elif namesay=="DRAW":
                sayings="Match IS Drawn"
            engine=pyttsx3.init()
            engine.say(sayings)
            engine.runAndWait()

        
        def checking():
                global plr_x_win
                global plr_o_win
                global plr_draw
                global plr_match
                name()
                if btn00["text"]=="X" and btn01["text"]=="X" and btn02["text"]=="X":
                    namesay="X"
                    self.plr_x_win+=1
                    self.plr_match+=1
                    btn00.configure(background="purple")
                    btn01.configure(background="purple")
                    btn02.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player X : "+self.plr_x.get()+ " Won")
                    reset()
                elif btn10["text"]=="X" and btn11["text"]=="X" and btn12["text"]=="X":
                    namesay="X"
                    self.plr_x_win+=1
                    self.plr_match+=1
                    btn10.configure(background="purple")
                    btn11.configure(background="purple")
                    btn12.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player X : "+self.plr_x.get()+ " Won")
                    reset()
                elif btn20["text"]=="X" and btn21["text"]=="X" and btn22["text"]=="X":
                    namesay="X"
                    self.plr_x_win+=1
                    self.plr_match+=1
                    btn20.configure(background="purple")
                    btn21.configure(background="purple")
                    btn22.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player X : "+self.plr_x.get()+ " Won")
                    reset()
                elif btn00["text"]=="X" and btn10["text"]=="X" and btn20["text"]=="X":
                    namesay="X"
                    self.plr_x_win+=1
                    self.plr_match+=1
                    btn00.configure(background="purple")
                    btn10.configure(background="purple")
                    btn20.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player X : "+self.plr_x.get()+ " Won")
                    reset()
                elif btn01["text"]=="X" and btn11["text"]=="X" and btn21["text"]=="X":
                    namesay="X"
                    self.plr_x_win+=1
                    self.plr_match+=1
                    btn01.configure(background="purple")
                    btn11.configure(background="purple")
                    btn21.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player X : "+self.plr_x.get()+ " Won")
                    reset()
                elif btn02["text"]=="X" and btn12["text"]=="X" and btn22["text"]=="X":
                    namesay="X"
                    self.plr_x_win+=1
                    self.plr_match+=1
                    btn02.configure(background="purple")
                    btn12.configure(background="purple")
                    btn22.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player X : "+self.plr_x.get()+ " Won")
                    reset()
                elif btn00["text"]=="X" and btn11["text"]=="X" and btn22["text"]=="X":
                    namesay="X"
                    self.plr_x_win+=1
                    self.plr_match+=1
                    btn00.configure(background="purple")
                    btn11.configure(background="purple")
                    btn22.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player X : "+self.plr_x.get()+ " Won")
                    reset()
                elif btn02["text"]=="X" and btn11["text"]=="X" and btn20["text"]=="X":
                    namesay="X"
                    self.plr_x_win+=1
                    self.plr_match+=1
                    btn02.configure(background="purple")
                    btn11.configure(background="purple")
                    btn20.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player X : "+self.plr_x.get()+ " Won")
                    reset()
                elif btn00["text"]=="O" and btn01["text"]=="O" and btn02["text"]=="O":
                    namesay="O"
                    self.plr_o_win+=1
                    self.plr_match+=1
                    btn00.configure(background="purple")
                    btn01.configure(background="purple")
                    btn02.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player O : "+self.plr_o.get()+ " Won")
                    reset()
                elif btn10["text"]=="O" and btn11["text"]=="O" and btn12["text"]=="O":
                    namesay="O"
                    self.plr_o_win+=1
                    self.plr_match+=1
                    btn10.configure(background="purple")
                    btn11.configure(background="purple")
                    btn12.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player O : "+self.plr_o.get()+ " Won")
                    reset()
                elif btn20["text"]=="O" and btn21["text"]=="O" and btn22["text"]=="O":
                    namesay="O"
                    self.plr_o_win+=1
                    self.plr_match+=1
                    btn20.configure(background="purple")
                    btn21.configure(background="purple")
                    btn22.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player O : "+self.plr_o.get()+ " Won")
                    reset()
                elif btn00["text"]=="O" and btn10["text"]=="O" and btn20["text"]=="O":
                    namesay="O"
                    self.plr_o_win+=1
                    self.plr_match+=1
                    btn00.configure(background="purple")
                    btn10.configure(background="purple")
                    btn20.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player O : "+self.plr_o.get()+ " Won")
                    reset()
                elif btn01["text"]=="O" and btn11["text"]=="O" and btn21["text"]=="O":
                    namesay="O"
                    self.plr_o_win+=1
                    self.plr_match+=1
                    btn01.configure(background="purple")
                    btn11.configure(background="purple")
                    btn21.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player O : "+self.plr_o.get()+ " Won")
                    reset()
                elif btn02["text"]=="O" and btn12["text"]=="O" and btn22["text"]=="O":
                    namesay="O"
                    self.plr_o_win+=1
                    self.plr_match+=1
                    btn02.configure(background="purple")
                    btn12.configure(background="purple")
                    btn22.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player O : "+self.plr_o.get()+ " Won")
                    reset()
                elif btn00["text"]=="O" and btn11["text"]=="O" and btn22["text"]=="O":
                    namesay="O"
                    self.plr_o_win+=1
                    self.plr_match+=1
                    btn00.configure(background="purple")
                    btn11.configure(background="purple")
                    btn22.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player O : "+self.plr_o.get()+ " Won")
                    reset()
                elif btn02["text"]=="O" and btn11["text"]=="O" and btn20["text"]=="O":
                    namesay="O"
                    self.plr_o_win+=1
                    self.plr_match+=1
                    btn02.configure(background="purple")
                    btn11.configure(background="purple")
                    btn20.configure(background="purple")
                    speech_(namesay)
                    msg.showinfo("Match Overed","Player O : "+self.plr_o.get()+ " Won")
                    reset()
                elif btn00["text"]!=" " and btn01["text"]!=" " and btn02["text"]!=" " and btn10["text"]!=" " and btn11["text"]!=" " and btn12["text"]!=" " and btn20["text"]!=" " and btn21["text"]!=" " and btn22["text"]!=" " :
                    namesay="DRAW"
                    self.plr_draw+=1
                    self.plr_match+=1
                    speech_(namesay)
                    msg.showinfo("Match Overed","Match Is Draw ♥♥♥")
                    reset()
                result()

        def reset_all():
            global plr_x_win
            global plr_o_win
            global plr_draw
            global plr_match

            self.plr_x_win=0
            self.plr_o_win=0
            self.plr_draw=0
            self.plr_match=0
            reset() 
            result()

        def new_game_fn():
            reset_all()
            clr_name_fn()
            result_name_back_frame()

        new_game_btn=Button(text="New Game",foreground="white",background="black",font=("arialblack",18,"bold"),width=8,relief=SUNKEN,command=new_game_fn).place(x=1150,y=490)

        reset_all_btn=Button(text="Reset",foreground="red",background="light grey",font=("arialblack",18,"bold"),width=8,relief=SUNKEN,command=reset_all).place(x=1150,y=560)

        btn00=Button(game_frame,text=" ",font=("Arialblack",20,"bold"),width=10,height=3,relief=RIDGE,bg="black",foreground="white",command=lambda:onclick(btn00))
        btn00.place(x=50,y=160)

        
        btn01=Button(game_frame,text=" ",font=("Arialblack",20,"bold"),width=10,height=3,relief=RIDGE,bg="black",foreground="white",command=lambda:onclick(btn01))
        btn01.place(x=235,y=160)

        btn02=Button(game_frame,text=" ",font=("Arialblack",20,"bold"),width=10,height=3,relief=RIDGE,bg="black",foreground="white",command=lambda:onclick(btn02))
        btn02.place(x=420,y=160)

        btn10=Button(game_frame,text=" ",font=("Arialblack",20,"bold"),width=10,height=3,relief=RIDGE,bg="black",foreground="white",command=lambda:onclick(btn10))
        btn10.place(x=50,y=285)

        btn11=Button(game_frame,text=" ",font=("Arialblack",20,"bold"),width=10,height=3,relief=RIDGE,bg="black",foreground="white",command=lambda:onclick(btn11))
        btn11.place(x=235,y=285)

        btn12=Button(game_frame,text=" ",font=("Arialblack",20,"bold"),width=10,height=3,relief=RIDGE,bg="black",foreground="white",command=lambda:onclick(btn12))
        btn12.place(x=420,y=285)

        btn20=Button(game_frame,text=" ",font=("Arialblack",20,"bold"),width=10,height=3,relief=RIDGE,bg="black",foreground="white",command=lambda:onclick(btn20))
        btn20.place(x=50,y=410)

        btn21=Button(game_frame,text=" ",font=("Arialblack",20,"bold"),width=10,height=3,relief=RIDGE,bg="black",foreground="white",command=lambda:onclick(btn21))
        btn21.place(x=235,y=410)

        btn22=Button(game_frame,text=" ",font=("Arialblack",20,"bold"),width=10,height=3,relief=RIDGE,bg="black",foreground="white",command=lambda:onclick(btn22))
        btn22.place(x=420,y=410)

        result_placing()
        name()
        main_screen.mainloop()

if __name__==__name__:
    obj=Tictactoe()
    obj.outline()