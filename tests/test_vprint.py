from verbose_print import vprint as vp


def test_vp_init(capsys):
    vp.vprint("Hello", "World", verbose=True, end="!")
    captured = capsys.readouterr()
    assert captured.out == "Hello World!"
