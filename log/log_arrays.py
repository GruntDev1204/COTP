import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from log.log import (
    LOG_DIR,
    buildFullStats,
    getArrayCommaIssues,
    getArrayDuplicates,
    getArraySizes,
    getArraySourcePaths,
)
from log.cotp_structure_log import buildCotpStructure

ARRAY_LOG_PATH = LOG_DIR / "log_arrays.txt"


def logArrays(logDir=LOG_DIR):
    logDir.mkdir(parents=True, exist_ok=True)
    statsText, _ = buildFullStats()
    arraySizes = getArraySizes()
    duplicateArrays = getArrayDuplicates()
    commaIssues = getArrayCommaIssues()
    arraySourcePaths = getArraySourcePaths()
    arraySizeLines = "\n".join(
        f"Array size - {name} ({arraySourcePaths[name]}): {size}"
        for name, size in sorted(arraySizes.items(), key=lambda item: item[0].casefold())
    )
    duplicateLines = [
        f"=== DUPLICATE ITEMS ({sum(map(len, duplicateArrays.values()))} duplicated values) ==="
    ]
    if duplicateArrays:
        duplicateLines.extend(
            f"Duplicate item - {arrayName} ({arraySourcePaths[arrayName]}): "
            f"{item!r} ({count} occurrences)"
            for arrayName, duplicates in sorted(
                duplicateArrays.items(), key=lambda item: item[0].casefold()
            )
            for item, count in duplicates
        )
    else:
        duplicateLines.append("No duplicate items found.")
    duplicateText = "\n".join(duplicateLines)
    commaLines = [
        f"=== POSSIBLE MISSING COMMAS ({sum(map(len, commaIssues.values()))} issues) ==="
    ]
    if commaIssues:
        commaLines.extend(
            f"Possible missing comma - {arrayName} ({arraySourcePaths[arrayName]}): "
            f"line {lineNumber} ({item!r})"
            for arrayName, issues in sorted(
                commaIssues.items(), key=lambda item: item[0].casefold()
            )
            for lineNumber, item in issues
        )
    else:
        commaLines.append("No possible missing commas found.")
    commaText = "\n".join(commaLines)
    cotpStructure = buildCotpStructure()
    logContent = (
        f"{statsText}\n"
        f"=== ARRAY SIZES ({len(arraySizes)} arrays, alphabetical ascending) ===\n"
        f"{arraySizeLines}\n"
        f"{duplicateText}\n"
        f"{commaText}\n"
        f"{'=' * 87}\n"
        f"{cotpStructure}\n"
        f"{'=' * 87}\n\n"
    )
    with (logDir / ARRAY_LOG_PATH.name).open("a", encoding="utf-8") as logFile:
        logFile.write(logContent)
    print(f"Logged full stats and array sizes to {logDir / ARRAY_LOG_PATH.name}")


if __name__ == "__main__":
    logArrays()
