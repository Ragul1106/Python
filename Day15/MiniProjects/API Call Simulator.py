import random
import time
import logging

logging.basicConfig(filename='api_calls.log', level=logging.ERROR)

class InvalidResponseError(Exception):
    pass

def simulate_api_call():
    max_retries = 3
    attempts = 0
    
    while attempts < max_retries:
        try:
            attempts += 1
            print(f"Attempt {attempts} of {max_retries}")
            
            # Simulate random failures
            if random.random() < 0.6:  # 60% chance of failure
                if random.random() < 0.5:
                    raise ConnectionError("Connection timeout")
                else:
                    raise InvalidResponseError("Invalid API response")
            
            # Successful response
            return {"status": "success", "data": "API response data"}
            
        except ConnectionError as e:
            logging.error(f"Attempt {attempts}: {e}")
            print(f"Connection error, retrying...")
            time.sleep(1)
        except InvalidResponseError as e:
            logging.error(f"Attempt {attempts}: {e}")
            print(f"Invalid response, retrying...")
            time.sleep(1)
    else:
        logging.error("Max retries reached")
        raise Exception("API call failed after max retries")

try:
    response = simulate_api_call()
    print("API call successful:", response)
except Exception as e:
    print("Error:", e)