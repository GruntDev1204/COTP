import tkinter as tk
from tkinter import ttk
from Script.script import *
from Script.caculate_pool import *


def generateOutput():
    output = ""
    option = outputType.get()

    if option == "RANDOM 🎲🎲🎲":
        option = random.choice(
            [
                "App Date Options",
                "Cảnh Indoor",
                "Cảnh Outdoor",
                "Lovely Prompt",
                "Modeling Prompt",
                "Random Rule L4D2",
                "Short Story 1 - Curse Breaking Journey",
                "Short Story 2 - Job Interview",
                "Short Story 3 - Dating",
                "Short Story 4 - Rebellious Past",
            ]
        )

    match option:
        case "Cảnh Indoor":
            output = generateIndoorOutput()
        case "Cảnh Outdoor":
            output = generateOutdoorOutput()
        case "Lovely Prompt":
            output = generateLovelyPrompt()
        case "Modeling Prompt":
            output = generateModelingPrompt()
        case "Random Rule L4D2":
            output = ruleL4D2()
        case "App Date Options":
            output = dateAppOptions()
        case "Short Story 1 - Curse Breaking Journey":
            output = generateShortStory1()
        case "Short Story 2 - Job Interview":
            output = generateShortStory2()
        case "Short Story 3 - Dating":
            output = generateShortStory3()
        case "Short Story 4 - Rebellious Past":
            output = generateShortStory4()
        case _:
            output = generateIndoorOutput()

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

    if isinstance(output, tuple):
        output = "\n".join(output)

    lines = output.split("\n")  
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
                        iconStart = None
                        for icon in all_icons:
                            pos = line.find(icon)
                            if pos != -1:
                                iconStart = pos
                                break
                        if iconStart is not None:
                            outputText.insert(tk.END, line[:iconStart], "content")
                            outputText.insert(tk.END, line[iconStart:], "icons")
                        else:
                            outputText.insert(tk.END, line, "content")
                    else:
                        outputText.insert(tk.END, line, "content")
                outputText.insert(tk.END, "\n")

    outputText.config(padx=15, pady=15)


def copyOutputToClipboard():
    output = outputText.get("1.0", tk.END).strip()
    if output:
        root.clipboard_clear()
        root.clipboard_append(output)
        copyButton.config(text="📋 Đã copy!", bg="#89F900", fg="black")
        root.after(
            1500, lambda: copyButton.config(text="📋 Copy", bg="#E9F900", fg="black")
        )

def copyStatsToClipboard():
    statsText = (
        f"📊📊📊 Tổng hợp nội dung có thể tạo bởi COTP (latest):\n"
        f"Cảnh Indoor: {indoorCombinations:,} [👉 {formatNumber(abs(indoorCombinations), 2)}]\n"
        f"Cảnh Outdoor: {outdoorCombinations:,} [👉 {formatNumber(abs(outdoorCombinations), 2)}]\n"
        f"L4D2 Case: {l4d2CaseTotal:,} [👉 {formatNumber(abs(l4d2CaseTotal), 2)}]\n"
        f"appDateTotal: {appDateTotal:,} [👉 {formatNumber(abs(appDateTotal), 2)}]\n"
        f"Short Story 1 - Curse Breaking Journey: {storyCombinations:,} [👉 {formatNumber(abs(storyCombinations), 2)}]\n"
        f"Short Story 2 - Job Interview: {story2Combinations:,} [👉 {formatNumber(abs(story2Combinations), 2)}]\n"
        f"Short Story 3 - Dating: {story3Combinations:,} [👉 {formatNumber(abs(story3Combinations), 2)}]\n"
        f"Short Story 4 - Rebellious Past: {shortStory4Total:,} [👉 {formatNumber(abs(shortStory4Total), 2)}]\n"
        f"Lovely Prompt: {lovelyPromptTotal:,} [👉 {formatNumber(abs(lovelyPromptTotal), 2)}]\n"
        f"Modeling Prompt: {modelingPromptTotal:,} [👉 {formatNumber(abs(modelingPromptTotal), 2)}]\n"
        f"📊📊📊 TOTAL : {totalCombinations:,} [👉 {formatNumber(abs(totalCombinations), 2)}]\n"
        f"=======================================================================================\n"
        f"📊📢📢📢 Phân tích chi tiết:\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Indoor: {len(str(indoorCombinations))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Outdoor: {len(str(outdoorCombinations))} số\n"
        f"Độ dài của con số tổng tổ kịch bản của L4D2: {len(str(l4d2CaseTotal))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của appDate: {len(str(appDateTotal))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Story 1 - Curse Breaking Journey: {len(str(storyCombinations))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Story 2 - Job Interview: {len(str(story2Combinations))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Story 3 - Dating: {len(str(story3Combinations))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Story 4 - Rebellious Past: {len(str(shortStory4Total))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Lovely Prompt: {len(str(lovelyPromptTotal))} số\n"
        f"Độ dài của con số tổng tổ hợp khả năng của Modeling Prompt: {len(str(modelingPromptTotal))} số\n"
        f"Độ dài của con số tổng tổ hợp : {len(str(totalCombinations))} số\n"
    )
    root.clipboard_clear()
    root.clipboard_append(statsText)
    copyStatsButton.config(text="📋 Đã copy!", bg="#89F900", fg="black")
    root.after(
        1500,
        lambda: copyStatsButton.config(text="📋 Copy Stats", bg="#FBFF00", fg="black"),
    )


root = tk.Tk()
root.title("👑👑👑 CHAOTICS ONE-TIME-PROMPT (COTP) - by GruntDev1204 👑👑👑")
root.geometry("1500x800")
root.resizable(True, True)
root.configure(bg="#1E1E1E")

outputType = tk.StringVar(value="🎲🎲🎲")  # <-- Đặt ở đây

(
    indoorCombinations,
    outdoorCombinations,
    storyCombinations,
    story2Combinations,
    story3Combinations,
    shortStory4Total,
    l4d2CaseTotal,
    appDateTotal,
    lovelyPromptTotal,
    modelingPromptTotal,
) = caculateQuantity()
totalCombinations = (
    indoorCombinations
    + outdoorCombinations
    + storyCombinations
    + story2Combinations
    + story3Combinations
    + shortStory4Total
    + l4d2CaseTotal
    + appDateTotal
    + lovelyPromptTotal
    + modelingPromptTotal
)

mainFrame = tk.Frame(root, bg="#1E1E1E")
mainFrame.pack(padx=20, pady=20, fill="both", expand=True)

# Cấu hình grid cho mainFrame để các cột/row co giãn
mainFrame.grid_rowconfigure(0, weight=0)  # statsFrame
mainFrame.grid_rowconfigure(1, weight=0)  # label + option + copy stats
mainFrame.grid_rowconfigure(2, weight=0)  # render button
mainFrame.grid_rowconfigure(3, weight=1)  # outputText
mainFrame.grid_rowconfigure(4, weight=0)  # copy button
mainFrame.grid_columnconfigure(0, weight=1)
mainFrame.grid_columnconfigure(1, weight=1)
mainFrame.grid_columnconfigure(2, weight=0)

# Tạo frame riêng cho bảng stats
statsFrame = tk.Frame(mainFrame, bg="#000000")
statsFrame.grid(row=0, column=0, columnspan=3, sticky="nsew", pady=(0, 10))

# Cấu hình grid cho statsFrame để textbox co giãn
statsFrame.grid_rowconfigure(1, weight=1)
statsFrame.grid_columnconfigure(0, weight=1)

# Thanh cuộn ngang trên đầu bảng đen
xscroll = tk.Scrollbar(
    statsFrame,
    orient="horizontal",
    bg="#000000",
    troughcolor="#000000",
    bd=0,
    highlightthickness=0,
    relief="flat",
)
xscroll.grid(row=0, column=0, sticky="ew")

# Textbox stats (chiếm hết chiều ngang của statsFrame)
statsDetailText = (
    f"📊📊📊 Tổng hợp nội dung có thể tạo bởi COTP (latest):\n"
    f"Cảnh Indoor: {indoorCombinations:,} [👉 {formatNumber(abs(indoorCombinations), 2)}]\n"
    f"Cảnh Outdoor: {outdoorCombinations:,} [👉 {formatNumber(abs(outdoorCombinations), 2)}]\n"
    f"Lovely Prompt: {lovelyPromptTotal:,} [👉 {formatNumber(abs(lovelyPromptTotal), 2)}]\n"
    f"Modeling Prompt: {modelingPromptTotal:,} [👉 {formatNumber(abs(modelingPromptTotal), 2)}]\n"
    f"L4D2 Case: {l4d2CaseTotal:,} [👉 {formatNumber(abs(l4d2CaseTotal), 2)}]\n"
    f"appDateTotal: {appDateTotal:,} [👉 {formatNumber(abs(appDateTotal), 2)}]\n"
    f"Short Story 1 - Curse Breaking Journey: {storyCombinations:,} [👉 {formatNumber(abs(storyCombinations), 2)}]\n"
    f"Short Story 2 - Job Interview: {story2Combinations:,} [👉 {formatNumber(abs(story2Combinations), 2)}]\n"
    f"Short Story 3 - Dating: {story3Combinations:,} [👉 {formatNumber(abs(story3Combinations), 2)}]\n"
    f"Short Story 4 - Rebellious Past: {shortStory4Total:,} [👉 {formatNumber(abs(shortStory4Total), 2)}]\n"
    f"📊📊📊 TOTAL : {totalCombinations:,} [👉 {formatNumber(abs(totalCombinations), 2)}]\n"
    f"=======================================================================================\n"
    f"📊📢📢📢 Phân tích chi tiết:\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Indoor: {len(str(indoorCombinations))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Outdoor: {len(str(outdoorCombinations))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Lovely Prompt: {len(str(lovelyPromptTotal))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Modeling Prompt: {len(str(modelingPromptTotal))} số\n"
    f"Độ dài của con số tổng tổ kịch bản của L4D2: {len(str(l4d2CaseTotal))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của appDate: {len(str(appDateTotal))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Story 1 - Curse Breaking Journey: {len(str(storyCombinations))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Story 2 - Job Interview: {len(str(story2Combinations))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Story 3 - Dating: {len(str(story3Combinations))} số\n"
    f"Độ dài của con số tổng tổ hợp khả năng của Story 4 - Rebellious Past: {len(str(shortStory4Total))} số\n"
    f"Độ dài của con số tổng tổ hợp : {len(str(totalCombinations))} số\n"
)

statsDetailTextbox = tk.Text(
    statsFrame,
    font=("Segoe UI", 10),
    fg="#00FFEA",
    bg="#000000",
    height=10,
    wrap="none",
    state="normal",
    padx=10,
    pady=10,
)
xscroll.config(command=statsDetailTextbox.xview)
statsDetailTextbox.insert("1.0", statsDetailText)
statsDetailTextbox.config(state="disabled", xscrollcommand=xscroll.set)
statsDetailTextbox.grid(row=1, column=0, sticky="nsew")

# Nút copy stats ở ngoài, bên dưới bảng đen, góc phải
copyStatsButton = tk.Button(
    mainFrame,
    text="📋 Copy Stats",
    command=copyStatsToClipboard,
    width=15,
    bg="#FBFF00",
    fg="black",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    bd=0,
)
copyStatsButton.grid(row=1, column=2, sticky="e", padx=(0, 10), pady=(0, 5))

outputType = tk.StringVar(value="🎲🎲🎲")

outputLabel = tk.Label(
    mainFrame,
    text="Chọn loại Prompt:",
    font=("Segoe UI", 13),
    fg="#FFFFFF",
    bg="#1E1E1E",
)
outputLabel.grid(row=1, column=0, sticky="w", pady=5)

optionMenu = tk.OptionMenu(
    mainFrame,
    outputType,
    "RANDOM 🎲🎲🎲",
    "Cảnh Indoor",
    "Cảnh Outdoor",
    "Lovely Prompt",
    "Modeling Prompt",
    "Random Rule L4D2",
    "App Date Options",
    "Short Story 1 - Curse Breaking Journey",
    "Short Story 2 - Job Interview",
    "Short Story 3 - Dating",
    "Short Story 4 - Rebellious Past",
    
)
optionMenu.config(
    bg="#2D2D2D", fg="#E0E0E0", font=("Segoe UI", 13), relief="flat", bd=0
)
optionMenu.grid(row=1, column=1, sticky="w", pady=5)

createButton = tk.Button(
    mainFrame,
    text="🎲🎲🎲 Render 🎲🎲🎲",
    command=generateOutput,
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
createButton.grid(row=2, columnspan=3, pady=15)

outputText = tk.Text(
    mainFrame,
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
    mainFrame, command=outputText.yview, bg="#2D2D2D", troughcolor="#1E1E1E"
)
scrollbar.grid(row=3, column=2, sticky="ns")
outputText.config(yscrollcommand=scrollbar.set)

mainFrame.grid_rowconfigure(3, weight=1)
mainFrame.grid_columnconfigure(1, weight=1)

copyButton = tk.Button(
    mainFrame,
    text="📋 Copy",
    command=copyOutputToClipboard,
    width=20,
    bg="#2196F3",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    bd=0,
    activebackground="#C3D219",
    activeforeground="white",
)
copyButton.grid(row=4, columnspan=2, pady=10)

root.mainloop()
