from collections.abc import Callable, Generator, Iterable
from typing import Any, Generic, TypeVar

from typing_extensions import TypeAlias

from pykka._types import OptExcInfo

_T = TypeVar("_T")
J = TypeVar("J")  # For when T is Iterable[J]  # noqa

_M = TypeVar("_M")  # For Future.map()
_R = TypeVar("_R")  # For Future.reduce()

GetHookFunc: TypeAlias = Callable[[float | None], _T]

class Future(Generic[_T]):
    _get_hook: GetHookFunc | None
    _get_hook_result: _T | None
    def get(self, timeout: float | None = ...) -> _T: ...
    def set(self, value: _T | None = ...) -> None: ...
    def set_exception(self, exc_info: OptExcInfo | None = ...) -> None: ...
    def set_get_hook(self, func: GetHookFunc) -> None: ...
    def filter(
        self: Future[Iterable[J]], func: Callable[[J], bool]
    ) -> Future[Iterable[J]]: ...
    def join(self, *futures: Future[Any]) -> Future[Iterable[Any]]: ...
    def map(self, func: Callable[[_T], _M]) -> Future[_M]: ...
    def reduce(
        self: Future[Iterable[J]], func: Callable[[_R, J], _R], *args: _R
    ) -> Future[_R]: ...
    def __await__(self) -> Generator[None, None, _T]: ...

def get_all(
    futures: Iterable[Future[Any]], timeout: float | None = ...
) -> Iterable[Any]: ...
