

from irequest import APIRequest


class Midjourney():
    def __init__(self, api_key, callback_uri):
        self.api_request = APIRequest(api_key, callback_uri)

    def imagine(self, prompt):
        return self.api_request.imagine(prompt)

    def result(self, seed):
        return self.api_request.get_result(seed)

    def upscale(self, task_id, position):
        return self.api_request.upscale_image(task_id, position)

    def seed(self, callback_uri):
        return self.api_request.seed(callback_uri)

    def describe(self, image):
        return self.api_request.describe_image(image)
