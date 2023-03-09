name = "TransparentPointer"

description = """TransparentPointer is the solution to "How to pass trough all gestures between two widgets in Stack" (https://stackoverflow.com/questions/65269190/pass-trough-all-gestures-between-two-widgets-in-stack) problem.

For example, if there is an ElevatedButton inside Container with GestureDetector then tapping on a button won't be "visible" to a gesture detector behind it. With TransparentPointer a tapping event doesn't stop on a button, but goes up to the parent, similar to event bubbling in HTML/JS.

"""

image_file = "appbar.svg"