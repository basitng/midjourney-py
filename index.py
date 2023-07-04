
from pymidjourney import Midjourney

midjourney = Midjourney(
    api_key="20ceee09-37b4-46c8-9d70-7da99315212b", callback_uri="")

seed = midjourney.imagine(prompt='cute lion with hats')
print("🚀 ~ file: index.py:10 ~ seed:", seed)

result = midjourney.result(seed=seed)
print("🚀 ~ file: index.py:14 ~ result:", result)

if result.get('status') == 'completed':
    response = result
    print(response)
else:
    # Handle the case when the result is not completed or an error occurred
    message = result.get('message')
    print(message)
