
def vprint(*args, verbose: bool = False, end: str = "\n"):
    out: str = ""
    l: int = len(args)
    for i in range(l):
        out = out + args[i]
        if i < l-1:
            out += " "
    if verbose and args:
        print(out, end=end)
