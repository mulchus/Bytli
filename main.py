from dotenv import load_dotenv
import requests
import os


def is_bitlink(token, bitlink):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    bitlink_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    response = requests.get(bitlink_url, headers=headers)
    return response.ok


def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    payload = {"long_url": url}
    shorten_url = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(shorten_url,
                             headers=headers, json=payload)
    response.raise_for_status() 
    return response.json()['id']


def count_clicks(token, bitlink):
    headers = {
        'Authorization': f'Bearer {token}'        
    }
    clicks_url = f'https://api-ssl.bitly.com/v4/bitlinks/'\
        f'{bitlink}/clicks/summary'
    response = requests.get(clicks_url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def main():
    load_dotenv()
    bitly_token = os.getenv("BITLY_TOKEN")

    user_input = input('Введите ссылку: ')
    if is_bitlink(bitly_token, user_input):
        try:
            clicks_count = count_clicks(bitly_token, user_input)
        except requests.exceptions.HTTPError:            
            print('Ошибка при попытке получить количество кликов на ссылке')
        else:
            print(f'По ссылке {user_input} перешли {clicks_count} раз(а)')
    else:
        try:
            bitlink = shorten_link(bitly_token, user_input)
        except requests.exceptions.HTTPError:
            print('Ошибка в ссылке')
        else:
            print('Битлинк: ', bitlink)


if __name__ == '__main__':
    main()
