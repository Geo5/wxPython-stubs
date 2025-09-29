# ---------------------------------------------------------------------------
# Name:        newevent.pyi
# Purpose:     Type stubs for newevent.py.
#
# Author:      Miki Tebeka <miki.tebeka@gmail.com>
#              Geo5
#
#
# Created:     29-Sept-2025
# Copyright:   (c) 2006-2020 by Total Control Software
# Licence:     wxWindows license
#
# Tags:        phoenix-port, documented
# ---------------------------------------------------------------------------

import wx

# Create type-checking-only subclasses of `PyEvent` and `PyCommandEvent` which allow setting
# arbitrary instance attributes by passing them as keyword arguments to `__init__`.  This models
# what `New{Command}Event()` does at runtime.  We cannot accurately represent the runtime here,
# because the subclasses are created inside of `New{Command}Event()`, so we cannot reference them in
# the type hints.
class _PyEventSubclass(wx.PyEvent):
    """This is a type-checking only subclass of wx.PyEvent which is not the real run time type
    created by NewEvent(), but improves the type checking experience.

    Can set arbitrary instance attributes by supplying them as keyword arguments on `__init__`.
    """
    def __init__(self, **kwargs: object) -> None: ...

class _PyCommandEventSubclass(wx.PyEvent):
    """This is a type-checking only subclass of `wx.PyCommandEvent` which is not the real run time type
    created by `NewCommandEvent()`, but improves the type checking experience.

    Can set arbitrary instance attributes by supplying them as keyword arguments on `__init__`.
    """
    def __init__(self, id: int, **kwargs: object) -> None: ...

def NewEvent() -> tuple[type[_PyEventSubclass], wx.PyEventBinder]: ...
def NewCommandEvent() -> tuple[type[_PyCommandEventSubclass], wx.PyEventBinder]: ...
