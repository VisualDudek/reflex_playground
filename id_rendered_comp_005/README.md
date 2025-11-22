# Identifying Rendered Components in the Browser

- add `id="str"` kward to rx component and next inspect web page
- try to find kwarg that act as parameter (on given rx.component) and find according docs e.g. 
```python
rx.vstack(
    ...
    spacing="5",
    justify="center",
    min_height="85vh",
)
```