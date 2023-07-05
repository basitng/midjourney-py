
from pymidjourney import Midjourney

midjourney = Midjourney(
    api_key="20ceee09-37b4-46c8-9d70-7da99315212b", callback_uri="")

# 4410563673654327
# seed = {
#     'taskId': '7017353063477976'
# }

seed = midjourney.imagine(
    prompt="A crying white kid holding a blue candy splash around his cute hoody, with blue eyes and curly blonde hair")
result = midjourney.result(seed=seed)
print("🚀 ~ file: index.py:15 ~ result:", result)

if result.get('status') == 'completed':
    response = result
    print(response)
else:
    # Handle the case when the result is not completed or an error occurred
    message = result.get('message')
    print(message)
