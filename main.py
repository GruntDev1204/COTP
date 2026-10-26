import tkinter as tk
from tkinter import ttk
from Script.script import *
from Script.caculate_pool import *


def generateScene():
    scene = ""
    option = sceneType.get()

    if option == "RANDOM 🎲🎲🎲":
        option = random.choice(
            [
                "Cảnh Indoor",
                "Cảnh Outdoor",
                "Random Rule L4D2",
                "App Date Options",
                "Lovely Prompt",
                "Short Story 1 - Curse Breaking Journey",
                "Short Story 2 - Job Interview",
                "Short Story 3 - Dating",
                "Short Story 4 - Rebellious Past",
            ]
        )

    match option:
        case "Cảnh Indoor":
            scene = generateIndoorScene()
        case "Cảnh Outdoor":
            scene = generateOutdoorScene()
        case "Lovely Prompt":
            scene = generateLovelyPromt()
        case "Random Rule L4D2":
            scene = ruleL4D2()
        case "App Date Options":
            scene = dateAppOptions()
        case "Short Story 1 - Curse Breaking Journey":
            scene = generateShortStory1()
        case "Short Story 2 - Job Interview":
            scene = generateShortStory2()
        case "Short Story 3 - Dating":
            scene = generateShortStory3()
        case "Short Story 4 - Rebellious Past":
            scene = generateShortStory4()
        case _:
            scene = generateIndoorScene()

    outputText.delete("1.0", tk.END)
    outputText.tag_configure(
        "title",
        font=(
            "Segoe UI",
            13,
            "bold",
        ),
        foreground="#FF6B6B",
    )
    outputText.tag_configure(
        "location", font=("Segoe UI", 13, "bold"), foreground="#4ECDC4"
    )
    outputText.tag_configure(
        "content", font=("Segoe UI", 13, "bold"), foreground="#E0E0E0"
    )
    outputText.tag_configure(
        "icons", font=("Segoe UI", 13, "normal"), foreground="#FFE66D"
    )

    if isinstance(scene, tuple):
        scene = "\n".join(scene)

    lines = scene.split("\n")  
    for i, line in enumerate(lines):
        if i == 0:
            outputText.insert(tk.END, line + "\n", "title")
        else:
            # Nếu dòng trống → vẫn insert dòng trống
            if line == "":
                outputText.insert(tk.END, "\n")
            else:
                if "Bên trong" in line or "đã" in line:
                    parts = line.split(", ", 1)
                    if len(parts) > 1:
                        outputText.insert(tk.END, parts[0] + ", ", "location")
                        outputText.insert(tk.END, parts[1], "content")
                    else:
                        outputText.insert(tk.END, line, "content")
                else:
                    if i == len(lines) - 1:
                        icon_start = None
                        for icon in all_icons:
                            pos = line.find(icon)
                            if pos != -1:
                                icon_start = pos
                                break
                        if icon_start is not None:
                            outputText.insert(tk.END, line[:icon_start], "content")
                            outputText.insert(tk.END, line[icon_start:], "icons")
                        else:
                            outputText.insert(tk.END, line, "content")
                    else:
                        outputText.insert(tk.END, line, "content")
                outputText.insert(tk.END, "\n")

    outputText.config(padx=15, pady=15)


def copySceneToClipboard():
    scene = outputText.get("1.0", tk.END).strip()
    if scene:
        root.clipboard_clear()
        root.clipboard_append(scene)
        copy_button.config(text="📋 Đã copy!", bg="#89F900", fg="black")
        root.after(
            1500, lambda: copy_button.config(text="📋 Copy", bg="#E9F900", fg="black")
        )


def copyStatsToClipboard():
    stats_text = (
        f"📊📊📊 Tổng hợp nội dung có thể tạo bởi COTP (latest):\n"
        f"Cảnh Indoor: {indoor_combinations:,} [👉 {formatNumber(abs(indoor_combinations), 2)}]\n"
        f"Cảnh Outdoor: {outdoor_combinations:,} [👉 {formatNumber(abs(outdoor_combinations), 2)}]\n"
        f"L4D2 Case: {L4D2caseTotal:,} [👉 {formatNumber(abs(L4D2caseTotal), 2)}]\n"
        f"appDateTotal: {appDateTotal:,} [👉 {formatNumber(abs(appDateTotal), 2)}]\n"
        f"Short Story 1 - Curse Breaking Journey: {story_combinations:,} [👉 {formatNumber(abs(story_combinations), 2)}]\n"
        f"Short Story 2 - Job Interview: {story2_combinations:,} [👉 {formatNumber(abs(story2_combinations), 2)}]\n"
        f"Short Story 3 - Dating: {story3_combinations:,} [👉 {formatNumber(abs(story3_combinations), 2)}]\n"
        f"Short Story 4 - Rebellious Past: {shortStory4Total:,} [👉 {formatNumber(abs(shortStory4Total), 2)}]\n"
        f"Lovely Prompt: {lovelyPromptTotal:,} [👉 {formatNumber(abs(lovelyPromptTotal), 2)}]\n"
        f"📊📊📊 TOTAL : {total_combinations:,} [👉 {formatNumber(abs(total_combinations), 2)}]\n"
        f"=======================================================================================\n"
        f"📊📢📢📢 Phân tích chi tiết:\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Indoor: {len(str(indoor_combinations))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Outdoor: {len(str(outdoor_combinations))} số\n"
        f"Độ dài của con số tổng tổ kịch bản của L4D2: {len(str(L4D2caseTotal))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của appDate: {len(str(appDateTotal))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Story 1 - Curse Breaking Journey: {len(str(story_combinations))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Story 2 - Job Interview: {len(str(story2_combinations))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Story 3 - Dating: {len(str(story3_combinations))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Story 4 - Rebellious Past: {len(str(shortStory4Total))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Lovely Prompt: {len(str(lovelyPromptTotal))} số\n"
        f"Độ dài của con số tổng tổ hợp : {len(str(total_combinations))} số\n"
    )
    root.clipboard_clear()
    root.clipboard_append(stats_text)
    copy_stats_btn.config(text="📋 Đã copy!", bg="#89F900", fg="black")
    root.after(
        1500,
        lambda: copy_stats_btn.config(text="📋 Copy Stats", bg="#FBFF00", fg="black"),
    )


root = tk.Tk()
root.title("👑👑👑 CHAOTICS ONE-TIME-PROMPT (COTP) - by GruntDev1204 👑👑👑")
root.geometry("1500x800")
root.resizable(True, True)
root.configure(bg="#1E1E1E")

sceneType = tk.StringVar(value="🎲🎲🎲")  # <-- Đặt ở đây

(
    indoor_combinations,
    outdoor_combinations,
    story_combinations,
    story2_combinations,
    story3_combinations,
    shortStory4Total,
    L4D2caseTotal
    , appDateTotal
    , lovelyPromptTotal
) = caculateQuantity()
total_combinations = (
    indoor_combinations
    + outdoor_combinations
    + story_combinations
    + story2_combinations
    + story3_combinations
    + shortStory4Total
    + L4D2caseTotal
    + appDateTotal
    + lovelyPromptTotal
)

main_frame = tk.Frame(root, bg="#1E1E1E")
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Cấu hình grid cho main_frame để các cột/row co giãn
main_frame.grid_rowconfigure(0, weight=0)  # stats_frame
main_frame.grid_rowconfigure(1, weight=0)  # label + option + copy stats
main_frame.grid_rowconfigure(2, weight=0)  # render button
main_frame.grid_rowconfigure(3, weight=1)  # outputText
main_frame.grid_rowconfigure(4, weight=0)  # copy button
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=0)

# Tạo frame riêng cho bảng stats
stats_frame = tk.Frame(main_frame, bg="#000000")
stats_frame.grid(row=0, column=0, columnspan=3, sticky="nsew", pady=(0, 10))

# Cấu hình grid cho stats_frame để textbox co giãn
stats_frame.grid_rowconfigure(1, weight=1)
stats_frame.grid_columnconfigure(0, weight=1)

# Thanh cuộn ngang trên đầu bảng đen
xscroll = tk.Scrollbar(
    stats_frame,
    orient="horizontal",
    bg="#000000",
    troughcolor="#000000",
    bd=0,
    highlightthickness=0,
    relief="flat",
)
xscroll.grid(row=0, column=0, sticky="ew")

# Textbox stats (chiếm hết chiều ngang của stats_frame)
stats_detail_text = (
    f"📊📊📊 Tổng hợp nội dung có thể tạo bởi COTP (latest):\n"
    f"Cảnh Indoor: {indoor_combinations:,} [👉 {formatNumber(abs(indoor_combinations), 2)}]\n"
    f"Cảnh Outdoor: {outdoor_combinations:,} [👉 {formatNumber(abs(outdoor_combinations), 2)}]\n"
    f"Lovely Prompt: {lovelyPromptTotal:,} [👉 {formatNumber(abs(lovelyPromptTotal), 2)}]\n"
    f"L4D2 Case: {L4D2caseTotal:,} [👉 {formatNumber(abs(L4D2caseTotal), 2)}]\n"
    f"appDateTotal: {appDateTotal:,} [👉 {formatNumber(abs(appDateTotal), 2)}]\n"
    f"Short Story 1 - Curse Breaking Journey: {story_combinations:,} [👉 {formatNumber(abs(story_combinations), 2)}]\n"
    f"Short Story 2 - Job Interview: {story2_combinations:,} [👉 {formatNumber(abs(story2_combinations), 2)}]\n"
    f"Short Story 3 - Dating: {story3_combinations:,} [👉 {formatNumber(abs(story3_combinations), 2)}]\n"
    f"Short Story 4 - Rebellious Past: {shortStory4Total:,} [👉 {formatNumber(abs(shortStory4Total), 2)}]\n"
    f"📊📊📊 TOTAL : {total_combinations:,} [👉 {formatNumber(abs(total_combinations), 2)}]\n"
    f"=======================================================================================\n"
    f"📊📢📢📢 Phân tích chi tiết:\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Indoor: {len(str(indoor_combinations))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Outdoor: {len(str(outdoor_combinations))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Lovely Prompt: {len(str(lovelyPromptTotal))} số\n"
    f"Độ dài của con số tổng tổ kịch bản của L4D2: {len(str(L4D2caseTotal))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của appDate: {len(str(appDateTotal))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Story 1 - Curse Breaking Journey: {len(str(story_combinations))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Story 2 - Job Interview: {len(str(story2_combinations))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Story 3 - Dating: {len(str(story3_combinations))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Story 4 - Rebellious Past: {len(str(shortStory4Total))} số\n"
    f"Độ dài của con số tổng tổ hợp : {len(str(total_combinations))} số\n"
)

stats_detail_textbox = tk.Text(
    stats_frame,
    font=("Segoe UI", 10),
    fg="#00FFEA",
    bg="#000000",
    height=10,
    wrap="none",
    state="normal",
    padx=10,
    pady=10,
)
xscroll.config(command=stats_detail_textbox.xview)
stats_detail_textbox.insert("1.0", stats_detail_text)
stats_detail_textbox.config(state="disabled", xscrollcommand=xscroll.set)
stats_detail_textbox.grid(row=1, column=0, sticky="nsew")

# Nút copy stats ở ngoài, bên dưới bảng đen, góc phải
copy_stats_btn = tk.Button(
    main_frame,
    text="📋 Copy Stats",
    command=copyStatsToClipboard,
    width=15,
    bg="#FBFF00",
    fg="black",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    bd=0,
)
copy_stats_btn.grid(row=1, column=2, sticky="e", padx=(0, 10), pady=(0, 5))

sceneType = tk.StringVar(value="🎲🎲🎲")

scene_label = tk.Label(
    main_frame,
    text="Chọn loại Prompt:",
    font=("Segoe UI", 13),
    fg="#FFFFFF",
    bg="#1E1E1E",
)
scene_label.grid(row=1, column=0, sticky="w", pady=5)

option_menu = tk.OptionMenu(
    main_frame,
    sceneType,
    "RANDOM 🎲🎲🎲",
    "Cảnh Indoor",
    "Cảnh Outdoor",
    "Lovely Prompt",
    "Random Rule L4D2",
    "App Date Options",
    "Short Story 1 - Curse Breaking Journey",
    "Short Story 2 - Job Interview",
    "Short Story 3 - Dating",
    "Short Story 4 - Rebellious Past",
    
)
option_menu.config(
    bg="#2D2D2D", fg="#E0E0E0", font=("Segoe UI", 13), relief="flat", bd=0
)
option_menu.grid(row=1, column=1, sticky="w", pady=5)

create_button = tk.Button(
    main_frame,
    text="🎲🎲🎲 Render 🎲🎲🎲",
    command=generateScene,
    width=30,
    height=2,
    bg="#12FFD8",
    fg="black",
    font=("Segoe UI", 13, "bold"),
    relief="flat",
    bd=0,
    activebackground="#919191",
    activeforeground="black",
)
create_button.grid(row=2, columnspan=3, pady=15)

outputText = tk.Text(
    main_frame,
    wrap="word",
    height=13,
    width=60,
    bg="#2D2D2D",
    fg="#E0E0E0",
    font=("Segoe UI", 13),
    insertbackground="#E0E0E0",
    relief="flat",
    bd=0,
)
outputText.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

scrollbar = tk.Scrollbar(
    main_frame, command=outputText.yview, bg="#2D2D2D", troughcolor="#1E1E1E"
)
scrollbar.grid(row=3, column=2, sticky="ns")
outputText.config(yscrollcommand=scrollbar.set)

main_frame.grid_rowconfigure(3, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

copy_button = tk.Button(
    main_frame,
    text="📋 Copy",
    command=copySceneToClipboard,
    width=20,
    bg="#2196F3",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    bd=0,
    activebackground="#1976D2",
    activeforeground="white",
)
copy_button.grid(row=4, columnspan=2, pady=10)

root.mainloop()
