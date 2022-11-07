def gamecountry():
    dic = {"Ukraine": "Kyiv", "Japan": "Tokyo", "Germany": "Berlin", "Poland": "Warsaw", "Canada": "Ottawa",
           "Austria": "Vienna", "Brazil": "Brasilia", "China": "Beijing", "Finland": "Helsinki", "Greece": "Athens"}
    print("If u want to stop game, enter: 'stop'.")
    while True:
        ask = input("Enter capital of country: ")
        if ask == 'stop':
            break
        try:
            key_list = list(dic.keys())
            val_list = list(dic.values())
            position = val_list.index(ask)
            print(key_list[position])
        except:
            print("unfortunately it is not the capital")
