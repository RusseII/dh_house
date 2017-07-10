import requests
r = requests.get(
    "http://api.wunderground.com/api/0dae8a759154fd46/conditions/q/OH/stow.json")


if __name__ == '__main__':
    print(r.content)
