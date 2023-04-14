from typing import Any

from pytest import raises

from src.result import *

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
