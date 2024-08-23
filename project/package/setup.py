from project.package.module.api import get_pokemon_data


if __name__ == '__main__':
    # Define the URL for the API request
    url = 'https://pokeapi.co/api/v2/pokemon/ditto'

    pokemon_data = get_pokemon_data(url)