# Step by step for "start here"

## Color mode
-`rx.color_mode.button(position="top-right")`
- play with position

## Buttons
- `rx.button("Check out our docs!")`
- add new button
- have `on_click` kwarg that is Event type
- add `State` method as event to button `on_click`

## App state
- This is huge thing
- subclass of `rx.State`
- can keep state in class attribute
- via adding methods to this subclass you can dynamic do things, e.g. change label
- add method that change label attribute
- use `itertools.cycle` for smart toggle_label method

# Questions
- what are `.web` and `.state` dirs?
- `on_click` is Button kwarg but plays Event role?