# This project covers some concepts on pagination:
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner


# Tasks

## 0. [Simple helper function](./0-simple_helper_function.py)

Write a function named ```index_range``` that takes two integer arguments ```page``` and ```page_size```.

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

- Page numbers are 1-indexed, i.e. the first page is page 1.
```
bob@dylan:~$ ./0-main.py
<class 'tuple'>
(0, 7)
<class 'tuple'>
(30, 45)
bob@dylan:~$
```