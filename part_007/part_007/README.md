# Contact Form

- add contact page:
    - use decorator to register url
    - do not forget to add to pkg, ~~when decorator is used it seems not needed BUT for sanity~~ Takeaway: why it is not working when decorator is used and not included into pkg?
    - use `navigation routes`
    - do not forget add links in navbar
- use docs form recipe
    - add `tx.text_area`
    - make name required
    - add email with type email, default is text

# Making the From Responsive (styling)
- styling with common Inline Styles
- use `rx.desktop_only()` for rendering Components only in desktop mode
- use `rx.box()` Component for styling
- Takeaway: 50vw stands for 50% "viewport width" -> 50% of the browser windows's width
- make name and last name in same row

# Conditional Rendering in Reflex
getting familiar with:
- `rx.cond()` keep in mind that both Components need to be the same type
- `@rx.var`

- use FormState to keep bool for rx.cond
- challenge with clearing thank_you_message rendered by `rx.cond`
    - timeout approach 

# Refresh State with Python Asyncio Timeouts
Takeaway: using yield for async method for refreshing state?

- kind of magic:
```python
        yield
        await asyncio.sleep(2) 
        self.did_submit = False
        yield
```

