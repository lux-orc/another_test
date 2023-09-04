
import datetime
from pathlib import Path
from typing import Any

def cp(s: Any = '', /, display: int = 0, fg: int = 37, bg: int = 40) -> str:
    """Return the string for color print in the console"""
    return f'\033[{display};{fg};{bg}m{s}\033[0m'

# Print the current time in the console
time_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
out_str = f"\n{cp('Current time', display=4, fg=36)} {cp('->', fg=35)} {cp(time_str, fg=34)}"
print(out_str)


# Create a output folder if not exists
op = Path('out')
if not op.exists():
    op.mkdir()

# Write the output string into a txt file
with open(op / 'output.txt', 'w') as f:
    f.write(out_str)
print(cp(
    '\nThe string producing the output in the console has been saved in "output.txt"\n',
    display=4,
    fg=32
))