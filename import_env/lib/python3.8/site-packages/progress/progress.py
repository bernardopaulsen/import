from IPython.display import clear_output

def update(progress: float, text: str = 'Progress', message : str = ''):
    """
    Progress bar.

    Parameters
    ----------
    Progress : float
        Progress to be displayed, from 0 to 1.

    Text : string
        Text to be displayed before the progress bar.

    Message : string
        Message to be displayed after the progress bar.

    Returns
    -------
    Progress bar : print(string)
    """
    bar_length = 20
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
    if progress < 0:
        progress = 0
    if progress >= 1:
        progress = 1
    block = int(round(bar_length * progress))
    clear_output(wait = True)
    text = "{0}: [{1}] {2:.1f}% {3}".format(text, "#" * block + "-" * (bar_length - block), progress * 100, message)
    print(text)

def clear():
    """
    Clears output.
    """
    clear_output(wait=True)