import json
import re
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from log.log import LOG_DIR, buildFullStats, formatNumber, getArraySizes

STATS_LOG_PATH = LOG_DIR / "log_stats.txt"
BASELINE_PATH = LOG_DIR / ".log_status_baseline.json"
LEGACY_LOG_PATH = LOG_DIR / "data.txt"


def readLegacySnapshot(logPath):
    if not logPath.exists():
        return None

    logText = logPath.read_text(encoding="utf-8")
    entries = re.split(r"(?=📊📊📊 Tổng hợp nội dung)", logText)
    for entry in reversed(entries):
        totalMatch = re.search(r"^Tổng:\s*([\d,]+)", entry, re.MULTILINE)
        if totalMatch is None:
            continue

        stats = {"total": int(totalMatch.group(1).replace(",", ""))}
        for key, label in (
            ("modelingMale", "Modeling Prompt Male:"),
            ("modelingFemale", "Modeling Prompt Female:"),
        ):
            match = re.search(
                rf"^{re.escape(label)}\s*([\d,]+)", entry, re.MULTILINE
            )
            if match:
                stats[key] = int(match.group(1).replace(",", ""))
        stats["arrays"] = {
            name: int(size)
            for name, size in re.findall(
                r"^Array size - ([^:\r\n]+):\s*(\d+)", entry, re.MULTILINE
            )
        }
        return stats
    return None


def loadPreviousSnapshot(logDir):
    baselinePath = logDir / BASELINE_PATH.name
    if baselinePath.exists():
        return json.loads(baselinePath.read_text(encoding="utf-8"))
    return readLegacySnapshot(logDir / LEGACY_LOG_PATH.name)


def buildGrowthAnalysis(previousSnapshot, currentStats, currentArraySizes):
    growthLines = ["📈 PHÂN TÍCH TĂNG TRƯỞNG:"]
    if previousSnapshot is None:
        growthLines.append("Chưa có snapshot trước đó để so sánh.")
        previousArraySizes = None
    else:
        previousTotal = previousSnapshot["total"]
        currentTotal = currentStats["total"]
        totalDelta = currentTotal - previousTotal
        percentageDelta = totalDelta / previousTotal * 100 if previousTotal else 0
        growthLines.extend(
            [
                f"Tổng trước: {previousTotal:,} [👉 {formatNumber(abs(previousTotal), 2)}]",
                f"Tổng hiện tại: {currentTotal:,} [👉 {formatNumber(abs(currentTotal), 2)}]",
                f"Chênh lệch tổng: {totalDelta:+,} [👉 {formatNumber(abs(totalDelta), 2)}]",
                f"Phần trăm thay đổi: {percentageDelta:+.2f}%",
            ]
        )
        for key, label in (
            ("modelingMale", "Modeling Prompt Male"),
            ("modelingFemale", "Modeling Prompt Female"),
        ):
            if key in previousSnapshot:
                delta = currentStats[key] - previousSnapshot[key]
                growthLines.append(
                    f"{label} chênh lệch: {delta:+,} "
                    f"[👉 {formatNumber(abs(delta), 2)}]"
                )
        previousArraySizes = previousSnapshot.get("arrays")

    changedArrays = []
    if previousArraySizes is not None:
        for name in sorted(set(previousArraySizes) | set(currentArraySizes)):
            previousSize = previousArraySizes.get(name, 0)
            currentSize = currentArraySizes.get(name, 0)
            delta = currentSize - previousSize
            if delta:
                changedArrays.append(
                    f"{name}: {previousSize} → {currentSize} ({delta:+})"
                )

    growthLines.extend(["", "Thay đổi kích thước mảng:"])
    if previousArraySizes is None:
        growthLines.append("Chưa có snapshot kích thước mảng trước đó để so sánh.")
    elif changedArrays:
        growthLines.extend(changedArrays)
    else:
        growthLines.append("Kích thước các mảng không thay đổi.")
    return "\n".join(growthLines)


def logStats(logDir=LOG_DIR):
    logDir.mkdir(parents=True, exist_ok=True)
    statsText, currentStats = buildFullStats()
    currentArraySizes = getArraySizes()
    previousSnapshot = loadPreviousSnapshot(logDir)
    growthText = buildGrowthAnalysis(previousSnapshot, currentStats, currentArraySizes)
    with (logDir / STATS_LOG_PATH.name).open("a", encoding="utf-8") as logFile:
        logFile.write(f"{statsText}\n{growthText}\n{'=' * 87}\n\n")

    baseline = {**currentStats, "arrays": currentArraySizes}
    (logDir / BASELINE_PATH.name).write_text(
        json.dumps(baseline, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Logged full stats and growth analysis to {logDir / STATS_LOG_PATH.name}")


if __name__ == "__main__":
    logStats()
