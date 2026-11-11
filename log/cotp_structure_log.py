import ast
import sys
from collections import defaultdict
from pathlib import Path

from ui.ui_properties import outputMenuOptions

PROJECT_DIR = Path(
    getattr(sys, "_MEIPASS", Path(__file__).resolve().parent.parent)
)
SCRIPT_DIR = PROJECT_DIR / "Script"

MENU_GENERATORS = {
    "Indoor Scene Prompt": "generateIndoorOutput",
    "Outdoor Scene Prompt": "generateOutdoorOutput",
    "Couple Prompt": "generateCouplePrompt",
    "Modeling Prompt": "generateModelingPrompt",
    "Random Rule L4D2": "ruleL4D2",
    "App Date Options": "dateAppOptions",
    "Short Story 1 - Curse Breaking Journey": "generateShortStory1",
    "Short Story 2 - Job Interview": "generateShortStory2",
    "Short Story 3 - Dating": "generateShortStory3",
    "Short Story 4 - Rebellious Past": "generateShortStory4",
}


def _menuOptions():
    return outputMenuOptions


def _functionDefinitions():
    functions = {}
    for sourcePath in SCRIPT_DIR.glob("*.py"):
        sourceTree = ast.parse(sourcePath.read_text(encoding="utf-8"))
        for node in sourceTree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                functions[node.name] = node
    return functions


def _resolve(node, values):
    while isinstance(node, ast.Name) and node.id in values:
        replacement = values[node.id]
        if replacement is node:
            break
        node = replacement
    return node


def _arrayName(node, values):
    node = _resolve(node, values)
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Call):
        if isinstance(node.value.func, ast.Name) and node.value.func.id == "globals":
            expression = node.slice
            if isinstance(expression, ast.JoinedStr):
                suffix = "".join(
                    part.value
                    for part in expression.values
                    if isinstance(part, ast.Constant)
                    and isinstance(part.value, str)
                )
                if suffix in ("Shoes", "Hair"):
                    return f"male{suffix}/female{suffix} (gender-dependent)"
    if isinstance(node, (ast.List, ast.Tuple)):
        valuesText = ", ".join(repr(ast.literal_eval(item)) for item in node.elts)
        return f"inline choices ({valuesText})"
    return ast.unparse(node)


class _StructureCollector:
    def __init__(self, functions):
        self.functions = functions
        self.entries = defaultdict(int)
        self.picks = defaultdict(int)

    def collectFunction(
        self,
        functionName,
        arguments=(),
        keywords=None,
        conditions=(),
        active=(),
    ):
        function = self.functions.get(functionName)
        if function is None or functionName in active:
            return

        keywords = keywords or {}
        parameters = [
            *function.args.posonlyargs,
            *function.args.args,
            *function.args.kwonlyargs,
        ]
        values = {}
        for index, parameter in enumerate(parameters):
            if index < len(arguments):
                values[parameter.arg] = arguments[index]
            elif parameter.arg in keywords:
                values[parameter.arg] = keywords[parameter.arg]

        self._visit(
            function,
            values,
            conditions,
            (*active, functionName),
        )

    def _record(self, kind, name, count, conditions, picks=None):
        condition = " and ".join(conditions) if conditions else ""
        key = (kind, name, condition)
        self.entries[key] += count
        self.picks[key] += count if picks is None else picks

    def _visit(self, node, values, conditions, active):
        if isinstance(node, ast.If):
            self._visit(node.test, values, conditions, active)
            condition = ast.unparse(node.test)
            for child in node.body:
                self._visit(child, values, (*conditions, f"if {condition}"), active)
            for child in node.orelse:
                self._visit(child, values, (*conditions, f"else {condition}"), active)
            return

        if isinstance(node, ast.IfExp):
            self._visit(node.test, values, conditions, active)
            condition = ast.unparse(node.test)
            self._visit(
                node.body,
                values,
                (*conditions, f"if {condition}"),
                active,
            )
            self._visit(
                node.orelse,
                values,
                (*conditions, f"else {condition}"),
                active,
            )
            return

        if isinstance(node, ast.Match):
            self._visit(node.subject, values, conditions, active)
            for case in node.cases:
                condition = ast.unparse(case.pattern)
                if case.guard is not None:
                    self._visit(case.guard, values, conditions, active)
                    condition += f" if {ast.unparse(case.guard)}"
                for child in case.body:
                    self._visit(
                        child,
                        values,
                        (*conditions, f"case {condition}"),
                        active,
                    )
            return

        if isinstance(node, (ast.For, ast.AsyncFor, ast.While)):
            self._visit(
                node.iter if hasattr(node, "iter") else node.test,
                values,
                conditions,
                active,
            )
            loop = ast.unparse(node.target if hasattr(node, "target") else node.test)
            for child in node.body:
                self._visit(child, values, (*conditions, f"loop {loop}"), active)
            for child in node.orelse:
                self._visit(child, values, (*conditions, f"after loop {loop}"), active)
            return

        if isinstance(node, ast.Call):
            for argument in (
                *node.args,
                *(keyword.value for keyword in node.keywords),
            ):
                self._visit(argument, values, conditions, active)

            isRandomCall = (
                isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "random"
            )
            if isRandomCall:
                method = node.func.attr
                if method in ("choice", "choices") and node.args:
                    array = _arrayName(node.args[0], values)
                    count = 1
                    if method == "choices":
                        countNode = next(
                            (
                                keyword.value
                                for keyword in node.keywords
                                if keyword.arg == "k"
                            ),
                            None,
                        )
                        if countNode is not None:
                            countNode = _resolve(countNode, values)
                            if isinstance(countNode, ast.Constant) and isinstance(
                                countNode.value, int
                            ):
                                count = countNode.value
                            else:
                                array = f"{array} (k={ast.unparse(countNode)})"
                    self._record("array", array, 1, conditions, picks=count)
                elif method in ("randint", "randrange", "uniform"):
                    bounds = ", ".join(
                        ast.unparse(_resolve(argument, values))
                        for argument in node.args
                    )
                    self._record(
                        "number",
                        f"random.{method}({bounds})",
                        1,
                        conditions,
                    )
                elif method == "random":
                    self._record("number", "random.random()", 1, conditions)
                return

            if isinstance(node.func, ast.Attribute):
                self._visit(node.func.value, values, conditions, active)
                return

            if isinstance(node.func, ast.Name) and node.func.id in self.functions:
                resolvedArguments = tuple(
                    _resolve(argument, values) for argument in node.args
                )
                resolvedKeywords = {
                    keyword.arg: _resolve(keyword.value, values)
                    for keyword in node.keywords
                    if keyword.arg is not None
                }
                self.collectFunction(
                    node.func.id,
                    resolvedArguments,
                    resolvedKeywords,
                    conditions,
                    active,
                )
            return

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for child in node.body:
                self._visit(child, values, conditions, active)
            return

        for child in ast.iter_child_nodes(node):
            self._visit(child, values, conditions, active)


def buildCotpStructure():
    menuOptions = _menuOptions()
    randomOption = menuOptions[0]
    generatorOptions = menuOptions[1:]
    if set(generatorOptions) != set(MENU_GENERATORS):
        raise ValueError(
            "The output menu options and COTP structure generator mapping differ"
        )

    functions = _functionDefinitions()
    sections = [
        "COTP Struct Details (mỗi lần tạo output sẽ gọi một generator; mỗi lời gọi random "
        "là một lượt rút riêng từ PRNG của Python; các nhánh điều kiện được ghi rõ):",
        "*n là số lần gọi; random.choices ghi thêm số phần tử được rút.",
        f"{randomOption}:",
        f"  - random.choice({len(generatorOptions)} lựa chọn) *1, "
        "sau đó chạy generator tương ứng bên dưới.",
    ]

    for menuName, functionName in MENU_GENERATORS.items():
        collector = _StructureCollector(functions)
        collector.collectFunction(functionName)
        arrays = []
        numbers = []
        for key, count in collector.entries.items():
            kind, name, condition = key
            item = f"{name} *{count} calls"
            if kind == "array" and collector.picks[key] != count:
                item += f" ({collector.picks[key]} picks)"
            if condition:
                item += f" [{condition}]"
            (arrays if kind == "array" else numbers).append(item)

        sections.append(f"{menuName}:")
        sections.append("  Arrays:")
        sections.extend(f"    - {item}" for item in arrays or ["none"])
        sections.append("  Random numbers:")
        sections.extend(f"    - {item}" for item in numbers or ["none"])

    return "\n".join(sections)
