posts = ['Product Launch', 'Weekly Update']

def add_post():
    post = input("Post content: ")
    posts.append(post)
    print("Post scheduled")

def add_priority_post():
    post = input("Priority post: ")
    posts.insert(0, post)
    print("Priority post added")

def publish_post():
    if posts:
        published = posts.pop(0)
        print(f"Published: {published}")
    else:
        print("No posts to publish")
add_post()
add_priority_post()
publish_post()