def add_item(inventory, item):
    if not item:
        raise ValueError
    elif len(inventory["items"]) >= inventory["capacity"]:
        raise ValueError
    elif inventory["locked"] == True:
        return inventory
    else:
        inventory["items"].append(item)
        return inventory

def remove_item(inventory, item):
    if inventory["locked"] == True:
        return inventory
    else:
        inventory["items"].remove(item)
        return inventory

def get_item_count(inventory):
    return len(inventory["items"])

