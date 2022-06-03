import tkinter as tk

main_screen = tk.Tk()
main_screen.title("currency convertor")
#Canvas is the window that gets created when we run the app
main_screen_canvas = tk.Canvas(main_screen, width = 400, height = 350, bg="pink")
main_screen_canvas.pack()


#Label 1 is for naming the App
header = tk.Label(main_screen, text='Currency Converter')
header.config(font=('helvetica',15 ,'bold','underline' ),bg='pink',fg='green')
#Label 2 is for giving the text to entry field
currency_INR_label = tk.Label(main_screen, text='INR:')
currency_INR_label.config(font=('helvetica', 10, 'bold'),bg='blue',fg='white')
#currency_INR_entry takes the amount
currency_INR_entry = tk.Entry(main_screen, width = 10, font=('helvetica', 10, 'bold'),bg='SkyBlue4',fg='white')

hack = tk.StringVar()
currency_dollar_converted_entry = tk.Entry(main_screen, width = 10, font=('helvetica', 10, 'bold'),bg='SkyBlue4',fg='white', textvariable = hack)
#Create window puts everything onto the canvas
main_screen_canvas.create_window(200, 20, window=header)
main_screen_canvas.create_window(140, 100, window=currency_INR_label)
main_screen_canvas.create_window(210, 100, window=currency_INR_entry)
main_screen_canvas.create_window(210, 300, window=currency_dollar_converted_entry)

#Function to convert our currency
def conversion():
    dollar = 76
    inr = currency_INR_entry.get()
    dollar_converted = round(float(inr)/dollar, 2)
    hack.set(str(dollar_converted))

#convert_button which when clicked, makes the function conversion run
currency_dollar_label = tk.Label(main_screen,text="DOLLAR:")
currency_dollar_label.config(font=('helvetica', 10, 'bold'),bg='blue',fg='white')
main_screen_canvas.create_window(120, 300, window=currency_dollar_label)
convert_button = tk.Button(text='Convert', command=conversion, font=('helvetica', 10, 'bold'),bg='navy blue',fg='white')
main_screen_canvas.create_window(200, 200, window=convert_button)
main_screen.mainloop()