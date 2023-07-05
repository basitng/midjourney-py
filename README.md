# PyMidjourney

PyMidjourney library provides a simplified and convenient way for developers to interact with the Midjourney API. With this library, developers can easily integrate Midjourney's powerful image processing capabilities into their applications without dealing with the complexities of manual API calls.

## Key Features

1. _Simplified Interface_: The APIRequest class abstracts away the complexities of API
2. _Authentication Handling_: he library handles the authentication process, ensuring that API requests are properly authenticated with the provided API key.
3. _Endpoint Methods_: The library provides intuitive methods for each API endpoint, making it easy to perform actions such as describing images, retrieving results, upscaling images, generating images based on prompts, and generating seeds for image generation.
4. _Response Handling_: The library processes API responses and provides them in a structured format, simplifying the integration of API results into the application workflow.

### Using the Imagine API

```python

from pymidjourney import Midjourney

midjourney = Midjourney(
    api_key="API_KEY", callback_uri="")

# IMAGINE
seed = midjourney.imagine(prompt='cute mouse with hats')

result = midjourney.result(seed=seed)
if result.get('status') == 'completed':
    response = result
    print(response)
else:
    message = result.get('message')
    print(message)

```

### Using the Describe API

Describe images using the describe api from midjourney

```python

from pymidjourney import Midjourney


midjourney = Midjourney(
    api_key="API_KEY", callback_uri="")

seed = midjourney.describe(
    image_path=r"C:\Users\Basit Ng\Downloads\rabbit.png")

result = midjourney.result(seed=seed)
if result.get('status') == 'completed':
    response = result
    print(response)
else:
    message = result.get('message')
    print(message)


```

#### Describe response

```json
{
  "taskId": "task_id_generated"
}
```

when passed to the result method

```json
{
  "status": "completed",
  "content": [
    "1️⃣ four images of a lion lying in water, in the style of cinematic sets, fantasy characters, cinematic lighting, ray tracing, soggy, naturalistic bird portraits, strong facial expression ",
    "2️⃣ four different images of a lion sitting in the water, in the style of vray tracing, realistic, emotive portraits, bokeh, [noah bradley](https://goo.gl/search?artist%20noah%20bradley), fairy tale, photorealistic compositions, 8k ",
    "3️⃣ lion portraits in the water, in the style of [raphael lacoste](https://goo.gl/search?artist%20raphael%20lacoste), bokeh, detailed character expressions, [charles spencelayh](https://goo.gl/search?artist%20charles%20spencelayh), emotional and dramatic scenes, nature inspired, fawncore ",
    "4️⃣ the lion  lion photo editing, lion phototutorials, lionphotography, portrait photography, animal photography, lion photo, in the style of vray tracing, wet-on-wet blending, multi-panel compositions, rendered in cinema4d, 8k 3d, fairy tale, bokeh"
  ]
}
```

#### Imagine response

_Note_ the _task id_ generated will be passed to the result method to generate the imageUrl

```json
{
  "taskId": "your_task_id"
}
```

when passed to the result method

```json
{
  "status": "completed",
  "imageUrl": "https://cdn.discordapp.com/attachments/1124090271676772432/1126110757319360582/olivier_A_crying_white_kid_holding_a_blue_candy_splash_around_h_5b0a4099-f398-4118-8206-33f64c1a5589.png"
}
```

### Using the RESULT API

```python

from pymidjourney import Midjourney


midjourney = Midjourney(
    api_key="API_KEY", callback_uri="")

seed = {
    "taskId": 'your_task_id',
}
result = midjourney.result(seed=seed)
if result.get('status') == 'completed':
    response = result
    print(response)
else:
    message = result.get('message')
    print(message)

```

#### Result response

```json
{
  "imageURL": "https://cdn.discordapp.com/attachments/1124090271676772432/1125924854990917713/njho_Lion_king_8k_ultra_reality_in_a_rainy_zone___4410563673654_de36ac34-3209-4940-ab10-7178305ca75f.png"
}
```

### Using the UPSCALE API

The response will contain the imageURL of the upscaled image.

```python
from pymidjourney import Midjourney

midjourney = Midjourney(
    api_key="API_KEY", callback_uri="")

upscale = midjourney.upscale(
    task_id="the_task_id", position="2")

print(upscale)

```

#### Upscale response

```json
{ "imageURL": "https://..........png" }
```

### Using the SEED API

```python
from pymidjourney import Midjourney

midjourney = Midjourney(
    api_key="AI_KEY", callback_uri="")

seed = midjourney.seed(task_id="the_task_id")

print(seed)
```

#### Seed response

```json
{ "taskId": "https://..........png" }
```
