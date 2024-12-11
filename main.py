import customtkinter
import tkintermapview
import time
import os
from geopy.geocoders import Nominatim
from PIL import Image, ImageTk
from get_weather import weather
from bus import locate_bus
locator = Nominatim(user_agent='mygeocoder')
active_markers = []
active_markers_bus = []
def search():
    place = input.get()
    locator = Nominatim(user_agent='mygeocoder')
    locator = locator.geocode(place)
    with open('data.txt', 'a+') as file:
        file.write(locator.address+'\n')
    if 'Астраханская область' not in locator.address:
        input.delete(0, len(place))
        label_error.configure(text='А вот не правильно!')
    else:
        marker = map_widget.set_position(locator.latitude, locator.longitude, marker=True)
        active_markers.append(marker)
        active_markers[0].delete()
        del active_markers[0]
        input.delete(0, len(place))
        label_error.configure(text='')


def trace():
    map_widget.delete_all_path()
    if len(active_markers) > 1:
        for value in range(len(active_markers)-1):
            active_markers[0].delete()
            del active_markers[0]
def add_marker_event(coords):
    if len(active_markers) > 1:
        for value in range(len(active_markers)-1):
            active_markers[0].delete()
            del active_markers[0]
    if len(active_markers) == 0:
        marker = map_widget.set_position(coords[0], coords[1], marker=True)
        active_markers.append(marker)
    else:
        active_markers[0].delete()
        del active_markers[0]
        marker = map_widget.set_position(coords[0],coords[1], marker=True)
        active_markers.append(marker)

def make_path(coords):
    marker = map_widget.set_position(coords[0], coords[1], marker=True)
    active_markers.append(marker)
    map_widget.set_path([active_markers[0].position, active_markers[1].position])

def tern_map():
    if not switch.get() == 1:
        map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        switch.configure(text='Setellite')
    else:
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        switch.configure(text='Deffolt')

def tern_team():
    if not switch_2.get() == 0:
        customtkinter.set_appearance_mode('light')
        switch_2.configure(text='Dark')
    else:
        customtkinter.set_appearance_mode('dark')
        switch_2.configure(text='Light')

def reload():
    label_time.configure(text=time.asctime().split(" ")[3].split(':')[0]+':'+time.asctime().split(" ")[3].split(':')[1])
    label_weather.configure(text=weather(48.5888072, 45.7253529))
    w_h = locate_bus(time.asctime().split(" ")[3].split(':')[0] + ':' + time.asctime().split(" ")[3].split(':')[1])
    active_markers_bus[0].delete()
    current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    bus_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "images", "bus.png")).resize((35, 35)))
    marker_bus = map_widget.set_position(w_h[0], w_h[1], marker=True, icon=bus_image)
def tern_map_2():
    if not switch_3.get() == 1:
        map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        switch_3.configure(text='Normal')
    else:
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        switch_3.configure(text='Deffolt')

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

root_tk = customtkinter.CTk()
root_tk.geometry(f'{680}x{550}')
root_tk.title('3_gis')

map_widget = tkintermapview.TkinterMapView(root_tk, width=root_tk.winfo_width()*2, height=root_tk.winfo_height()*2, corner_radius=1)

input = customtkinter.CTkEntry(root_tk, placeholder_text='Ваш адрес!', width=450)


button_search = customtkinter.CTkButton(root_tk, text='Поиск',command=search)
button_trace = customtkinter.CTkButton(root_tk, text='Очистить', command=trace)
button_reload = customtkinter.CTkButton(root_tk, text='Обновить данные', command=reload)
label_error = customtkinter.CTkLabel(root_tk, text='', text_color='red')
label_time = customtkinter.CTkLabel(root_tk, text=time.asctime().split(" ")[3].split(':')[0]+':'+time.asctime().split(" ")[3].split(':')[1], font=('', 20))
label_weather = customtkinter.CTkLabel(root_tk, text=weather(48.5888072, 45.7253529))
switch = customtkinter.CTkSwitch(root_tk, text='Setellite', command=tern_map)
switch_2 = customtkinter.CTkSwitch(root_tk, text='Light', command=tern_team)
switch_3 = customtkinter.CTkSwitch(root_tk, text='Normal', command=tern_map_2)
button_search.grid(row=1,column=0, padx=20, pady=20)
button_trace.grid(row=2,column=0, padx=20, pady=10)
button_reload.grid(row=3,column=0,padx=20,pady=10)
label_error.grid(row=4,column=0, padx=20, pady=10)
switch.grid(row=5,column=0, padx=20, pady=10)
switch_3.grid(row=6,column=0, padx=20, pady=10)
switch_2.grid(row=7,column=0, padx=20, pady=10)
label_weather.grid(row=8,column=0, padx=20, pady=10)
input.grid(row=1,column=1, padx=20, pady=10)
label_time.grid(row=2,column=1, padx=20, pady=10)
map_widget.place(relx=0.625, rely=0.58, anchor=customtkinter.CENTER)








marker = map_widget.set_position(48.5888072, 45.7253529, marker=True)
w_h = locate_bus(time.asctime().split(" ")[3].split(':')[0]+':'+time.asctime().split(" ")[3].split(':')[1])
current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
bus_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "images", "bus.png")).resize((35, 35)))
marker_bus = map_widget.set_position(w_h[0], w_h[1], marker=True, icon=bus_image)
active_markers_bus.append(marker_bus)
active_markers.append(marker)
map_widget.set_zoom(12)
map_widget.add_right_click_menu_command(label='Marker',command=add_marker_event, pass_coords=True)
map_widget.add_right_click_menu_command(label='Path',command=make_path, pass_coords=True)

root_tk.mainloop()