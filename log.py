from data.data import *
from datetime import datetime
from Script.script import caculateQuantity, formatNumber


def print_array_sizes():
    global_vars = globals()
    for var_name, value in global_vars.items():
        if isinstance(value, list):
            print(f"{var_name}: {len(value)} phần tử")


print_array_sizes()


def check_duplicates_in_array(array_name, array):
    """Kiem tra trung lap trong mot mang"""
    duplicates = []
    seen = set()

    for item in array:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)

    if duplicates:
        print(f"[DUPLICATE] {array_name}: {len(duplicates)} items trùng lặp")
        for dup in set(duplicates):
            count = duplicates.count(dup)
            print(f"   - '{dup}' lặp lại {count} lan")
    else:
        print(f"[OK] {array_name} : Không có trùng lặp")

    return len(duplicates)


def check_cross_array_duplicates():
    """Kiem tra trung lap giua cac mang khac nhau"""
    print("\n=== KIEM TRA TRUNG LAP GIUA CAC MANG ===")
    print("=" * 50)

    # Tao dictionary tat ca arrays
    all_arrays = {
        "ending": ending,
        "comment": comment,
        "starting": starting,
        "emojiMeme": emojiMeme,
        "cuteEmojis": cuteEmojis,
        "foodEmojis": foodEmojis,
        "emojiStatus": emojiStatus,
        "animalsEmojis": animalsEmojis,
        "NPCEmojis": NPCEmojis,
        "titleEmojis": titleEmojis,
        "entertainmentIcons": entertainmentIcons,
        "sportsIcons": sportsIcons,
        "chaosEmojis": chaosEmojis,
        "colors": colors,
        "quantities": quantities,
        "shapes": shapes,
        "emotionPunctuations": emotionPunctuations,
        "status": status,
        "indoorStatus": indoorStatus,
        "indoorLocations": indoorLocations,
        "indoorMaterials": indoorMaterials,
        "indoorItems": indoorItems,
        "indoorItemStatus": indoorItemStatus,
        "indoorLightVerb": indoorLightVerb,
        "indoorItemLightningSource": indoorItemLightningSource,
        "indoorObjectItems": indoorObjectItems,
        "liveNPCs": liveNPCs,
        "liveNPCApperances": liveNPCApperances,
        "liveNPCEmotions": liveNPCEmotions,
        "liveNPCActions": liveNPCActions,
        "nameNPC": nameNPC,
        "NPCjobs": NPCjobs,
        "outdoorView": outdoorView,
        "outDoorStatus": outDoorStatus,
        "weatherConditions": weatherConditions,
        "times": times,
        "outDoorSkyStrongObjects": outDoorSkyStrongObjects,
        "outDoorSkyStrongObjectStatus": outDoorSkyStrongObjectStatus,
        "outDoorSkyObjects": outDoorSkyObjects,
        "outdoorObjectDensity": outdoorObjectDensity,
        "outdoorObjects": outdoorObjects,
        "businesses": businesses,
        "magicTypes": magicTypes,
        "proverbs": proverbs,
        "slogan": slogan,
        "sourceInfo": sourceInfo,
        "gpsLocations": gpsLocations,
        "companies": companies,
        "buildings": buildings,
        "loveIcons" : loveIcons,
        "yearOfBirth" : yearOfBirth,
        "nameUser" : nameUser,
        "callName" : callName,
        "mapsL4D2": mapsL4D2,
        "charactersL4D2": charactersL4D2,
        "grenadesL4D2": grenadesL4D2,
        "pickupsL4D2": pickupsL4D2,
        "medicineL4D2": medicineL4D2,
        "weaponsL4D2": weaponsL4D2,
        "meleeL4D2": meleeL4D2,
        "playerRulesL4D2": playerRulesL4D2,
        "fashionHair": fashionHair,
    }

    # Kiem tra trung lap trong tung mang
    total_duplicates = 0
    print("\n--- KIỂM TRA THỐNG KÊ ITEM BỊ LẶP ---")
    print("-" * 50)

    for name, array in all_arrays.items():
        if isinstance(array, list):
            duplicates = check_duplicates_in_array(name, array)
            total_duplicates += duplicates

    # Kiem tra trung lap giua cac arrays
    print(f"\n=== TỔNG KẾT ===")
    print(f"   - TỔNG SỐ MẢNG: {len(all_arrays)}")
    print(f"   - TỔNG ITEM BỊ LẶP: {total_duplicates}")

    if total_duplicates == 0:
        print("ĐÉO LẶP GÌ HẾT! ĐMM ĐƯỢC ĐÓ CON TRAI!")
    else:
        print("CẦN KTRA LẠI CÁC ITEM BỊ LẶP DDUMAMAAY THẰNG RANH CON NÀY!")


def log_combinations_to_file():
    """Log tổng tổ hợp ra file txt với timestamp"""
    try:
        # Tính toán tổng tổ hợp
        (
            indoor_total,
            outdoor_total,
            story_total,
            story2_total,
            short_story3_total,
            shortStory4Total,
            L4D2caseTotal,
            app_date_total,
            lovely_prompt_total,
        ) = caculateQuantity()
        total_combinations = (
            indoor_total
            + outdoor_total
            + story_total
            + story2_total
            + short_story3_total
            + shortStory4Total
            + L4D2caseTotal
            + app_date_total
            + lovely_prompt_total
        )

        # Format timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Format số liệu giống GUI
        log_content = f"""📊📊📊 Tổng hợp nội dung có thể tạo bởi COTP (latest) - {current_time}:
Cảnh Indoor: {indoor_total:,} [👉 {formatNumber(abs(indoor_total), 2)}]
Cảnh Outdoor: {outdoor_total:,} [👉 {formatNumber(abs(outdoor_total), 2)}]
Short Story 1 - Curse Breaking Journey: {story_total:,} [👉 {formatNumber(abs(story_total), 2)}]
Short Story 2 - Job Interview: {story2_total:,} [👉 {formatNumber(abs(story2_total), 2)}]
Short Story 3 - Dating: {short_story3_total:,} [👉 {formatNumber(abs(short_story3_total), 2)}]
Short Story 4 - Rebellious Past: {shortStory4Total:,} [👉 {formatNumber(abs(shortStory4Total), 2)}]
Kịch bản L4D2: {L4D2caseTotal:,} [👉 {formatNumber(abs(L4D2caseTotal), 2)}]
App Date Options: {app_date_total:,} [👉 {formatNumber(abs(app_date_total), 2)}]
Lovely Prompt: {lovely_prompt_total:,} [👉 {formatNumber(abs(lovely_prompt_total), 2)}]
Tổng: {total_combinations:,} [👉 {formatNumber(abs(total_combinations), 2)}]
=======================================================================================
📊📢📢📢 Phân tích chi tiết:
Độ dài của con số tổng tổ hợp khả năng của Indoor: {len(str(indoor_total))} số
Độ dài của con số tổng tổ hợp khả năng của Outdoor: {len(str(outdoor_total))} số
Độ dài của con số tổng tổ hợp khả năng của Story 1: {len(str(story_total))} số
Độ dài của con số tổng tổ hợp khả năng của Story 2: {len(str(story2_total))} số
Độ dài của con số tổng tổ hợp khả năng của Story 3: {len(str(short_story3_total))} số
Độ dài của con số tổng tổ hợp khả năng của Story 4: {len(str(shortStory4Total))} số
Độ dài của con số tổng tổ kịch bản của L4D2: {len(str(L4D2caseTotal))} số
Độ dài của con số tổng tổ hợp khả năng của App Date Options: {len(str(app_date_total))} số
Độ dài của con số tổng tổ hợp khả năng của Lovely Prompt: {len(str(lovely_prompt_total))} số

Độ dài của con số tổng tổ hợp: {len(str(total_combinations))} số
=======================================================================================

"""

        # Ghi vào file
        with open("data.txt", "a", encoding="utf-8") as f:
            f.write(log_content)

        print(f"✅ Đã log tổng tổ hợp ra file data.txt - {current_time}")

        # Tính toán tăng trưởng
        calculate_growth()

    except Exception as e:
        print(f"❌ Lỗi khi log: {e}")


def calculate_growth():
    """Tính toán tăng trưởng từ 2 entry mới nhất"""
    try:
        # Đọc file data.txt
        with open("data.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Tìm các dòng "Tổng:"
        total_lines = []
        for i, line in enumerate(lines):
            if line.strip().startswith("Tổng:"):
                total_lines.append((i, line.strip()))

        if len(total_lines) < 2:
            print("📊 Chưa đủ dữ liệu để so sánh (cần ít nhất 2 entries)")
            return

        # Lấy 2 entry mới nhất
        latest_line = total_lines[-1][1]  # Latest
        previous_line = total_lines[-2][1]  # Previous

        # Extract số từ dòng "Tổng:"
        def extract_number(line):
            # Format: "Tổng: 123,456,789 [👉 1.2×10^8]"
            parts = line.split()
            if len(parts) >= 2:
                return int(parts[1].replace(",", ""))
            return 0

        latest_total = extract_number(latest_line)
        previous_total = extract_number(previous_line)

        if latest_total == 0 or previous_total == 0:
            print("📊 Không thể parse số từ file log")
            return

        # Tính toán tăng trưởng
        increase = latest_total - previous_total
        percentage_increase = (increase / previous_total) * 100

        # Format kết quả
        growth_info = f"""
📈 PHÂN TÍCH TĂNG TRƯỞNG:
Tổng trước: {previous_total:,} [👉 {formatNumber(abs(previous_total), 2)}]
Tổng hiện tại: {latest_total:,} [👉 {formatNumber(abs(latest_total), 2)}]
Tăng: +{increase:,} [👉 +{formatNumber(abs(increase), 2)}]
Phần trăm tăng: +{percentage_increase:.2f}%
=======================================================================================

"""

        # Ghi thêm vào file
        with open("data.txt", "a", encoding="utf-8") as f:
            f.write(growth_info)

        print(f"📈 Đã tính toán tăng trưởng: +{percentage_increase:.2f}%")

    except Exception as e:
        print(f"❌ Lỗi khi tính tăng trưởng: {e}")


if __name__ == "__main__":
    print("COTP DATA DUPLICATE CHECKER")
    print("=" * 50)
    check_cross_array_duplicates()

    # Thêm log combinations
    print("\n" + "=" * 50)
    log_combinations_to_file()
