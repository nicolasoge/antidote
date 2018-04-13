from .__version__ import __version__
from .container import Dependency, DependencyContainer, Prepare
from .exceptions import (
    DependencyCycleError, DependencyDuplicateError, DependencyError,
    DependencyInstantiationError, DependencyNotFoundError,
    DependencyNotProvidableError
)
from .injector import DependencyInjector
from .manager import DependencyManager

__all__ = [
    'Dependency',
    'DependencyContainer',
    'DependencyInjector',
    'DependencyManager',
    'DependencyError',
    'DependencyNotProvidableError',
    'DependencyNotFoundError',
    'DependencyDuplicateError',
    'DependencyCycleError',
    'DependencyInstantiationError',
    'Prepare',
    'antidote'
]

antidote = DependencyManager()