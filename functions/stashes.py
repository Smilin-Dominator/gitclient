from subprocess import getoutput, call, DEVNULL
from config import header, input, warning


def get_stashes():
    return getoutput("git stash list").splitlines()


def set_header():
    stashes = get_stashes()
    stash_messages = [line.split(": ")[2].strip("'") for line in stashes]
    header(
        f"[tan][ Stashes: '{', '.join(stash_messages)}' ][/tan]"
    )


def get_index(message: str) -> int:
    stashes = get_stashes()
    for line in stashes:
        line = line.split(": ")
        if line[2].strip("'") == message:
            return int(line[0].strip("stash@{}"))


def stash(message: str = None):
    if message is not None:
        message = message
    else:
        message = input("\tMessage", override="red")
    call(f"git stash -m '{message}'", shell=True, stderr=DEVNULL, stdout=DEVNULL)


def apply_stash(pop: bool):
    stashes = get_stashes()
    if len(stashes) == 0:
        warning("You Have No Stashes")
    else:
        stashes = [line.split(": ")[2].strip("'") for line in stashes]
        try:
            st = input("\tWhich Stash Would You Like To Apply?", choices=stashes, override="orange1")
            if pop:
                call(f"git stash pop {get_index(st)}", shell=True)
            else:
                call(f"git stash apply {get_index(st)}", shell=True)
        except KeyboardInterrupt:
            pass
