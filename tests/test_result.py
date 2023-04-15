from typing import Any

from pytest import raises

from result import *
from result.errors import InvalidUnwrapError

_ = Any


def test_the_unwrap_method_in_the_ok_state_should_return_the_correct_value():
    result: Result[int, _] = Ok(1)
    assert result.unwrap() == 1


def test_the_expect_method_in_the_ok_state_should_return_the_correct_value():
    result: Result[int, _] = Ok(1)
    assert result.expect("ops") == 1


def test_the_unwrap_or_method_in_the_ok_state_should_return_the_correct_value():
    result: Result[int, _] = Ok(1)
    assert result.unwrap_or(3) == 1


def test_the_unwrap_or_else_method_in_the_ok_state_should_return_the_correct_value():
    result: Result[int, _] = Ok(1)
    assert result.unwrap_or_else(lambda _: 3) == 1


def test_unwrap_err_method_in_ok_state_should_raise_an_exception():
    result: Result[int, _] = Ok(1)
    with raises(InvalidUnwrapError):
        result.unwrap_err()


def test_expect_err_method_in_ok_state_should_raise_an_exception_and_show_the_correct_message():
    result: Result[int, _] = Ok(1)
    error_message = "error message"
    with raises(InvalidUnwrapError) as error:
        result.expect_err(error_message)
        assert str(error) == error_message


def test_map_method_in_the_ok_state_should_correctly_apply_the_passed_function():
    result: Result[int, _] = Ok(1)
    assert result.map(lambda x: x + 2).unwrap() == 3


def test_map_or_method_in_the_ok_state_should_correctly_apply_the_passed_function():
    result: Result[int, _] = Ok(1)
    assert result.map_or(2, lambda x: x + 2) == 3


def test_map_or_else_method_in_the_ok_state_should_correctly_apply_the_passed_function():
    result: Result[int, _] = Ok(1)
    assert result.map_or_else(lambda x: 2, lambda x: x + 2) == 3


def test_map_err_in_the_ok_state_should_return_the_correct_value():
    result: Result[int, _] = Ok(1)
    assert result.map_err(lambda x: "other error").unwrap() == 1


def test_is_ok_method_in_the_ok_state_must_return_true():
    result: Result[int, _] = Ok(1)
    assert result.is_ok()


def test_is_err_method_in_the_ok_state_must_return_false():
    result: Result[int, _] = Ok(1)
    assert not result.is_err()


def test_the_unwrap_method_in_the_err_state_should_raise_an_exception():
    result: Result[_, str] = Err("error")
    with raises(InvalidUnwrapError):
        result.unwrap()


def test_the_expect_method_in_the_err_state_should_raise_an_exception_and_show_the_correct_message():
    result: Result[_, str] = Err("error")
    error_message = "error message"
    with raises(InvalidUnwrapError) as error:
        result.expect(error_message)
        assert str(error) == error_message


def test_the_unwrap_or_method_in_the_err_state_should_return_the_default_value():
    result: Result[int, str] = Err("error")
    default_value = 3
    assert result.unwrap_or(default_value) == default_value


def test_the_unwrap_or_else_method_in_the_err_state_should_correctly_apply_the_passed_default_function():
    result: Result[_, str] = Err("error")
    default_value = 3
    assert result.unwrap_or_else(lambda _: default_value) == default_value


def test_unwrap_err_method_in_err_state_return_the_correct_value():
    result: Result[_, str] = Err("error")
    assert result.unwrap_err() == "error"


def test_expect_err_method_in_err_state_return_the_correct_value():
    result: Result[_, str] = Err("error")
    assert result.expect_err("error message") == "error"


def test_map_method_in_the_err_state_should_return_an_err_object():
    result: Result[_, str] = Err("error")
    assert isinstance(result.map(lambda x: 1), Err)


def test_map_or_method_in_the_err_state_should_return_the_default_value():
    result: Result[int, str] = Err("error")
    default_value = 3
    assert result.map_or(default_value, lambda x: 1) == default_value


def test_map_or_else_method_in_the_err_state_should_correctly_apply_the_passed_default_function():
    result: Result[int, str] = Err("error")
    assert result.map_or_else(lambda e: 3, lambda x: 1) == 3


def test_map_err_in_the_err_state_should_correctly_apply_the_passed_function():
    result: Result[int, str] = Err("error")
    assert result.map_err(lambda e: "error_2").unwrap_err() == "error_2"


def test_is_ok_method_in_the_err_state_must_return_false():
    result: Result[_, str] = Err("error")
    assert not result.is_ok()


def test_is_err_method_in_the_err_state_must_return_true():
    result: Result[_, str] = Err("error")
    assert result.is_err()
