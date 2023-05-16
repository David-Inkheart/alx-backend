# This project covers different caching algorithms:
- Cache replacement policies like FIFO, LIFO, LRU, MRU, LFU
- The  purpose of a caching system and its limits

### Parent Class `BaseCaching`
All your classes must inherit from `BaseCaching`:

# Tasks

**[0. Basic dictionary](./0-basic_cache.py)**

Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system:
- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- This caching system doesn’t have limit
- def put(self, key, item):
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`
    - If `key` or `item` is `None`, this method should not do anything
- def get(self, key):
    - Must return the value in `self.cache_data` linked to `key`
    - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/0x01$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
guillaume@ubuntu:~/0x01$ 
```

**[1. FIFO caching](./1-fifo_cache.py)**

Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system:
- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`
    - If `key` or `item` is `None`, this method should not do anything
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        - must discard the first item put in cache (FIFO algorithm)
        - must print `DISCARD:` with the `KEY` discarded and following by a new line
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`
    - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/0x01$ ./1-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
guillaume@ubuntu:~/0x01$ 
```

**[2. LIFO Caching](./2-lifo_cache.py)**

Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system:
- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`
    - If `key` or `item` is `None`, this method should not do anything
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        - must discard the last item put in cache (LIFO algorithm)
        - must print `DISCARD:` with the `KEY` discarded and following by a new line
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`
    - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/0x01$ ./2-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: D
Current cache:
A: Hello
B: World
C: Holberton
E: Battery
Current cache:
A: Hello
B: World
C: Street
E: Battery
DISCARD: C
Current cache:
A: Hello
B: World
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
B: World
E: Battery
G: San Francisco
guillaume@ubuntu:~/0x01$ 
```

**[3. LRU Caching](./3-lru_cache.py)**
Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system:
- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`
    - If `key` or `item` is `None`, this method should not do anything
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        - must discard the least recently used item (LRU algorithm)
        - must print `DISCARD:` with the `KEY` discarded and following by a new line
- def get(self, key):
    - Must return the value in `self.cache_data` linked to `key`
    - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/0x01$ ./3-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: B
Current cache:
C: Street
F: Mission
G: San Francisco
H: H
DISCARD: C
Current cache:
F: Mission
G: San Francisco
H: H
I: I
DISCARD: F
Current cache:
G: San Francisco
H: H
I: I
J: J
DISCARD: G
Current cache:
H: H
I: I
J: J
K: K
guillaume@ubuntu:~/0x01$ 
```

**[4. MRU Caching](./4-mru_cache.py)**

Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system:
- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`
    - If `key` or `item` is `None`, this method should not do anything
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        - must discard the most recently used item (MRU algorithm)
        - must print `DISCARD:` with the `KEY` discarded and following by a new line
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`
    - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/0x01$ ./4-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: B
Current cache:
A: Hello
C: Holberton
D: School
E: Battery
Current cache:
A: Hello
C: Street
D: School
E: Battery
Hello
None
Street
DISCARD: C
Current cache:
A: Hello
D: School
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
D: School
E: Battery
G: San Francisco
DISCARD: G
Current cache:
A: Hello
D: School
E: Battery
H: H
DISCARD: H
Current cache:
A: Hello
D: School
E: Battery
I: I
DISCARD: I
Current cache:
A: Hello
D: School
E: Battery
J: J
DISCARD: J
Current cache:
A: Hello
D: School
E: Battery
K: K
guillaume@ubuntu:~/0x01$ 
```

**[5. LFU Caching](./100-lfu_cache.py)**

Create a class `LFUCache` that inherits from `BaseCaching` and is a caching system:
- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`
- `def put(self, key, item):`
    - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`
    - If `key` or `item` is `None`, this method should not do anything
    - If the number of items in `self.cache_data` is higher that `BaseCaching.MAX_ITEMS`:
        - must discard the least frequently used item (LFU algorithm)
        - must print `DISCARD:` with the `KEY` discarded and following by a new line
- `def get(self, key):`
    - Must return the value in `self.cache_data` linked to `key`
    - If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

```
guillaume@ubuntu:~/0x01$ ./100-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: F
Current cache:
B: World
C: Street
G: San Francisco
H: H
DISCARD: G
Current cache:
B: World
C: Street
H: H
I: I
I
H
I
H
I
H
DISCARD: B
Current cache:
C: Street
H: H
I: I
J: J
DISCARD: J
Current cache:
C: Street
H: H
I: I
K: K
DISCARD: K
Current cache:
C: Street
H: H
I: I
L: L
DISCARD: L
Current cache:
C: Street
H: H
I: I
M: M
guillaume@ubuntu:~/0x01$ 
```

```
In order to implement the LFUCache class, I used the following logic:

In the __init__ method, I called the constructor of the parent class (BaseCaching) and initialized additional data structures. I used an OrderedDict called cache_data to store the key-value pairs in the cache, and a defaultdict called item_freq to store the frequency of each item.

In the put method, I first checked if the key or item is None. If either of them is None, I returned without performing any operation.

If the key already exists in the cache (cache_data), I updated the item value and increased its frequency. To maintain the LFU property, I moved the item to the end of the cache by calling the update_cache_order method.

If the cache is full (the number of items in cache_data is greater than or equal to MAX_ITEMS), I needed to discard the least frequently used item(s). To determine the least frequent item(s), I found the minimum frequency in item_freq and identified the items with that frequency. If there were multiple items with the minimum frequency, I used the LRU (Least Recently Used) tiebreaker to choose the item to discard. I removed the LFU item from both item_freq and cache_data and printed a message indicating the discarded key.

Finally, if the key is not already in the cache, I checked if the cache is full. If it is, I followed the same procedure as mentioned above to discard the least frequent item(s). Then, I added the new item to the cache with a frequency of 1.

In the get method, I first checked if the key is None or if it doesn't exist in the cache. In such cases, I returned None. Otherwise, I increased the frequency of the accessed item, updated its position in the cache using update_cache_order, and returned its value.

By implementing the above logic, the LFUCache class effectively maintains a cache based on the LFU algorithm and handles the eviction of least frequently used items, using LRU tiebreaker if needed.
```