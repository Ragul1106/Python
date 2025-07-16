skus = ['SKU1', 'SKU2', 'SKU1', 'SKU3']
unique_skus = set(skus)

if len(skus) != len(unique_skus):
    print(f"Found {len(skus) - len(unique_skus)} duplicates")