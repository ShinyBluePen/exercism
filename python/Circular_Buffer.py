"""Circular Buffer

https://exercism.org/tracks/python/exercises/circular-buffer
"""

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    :param BufferError: str - Explanation of the error.
    """
    def __init__(self, message):
        self.message = message

class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.
    
    :param BufferError: str - Explanation of the error.
    """
    def __init__(self, message):
        self.message = message

class CircularBuffer:
    """Representation of a circular buffer.

    Parameters:
    :param capacity: int - The size of the buffer.
    
    Attributes:
    :capacity: list[str] - The total number of items of data which can fit in the buffer.
    :position: int - The current position of the buffer "pointer".
    :entries: int - The current number of data items in the buffer.

    Methods:
    :read(): - Return the oldest written data from the buffer.
    :write(data): - Save data into the buffer without overwriting.
    :overwrite(data): - Save data into the buffer, overwriting oldest values first.
    :clear(): - Remove all data from the buffer.

    Raises:
    :BufferEmptyException: - If trying to read from an empty buffer.
    :BufferFullException: - If trying to write to a full buffer.
    """
    def __init__(self, capacity: int) -> None:
        self.capacity = ["" for i in range(capacity)] # [""] * capacity
        self.position = 0
        self.entries = 0

    def read(self) -> list:
        if not self.entries:
            raise BufferEmptyException("Circular buffer is empty")
            
        out = self.capacity[self.position - self.entries]
        self.capacity[self.position - self.entries] = ""
        self.entries -= 1

        return out

    def write(self, data: str) -> None:
        if self.entries == len(self.capacity):
            raise BufferFullException("Circular buffer is full")

        self.capacity[self.position] = data
        self.position = (self.position + 1) % len(self.capacity)
        self.entries += 1
        
    def overwrite(self, data: str) -> None:
        # no data present, so just do a normal write
        if not self.capacity[self.position]:
            self.write(data)
        # data present and will be overwritten: self.entries does not increment
        else:
            self.capacity[self.position] = data
            self.position = (self.position + 1) % len(self.capacity)

    def clear(self) -> None:
        self.capacity = ["" for i in range(len(self.capacity))]
        self.entries = 0
