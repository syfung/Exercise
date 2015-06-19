# CSC148 Exercise 5
# Joshua Fung June 17th,2015


class DLLNode(object):
    '''A class for a double linked list node
    Contain data, prev_node, and next_node
    If no node is provided it will set them as None
    '''

    def __init__(self, data, prev_node=None, next_node=None):
        '''(Object, DLLNode, DLLNode) -> NoType
        Data must be prvided, node will be set to None if not provided
        '''
        # I would like data, pre_node and next_node as a private variable
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __str__(self):
        '''(NoType) -> str
        Print the data when printed
        '''
        return str(self.data)

    def get_data(self):
        '''(NoType) -> object
        Return data
        '''
        return self.data

    def get_prev(self):
        '''(NoType) -> DLLNode
        Return prev_node
        '''
        return self.prev_node

    def get_next(self):
        '''(NoType) -> DLLNode
        Return next_node
        '''
        return self.next_node

    def change_prev(self, prev_node):
        '''(NoType) -> NoType
        Change prev_node
        '''
        self.prev_node = prev_node

    def change_next(self, next_node):
        '''(NoType) -> NoType
        Change next_node
        '''
        self.next_node = next_node


class DLList(object):
    '''Double linked list class, also used for a sorted list
    Initialized empty

    Method:
    add_to_head
    add_to_tail
    remove_head
    remove_tail
    search
    count
    sorted_add
    remove_item
    '''

    def __init__(self):
        '''(NoType) -> NoType
        Init a empty list
        '''
        self._head = None

    def __str__(self):
        '''(NoType) -> str
        Print the whole list
        '''
        list_content = ""
        current = self._head

        while(current is not None):
            list_content = list_content + str(current.get_data())
            list_content = list_content + " (" + str(current.get_prev())
            list_content = list_content + ", " + str(current.get_next())
            list_content = list_content + ") -> "
            current = current.get_next()

        list_content = list_content + "None"
        return list_content

    def add_to_head(self, data):
        '''(Object) -> NoType
        Add an object to the head
        '''
        if(self._head is None):
            self._head = DLLNode(data)

        else:
            new_node = DLLNode(data, None, self._head)
            if(self._head is not None):
                self._head.change_prev(new_node)
            self._head = new_node

    def add_to_tail(self, data):
        '''(Object) -> NoType
        Add an object to the tail
        '''
        if(self._head is None):
            self._head = DLLNode(data)

        else:
            current = self._head
            while(current.get_next() is not None):
                current = current.get_next()

            current.change_next(DLLNode(data, current, None))

    def remove_head(self):
        '''(NoType) -> Object
        Return and remove object from head
        '''
        if(self._head is None):
            raise EmptyListError

        else:
            head = self._head
            data = self._head.get_data()
            self._head = head.get_next()

            if(self._head is not None):
                self._head.change_prev(None)

            del head
            return data

    def remove_tail(self):
        '''(NoType) -> Object
        Return and remove object from tail
        '''
        if(self._head is None):
            raise EmptyListError

        else:
            current = self._head
            if(current.get_next() is None):
                data = current.get_data()
                del current
                self._head = None

            else:
                while(current.get_next() is not None):
                    current = current.get_next()

                data = current.get_data()
                current.get_prev().change_next(None)
                del current

            return data

    def search(self, data):
        '''(Object) -> int
        Return the index of the search object
        If none return -1
        '''
        counter = 0
        current = self._head

        while(current is not None):

            if(current.get_data() == data):
                return counter

            else:
                current = current.get_next()
                counter = counter + 1

        return -1

    def count(self):
        '''(NoType) -> int
        Count the list
        '''
        return self._rec_count(self._head)

    def _rec_count(self, head):
        '''(DLLNode) -> int
        Recursively count the list
        '''
        if(head is not None):
            return 1 + self._rec_count(head.get_next())

        else:
            return 0

    def getitem(self, index):
        '''(int) -> Object
        Return the object at given index
        '''
        if(index > self.count()):
            raise IndexOutOfBoundError("Index is longer than list")

        return self._rec_getitem(index, self._head)

    def _rec_getitem(self, index, node):
        '''(int) -> Object
        Recursively return the object at given index
        '''
        if(index < 1):
            return node.get_data()

        else:
            return self._rec_getitem(index - 1, node.get_next())

    def sorted_add(self, data):
        '''(Object) -> NoType
        Add the data in non-decreasing order
        '''
        if(self._head is None):
            self._head = DLLNode(data)

        if(self._head.get_data() > data):
            self._head = DLLNode(data, None, self._head)
            self._head.get_next().change_prev(self._head)

        else:
            current = self._head
            while(current.get_data() <= data):
                if(current.get_next() is None):
                    new_node = DLLNode(data, current, None)
                    current.change_next(new_node)
                    return None
                current = current.get_next()

            new_node = DLLNode(data, current.get_prev(), current)
            if(current.get_prev() is not None):
                current.get_prev().change_next(new_node)
            current.change_prev(new_node)
        return None

    def remove_item(self, data):
        '''(Object) -> NoType
        Remove specfied data
        '''
        if(self._head is None):
            raise EmptyListError

        else:
            current = self._head
            if(current.get_data() == data):
                self._head = current.get_next()
                self._head.change_prev(None)
                del current
                return None
            
            while(current is not None):
                if(current.get_data() == data):
                    if(current.get_prev() is not None):
                        current.get_prev().change_next(current.get_next())

                    if(current.get_next() is not None):
                        current.get_next().change_prev(current.get_prev())

                    del current
                    return None

                else:
                    current = current.get_next()

            raise RemoveNonExistItemError


class EmptyListError(Exception):
    '''Raise this error when list is empty'''
    pass


class IndexOutOfBoundError(Exception):
    '''Raise this error when index is outside list'''
    pass


class RemoveNonExistItemError(Exception):
    '''Raise when attemp to remove a item that is not in the list'''
    pass


class SortedList(object):
    '''A sorted list class, in non-decreasing order'''

    def __init__(self):
        '''(NoType) -> NoType
        Init empty list
        '''
        self._list = DLList()

    def __str__(self):
        '''(NoType) -> str
        Print the whole list
        '''
        return str(self._list)

    def add(self, data):
        '''(Object) -> NoType
        Add data in a non-decreasing order
        '''
        self._list.sorted_add(data)
        
    def remove(self, data):
        '''(Object) -> NoType
        Remove the specified data out of the list
        '''
        self._list.remove_item(data)

    def middle(self):
        '''(NoType) -> Object
        Return the object in the middle of the list
        if even number return the one closer to the head
        '''
        # Count the total length of the list
        len = self._list.count()

        # Find the half length, add 0.5 to make it round properly
        half = (len / 2) + 0.5

        # Find the index
        index = int(half - 1)

        # Return the element at the index
        return self._list.getitem(index)
