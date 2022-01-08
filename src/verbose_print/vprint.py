from verbose_print.styles import Styles
from verbose_print.style_decorators import PrintStyle
from typing import Optional


def vprint(
        *args,
        verbose: bool = False,
        end: str = "\n",
        underline: bool = False,
        bold: bool = False,
        color: Optional[Styles] = None
):
    """
    Basic verbose printing function.

    :param args: Everything to print out.
    :param verbose: Boolean to toggle printing.
    :param end: [Optional] String to print at the end.
    :param underline: [Optional] Boolean to underline the text or not.
    :param bold: [Optional] Boolean to bold the text or not.
    :param color: [Optional] Color to style the text.
    """
    if not (verbose and args):
        return

    out: str = ""
    if bold:
        out = out + Styles.BOLD
    if underline:
        out = out + Styles.UNDERLINE
    if color is not None:
        out = out + str(color)
    l: int = len(args)
    for i in range(l):
        out = out + args[i]
        if i < l-1:
            out += " "

    print(out, end=end)

    if bold or underline or color:
        print(Styles.END)


@PrintStyle.warning
def vwarn(
        *args,
        verbose: bool = False,
        end: str = "\n",
        underline: bool = False,
        bold: bool = False
):
    """
    Warning verbose printing function, prints in yellow.

    :param args: Everything to print out.
    :param verbose: Boolean to toggle printing.
    :param end: [Optional] String to print at the end.
    :param underline: [Optional] Boolean to underline the text or not.
    :param bold: [Optional] Boolean to bold the text or not.
    """
    vprint(*args, verbose=verbose, end=end)


@PrintStyle.fail
def vfail(
        *args,
        verbose: bool = False,
        end: str = "\n",
        underline: bool = False,
        bold: bool = False
):
    """
    Warning verbose printing function, prints in red.

    :param args: Everything to print out.
    :param verbose: Boolean to toggle printing.
    :param end: [Optional] String to print at the end.
    :param underline: [Optional] Boolean to underline the text or not.
    :param bold: [Optional] Boolean to bold the text or not.
    """
    vprint(*args, verbose=verbose, end=end)


@PrintStyle.blue
def vblue(
        *args,
        verbose: bool = False,
        end: str = "\n",
        underline: bool = False,
        bold: bool = False
):
    """
    Warning verbose printing function, prints in blue.

    :param args: Everything to print out.
    :param verbose: Boolean to toggle printing.
    :param end: [Optional] String to print at the end.
    :param underline: [Optional] Boolean to underline the text or not.
    :param bold: [Optional] Boolean to bold the text or not.
    """
    vprint(*args, verbose=verbose, end=end)


@PrintStyle.cyan
def vcyan(
        *args,
        verbose: bool = False,
        end: str = "\n",
        underline: bool = False,
        bold: bool = False
):
    """
    Warning verbose printing function, prints in cyan.

    :param args: Everything to print out.
    :param verbose: Boolean to toggle printing.
    :param end: [Optional] String to print at the end.
    :param underline: [Optional] Boolean to underline the text or not.
    :param bold: [Optional] Boolean to bold the text or not.
    """
    vprint(*args, verbose=verbose, end=end)


@PrintStyle.green
def vsuccess(
        *args,
        verbose: bool = False,
        end: str = "\n",
        underline: bool = False,
        bold: bool = False
):
    """
    Warning verbose printing function, prints in green.

    :param args: Everything to print out.
    :param verbose: Boolean to toggle printing.
    :param end: [Optional] String to print at the end.
    :param underline: [Optional] Boolean to underline the text or not.
    :param bold: [Optional] Boolean to bold the text or not.
    """
    vprint(*args, verbose=verbose, end=end)


@PrintStyle.bold
def vbold(
        *args,
        verbose: bool = False,
        end: str = "\n",
        color: Optional[Styles] = None
):
    """
    Basic verbose printing function, prints bolded.

    :param args: Everything to print out.
    :param verbose: Boolean to toggle printing.
    :param end: [Optional] String to print at the end.
    :param color: [Optional] Color to style the text.
    """
    vprint(*args, verbose=verbose, end=end, color=color)


@PrintStyle.underline
def vunderline(
        *args,
        verbose: bool = False,
        end: str = "\n",
        color: Optional[Styles] = None
):
    """
    Basic verbose printing function, prints underlined.

    :param args: Everything to print out.
    :param verbose: Boolean to toggle printing.
    :param end: [Optional] String to print at the end.
    :param color: [Optional] Color to style the text.
    """
    vprint(*args, verbose=verbose, end=end, color=color)
