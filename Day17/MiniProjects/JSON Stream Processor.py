import json

def json_stream_reader(filename, stop_key=None):
    with open(filename) as file:
        for line in file:
            try:
                data = json.loads(line)
                if stop_key and stop_key in data:
                    raise StopIteration(f"Stop key '{stop_key}' found")
                yield data
            except json.JSONDecodeError:
                continue

# for obj in json_stream_reader('data.jsonl', stop_key='terminate'):
#     print(obj)