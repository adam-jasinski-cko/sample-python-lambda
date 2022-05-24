from contextlib import contextmanager
import os
import sys
TOOLS_ROOT = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.join(TOOLS_ROOT, '../')
PYTHON_VERSION = f'{sys.version_info.major}.{sys.version_info.minor}'

@contextmanager
def cd(path):
    """Change directory while inside context manager."""
    cwd = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(cwd)