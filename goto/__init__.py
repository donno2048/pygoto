from os import _exit
from sys import modules, exit
from inspect import getsourcelines
def goto(line: int) -> None:
    try:
        if not isinstance(line, int):
            raise TypeError("You should only use integer values in goto")
        if line < 1:
            raise ValueError("The line number must be positive")
        exit(exec("\n".join(getsourcelines(modules["__main__"])[0][line - 1:]), modules["__main__"].__dict__))
    except RecursionError:
        print("You have passed the recursion limit, please check your goto")
        _exit(1)
    except (SystemExit, KeyboardInterrupt):
        _exit(0)
    except BaseException as e:
        traceback = e.__traceback__.tb_next
        message = "Traceback (most recent call last):"
        errorline = line + (traceback.tb_lineno - 1) // 2
        module = modules["__main__"]
        file = module.__file__
        source = getsourcelines(module)[0]
        while True:
            message += "\n  File \"" + file + "\", line " + str(errorline) + ", in " + traceback.tb_frame.f_code.co_name + "\n    " + source[errorline - 1].replace("\n", "")
            traceback = traceback.tb_next
            if traceback:
                if traceback.tb_frame.f_code.co_filename == "<string>":
                    errorline = line + (traceback.tb_lineno - 1) // 2
                    file = module.__file__
                    source = getsourcelines(module)[0]
                else:
                    errorline = traceback.tb_lineno
                    file = traceback.tb_frame.f_code.co_filename
                    source = open(file).readlines()
            else:
                break
        exit(message + "\n" + type(e).__name__ + ": " + str(e))