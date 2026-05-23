class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = None
        self.tail = None        
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.updateOrder(key)
            return self.cache[key][1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.updateOrder(key, value=value)

    def updateOrder(self, key: int, value: int = None) -> None:
        if not self.cache: # If this is the first entry
            self.cache[key] = [None, value, None]
            self.head = key
            self.tail = key
            return
        
        if key in self.cache:
            if value is not None: # Update the value if one is supplied
                self.cache[key][1] = value
            if key == self.head:
                return

            prevKey = self.cache[key][0]
            nextKey = self.cache[key][2]
            if prevKey is not None: # If this is some middle entry
                self.cache[prevKey][2] = nextKey
            else: # If this is the head
                pass
            if nextKey is not None: # If this is some middle entry
                self.cache[nextKey][0] = prevKey
            else: # If this is the tail
                if prevKey is not None: # only if theres more than one entry in cache
                    self.tail = prevKey
                else: # The tail should already be correct if theres only a single other entry in cache
                    pass
        else:
            self.cache[key] = [None, value, self.head]

        # Here's where we update the head
        if self.head is not None and self.head != key:
            self.cache[self.head][0] = key # set the current head's prev to the key
            self.cache[key][0] = None
            self.cache[key][2] = self.head # set the key's next to the current head
        
        self.head = key # This will ALWAYS be the case

        # Eliminate objects
        while len(self.cache) > self.capacity:
            prevKey = self.cache[self.tail][0]
            if prevKey is not None: # If there is actually something before the tail
                self.cache[prevKey][2] = None
            del self.cache[self.tail] # Delete the object
            self.tail = prevKey
