# set version string using versioneer
from .._version import get_versions
__version__ = get_versions()['version']
del get_versions

# Now import useful functions

__all__ = ['image_stack_to_movie', 'show_image_stack',
           'notebook_to_nbviewer']

from .animation import image_stack_to_movie, show_image_stack
from .nbviewer import notebook_to_nbviewer
from .info import get_sys_info, show_kernels
