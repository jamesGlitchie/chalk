"""
The chalk module is a Python library that provides a simple and convenient way to color text in the terminal .

Features:
- Base colors : black, red, green, yellow, blue, magenta, cyan, white
- Modifiers : bold, dim, italic, inverse, hidden, overline, underline, srikethrough
- Foreground colors : Begin with a lowercase letter.
- Background colors : Begin with a uppercase letter.
- Bright colors : Contain the `_bright` suffix.
- Color functions : rgb, hex and ansi256

Chalks:
They are objects used to contain the colors. 
- Called with any object as an argument and a colored string is returned.
- Resets the color applied automatically.

Controls:
- enable  : enables color application as long as the output is connected to a terminal device.
- disable : disables color application .
- force   : enables color application even when the output is not connected to a terminal device.

Concatenation:
Chalks can be added together.
- If a and b contain the same reset value, a + b = b
- if a and b contain the same code value, a + b = a
- This prevents unnecesary creation of new Chalk objects.

Chaining:
Chalks can be chained together to create new `Chalk` objects.
- The getattribute syntax is used although the chalks accessed aren't actual attributes in the object.
- The chalks obtained are summed and the result is returned.
- The chalks can also be chained with color functions ie `<chalk>.<method>(...)`

Example:
>>> import chalk
    text = chalk.green + "Hello world"
    text = chalk.green("Hello world")
    text = chalk.hex("#26262")("hello world")
    new  = chalk.green + chalk.bold 
    text = new("Hello world")
    text = chalk.yellow.Hex("#7878ee").underline("Hello world")
"""
from typing import Any, overload

black: Chalk
red: Chalk
green: Chalk
yellow: Chalk
blue: Chalk
magenta: Chalk
cyan: Chalk
white: Chalk

Black: Chalk
Red: Chalk
Green: Chalk
Yellow: Chalk
Blue: Chalk
Magenta: Chalk
Cyan: Chalk
White: Chalk

black_bright: Chalk
red_bright: Chalk
green_bright: Chalk
yellow_bright: Chalk
blue_bright: Chalk
magenta_bright: Chalk
cyan_bright: Chalk
white_bright: Chalk

Black_bright: Chalk
Red_bright: Chalk
Green_bright: Chalk
Yellow_bright: Chalk
Blue_bright: Chalk
Magenta_bright: Chalk
Cyan_bright: Chalk
White_bright: Chalk

reset: Chalk
bold: Chalk
dim: Chalk
italic: Chalk
inverse: Chalk
hidden: Chalk
overline: Chalk
underline: Chalk
strikethrough: Chalk

class Chalk:
    """
    This is the base class for all colors.
    
    Parameters:
        open  : the ansi code for the color.
        close : the reset code for the color.
    """

    def __init__(self, open: str | int, close: str | int) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __call__(self, colored: Any) -> str: ...
    @overload
    def __add__(self, to: Chalk) -> Chalk: ...
    @overload
    def __add__(self, to: str) -> str: ...

    black: Chalk  # For nice linting
    red: Chalk
    green: Chalk
    yellow: Chalk
    blue: Chalk
    magenta: Chalk
    cyan: Chalk
    white: Chalk

    Black: Chalk
    Red: Chalk
    Green: Chalk
    Yellow: Chalk
    Blue: Chalk
    Magenta: Chalk
    Cyan: Chalk
    White: Chalk

    black_bright: Chalk
    red_bright: Chalk
    green_bright: Chalk
    yellow_bright: Chalk
    blue_bright: Chalk
    magenta_bright: Chalk
    cyan_bright: Chalk
    white_bright: Chalk

    Black_bright: Chalk
    Red_bright: Chalk
    Green_bright: Chalk
    Yellow_bright: Chalk
    Blue_bright: Chalk
    Magenta_bright: Chalk
    Cyan_bright: Chalk
    White_bright: Chalk

    reset: Chalk
    bold: Chalk
    dim: Chalk
    italic: Chalk
    inverse: Chalk
    hidden: Chalk
    overline: Chalk
    underline: Chalk
    strikethrough: Chalk
    
    def rgb(self, red: int, green: int, blue: int,/) -> Chalk:...

    def Rgb(self, red: int, green: int, blue: int,/) -> Chalk:...

    def hex(self, color: str,/) -> Chalk: ...

    def Hex(self, color: str,/) -> Chalk: ...

    def ansi256(self, base: int | str) -> Chalk:...

    def Ansi256(self, base: int | str) -> Chalk:...

def rgb(red: int, green: int, blue: int,/) -> Chalk:
    """Takes in a rgb values  and returns a foreground chalk."""

def Rgb(red: int, green: int, blue: int,/) -> Chalk:
    """Takes in a rgb values  and returns a background chalk."""

def hex(color: str,/) -> Chalk:
    """Takes in a hex string and returns a foreground chalk."""

def Hex(color: str,/) -> Chalk:
    """Takes in a hex string and returns a background chalk."""

def ansi256(base: int | str,/) -> Chalk:
    """Takes in a base code and returns a ansi 256 foreground chalk."""

def Ansi256(base: int | str,/) -> Chalk:
    """Takes in a base code and returns a ansi 256 background chalk."""

def enable() -> None:
    """
    Enables application of color.
    - This has no effect if the standard output is not connected to a terminal device.'
    - Use the `chalk.force` function to force application of the color.
    """

def disable() -> None:
    """Disables application of color to the text."""

def force() -> None:
    """
    Used to force color application.
    - It ignores whether or not the output is connected to a terminal.
    - Useful if the colored text is being logged to the `stderr`
    """

__all__ = []