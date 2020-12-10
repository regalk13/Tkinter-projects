from tkinter import *
from PIL import Image,ImageTk
import requests
import json

root = Tk()
root.title("Weather")
img = PhotoImage(file='images/icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.geometry("600x100")

def lookup():
    #zip.get()
    #ziplabel = Label(root, text=zip.get())
    #ziplabel.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=F8BFB56E-877A-4D01-9FB2-57B1E3F017A7")
        api = json.loads(api_request.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category=api[0]['Category']['Name']
        if category == "Good":
            weater_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"
        
        root.configure(background=weater_color)
        label = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weater_color)
        label.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api = "Error..."

zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

zipb = Button(root, text="Find Zip Code", command=lookup)
zipb.grid(row=0, column=1, stick=W+E+N+S)

root.mainloop()


