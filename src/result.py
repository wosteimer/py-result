from typing import Callable, Generic, TypeAlias, TypeVar

_T = TypeVar("_T")
_E = TypeVar("_E")
_U = TypeVar("_U")
_F = TypeVar("_F")


class InvalidUnwrapError(Exception):
    ...


class Ok(Generic[_T, _E]):
    __match_args__ = ("value",)

    def __init__(self, value: _T) -> None:
        self.__value = value

    @property
    def value(self) -> _T:
        return self.__value

    def unwrap(self) -> _T:
        return self.value

    def expect(self, error_message: str) -> _T:
        return self.value

    def unwrap_or(self, default: _T) -> _T:
        return self.value

    def unwrap_or_else(self, default: Callable[[_E], _T]) -> _T:
        return self.value

    def unwrap_err(self) -> _E:
        raise InvalidUnwrapError()

    def expect_err(self, message: str) -> _E:
        raise InvalidUnwrapError(message)

    def map(self, function: Callable[[_T], _U]) -> "Result[_U, _E]":
        new_value = function(self.value)
        return Ok(new_value)

    def map_or(self, default: _U, function: Callable[[_T], _U]) -> _U:
        return function(self.value)

    def map_or_else(
        self, default: Callable[[_E], _U], function: Callable[[_T], _U]
    ) -> _U:
        return function(self.value)

    def map_err(self, function: Callable[[_E], _F]) -> "Result[_T, _F]":
        return Ok(self.value)

    def is_ok(self) -> bool:
        return True

    def is_err(self) -> bool:
        return False


class Err(Generic[_T, _E]):
    __match_args__ = ("value",)

    def __init__(self, value: _E) -> None:
        self.__value = value

    @property
    def value(self) -> _E:
        return self.__value

    def unwrap(self) -> _T:
        ...


Result: TypeAlias = Ok[_T, _E] | Err[_T, _E]
