from verbose_print import vprint as vp
from verbose_print.styles import Styles


def test_vprint(capsys):
    vp.vprint("Hello", "World", verbose=True, end="!")
    captured = capsys.readouterr()
    assert captured.out == "Hello World!"


def test_vprint_false(capsys):
    vp.vprint("Hello", "World", verbose=False, end="!")
    captured = capsys.readouterr()
    assert captured.out == ""


def test_vprint_no_args(capsys):
    vp.vprint(verbose=True, end="!")
    captured = capsys.readouterr()
    assert captured.out == ""


def test_vprint_args(capsys):
    vp.vprint(
        "Hello",
        "World",
        verbose=True,
        end="!",
        bold=True,
        underline=True,
        color=Styles.GREEN
    )
    captured = capsys.readouterr()
    assert captured.out == "\x1b[1m\x1b[4m\x1b[92mHello World!\x1b[0m\n"


def test_vwarn(capsys):
    vp.vwarn("Hello", "World", verbose=True, end="!")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[93m\nHello World!\x1b[0m\n"


def test_vfail(capsys):
    vp.vfail("Hello", "World", verbose=True, end="!")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[91m\nHello World!\x1b[0m\n"


def test_vblue(capsys):
    vp.vblue("Hello", "World", verbose=True, end="!")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[94m\nHello World!\x1b[0m\n"


def test_vcyan(capsys):
    vp.vcyan("Hello", "World", verbose=True, end="!")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[96m\nHello World!\x1b[0m\n"


def test_vsuccess(capsys):
    vp.vsuccess("Hello", "World", verbose=True, end="!")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[92m\nHello World!\x1b[0m\n"


def test_vbold(capsys):
    vp.vbold("Hello", "World", verbose=True, end="!")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[1m\nHello World!\x1b[0m\n"


def test_vunderline(capsys):
    vp.vunderline("Hello", "World", verbose=True, end="!")
    captured = capsys.readouterr()
    assert captured.out == "\x1b[4m\nHello World!\x1b[0m\n"
