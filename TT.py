import tkinter as tk
import time as t
Process = True
while Process:
    Process = False
    global turn
    turn = True
    game = True
    class player_array:
        def __init__(self):
            self.player_array = []

        def append(self, element):
            self.player_array.append(element)
        def reset(self):
            self.player_array = []
    player2_array = player_array()
    player1_array = player_array()

    txt = " "
    print ("Player1 is active")
    win_arrays = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0, 4, 8],[6, 4, 2] ]
    def check(win_arrays, player_arrays):
        for win_combo in win_arrays:
            if set(win_combo).issubset(player_arrays.player_array):
                    return True
        return False





    class button:
        def __init__(self, number,reihe,spalte,):
            self.number = number
            self.button = tk.Button(root, command=self.on_button_press)#button displayes new text after it was pressed
            self.button.grid(row=reihe, column=spalte,sticky="nsew")
            self.button.grid(padx=0,pady=0)
            self.button.config(text=txt)
            self.button.name = number
            self.is_pressed = True
        def button_reset(self):
            self.button.is_pressed = False
            self.button.config(text=" ")





        def on_button_press(self):
            print("button pressed")
            global player2_array
            global player1_array
            global turn
            global game


            if self.is_pressed:
                if turn:
                    self.button.config(text="O", font=300)
                    turn = not turn
                    print("player1 is active")
                    player2_array.append(self.button.name)
                    print (turn)
                    print(player2_array.player_array)
                    self.is_pressed = False
                    if check(win_arrays,player2_array):
                        self.button.config(text="O", font=300)
                        print("Spieler1 Gewonnen")
                        game = False

                elif not turn:
                    self.button.config(text="X", font=300)
                    turn = not turn
                    print("player2 is active")
                    player1_array.append(self.button.name)
                    print(player1_array.player_array)
                    self.is_pressed = False
                    if check(win_arrays,player1_array):
                        self.button.config(text="X", font=300)
                        print("Spieler2 Gewonnen")
                        game = False
                if not game:
                    print("Started neu in " + {t.sleep(3)})
                    global Process
                    Process = True

                    root.destroy()




    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.title("Tic Tac To")
    root.geometry("300x300")
    b1 = button(0,0,0)
    b2 = button(1,0,1)
    b3 = button(2,0,2)
    b4 = button(3,1,0)
    b5 = button(4,1,1)
    b6 = button(5,1,2)
    b7 = button(6,2,0)
    b8 = button(7,2,1)
    b9 = button(8,2,2)

    root.mainloop()
