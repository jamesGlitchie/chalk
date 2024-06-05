# Chalk

Chalk is a Python module that provides a simple and convenient way to color text in the terminal.

## Installation

```bash
pip install chalk
```

## Chalks

The module uses chalk objects to contain, control and apply colors.

## Naming convention

- Foreground colors begin with a lowercase letter.
- Background colors begin with an uppercase letter.
- Bright colors contain the `_bright` suffix.

## Base colors

`black`
`red`
`green`
`yellow`
`blue`
`magenta`
`cyan`
`white`

## Modifiers

`bold`
`dim`
`italic`
`inverse`
`hidden`
`overline`
`underline`
`strikethrough`

## Controls

The module contains ways to control whether or not color is applied.

- ### Enable colors

The module contains the `enable` function that enables colored output.

- ### Disable colors

The module contains the `disable` function that disables color application.
It is called by default if the terminal is not tty.

- ### Force colors

The `force` function enables color application even when the standard output is
not connected to a terminal device. Can be useful when writing to [stderr](https://www.askpython.com/python/python-stdin-stdout-stderr)

## Concatenation rules

Chalks can be added together.

- If `a` and `b` contain the same reset value, `a + b = b`

<image src="media/concat1.png">

- If `a` and `b` contain the same color code value, `a + b = a`

<image src="media/concat2.png">

This prevents unnecessary creation of new Chalk objects.

## Custom Chalks

Custom chalks can be created through:

- ### Adding

You can add a chalk to another chalk or a color function.

<image src="media/adding.png">

- ### Chaining

You can chain chalks together to form a custom chalk.

<image src="media/chaining.png">

## Conhost

- The chalk module ensures color support for the windows `conhost.exe` emulator.

<image src="media/conhost-demo.png">

## License

[MIT](LICENSE)
