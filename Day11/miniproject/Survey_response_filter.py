responses = set()
invalid = set()

def add_response(id):
    responses.add(id)

def mark_invalid(id):
    if id in responses:
        responses.remove(id)
        invalid.add(id)
    else:
        print(f"ID {id} not found")

add_response(101)
add_response(102)
mark_invalid(101)
print("Valid responses:", responses)
print("Invalid responses:", invalid)