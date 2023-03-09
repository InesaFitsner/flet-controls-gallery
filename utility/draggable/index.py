name = "Draggable"

description = """A control that can be dragged from to a DragTarget.

When a draggable control recognizes the start of a drag gesture, it displays a content_feedback control that tracks the user's finger across the screen. If the user lifts their finger while on top of a DragTarget, that target is given the opportunity to complete drag-and-drop flow.

This control displays content when zero drags are under way. If content_when_dragging is non-null, this control instead displays content_when_dragging when one or more drags are underway. Otherwise, this widget always displays `content`.

"""

image_file = "appbar.svg"