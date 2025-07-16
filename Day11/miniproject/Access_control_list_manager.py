admin = {'view', 'edit', 'delete', 'settings'}
editor = {'view', 'edit'}
viewer = {'view'}

print("Editor permissions subset of admin?", editor <= admin)
print("Admin has all viewer permissions?", admin >= viewer)
print("No overlap between editor and viewer?", editor.isdisjoint(viewer))