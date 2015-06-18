# CSC148 Exercise 5
# Joshua Fung June 17th,2015
class DLLNode(object):
    '''A class for a double linked list node
    Contain data, prev_node, and next_node
    
    If no node is provided it will set them as None
    '''

    def __init__(self, data, prev_node = None, next_node = None):
        '''(Object, DLLNode, DLLNode) -> NoType
        
        Data must be prvided, node will be set to None if not provided
        '''
        #I would like data, pre_node and next_node as a private variable
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


class EmptyListError(Exception):
    '''Raise this error when list is empty'''

    
class DLList(object):
    '''Double linked list

    Initialized empty
    
    Method:
    add_to_head
    add_to_tail
    remove_head
    remove_tail
    search
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

        while(current != None):
            list_content = list_content + str(current.get_data())
            list_content = list_content + " (" + str(current.get_prev())
            list_content = list_content + ", " + str(current.get_next()) + ") -> "
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
            
    def remove_tail(self):
        '''(NoType) -> Object

        Return and remove object from tail
        '''
        if(self._head is None):
            raise EmptyListError

        else:
            
    def search(self, data):
        '''(Object) -> int

        Return the index of the search object
        If none return -1
        '''
        
        
