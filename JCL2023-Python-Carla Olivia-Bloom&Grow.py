import tkinter as tk
import random
from tkinter import *
from tkinter import Tk, font

root= tk.Tk()
root.geometry("1600x900")
root.title("Bloom & Grow")
root.resizable(False, False)

#PhotoImages
bg= PhotoImage(file= r"C:\Users\62811\mu_code\images\JCL\bg.gif")
title= PhotoImage(file= r"C:\Users\62811\mu_code\images\JCL\title label.png")
wlcm_btn= PhotoImage(file= r"C:\Users\62811\mu_code\images\JCL\welcome button.png")
flower= PhotoImage(file= r"C:\Users\62811\mu_code\images\JCL\flower.png")
note= PhotoImage(file= r"C:\Users\62811\mu_code\images\JCL\notes.png")
stats= PhotoImage(file= r"C:\Users\62811\mu_code\images\JCL\name box.png")

#icon
root.iconphoto(False, flower)

#background
bg_img= Label(root, image=bg)
bg_img.place(x=0, y=0, relwidth=1, relheight=1)

#globals
file_name= str(random.randint(1,35))
task_list= []
inputs= 0
checkboxes= []
score= 0
hp= 0
day_variable=1

#tabs
def tab1():
    def tab2():
        #destroy tab1 items
        title_label.destroy()
        subtitle.destroy()
        instruction.destroy()
        welcome_button.destroy()

        #flower virtual assistant
        flw_assist= Label(root, image=flower, background="#E2FCFF")
        flw_assist.place(x=40, y=40)

        #input name
        name= StringVar(root)
        name_input= Entry(root, textvariable= name, font= ("Comic Sans MS", 20,"bold"), fg="#3E4677", background= "#F0FBFF")
        name_input.place(x=400,y=140)

        def characters(*args):
            if(len(name.get())>0):
                next_btn2.config(state= "normal")
            else:
                next_btn2.config(state= "disabled")

        name.trace("w", characters)

        #function to go to next line with button
        def clicked():
            global next_btn2
            m2_config()
            next_btn.destroy()

            next_btn2= Button(root, text="NEXT", font= ("Comic Sans MS", 15,"bold"), borderwidth= 0, fg="#3E4677", background= "#E2FCFF", activebackground= "#BEEDFF", command=clicked2, state="disabled")
            next_btn2.place(x=860, y=140)

        def clicked2():
            global next_btn2, next_btn3
            m3_config()
            next_btn2.destroy()
            name_input.destroy()

            next_btn3= Button(root, text="NEXT", font= ("Comic Sans MS", 15,"bold"), borderwidth= 0, fg="#3E4677", background= "#E2FCFF", activebackground= "#BEEDFF", command=clicked3)
            next_btn3.place(x=1120, y=190)

        def clicked3():
            global next_btn3, proceed_btn
            m4_config()
            next_btn3.destroy()

            proceed_btn= Button(root, text="PROCEED", font= ("Comic Sans MS", 15,"bold"), borderwidth= 0, fg="#3E4677", background= "#E2FCFF", activebackground= "#BEEDFF", command=proceed)
            proceed_btn.place(x=400, y= 290)

        #delete all text and input box
        def proceed():
            global proceed_btn, add_btn
            m1.destroy()
            m2.destroy()
            m3.destroy()
            m4.destroy()
            proceed_btn.destroy()
            name_input.destroy()

            #input habits
            m5= Label(root, text="What habits do you want to include in your routine?", font= ("Comic Sans MS", 20,"bold"), borderwidth= 0, fg="#3E4677", background= "#F0FBFF")
            m5.place(x=400, y=40)

            habit= StringVar()
            habit_input= Entry(root, textvariable= habit, font= ("Comic Sans MS", 20,"bold"), width= 35, fg="#3E4677", background= "#F0FBFF")
            habit_input.place(x=400,y=90)

            def end():
                global end_tutorial

                end_tutorial.destroy()
                tmr_btn.config(state="normal")

                m5.destroy()
                m6.destroy()

                title_label= Label(root, image=title, borderwidth=0, background="#BEEDFF")
                title_label.place(x=575, y=35)

            def tmr():
                global score, hp, day_variable, option1, option2, option3, option4, option5, c1, c2, c3, c4, c5
                score= 0
                hp= 0
                day_variable+=1

                day_label.config(text=day_variable)

                c1.deselect()
                option1.set(0)

                c2.deselect()
                option2.set(0)

                c3.deselect()
                option3.set(0)

                c4.deselect()
                option4.set(0)

                c5.deselect()
                option5.set(0)

                hp_bar.config(width= 1)

            def clicked6():
                global next_btn6, end_tutorial

                next_btn6.destroy()
                m5.config(text= "Complete your checklist everyday and make YOU happy!")
                m6.config(text= "Remember, consistency is key! You got this!")

                end_tutorial= Button(root, text="END TUTORIAL", font= ("Comic Sans MS", 15,"bold"), borderwidth= 0, fg="#3E4677", background= "#E2FCFF", activebackground= "#BEEDFF", command=end)
                end_tutorial.place(x=1300, y=40)

            def clicked5():
                global next_btn5, m6, next_btn6

                next_btn5.destroy()

                m5.config(text= "When you check the checkboxes in your list, you will gain HP.")
                m6.config(text= "When you click [TMR], the list will refresh into a new day.")

                next_btn6= Button(root, text="NEXT", font= ("Comic Sans MS", 15,"bold"), borderwidth= 0, fg="#3E4677", background= "#E2FCFF", activebackground= "#BEEDFF", command=clicked6)
                next_btn6.place(x=1300, y=40)

            def clicked4():
                global next_btn4, name_input, hp_bar, next_btn5, m6

                next_btn4.destroy()

                m6= Label(root, text="Beside this is your HP [Health Points] bar", font= ("Comic Sans MS", 20,"bold"), borderwidth= 0, fg="#3E4677", background= "#F0FBFF")
                m6.place(x=400, y=90)

                next_btn5= Button(root, text="NEXT", font= ("Comic Sans MS", 15,"bold"), borderwidth= 0, fg="#3E4677", background= "#E2FCFF", activebackground= "#BEEDFF", command=clicked5)
                next_btn5.place(x=800, y=40)

                stats_bar= Label(root, image=stats, background="#E2FCFF")
                stats_bar.place(x=1030, y=135)

                stats_heading = Label(root, text="Health Level", font=("Comic Sans MS", 20, "bold"), background="#FFFFFF", fg="#3E4677")
                stats_heading.place(x=1100, y=205)

                hp_background= Label(root, text="", font=("Comic Sans MS", 20, "bold"), width= 18, background="#E2FCFF")
                hp_background.place(x= 1100, y=255)

                hp_bar= Label(root, text="", font=("Comic Sans MS", 20, "bold"), width=1, background="light pink", fg="#3E4677")
                hp_bar.place(x= 1100, y=255)

            def done():
                global next_btn4

                add_btn.destroy()

                done_btn.destroy()

                habit_input.destroy()

                m5.config(text="Okay, now let's get started!")

                next_btn4= Button(root, text="NEXT", font= ("Comic Sans MS", 15,"bold"), borderwidth= 0, fg="#3E4677", background= "#E2FCFF", activebackground= "#BEEDFF", command=clicked4)
                next_btn4.place(x=800, y=40)

            def habit_charac(*args):
                if(len(habit.get())>0):
                    add_btn.config(state= "normal")
                elif inputs<5:
                    add_btn.config(state="normal")
                else:
                    add_btn.config(state= "disabled")
                    add_btn.destroy()

            habit.trace("w", habit_charac)

            #note frame
            list_note= Label(root, image= note, background="#E2FCFF")
            list_note.place(x=400, y=135)

            listbox= Listbox(root, font=("Comic Sans MS", 20), width= 18, height=10, background= "white", fg="black", cursor="hand2", selectbackground= "light pink")
            listbox.place(x=525, y=305)

            def hp_update():
                global hp_bar, score
                if score>=10:
                    hp_bar.config(width= 4)

                    if score>=20:
                        hp_bar.config(width= 7)

                        if score>=30:
                            hp_bar.config(width= 11)

                            if score>=40:
                                hp_bar.config(width= 14)

                                if score>=50:
                                    hp_bar.config(width= 18)

            def update_score():
                global score, option1, option2, option3, option4, option5, hp_bar
                if option1.get()==1:
                    score+=10
                    print(score)
                    hp_update()
                elif option1.get()==0:
                    score-=10

                elif option2.get()==1:
                    score+=10
                    print(score)
                    hp_update()
                elif option2.get()==0:
                    score-=10

                elif option3.get()==1:
                    score+=10
                    print(score)
                    hp_update()
                elif option3.get()==0:
                    score-=10

                elif option4.get()==1:
                    score+=10
                    print(score)
                    hp_update()
                elif option4.get()==0:
                    score-=10

                elif option5.get()==1:
                    score+=10
                    print(score)
                    hp_update()
                elif option5.get()==0:
                    score-=10

            def addTask():
                global inputs, file, add_btn, checkboxes, score
                global option1, option2, option3, option4, option5
                global c1, c2, c3, c4, c5

                habit= habit_input.get()
                habit_input.delete(0, END)

                if habit:
                    with open("tasklist.txt", "a") as taskfile:
                        taskfile.write(f"\n{habit}")

                    task_list.append(habit)
                    listbox.insert(END, habit)

                    inputs+=1
                    #print(inputs)

                    if inputs>=5:
                        m5.config(text="Whoa that's a lot, let's just start small for now")
                        add_btn.config(state="disabled")

                    #for i in range(5):
                        #option=IntVar()
                        #option.set(0)
                        #checkboxes.append(option)
                        #print(checkboxes)

                    if inputs==1:
                        option1=IntVar()
                        option1.set(0)
                        c1= Checkbutton(root, text= "", font=("Comic Sans MS", 20), variable= option1, onvalue=1, offvalue=0, background="white", command= update_score)
                        c1.deselect()
                        c1.place(x=480, y=300)

                    elif inputs==2:
                        option2=IntVar()
                        option2.set(0)
                        c2= Checkbutton(root, text= "", font=("Comic Sans MS", 20), variable= option2, onvalue=1, offvalue=0, background="white", command= update_score)
                        c2.deselect()
                        c2.place(x=480, y=340)

                    elif inputs==3:
                        option3=IntVar()
                        option3.set(0)
                        c3= Checkbutton(root, text= "", font=("Comic Sans MS", 20), variable= option3, onvalue=1, offvalue=0, background="white", command= update_score)
                        c3.deselect()
                        c3.place(x=480, y=380)

                    elif inputs==4:
                        option4=IntVar()
                        option4.set(0)
                        c4= Checkbutton(root, text= "", font=("Comic Sans MS", 20), variable= option4, onvalue=1, offvalue=0, background="white", command= update_score)
                        c4.deselect()
                        c4.place(x=480, y=420)

                    elif inputs==5:
                        option5=IntVar()
                        option5.set(0)
                        c5= Checkbutton(root, text= "", font=("Comic Sans MS", 20), variable= option5, onvalue=1, offvalue=0, background="white", command= update_score)
                        c5.deselect()
                        c5.place(x=480, y=460)

            def openTaskFile():
                global file, file_name, create_file_name
                create_file_name= file_name + ".txt"
                try:
                    global task_list
                    with open(create_file_name,"r") as taskfile:
                        tasks= taskfile.readlines()

                    for task in tasks:
                        if task!='\n':
                            task_list.append(task)
                            listbox.insert(END, task)

                except:
                    file=open(create_file_name, "w")
                    file.close()

            openTaskFile()

            add_btn= Button(root, text="ADD", font= ("Comic Sans MS", 15,"bold"), borderwidth= 0, fg="#3E4677", background= "#E2FCFF", activebackground= "#BEEDFF", command= addTask)
            add_btn.place(x=980, y=90)

            done_btn= Button(root, text="DONE", font= ("Comic Sans MS", 15,"bold"), borderwidth= 0, fg="#3E4677", background= "#E2FCFF", activebackground= "#BEEDFF", command= done)
            done_btn.place(x=1050, y=90)

            heading= Label(root, text= "DAY: ", font= ("Comic Sans MS", 34,"bold"), background="#FFFFFF", fg="#3E4677")
            heading.place(x=480, y=220)

            day_label= Label(root, text=day_variable, font= ("Comic Sans MS", 34,"bold"), background="#FFFFFF", fg="#3E4677")
            day_label.place(x=600, y=220)

            tmr_btn= Button(root, text="TMR", font= ("Comic Sans MS", 15,"bold"), borderwidth= 0, fg="#3E4677", background= "light pink", activebackground= "#BEEDFF", command= tmr, state="disabled")
            tmr_btn.place(x=700, y=230)

        next_btn= Button(root, text="NEXT", font= ("Comic Sans MS", 15,"bold"), borderwidth= 0, fg="#3E4677", background= "#E2FCFF", activebackground= "#BEEDFF", command=clicked)
        next_btn.place(x=1100, y=35)

        #introductions
        m1= Label(root, text="", font= ("Comic Sans MS", 20,"bold"), borderwidth= 0, fg="#3E4677", background= "#F0FBFF")
        m1.place(x=400, y=40)
        m2= Label(root, text="", font= ("Comic Sans MS", 20,"bold"), borderwidth= 0, fg="#3E4677", background= "#F0FBFF")
        m2.place(x=400, y=90)



        m3= Label (root, text="", font= ("Comic Sans MS", 20,"bold"), borderwidth= 0, fg="#3E4677", background= "#F0FBFF")
        m3.place(x=400, y=190)

        m4= Label(root, text="", font= ("Comic Sans MS", 20,"bold"), borderwidth= 0, fg="#3E4677", background= "#F0FBFF")
        m4.place(x=400, y=240)

        #next line function
        def m1_config():
            m1.config(text="Welcome to your first step into a healthy lifestyle!")

        m1_config()

        def m2_config():
            m2.config(text="Before we go any further, what is your name?")

        def m3_config():
            message= name_input.get()
            m3.config(text="Hello " + message + ", I'm so proud of you for taking this step!")

        def m4_config():
            m4.config(text="Bloom & Grow is here to help you reach your healthy lifestyle goals!")

    #title label
    title_label= Label(root, image=title, borderwidth=0, background="#BEEDFF")
    title_label.place(x=575, y=90)

    #subtitle
    subtitle= Label(root, text="Your jolliest healthy habit tracker!", font= ("Comic Sans MS", 15,"bold"), fg="#3E4677", background= "#E2FCFF")
    subtitle.place(x=645, y=190 )

    #instruction label
    instruction= Label(root, text="Click the welcome button above to start.", font= ("Comic Sans MS", 15,"bold"), fg="#3E4677", background= "#E2FCFF")
    instruction.place(x=615, y=760)

    #welcome button
    common_image= PhotoImage(width= 1, height= 1)
    welcome_button= Button(root, image=wlcm_btn, borderwidth=0, background= "#E2FCFF", height= 500, activebackground= "#BEEDFF", command=tab2)
    welcome_button.place(x=470, y=240)

tab1()

root.mainloop()
