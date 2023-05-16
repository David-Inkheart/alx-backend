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