import random
import requests

POKEMON_LIST = ["pikachu", "charmander", "bulbasaur", "squirtle", "eevee", "snorlax"]


def get_pokemon(name):
    """Fetch a Pokémon from PokeAPI. Returns a dict, or None on failure."""
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException:
        print("Network error. Please check your connection.")
        return None

    if response.status_code == 404:
        print(f"'{name}' is not a valid Pokémon name.")
        return None
    if response.status_code != 200:
        print(f"Request failed (status {response.status_code}).")
        return None

    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
    }


def play_game():
    answer = get_pokemon(random.choice(POKEMON_LIST))
    if answer is None:
        return

    print("Who's that Pokémon?")
    print(f"Height: {answer['height']} | Weight: {answer['weight']}")

    attempts = 0
    while attempts < 3:
        guess = input(f"Attempt {attempts + 1}/3: ").strip().lower()

        if not guess:
            print("Please type a name.")
            continue

      
        if get_pokemon(guess) is None:
            continue

        attempts += 1
        if guess == answer["name"]:
            print(f"Correct! It's {answer['name'].capitalize()}!")
            return
        print("Wrong guess.")

    print(f"Out of attempts! It was {answer['name'].capitalize()}.")


if __name__ == "__main__":
    play_game()