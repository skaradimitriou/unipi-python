# challenge - Φερε 10 τελευταιες κληρωσεις και βγαλε στατιστικα

import requests

request = requests.get('https://api.opap.gr/draws/v3.0/1100/928694')
data = request.json()

lastDraw = data['drawId']
nums = data['winningNumbers']['list']


def get_draw(id):
    newRequest = requests.get('https://api.opap.gr/draws/v3.0/1100/' + str(id))
    data = newRequest.json()
    return data['winningNumbers']['list']

for i in range(5):
    nums += get_draw(lastDraw - 1 - i)

print(nums)

from matplotlib import pyplot as plt

# Figure Size
fig = plt.figure(figsize=(10, 7))

plt.title = "Hello"

# Horizontal Bar Plot
plt.bar(list(range(1, 81)), [nums.count(i) for i in range(1, 81)])
plt.show()