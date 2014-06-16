class StackUnderFlow(Exception): pass
class StackOverFlow(Exception): pass

class Stack(object):
    def __init__(self):
        import threading

        self._stack = []
        self._lock = threading.RLock()

    def pop(self):
        with self._lock:
            try:
                return self._stack.pop()
            except IndexError:
                raise StackUnderFlow()

    def push(self,item):
        with self._lock:
            self._stack.append(item)

    def size(self):
        with self._lock:
            return len(self._stack)