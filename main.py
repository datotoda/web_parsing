import requests
from bs4 import BeautifulSoup

import csv
from random import uniform
from time import sleep, time


def get_random_time():
    return uniform(15, 20)


url = 'https://store.edison.ge/product-category/'

category_list = {
    'modules and sensors': 'modulesensor',
    'electronic components': 'electronic-components',
    'chargers': 'chargers',
    'chips': 'მიკროსქემები',
    'tools': 'tools'
}

while True:
    inp = input('Choose one:\n\t' + '\n\t'.join(category_list) + '\n> ')
    if inp in category_list:
        cat = category_list[inp]
        break
    print('\nWrong input!\n')

response = requests.get(url + f'{cat}/')
soup = BeautifulSoup(response.text, 'html.parser')
max_pages = int(soup.find(class_='electro-advanced-pagination').text.split()[1][:-1])
print('\n')

while True:
    pages = input(f'How many pages do you want? (1 to {max_pages}):\n> ')
    if pages.isdigit() and int(pages) <= max_pages:
        pages = int(pages)
        break
    print('\nWrong input!\n')

print(f'Estimated sleep time: {(pages - 1) * get_random_time():.2f} s')
start_time = time()

with open('database.csv', 'w', encoding='utf-8_sig', newline='\n') as file:
    csv_obj = csv.writer(file)
    csv_obj.writerow(["Title", "Price", "Category", "Image url"])

    for i in range(1, pages + 1):
        if i != 1:
            sleep_start_time = time()
            print(f'Start sleep')
            sleep(get_random_time())
            print(f'End sleep in {time() - sleep_start_time:.2f}')

        loop_start_time = time()
        response = requests.get(url + f'{cat}/page/{i}/')
        soup = BeautifulSoup(response.text, 'html.parser')

        all_components = soup.find('ul', class_='products').find_all('li')
        for item in all_components:
            inner_div = item.find('div', classs_='product-item__inner')

            title = item.find('h2', class_='woocommerce-loop-product__title').text
            price = item.find('span', class_='electro-price').text
            image_url = item.img.attrs.get('src')
            category = item.find('span', class_='loop-product-categories').a.text

            if price:
                price = float(price.split(chr(160))[0].replace(',', '.'))  # აქ გამოყენებული აქვთ chr(160) სიმბოლო
            else:
                price = 0

            csv_obj.writerow([title, price, category, image_url])

        print(f'Page N-{i} parsed in {time() - loop_start_time:.2f} s')

print('-' * 40)
print(f'Successfully completed in {time() - start_time:.2f} seconds')
