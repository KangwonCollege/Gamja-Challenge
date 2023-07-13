

class PointerQueue:
    def __init__(self):
        self._pointer_value = []

    def _add_pointer(self, value) -> int:
        self._pointer_value.append(value)
        return len(self._pointer_value) - 1

    def _get_pointer(self, position: int) -> str:
        return self._pointer_value.pop(position)
