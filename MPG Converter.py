#Calculate MPG of a car using a GUI built with tkinter

import tkinter

class GasMileageGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.main_window.title("Calculate Gas Mileage")
#Frames to organize widgets:
        self.gallons_frame=tkinter.Frame(self.main_window)
        self.miles_frame=tkinter.Frame(self.main_window)
        self.result_frame=tkinter.Frame(self.main_window)
        self.button_frame=tkinter.Frame(self.main_window)
#Widgets for gallons frame:
        self.gallons_label=tkinter.Label(self.gallons_frame,text="Gallons the Car Holds:")
        self.gallons_entry=tkinter.Entry(self.gallons_frame,width=10)
#Widget formatting horizontally (Gallons):
        self.gallons_label.pack(side="left")
        self.gallons_entry.pack(side="left")
#Miles frame widgets:
        self.miles_label=tkinter.Label(self.miles_frame,text="Full Tank Mileage:")
        self.miles_entry=tkinter.Entry(self.miles_frame,width=10)
#Widget formatting horizontally (Miles):
        self.miles_label.pack(side="left")
        self.miles_entry.pack(side="left")
#Widgets for result frame with StringVar
        self.result_desc_label=tkinter.Label(self.result_frame,text="Miles Per Gallon (MPG):")
        self.mpg_value=tkinter.StringVar()
        self.mpg_label=tkinter.Label(self.miles_frame,textvariable=self.mpg_value)
#Widget formatting horizontally:
        self.result_desc_label.pack(side="left")
        self.mpg_label.pack(side="left")
#Button widgets for bottom frame:
        self.calc_button=tkinter.Button(self.button_frame,text='Calculate MPG', command=self.calculate_mpg)
        self.quit_button=tkinter.Button(self.button_frame,text='Quit', command=self.main_window.destroy)
#Buttons packed horizontally:
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
#Pack all frames in main window:
        self.gallons_frame.pack(padx=10,pady=5)
        self.miles_frame.pack(padx=10,pady=5)
        self.button_frame.pack(padx=10,pady=5)
        self.result_frame.pack(padx=10,pady=5)

        tkinter.mainloop()

    #Callback function:
    def calculate_mpg(self):
        try:
            #Input from entry widgets converted to float:
            gallons=float(self.gallons_entry.get())
            miles= float(self.miles_entry.get())

            #Prevent dividing by zero:
            if gallons>0:
                mpg=miles/gallons
                self.mpg_value.set(f"{mpg:.2f}")
            else:
                self.mpg_value.set("Error: Gallons > 0")
        except ValueError:
            self.mpg_value.set("Invalid Value Entered")

#GasMileageGUI:
if __name__ == "__main__":
    gas_gui= GasMileageGUI()
