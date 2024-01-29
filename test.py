import httpx

base_url = 'https://parsinger.ru/3.3/1/'


for page_number in range(1, 201):
    response = httpx.get(base_url + str(page_number) + '.html')
    if response.status_code == 200:
        print(response.text)
