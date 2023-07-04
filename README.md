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

### Using the RESULT API

```python

from pymidjourney import Midjourney


midjourney = Midjourney(
    api_key="API_KEY", callback_uri="")

result = midjourney.result(seed="seed")
if result.get('status') == 'completed':
    response = result
    print(response)
else:
    message = result.get('message')
    print(message)


```

### Using the UPSCALE API

```python
from pymidjourney import Midjourney

midjourney = Midjourney(
    api_key="API_KEY", callback_uri="")

seed = midjourney.upscale(
    task_id="the_task_id", position=2)

result = midjourney.result(seed=seed)
if result.get('status') == 'completed':
    response = result
    print(response)
else:
    message = result.get('message')
    print(message)

```

### Using the VARIANTION API

```python
from pymidjourney import Midjourney

midjourney = Midjourney(
    api_key="AI_KEY", callback_uri="")

variantions = midjourney.variants(jobId="xxxxxxxxxxxxxxxx",
        messageId="xxxxxxxxxxxxxxxx", position=1)

print(variantions)
```
