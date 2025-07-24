def data_producer():
    for i in range(100):
        yield {"raw": i}

def data_filter(source):
    for item in source:
        if item["raw"] % 2 == 0:  
            yield item

def data_transformer(source):
    for item in source:
        item["processed"] = item["raw"] * 10
        yield item

pipeline = data_transformer(data_filter(data_producer()))

for i, result in enumerate(pipeline):
    print(result)
    if i >= 5:  
        break