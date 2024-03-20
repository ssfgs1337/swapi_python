import swapi

film_id = input('Введіть номер фільму: ')

if film_id.isdigit():
    film = swapi.get_film(int(film_id))
    if film:
        print(f"Фільм: {film.title}\n")
        
        print("Персонажі:")
        for i, character in enumerate(film.get_characters().items, 1):
            homeworld = swapi.get_planet(character.homeworld.split('/')[-2])
            print(f"{i}. {character.name} з планети {homeworld.name}")
        
        print("\nТранспортні засоби:")
        for i, vehicle in enumerate(film.get_vehicles().items, 1):
            print(f"{i}. {vehicle.name}")
        
        print("\nКосмічні кораблі:")
        for i, starship in enumerate(film.get_starships().items, 1):
            print(f"{i}. {starship.name}")
        
        print("\nВиди істот:")
        for i, specie in enumerate(film.get_species().items, 1):
            print(f"{i}. {specie.name}")
    else:
        print('Фільм не знайдено')
else:
    print('Номер фільму має бути числом')
