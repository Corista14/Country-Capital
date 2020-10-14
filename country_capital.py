import requests


def formatResponse(capital):
    try:
        country_name = capital[0]['name'].capitalize()
        capital = capital[0]["capital"]
        return f'The capital of {country_name} is {capital}.'
    except:
        return 'Invalid country.'


def getCapital(country):
    API_URL = f'https://restcountries.eu/rest/v2/name/{country}'
    response = requests.get(API_URL)
    capital = response.json()
    print(formatResponse(capital))


def main():
    userCountry = input('Insert the country: ')
    getCapital(userCountry)
    again()


def again():
    answer = input('Do you want to check another capital? (Y/N): ').upper()
    if answer == 'Y':
        main()
    elif answer == 'N':
        exit()
    else:
        print('Invalid answer, try again.')
        again()


main()
