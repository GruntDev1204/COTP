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

    def iterComparableItems(item):
        if isinstance(item, str):
            yield item
        elif isinstance(item, (tuple, list)):
            for nestedItem in item:
                if isinstance(nestedItem, (str, tuple, list)):
                    yield from iterComparableItems(nestedItem)
        else:
            try:
                hash(item)
            except TypeError:
                return
            yield item

    for varName, value in globals().items():
        if not isinstance(value, list):
            continue
        duplicates = [
            (item, count)
            for item, count in Counter(
                comparableItem
                for arrayItem in value
                for comparableItem in iterComparableItems(arrayItem)
            ).items()
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
        couplePromptTotal,
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
        + couplePromptTotal
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
        "couplePrompt": couplePromptTotal,
        "modelingMale": modelingMaleTotal,
        "modelingFemale": modelingFemaleTotal,
        "modelingPrompt": modelingPromptTotal,
        "total": totalCombinations,
    }
    statsText = f"""📊📊📊 Tổng không gian trạng thái của COTP (COTP - Total Combinations and Possibilities):
Updated Timestamp (latest): {timestamp}
=================================================================================================
🖼️🎨 PROMPTS FOR AI ART MENU:
    - Indoor Scene Prompt: {indoorTotal:,} [👉 {formatNumber(abs(indoorTotal), 2)}]
    - Outdoor Scene Prompt: {outdoorTotal:,} [👉 {formatNumber(abs(outdoorTotal), 2)}]
    - Couple Prompt: {couplePromptTotal:,} [👉 {formatNumber(abs(couplePromptTotal), 2)}]
    - Modeling Prompt: {modelingMaleTotal:,} (Male) + {modelingFemaleTotal:,} (Female)= {modelingPromptTotal:,} [👉 {formatNumber(abs(modelingPromptTotal), 2)}]
🕹️🎮 ANY GAMES RULE CUSTOM:
    - L4D2 Case: {l4d2Total:,} [👉 {formatNumber(abs(l4d2Total), 2)}]
    - appDateTotal: {appDateTotal:,} [👉 {formatNumber(abs(appDateTotal), 2)}]
🎲📖 SHORT STORIES MENU:
    - Short Story 1 - Curse Breaking Journey: {storyTotal:,} [👉 {formatNumber(abs(storyTotal), 2)}]
    - Short Story 2 - Job Interview: {story2Total:,} [👉 {formatNumber(abs(story2Total), 2)}]
    - Short Story 3 - Dating: {story3Total:,} [👉 {formatNumber(abs(story3Total), 2)}]
    - Short Story 4 - Rebellious Past: {story4Total:,} [👉 {formatNumber(abs(story4Total), 2)}]
📜TOTAL : {totalCombinations:,} [👉 {formatNumber(abs(totalCombinations), 2)}]
=====================================================================================================
📊📢📢📢 Phân tích chi tiết (Details):
🖼️🎨 PROMPTS FOR AI ART MENU:
    - Indoor combinations (digits): {len(str(indoorTotal))}
    - Outdoor combinations (digits): {len(str(outdoorTotal))}
    - Couple Prompt combinations (digits): {len(str(couplePromptTotal))}
    - Modeling Prompt combinations (digits): {len(str(modelingMaleTotal))} (Male) + {len(str(modelingFemaleTotal))} (Female)= {len(str(modelingPromptTotal))}
🕹️🎮 ANY GAMES RULE CUSTOM:
    - L4D2 scenarios (digits): {len(str(l4d2Total))}
    - appDate combinations (digits): {len(str(appDateTotal))}
🎲📖 SHORT STORIES MENU:
    - Story 1 - Curse Breaking Journey combinations (digits): {len(str(storyTotal))}
    - Story 2 - Job Interview combinations (digits): {len(str(story2Total))}
    - Story 3 - Dating combinations (digits): {len(str(story3Total))}
    - Story 4 - Rebellious Past combinations (digits): {len(str(story4Total))}
📜TOTAL combinations (digits): {len(str(totalCombinations))}
"""
    return statsText, stats
