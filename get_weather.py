def weather(lat,lon):
    import requests
    with open('api_key.txt', 'r+') as file:
        API_key = file.read()
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'

    try:
        response = requests.get(url).json()
        #print(response)
        data = [int(response['main']['temp']) - 273, response['weather'][0]['main'], response['wind']['speed']]
        we = f'\nТемпература: {data[0]} градусов\n\n Состояние: {data[1]}\n\n Ск. ветра: {data[2]} м/c'
    except:
        we = f'\nТемпература: ~ градусов\n\n Состояние: ~\n\n Ск. ветра: ~ м/c'
    return we

