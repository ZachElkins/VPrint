from verbose_print.styles import Styles


class PrintStyle:
    """ Class to group all the style decorators. """

    @staticmethod
    def warning(fn):
        """
        Functions to add warning color style to anything printed within
        the given function fn.

        :param fn: Function to execute with warning color style.
        """
        def f(*args, **kwargs):
            print(Styles.YELLOW)
            fn(*args, **kwargs)
            print(Styles.END)
        return f

    @staticmethod
    def fail(fn):
        """
        Functions to add fail color style to anything printed within
        the given function fn.

        :param fn: Function to execute with fail color style.
        """
        def f(*args, **kwargs):
            print(Styles.RED)
            fn(*args, **kwargs)
            print(Styles.END)
        return f

    @staticmethod
    def blue(fn):
        """
        Functions to add blue color style to anything printed within
        the given function fn.

        :param fn: Function to execute with blue color style.
        """
        def f(*args, **kwargs):
            print(Styles.BLUE)
            fn(*args, **kwargs)
            print(Styles.END)
        return f

    @staticmethod
    def cyan(fn):
        """
        Functions to add cyan color style to anything printed within
        the given function fn.

        :param fn: Function to execute with cyan color style.
        """
        def f(*args, **kwargs):
            print(Styles.CYAN)
            fn(*args, **kwargs)
            print(Styles.END)
        return f

    @staticmethod
    def green(fn):
        """
        Functions to add green color style to anything printed within
        the given function fn.

        :param fn: Function to execute with green color style.
        """
        def f(*args, **kwargs):
            print(Styles.GREEN)
            fn(*args, **kwargs)
            print(Styles.END)
        return f

    @staticmethod
    def bold(fn):
        """
        Functions to add bold color style to anything printed within
        the given function fn.

        :param fn: Function to execute with bold style.
        """
        def f(*args, **kwargs):
            print(Styles.BOLD)
            fn(*args, **kwargs)
            print(Styles.END)
        return f

    @staticmethod
    def underline(fn):
        """
        Functions to add underline color style to anything printed within
        the given function fn.

        :param fn: Function to execute with underline style.
        """
        def f(*args, **kwargs):
            print(Styles.UNDERLINE)
            fn(*args, **kwargs)
            print(Styles.END)
        return f
