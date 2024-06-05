import sys
from typing import Any, Callable
from atexit import register as atexit


@(lambda _: _())
def windows_init():
    try:
        from ctypes import windll, byref, c_ulong
    except ImportError:
        return  # Probably Not windows
    # Initializes window's virtual terminal processing which enables support for escape codes.
    # Useful for hiding cursors and also enables color support especially for the old conhost.exe emulator.
    # Read : https://learn.microsoft.com/en-us/windows/console/setconsolemode
    VT_PROCESSING = 0x0004
    OUTPUT_HANDLE = -11
    kernel32 = windll.kernel32
    GetStdHandle = kernel32.GetStdHandle
    GetConsoleMode = kernel32.GetConsoleMode
    SetConsoleMode = kernel32.SetConsoleMode

    handle = GetStdHandle(OUTPUT_HANDLE)
    mode = c_ulong()
    GetConsoleMode(handle, byref(mode))
    mode.value |= VT_PROCESSING
    SetConsoleMode(handle, mode)


@atexit
def cleanup():
    if Chalk.state():
        sys.stdout.buffer.write(b"\x1b[0m")
        sys.stdout.buffer.flush()


def cf(func: Callable[..., "Chalk"]):
    setattr(func, "gen", None)
    return func


class Chalk:
    """This is the base class for all colors"""

    __state = int(sys.stdout.isatty())
    __slots__ = "_dir"

    def __init__(self, open: str | int, close: str | int) -> None:
        self._dir = (open, close)

    def __str__(self) -> str:
        if Chalk.state():
            return f"\x1b[{self._dir[0]}m"
        return ""

    def __repr__(self) -> str:
        return f"Chalk({repr(self._dir[0])}, {repr(self._dir[1])})"

    def __call__(self, colored: Any):
        if Chalk.state():
            return f"\x1b[{self._dir[0]}m{colored}\x1b[{self._dir[1]}m"
        return str(colored)

    def __add__(self, to: Any) -> Any:
        if isinstance(to, Chalk):
            (a, b), (c, d) = self._dir, to._dir
            if a == c:
                return self
            elif b == d and b != 22:
                return to
            return Chalk(f"{a}m\x1b[{c}", f"{b}m\x1b[{d}")
        elif callable(to) and hasattr(to, "gen"):
            return stacked(self, to)
        else:
            return str(self) + str(to)

    def __getattribute__(self, name: str) -> Any:
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass
        return get_color(self, name)

    @classmethod
    def state(cls, new: int | None = None):
        if new is None:
            if cls.__state == 1 and sys.stdout.isatty() or cls.__state == 3:
                return True
            return False
        cls.__state = new


def builder(close: int | str):
    def build(open: int | str):
        return Chalk(open, close)

    return build


def build():
    try:
        return getattr(build, "built")
    except AttributeError:
        setattr(build, "built", None)
    gl = globals()
    fg = builder(39)
    bg = builder(49)
    fgen = map(fg, range(30, 38))
    bgen = map(bg, range(40, 48))
    bfgen = map(builder(99), range(90, 98))
    bbgen = map(builder(109), range(100, 108))

    gl["black"] = next(fgen)
    gl["red"] = next(fgen)
    gl["green"] = next(fgen)
    gl["yellow"] = next(fgen)
    gl["blue"] = next(fgen)
    gl["magenta"] = next(fgen)
    gl["cyan"] = next(fgen)
    gl["white"] = next(fgen)

    gl["Black"] = next(bgen)
    gl["Red"] = next(bgen)
    gl["Green"] = next(bgen)
    gl["Yellow"] = next(bgen)
    gl["Blue"] = next(bgen)
    gl["Magenta"] = next(bgen)
    gl["Cyan"] = next(bgen)
    gl["White"] = next(bgen)

    gl["black_bright"] = next(bfgen)
    gl["red_bright"] = next(bfgen)
    gl["green_bright"] = next(bfgen)
    gl["yellow_bright"] = next(bfgen)
    gl["blue_bright"] = next(bfgen)
    gl["magenta_bright"] = next(bfgen)
    gl["cyan_bright"] = next(bfgen)
    gl["white_bright"] = next(bfgen)

    gl["Black_bright"] = next(bbgen)
    gl["Red_bright"] = next(bbgen)
    gl["Green_bright"] = next(bbgen)
    gl["Yellow_bright"] = next(bbgen)
    gl["Blue_bright"] = next(bbgen)
    gl["Magenta_bright"] = next(bbgen)
    gl["Cyan_bright"] = next(bbgen)
    gl["White_bright"] = next(bbgen)

    gl["reset"] = Chalk(0, 0)
    gl["bold"] = Chalk(1, 22)
    gl["dim"] = Chalk(2, 22)
    gl["italic"] = Chalk(3, 23)
    gl["inverse"] = Chalk(7, 27)
    gl["hidden"] = Chalk(8, 28)
    gl["overline"] = Chalk(53, 55)
    gl["underline"] = Chalk(4, 24)
    gl["strikethrough"] = Chalk(9, 29)


def base(red: int, green: int, blue: int):
    if red == green == blue:
        if red < 8:
            return 16
        if red > 248:
            return 231
        return round(((red - 8) / 247) * 24) + 232
    return (
        16
        + (36 * round(red / 255 * 5))
        + (6 * round(green / 255 * 5))
        + round(blue / 255 * 5)
    )


@cf
def rgb(red: int, green: int, blue: int, /):
    return Chalk(f"38;2;{red};{green};{blue}", 39)


@cf
def Rgb(red: int, green: int, blue: int, /):
    return Chalk(f"48;2;{red};{green};{blue}", 49)


@cf
def hex(color: str, /):
    color = color.lstrip("#").ljust(6, "0")
    return rgb(*map(lambda s: int(s, 16), (color[0:2], color[2:4], color[4:6])))


@cf
def Hex(color: str, /):
    color = color.lstrip("#").ljust(6, "0")
    return Rgb(*map(lambda s: int(s, 16), (color[0:2], color[2:4], color[4:6])))


@cf
def ansi256(base: int | str, /):
    return Chalk(f"38;5;{base}", 0)


@cf
def Ansi256(base: int, /):
    return Chalk(f"48;5;{base}", 0)


def stacked(base: Chalk, func: Callable[..., Chalk]):
    def wrapper(*args: Any):
        return base + func(*args)

    return wrapper


def enable():
    Chalk.state(1)


def disable():
    Chalk.state(0)


def force():
    Chalk.state(3)


def __getattr__(name: str):
    if attribute := globals().get(name):
        return attribute
    build()
    if attribute := globals().get(name):
        return attribute
    raise AttributeError(f"module 'chalk' has no attribute {name!r}")


def get_color(base: Chalk, name: str):
    if (color := globals().get(name)) and isinstance(color, Chalk):
        return base + color
    elif callable(color) and hasattr(color, "gen"):
        return stacked(base, color)
    build()
    if (color := globals().get(name)) and isinstance(color, Chalk):
        return base + color
    raise AttributeError(f"Chalk `{name}` is undefined.")


__all__ = []
