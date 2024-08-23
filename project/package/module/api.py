import requests

def get_pokemon_data(url: str) -> dict:

    # Make the GET request
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        return data
    else:
        raise Exception('Failed to retrieve data')
    
    
if __name__ == '__main__':
    data = get_pokemon_data('https://pokeapi.co/api/v2/pokemon/ditto')
    print(data)