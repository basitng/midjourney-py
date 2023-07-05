from typing import Dict
import time
from midjourney.irequest import APIRequest


class Midjourney:
    def __init__(self, api_key: str, callback_uri: str):
        self.api_request = APIRequest(api_key, callback_uri)

    def result(self, seed: Dict) -> Dict:
        task_id = seed.get('taskId')

        if not task_id:
            return {'status': 'error', 'message': 'Invalid seed data'}

        print("Running task....")
        while True:
            try:
                response = self.api_request.get_result(task_id)
            except Exception as e:
                return {'status': 'error', 'message': str(e)}

            if response and isinstance(response, dict):
                if 'imageURL' in response:
                    print("Completed task....")
                    return {'status': 'completed', 'imageUrl': response['imageURL']}
                elif 'seed' in response:
                    print("Completed task....")
                    return {'status': 'completed', 'seed': response['seed']}
                elif 'content' in response:
                    print("Completed task....")
                    return {'status': 'completed', 'content': response['content']}
                elif response.get('status') == 'running':
                    percentage = response.get('percentage')
                    print(f"Task is {percentage}% complete.")
                elif response.get('status') in ['pending', 'waiting-to-start', 'unknown', {}, 'failed-please-resubmit']:
                    print("Task is pending. Waiting for it to start...")
                    time.sleep(2)
                    continue
            else:
                print("Waiting for task to start...")
                time.sleep(2)
                continue

            if response.get('status') not in ['running', 'pending', 'unknown']:
                break

    def imagine(self, prompt: str) -> Dict:
        return self.api_request.imagine(prompt)

    def upscale(self, task_id: str, position: str) -> Dict:
        return self.api_request.upscale_image(task_id, position)

    def seed(self, task_id: str) -> Dict:
        return self.api_request.seed(task_id)

    def describe(self, image_path: str, filename: str) -> Dict:
        return self.api_request.describe_image(image_file_path=image_path, filename=filename)
