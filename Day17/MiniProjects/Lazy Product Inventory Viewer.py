def inventory_viewer(products, page_size=5):
    page = 0
    while True:
        start = page * page_size
        batch = products[start:start+page_size]
        if not batch:
            raise StopIteration("End of inventory")
        for product in batch:
            yield product
        page += 1
        yield "--- Next Page ---"

products = [{"id": i, "name": f"Product {i}", "stock": i%3} for i in range(1, 21)]
viewer = inventory_viewer(products)

in_stock = (p for p in viewer if p.get("stock", 0) > 0)

for _ in range(15):  
    print(next(in_stock))