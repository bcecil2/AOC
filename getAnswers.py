import requests

url = "https://adventofcode.com/2020/day/6/input"

r = requests.get(url,cookies={"f":"53616c7465645f5fcfe85e97875d176d1eb86a280b393847671a4804e38eed5473ad8744d3a140de9262c0dadb97e5ac"})

open('tester.txt','wb').write(r.content)
