class ContainerFullException(Exception):
    """ """

    
class ContainerEmptyException(Exception):
    """ """

    
class MyQueue(object):
    """A test container as a queue"""
    def __init__(self):
        """
        """
        self._queue = []

    def __str__(self):
        """
        """
        return str(self._queue)

    def __eq__(self, other):
        """
        """
        return self._queue == other._queue

    def put(self, obj):
        """
        """
        self._queue.insert(0, obj)
        
    def get(self):
        """
        """
        try:
            return self._queue.pop()
        except IndexError:
            raise ContainerEmptyException
        
    def peek(self):
        """
        """
        try:
            return self._queue[-1]
        except IndexError:
            raise ContainerEmptyException
        
    def is_empty(self):
        """
        """
        return self._queue == []

    def copy(self):
        """
        """
        new_queue = MyQueue()
        new_queue._queue = self._queue.copy()
        return new_queue

class MyBucket(object):
    """A test container as a queue"""
    def __init__(self):
        """
        """
        self._bucket = []

    def __str__(self):
        """
        """
        return str(self._bucket)

    def __eq__(self, other):
        """
        """
        return self._bucket == other._bucket

    def put(self, obj):
        """
        """
        if(self._bucket == []):
            self._bucket.insert(0, obj)
        else:
            raise ContainerFullException
        
    def get(self):
        """
        """
        try:
            return self._bucket.pop()
        except IndexError:
            raise ContainerEmptyException
        
    def peek(self):
        """
        """
        try:
            return self._bucket[0]
        except IndexError:
            raise ContainerEmptyException
        
    def is_empty(self):
        """
        """
        return self._bucket == []

    def copy(self):
        """
        """
        new_bucket = MyBucket()
        new_bucket._bucket = self._bucket.copy()
        return new_bucket
    
