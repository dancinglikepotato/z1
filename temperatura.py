import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
#Po drugie, utwórz okno główne i ustaw jego konfiguracje:
# root window
root = tk.Tk()
root.title('Temperature Converter')
root.geometry('300x70')
root.resizable(False, False)


#Po trzecie, zdefiniuj funkcję przeliczającą temperaturę ze stopni Fahrenheita na stopnie Celsjusza:
def fahrenheit_to_celsius(f):
    """ Convert fahrenheit to celsius
    """
    return (f - 32) * 5/9


#Po czwarte, utwórz ramkę zawierającą pola formularza:
frame = ttk.Frame(root)
#Po piąte, zdefiniuj opcję, która będzie używana we wszystkich polach formularza:
options = {'padx': 5, 'pady': 5}
#Po szóste, zdefiniuj etykietę, wpis i przycisk. Etykieta wyświetli wynik po kliknięciu przycisku Convert:
# temperature label
temperature_label = ttk.Label(frame, text='Fahrenheit')
temperature_label.grid(column=0, row=0, sticky='W', **options)


# temperature entry
temperature_entry = ttk.Entry(frame, textvariable=temperature)
temperature_entry.grid(column=1, row=0, **options)
temperature_entry.focus()


# convert button
convert_button = ttk.Button(frame, text='Convert')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_clicked)


# result label
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)
#Na koniec umieść ramkę w oknie głównym i uruchom mainloop()metodę:
frame.grid(padx=10, pady=10)
root.mainloop()
Poskładać wszystko do kupy.
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


# root window
root = tk.Tk()
root.title('Temperature Converter')
root.geometry('300x70')
root.resizable(False, False)




def fahrenheit_to_celsius(f):
    """ Convert fahrenheit to celsius
    """
    return (f - 32) * 5/9




# frame
frame = ttk.Frame(root)




# field options
options = {'padx': 5, 'pady': 5}


# temperature label
temperature_label = ttk.Label(frame, text='Fahrenheit')
temperature_label.grid(column=0, row=0, sticky='W', **options)


# temperature entry
temperature = tk.StringVar()
temperature_entry = ttk.Entry(frame, textvariable=temperature)
temperature_entry.grid(column=1, row=0, **options)
temperature_entry.focus()


# convert button




def convert_button_clicked():
    """  Handle convert button click event 
    """
    try:
        f = float(temperature.get())
        c = fahrenheit_to_celsius(f)
        result = f'{f} Fahrenheit = {c:.2f} Celsius'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)




convert_button = ttk.Button(frame, text='Convert')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_clicked)


# result label
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)


# add padding to the frame and show it
frame.grid(padx=10, pady=10)




# start the app
root.mainloop()
