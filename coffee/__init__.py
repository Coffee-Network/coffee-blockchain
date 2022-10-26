import nest_asyncio
from pkg_resources import DistributionNotFound, get_distribution, resource_filename

nest_asyncio.apply()

try:
    __version__ = get_distribution("coffee-blockchain").version
except DistributionNotFound:
    # package is not installed
    __version__ = "unknown"

PYINSTALLER_SPEC_PATH = resource_filename("coffee", "pyinstaller.spec")
