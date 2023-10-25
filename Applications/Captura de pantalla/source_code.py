from tkinter import*
import pyautogui 

win = Tk()
win.title("LoopGlitch Screenshoter")

def callback():
    #mySS = pyautogui.screenshot()
    mySS = pyautogui.screenshot()
    mySS.save(r'F:\DESARROLLOS\Practicas_python\my-portfolio\Applications\Captura de pantalla\captura.jpg')  #r'Path to save the screenshot\file name.png or jpg'

button = Button(win, text = "Screenshot This !", command = callback)
button.grid(row = 50, column = 50)

win.mainloop()