"""Chaitana's Colossal Coaster

https://exercism.org/tracks/python/exercises/chaitanas-colossal-coaster

TODO: (more accurate) type annotations in docstrings.  This will never happen.
"""
def add_me_to_the_queue(
    express_queue: list[str], 
    normal_queue: list[str], 
    ticket_type: int, 
    person_name: str
    ) -> list[str]:
    """

    :param express_queue: list - Names in the Fast-track queue.
    :param normal_queue:  list - Names in the normal queue.
    :param ticket_type:  int - Type of ticket. 1 = express, 0 = normal.
    :param person_name: str - Name of person to add to a queue.
    :return: list - The (updated) queue the name was added to.
    """
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue

    normal_queue.append(person_name)
    return normal_queue

def find_my_friend(queue: list[str], friend_name: str):
    """Return the index of `friend_name` or print "[no person]".

    :param queue: list - Names in the queue.
    :param friend_name: str - Name of friend to find.
    :return: int - Index at which the friends name was found.
    """
    if friend_name in queue:
        return queue.index(friend_name)
    else:
        print("No person with that name in this queue!")

def add_me_with_my_friends(queue: list[str], index: int, person_name: str) -> list[str]:
    """Insert `person_name` into the queue at the given `index`.

    :param queue: list - Names in the queue.
    :param index: int - The index at which to add the new name.
    :param person_name: str - The name to add.
    :return: list - Queue updated with new name.
    """
    queue.insert(index, person_name)

    return queue

def remove_the_mean_person(queue: list[str], person_name: str):
    """Return the queue with the given `person_name` removed, or print "[no person]".

    :param queue: list - Names in the queue.
    :param person_name: str - Name of mean person.
    :return:  list - Queue update with the mean persons name removed.
    """
    if person_name in queue:
        queue.remove(person_name)
        return queue
    else:
        print("No such person in this queue!")

def how_many_namefellows(queue: list[str], person_name: str) -> int:
    """Return how many time the given `person_name` appears in the queue.

    :param queue: list - Names in the queue.
    :param person_name: str - Name you wish to count or track.
    :return: int - The number of times the name appears in the queue.
    """
    return queue.count(person_name)

def remove_the_last_person(queue: list[str]) -> str:
    """Return the last individual in the queue.

    :param queue: list - Names in the queue.
    :return: str - Name that has been removed from the end of the queue.
    """
    return queue.pop(-1)

def sorted_names(queue: list[str]) -> list[str]:
    """Return the queue, sorted in alphabetical order.

    :param queue: list - Names in the queue.
    :return: list - Copy of the queue in alphabetical order.
    """
    return sorted(queue)
