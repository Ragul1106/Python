def order_processor(orders):
    processed = 0
    for order in orders:
        status = yield f"Processing order {order['id']}"
        if status == "pause":
            yield "PAUSED - send 'resume' to continue"
        processed += 1
    return f"Completed {processed} orders"

orders = [{"id": i, "items": i%3+1} for i in range(1, 6)]
processor = order_processor(orders)
next(processor)  

while True:
    try:
        cmd = input("Enter command (pause/resume/next): ")
        if cmd == "pause":
            print(processor.send("pause"))
        elif cmd == "resume":
            print(next(processor))
        else:
            print(next(processor))
    except StopIteration as e:
        print(e.value)
        break