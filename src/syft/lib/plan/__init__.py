# stdlib
from typing import Any as TypeAny
from typing import List as TypeList
from typing import Tuple as TypeTuple

# syft relative
from ...ast import add_classes
from ...ast import add_methods
from ...ast import add_modules
from ...ast.globals import Globals
from ...core.plan.plan import Plan


def create_plan_ast(client: TypeAny = None) -> Globals:
    """Adds plan classes to the ast

    Args:
        client: client. Defaults to None.

    Returns:
        Globals: plan ast
    """
    ast = Globals(client)

    modules = [
        "syft",
        "syft.core",
        "syft.core",
        "syft.core.plan",
        "syft.core.plan.plan",
    ]

    classes: TypeList[TypeTuple[str, str, TypeAny]] = [
        (
            "syft.core.plan.Plan",
            "syft.core.plan.Plan",
            Plan,
        ),
    ]

    methods: TypeList[TypeTuple[str, str]] = [
        ("syft.core.plan.Plan.__call__", "syft.lib.python._SyNone"),
    ]

    add_modules(ast, modules)
    add_classes(ast, classes)
    add_methods(ast, methods)

    for klass in ast.classes:
        klass.create_pointer_class()
        klass.create_send_method()
        klass.create_storable_object_attr_convenience_methods()

    return ast
