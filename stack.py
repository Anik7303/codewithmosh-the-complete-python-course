"""
Python implementaion of Stack [LIFO - Last In First Out]
"""


class Stack:
    _list = []

    def push(self, data):
        """Push an item at the top of stack

        Args:
            data ([any]): The data to be put in stack, can be any type of data
        """
        self._list.append(data)

    def pop(self):
        """Remove the last entered data from stack

        Returns:
            [any]: The removed data from stack
        """
        return self._list.pop()

    def top(self):
        """Fetch the top value the stack

        Returns:
            [any]: The value at the top of stack
        """
        # return self._list[-1] if len(self._list) > 0 else None
        return self._list[-1] if not self._list else None

    def clear(self):
        """Empties the stack
        """
        self._list.clear()
