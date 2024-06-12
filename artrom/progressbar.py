"""Progress bar

This module allows for a progress bar to be displayed for loops.

This file can be imported to run:
    * progress_bar - loops over iterable and displays progress.
"""
import sys
import time

def progress_bar(it, prefix="", size=60, out=sys.stdout):
    """Loops over iterable and displays progress.

    Parameters
    ----------
    it : iterable, required
        iterable to loop over
    prefix: str, optional
        string to display before progress bar.
    size: int, optional
        length of progress bar
    out: int, optional
        where to print!
    """
    count = len(it)
    start = time.time() # time estimate start
    def show(j):
        x = int(size*j/count)
        # time estimate calculation and string
        remaining = ((time.time() - start) / j) * (count - j)        
        mins, sec = divmod(remaining, 60) # limited to minutes
        time_str = f"{int(mins):02}:{sec:03.1f}"
        print(f"{prefix}[{u'█'*x}{('.'*(size-x))}] {j}/{count} Est wait {time_str}", end='\r', file=out, flush=True)
    show(0.1) # avoid div/0 
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)
