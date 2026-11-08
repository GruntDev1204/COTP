import ast
import io
import sys
import tokenize
from collections import Counter
from datetime import datetime
from pathlib import Path

from data.data import *
from Script.caculate_pool import (
    caculateModelingPromptPool,
    caculateQuantity,
    formatNumber,
)

PROJECT_DIR = Path(
    getattr(sys, "_MEIPASS", Path(__file__).resolve().parent.parent)
)
LOG_DIR = PROJECT_DIR / "log"
DATA_DIR = PROJECT_DIR / "data"


def getArraySizes():
    return {
        varName: len(value)
        for varName, value in globals().items()
        if isinstance(value, list)
    }


def getArraySourcePaths():
    arrayValues = {
        varName: value
        for varName, value in globals().items()
        if isinstance(value, list)
    }
    sourcePaths = {}

    def collectAssignedNames(target):
        if isinstance(target, ast.Name):
            return {target.id}
        if isinstance(target, (ast.Tuple, ast.List)):
            return set().union(
                *(collectAssignedNames(element) for element in target.elts)
            )
        return set()

    for sourcePath in DATA_DIR.glob("*.py"):
        module = sys.modules.get(f"data.{sourcePath.stem}")
        if module is None:
            continue
        sourceTree = ast.parse(sourcePath.read_text(encoding="utf-8"))
        declaredNames = set()
        for node in sourceTree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    declaredNames.update(collectAssignedNames(target))
            elif isinstance(node, ast.AnnAssign):
                declaredNames.update(collectAssignedNames(node.target))

        for arrayName in declaredNames & arrayValues.keys():
            if getattr(module, arrayName, None) is arrayValues[arrayName]:
                relativePath = sourcePath.relative_to(PROJECT_DIR).as_posix()
                sourcePaths.setdefault(arrayName, f"./{relativePath}")

    return sourcePaths


def getArrayDuplicates():
    duplicateArrays = {}
    for varName, value in globals().items():
        if not isinstance(value, list):
            continue
        duplicates = [
            (item, count)
            for item, count in Counter(value).items()
            if count > 1
        ]
        if duplicates:
            duplicateArrays[varName] = duplicates
    return duplicateArrays


def _getAdjacentStringLiteralLines(sourceText, arrayNode):
    issues = []
    for element in arrayNode.elts:
        if not isinstance(element, ast.Constant) or not isinstance(element.value, str):
            continue
        elementSource = ast.get_source_segment(sourceText, element)
        if elementSource is None:
            continue
        stringTokens = [
            token
            for token in tokenize.generate_tokens(io.StringIO(elementSource).readline)
            if token.type == tokenize.STRING
        ]
        if len(stringTokens) > 1:
            lineNumber = element.lineno + stringTokens[1].start[0] - 1
            issues.append((lineNumber, element.value))
    return issues


def getArrayCommaIssues():
    commaIssues = {}
    for arrayName, relativePath in getArraySourcePaths().items():
        sourcePath = (PROJECT_DIR / relativePath).resolve()
        sourceText = sourcePath.read_text(encoding="utf-8")
        sourceTree = ast.parse(sourceText)
        for node in sourceTree.body:
            if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.List):
                continue
            if not any(
                isinstance(target, ast.Name) and target.id == arrayName
                for target in node.targets
            ):
                continue
            issues = _getAdjacentStringLiteralLines(sourceText, node.value)
            if issues:
                commaIssues[arrayName] = issues
            break
    return commaIssues


def buildFullStats(timestamp=None):
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    (
        indoorTotal,
        outdoorTotal,
        storyTotal,
        story2Total,
        story3Total,
        story4Total,
        l4d2Total,
        appDateTotal,
        lovelyPromptTotal,
        modelingPromptTotal,
    ) = caculateQuantity()
    modelingMaleTotal, modelingFemaleTotal = caculateModelingPromptPool()
    totalCombinations = (
        indoorTotal
        + outdoorTotal
        + storyTotal
        + story2Total
        + story3Total
        + story4Total
        + l4d2Total
        + appDateTotal
        + lovelyPromptTotal
        + modelingPromptTotal
    )

    stats = {
        "indoor": indoorTotal,
        "outdoor": outdoorTotal,
        "story1": storyTotal,
        "story2": story2Total,
        "story3": story3Total,
        "story4": story4Total,
        "l4d2": l4d2Total,
        "appDate": appDateTotal,
        "lovelyPrompt": lovelyPromptTotal,
        "modelingMale": modelingMaleTotal,
        "modelingFemale": modelingFemaleTotal,
        "modelingPrompt": modelingPromptTotal,
        "total": totalCombinations,
    }
    statsText = f"""📊📊📊 Tổng hợp nội dung có thể tạo bởi COTP (latest):
Updated Timestamp: {timestamp}
Cảnh Indoor: {indoorTotal:,} [👉 {formatNumber(abs(indoorTotal), 2)}]
Cảnh Outdoor: {outdoorTotal:,} [👉 {formatNumber(abs(outdoorTotal), 2)}]
L4D2 Case: {l4d2Total:,} [👉 {formatNumber(abs(l4d2Total), 2)}]
appDateTotal: {appDateTotal:,} [👉 {formatNumber(abs(appDateTotal), 2)}]
Short Story 1 - Curse Breaking Journey: {storyTotal:,} [👉 {formatNumber(abs(storyTotal), 2)}]
Short Story 2 - Job Interview: {story2Total:,} [👉 {formatNumber(abs(story2Total), 2)}]
Short Story 3 - Dating: {story3Total:,} [👉 {formatNumber(abs(story3Total), 2)}]
Short Story 4 - Rebellious Past: {story4Total:,} [👉 {formatNumber(abs(story4Total), 2)}]
Lovely Prompt: {lovelyPromptTotal:,} [👉 {formatNumber(abs(lovelyPromptTotal), 2)}]
Modeling Prompt Male: {modelingMaleTotal:,} [👉 {formatNumber(abs(modelingMaleTotal), 2)}]
Modeling Prompt Female: {modelingFemaleTotal:,} [👉 {formatNumber(abs(modelingFemaleTotal), 2)}]
Modeling Prompt: {modelingMaleTotal:,} + {modelingFemaleTotal:,} = {modelingPromptTotal:,} [👉 {formatNumber(abs(modelingPromptTotal), 2)}]
TOTAL : {totalCombinations:,} [👉 {formatNumber(abs(totalCombinations), 2)}]
=======================================================================================
📊📢📢📢 Phân tích chi tiết:
Độ dài của con số tổng tổ hợp khả năng của Indoor: {len(str(indoorTotal))} số
Độ dài của con số tổng tổ hợp khả năng của Outdoor: {len(str(outdoorTotal))} số
Độ dài của con số tổng kịch bản của L4D2: {len(str(l4d2Total))} số
Độ dài của con số tổng tổ hợp khả năng của appDate: {len(str(appDateTotal))} số
Độ dài của con số tổng tổ hợp khả năng của Story 1 - Curse Breaking Journey: {len(str(storyTotal))} số
Độ dài của con số tổng tổ hợp khả năng của Story 2 - Job Interview: {len(str(story2Total))} số
Độ dài của con số tổng tổ hợp khả năng của Story 3 - Dating: {len(str(story3Total))} số
Độ dài của con số tổng tổ hợp khả năng của Story 4 - Rebellious Past: {len(str(story4Total))} số
Độ dài của con số tổng tổ hợp khả năng của Lovely Prompt: {len(str(lovelyPromptTotal))} số
Độ dài của con số tổng tổ hợp khả năng của Modeling Prompt Male: {len(str(modelingMaleTotal))} số
Độ dài của con số tổng tổ hợp khả năng của Modeling Prompt Female: {len(str(modelingFemaleTotal))} số
Độ dài của con số tổng tổ hợp khả năng của Modeling Prompt: {len(str(modelingPromptTotal))} số
Độ dài của con số tổng tổ hợp : {len(str(totalCombinations))} số
"""
    return statsText, stats
