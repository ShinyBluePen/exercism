"""Inventory Management

https://exercism.org/tracks/python/exercises/inventory-management
"""

def create_inventory(items: list[str]) -> dict:
    """

    :param items: list[str] - List of items to create an inventory from.
    :return: dict - The inventory dictionary.
    """
    inventory = {}

    for item in items:
        if item not in inventory:
            inventory.update({item: 1})
        else:
            inventory[item] += 1
            
    return inventory

def add_items(inventory: dict, items: list[str]) -> dict:
    """

    :param inventory: dict - Dictionary of existing inventory.
    :param items: list[str] - List of items to update the inventory with.
    :return:  dict - The inventory dictionary updated with the new items.
    """

    for item in items:
        if item not in inventory:
            inventory.update({item: 1})
        else:
            inventory[item] += 1

    return inventory

def decrement_items(inventory: dict, items: list[str]) -> dict:
    """

    :param inventory: dict - Inventory dictionary.
    :param items: list[str] - List of items to decrement from the inventory.
    :return:  dict - Updated inventory dictionary with items decremented.
    """

    for item in items:
        if item in inventory and inventory[item] != 0:
            inventory[item] -= 1

    return inventory

def remove_item(inventory: dict, item: str) -> dict:
    """
    
    :param inventory: dict - Inventory dictionary.
    :param item: str - Item to remove from the inventory.
    :return:  dict - Updated inventory dictionary with item removed.
    """
    
    if item in inventory:
        del inventory[item]

    return inventory

def list_inventory(inventory: dict) -> list[tuple[str, int]]:
    """

    :param inventory: dict - An inventory dictionary.
    :return: list[tuple[str, int]] - List of key, value pairs from the inventory dictionary.
    """

    return [(k, v) for k, v in inventory.items() if v != 0]
