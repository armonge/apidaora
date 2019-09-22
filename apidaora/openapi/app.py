from typing import Any, Callable, Sequence

from ..core.app import AsgiCallable, asgi_app


def operations_app(operations: Sequence[Callable[..., Any]]) -> AsgiCallable:
    routes = []

    for operation in operations:
        routes.append(operation.__route__)  # type: ignore

    return asgi_app(routes)


def spec_app() -> None:
    ...