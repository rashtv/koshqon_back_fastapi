from typing import (
    Optional,
    Union,
)


def success_response(
        details: str,
        data: Optional[Union[list, dict]],
) -> dict:
    return {
        "code": 0,
        "data": data,
        "details": details,
    }


def error_response(
        code: int,
        name: str,
        details: str,
) -> dict:
    return {
        "code": code,
        "name": name,
        "details": details,
    }
