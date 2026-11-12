import tkinter as tk
import sys
from pathlib import Path
from Script.script import *
from log.log import (
    buildFullStats,
    getArrayCommaIssues,
    getArrayDuplicates,
    getArraySizes,
    getArraySourcePaths,
)
from log.cotp_structure_log import buildCotpStructure
from ui.ui_properties import (
    dataPaneColors,
    infoMenuOptions,
    outputMenuOptions,
    sharedUiColors,
    themePalettes,
)

projectDir = Path(
    getattr(sys, "_MEIPASS", Path(__file__).resolve().parent.parent)
)
if not (projectDir / "instruction.txt").is_file():
    internalDir = projectDir / "_internal"
    if (internalDir / "instruction.txt").is_file():
        projectDir = internalDir

currentTheme = themePalettes["Dark"]
outerTheme = currentTheme
createClickCount = 0
headerCanvas = None
headerCountTextId = None

outputGenerators = {
    "Indoor Scene Prompt": generateIndoorOutput,
    "Outdoor Scene Prompt": generateOutdoorOutput,
    "Couple Prompt": generateCouplePrompt,
    "Modeling Prompt": generateModelingPrompt,
    "Random Rule L4D2": ruleL4D2,
    "App Date Options": dateAppOptions,
    "Short Story 1 - Curse Breaking Journey": generateShortStory1,
    "Short Story 2 - Job Interview": generateShortStory2,
    "Short Story 3 - Dating": generateShortStory3,
    "Short Story 4 - Rebellious Past": generateShortStory4,
}

def generateOutput():
    option = outputType.get()

    if option == outputMenuOptions[0]:
        option = random.choice(tuple(outputGenerators))

    output = outputGenerators.get(option, generateIndoorOutput)()

    outputText.delete("1.0", tk.END)
    outputText.tag_configure(
        "title",
        font=(
            "Segoe UI",
            15,
            "bold",
        ),
        foreground=dataPaneColors["titleFg"],
    )
    outputText.tag_configure(
        "location",
        font=("Consolas", 13, "bold"),
        foreground=dataPaneColors["locationFg"],
    )
    outputText.tag_configure(
        "content",
        font=("Consolas", 13, "bold"),
        foreground=dataPaneColors["outputFg"],
    )
    outputText.tag_configure(
        "icons",
        font=("Segoe UI", 13, "normal"),
        foreground=dataPaneColors["iconFg"],
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
                        for icon in allIcons:
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
    copyButton.config(
        state=tk.NORMAL,
        bg=sharedUiColors["buttonBg"],
        fg=sharedUiColors["buttonFg"],
    )


def handleCreateClick():
    global createClickCount
    createClickCount += 1
    if headerCanvas is not None and headerCountTextId is not None:
        headerCanvas.itemconfigure(
            headerCountTextId,
            text=f"CREATE PRESSES  •  {createClickCount:02d}",
        )
    generateOutput()


def copyOutputToClipboard():
    output = outputText.get("1.0", tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(output)
    copyButton.config(
        text="📋 Copied!",
        bg=sharedUiColors["buttonHoverBg"],
        fg=sharedUiColors["buttonFg"],
    )
    root.after(
        1500,
        lambda: copyButton.config(
            text="📋 Copy Output",
            bg=sharedUiColors["buttonBg"],
            fg=sharedUiColors["buttonFg"],
        ),
    )

def copyStatsToClipboard():
    infoText = statsDetailTextbox.get("1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(infoText)
    copyStatsButton.config(
        text="📋 Copied!",
        bg=sharedUiColors["buttonHoverBg"],
        fg=sharedUiColors["buttonFg"],
    )
    root.after(
        1500,
        lambda: copyStatsButton.config(
            text="📋 Copy Info",
            bg=sharedUiColors["buttonBg"],
            fg=sharedUiColors["buttonFg"],
        ),
    )


def createInterface():
    global root, outputType, themeMode, statsDetailText, statsValues, infoMode
    global statsDetailTextbox, outputText, copyButton, copyStatsButton
    global createClickCount, headerCanvas, headerCountTextId
    createClickCount = 0
    headerCountTextId = None
    root = tk.Tk()
    root.title("👑👑👑🎲 CHAOS ONE-TIME PROMPT (COTP) - CREATED BY HỒ TRUNG - 🤪😵😵‍💫🥴🫠😭🤮🤧🤕💀🤯😫🤡 🎲👑👑👑")
    root.geometry("1600x900")
    root.resizable(True, True)
    root.configure(bg=currentTheme["appBg"])

    outputType = tk.StringVar(value="🎲🎲🎲")  # <-- Đặt ở đây
    themeMode = tk.StringVar(value="Dark")

    (
        statsDetailText,
        statsValues,
    ) = buildFullStats()
    infoMode = tk.StringVar(value="COTP Introduction")

    def buildCotpIntroduction():
        instructionText = (projectDir / "instruction.txt").read_text(encoding="utf-8")
        lines = instructionText.splitlines()
        start = next(
            index for index, line in enumerate(lines)
            if line.strip() == "Details about COTP :"
        )
        end = next(
            index for index in range(start + 1, len(lines))
            if lines[index].strip().startswith("This COTP App:")
        )
        return "\n".join(lines[start:end]).rstrip()

    def buildCotpComponentsDataPool():
        return (projectDir / "log" / "cotp_components_data_pool.txt").read_text(encoding="utf-8")


    def buildArraySizesText():
        arraySizes = getArraySizes()
        duplicateArrays = getArrayDuplicates()
        commaIssues = getArrayCommaIssues()
        arraySourcePaths = getArraySourcePaths()
        lines = [
            "All Arrays Used By COTP :",
            *(
                f"Array size - {name} ({arraySourcePaths[name]}): {size}"
                for name, size in sorted(
                    arraySizes.items(), key=lambda item: item[0].casefold()
                )
            ),
            "",
            f"Duplicate Items ({sum(map(len, duplicateArrays.values()))} duplicated values):",
        ]
        if duplicateArrays:
            for arrayName, duplicates in sorted(
                duplicateArrays.items(), key=lambda item: item[0].casefold()
            ):
                lines.extend(
                    f"  - {arrayName} ({arraySourcePaths[arrayName]}): "
                    f"{item!r} ({count} occurrences)"
                    for item, count in duplicates
                )
        else:
            lines.append("  - No duplicate items found.")
        lines.extend(
            [
                "",
                f"Possible Missing Commas ({sum(map(len, commaIssues.values()))} issues):",
            ]
        )
        if commaIssues:
            for arrayName, issues in sorted(
                commaIssues.items(), key=lambda item: item[0].casefold()
            ):
                lines.extend(
                    f"  - {arrayName} ({arraySourcePaths[arrayName]}): "
                    f"line {lineNumber} ({item!r})"
                    for lineNumber, item in issues
                )
        else:
            lines.append("  - No possible missing commas found.")
        return "\n".join(lines)


    infoTextBuilders = {
        "COTP Introduction": buildCotpIntroduction,
        "COTP Components data pool": buildCotpComponentsDataPool,
        "Stats": lambda: statsDetailText,
        "Arrays COTP": buildArraySizesText,
        "COTP Struct Details": buildCotpStructure,
    }

    def updateInfoDisplay(*_args):
        selectedInfo = infoMode.get()
        infoText = infoTextBuilders[selectedInfo]()
        statsDetailTextbox.configure(state="normal")
        statsDetailTextbox.delete("1.0", tk.END)
        statsDetailTextbox.insert("1.0", infoText)
        statsDetailTextbox.configure(
            font=("Consolas", 13 if selectedInfo == "COTP Introduction" else 11)
        )
        if selectedInfo == "Stats":
            for lineNumber, line in enumerate(infoText.splitlines(), start=1):
                if "TOTAL :" in line or "TOTAL combinations (digits):" in line:
                    statsDetailTextbox.tag_add(
                        "statsTotal",
                        f"{lineNumber}.0",
                        f"{lineNumber}.end",
                    )
        statsDetailTextbox.configure(state="disabled")

    mainFrame = tk.Frame(
        root,
        bg=currentTheme["mainBg"],
        highlightthickness=1,
        highlightbackground=currentTheme["border"],
    )
    mainFrame.pack(padx=20, pady=20, fill="both", expand=True)

    # Cấu hình grid cho mainFrame để các cột/row co giãn
    mainFrame.grid_rowconfigure(0, weight=0)  # decorative header
    mainFrame.grid_rowconfigure(1, weight=0)  # statsFrame
    mainFrame.grid_rowconfigure(2, weight=0)  # label + option + copy stats
    mainFrame.grid_rowconfigure(3, weight=0)  # render button
    mainFrame.grid_rowconfigure(4, weight=1)  # outputText
    mainFrame.grid_rowconfigure(5, weight=0)  # copy button
    mainFrame.grid_columnconfigure(0, weight=1)
    mainFrame.grid_columnconfigure(1, weight=0)
    mainFrame.grid_columnconfigure(2, weight=0)

    headerCanvas = tk.Canvas(
        mainFrame,
        height=42,
        highlightthickness=0,
        bd=0,
    )
    headerCanvas.grid(
        row=0,
        column=0,
        columnspan=3,
        sticky="ew",
        padx=12,
        pady=(0, 10),
    )

    # Tạo frame riêng cho bảng stats
    statsFrame = tk.Frame(
        mainFrame,
        bg=sharedUiColors["panelBg"],
        highlightthickness=1,
        highlightbackground=currentTheme["border"],
    )
    statsFrame.grid(row=1, column=0, columnspan=3, sticky="nsew", pady=(0, 10))

    # Cấu hình grid cho statsFrame để textbox co giãn
    statsFrame.grid_rowconfigure(1, weight=1)
    statsFrame.grid_columnconfigure(0, weight=1)

    # Thanh cuộn ngang trên đầu bảng đen
    xscroll = tk.Scrollbar(
        statsFrame,
        orient="horizontal",
        bg=sharedUiColors["panelBg"],
        troughcolor=dataPaneColors["statsBg"],
        bd=0,
        highlightthickness=0,
        relief="flat",
    )
    xscroll.grid(row=0, column=0, columnspan=2, sticky="ew")

    yscroll = tk.Scrollbar(
        statsFrame,
        orient="vertical",
        bg=sharedUiColors["panelBg"],
        troughcolor=dataPaneColors["statsBg"],
        bd=0,
        highlightthickness=0,
        relief="flat",
    )
    yscroll.grid(row=1, column=1, sticky="ns")

    # Textbox stats (chiếm hết chiều ngang của statsFrame)
    statsDetailTextbox = tk.Text(
        statsFrame,
        font=("Consolas", 11),
        fg=dataPaneColors["statsFg"],
        bg=dataPaneColors["statsBg"],
        height=10,
        wrap="none",
        state="normal",
        padx=10,
        pady=10,
    )
    statsDetailTextbox.tag_configure(
        "statsTotal",
        font=("Consolas", 12, "bold"),
    )
    xscroll.config(command=statsDetailTextbox.xview)
    statsDetailTextbox.config(
        state="disabled",
        xscrollcommand=xscroll.set,
        yscrollcommand=yscroll.set,
    )
    statsDetailTextbox.grid(row=1, column=0, sticky="nsew")
    yscroll.config(command=statsDetailTextbox.yview)
    updateInfoDisplay()

    controlsFrame = tk.Frame(mainFrame, bg=currentTheme["mainBg"])
    controlsFrame.grid(
        row=2, column=0, columnspan=3, sticky="ew", padx=14, pady=(2, 8)
    )
    controlsFrame.grid_columnconfigure(6, weight=1)

    themeLabel = tk.Label(
        controlsFrame,
        text="Theme:",
        font=("Segoe UI", 10),
        fg=currentTheme["controlFg"],
        bg=currentTheme["mainBg"],
    )
    themeLabel.grid(row=0, column=0, sticky="w", padx=(0, 6))

    themeSwitchBorder = tk.Frame(
        controlsFrame,
        bg=currentTheme["menuBorder"],
        padx=1,
        pady=1,
    )
    themeSwitchBorder.grid(row=0, column=1, sticky="w", padx=(0, 18))

    themeSwitch = tk.Canvas(
        themeSwitchBorder,
        width=54,
        height=30,
        bg=currentTheme["mainBg"],
        highlightthickness=0,
        bd=0,
        cursor="hand2",
        takefocus=True,
    )
    themeSwitch.pack()

    outputLabel = tk.Label(
        controlsFrame,
        text="Prompt:",
        font=("Segoe UI", 11),
        fg=currentTheme["textFg"],
        bg=currentTheme["mainBg"],
    )
    outputLabel.grid(row=0, column=2, sticky="w", padx=(0, 6))

    optionMenu = tk.OptionMenu(
        controlsFrame,
        outputType,
        *outputMenuOptions,
    )
    optionMenu.config(
        bg=currentTheme["menuBg"],
        fg=currentTheme["textFg"],
        activebackground=currentTheme["menuActiveBg"],
        activeforeground=currentTheme["textFg"],
        font=("Segoe UI", 11),
        cursor="hand2",
        relief="flat",
        bd=0,
        highlightthickness=1,
        highlightbackground=currentTheme["menuBorder"],
        highlightcolor=currentTheme["menuBorder"],
        padx=8,
    )
    optionMenu["menu"].config(
        bg=currentTheme["menuBg"],
        fg=currentTheme["textFg"],
        activebackground=currentTheme["menuActiveBg"],
        activeforeground=currentTheme["textFg"],
        borderwidth=0,
        cursor="hand2",
    )
    optionMenu.grid(row=0, column=3, sticky="w")

    infoLabel = tk.Label(
        controlsFrame,
        text="Info:",
        font=("Segoe UI", 11),
        fg=currentTheme["controlFg"],
        bg=currentTheme["mainBg"],
    )
    infoLabel.grid(row=0, column=4, sticky="w", padx=(14, 6))

    infoMenu = tk.OptionMenu(
        controlsFrame,
        infoMode,
        *infoMenuOptions,
        command=updateInfoDisplay,
    )
    infoMenu.config(
        bg=currentTheme["menuBg"],
        fg=currentTheme["menuFg"],
        activebackground=currentTheme["menuActiveBg"],
        activeforeground=currentTheme["menuFg"],
        font=("Segoe UI", 11),
        cursor="hand2",
        relief="flat",
        bd=0,
        highlightthickness=1,
        highlightbackground=currentTheme["menuBorder"],
        highlightcolor=currentTheme["menuBorder"],
        padx=8,
    )
    infoMenu["menu"].config(
        bg=currentTheme["menuBg"],
        fg=currentTheme["menuFg"],
        activebackground=currentTheme["menuActiveBg"],
        activeforeground=currentTheme["menuFg"],
        borderwidth=0,
        cursor="hand2",
    )
    infoMenu.grid(row=0, column=5, sticky="w")

    copyStatsBorder = tk.Frame(
        controlsFrame,
        bg=currentTheme["menuBorder"],
        padx=1,
        pady=1,
    )
    copyStatsBorder.grid(row=0, column=7, sticky="e", padx=(12, 0))

    copyStatsButton = tk.Button(
        copyStatsBorder,
        text="📋 Copy Info",
        command=copyStatsToClipboard,
        width=15,
        bg=sharedUiColors["buttonBg"],
        fg=sharedUiColors["buttonFg"],
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        bd=0,
        cursor="hand2",
        activebackground=sharedUiColors["buttonHoverBg"],
        activeforeground=sharedUiColors["buttonFg"],
        highlightthickness=1,
        highlightbackground=currentTheme["menuBorder"],
        highlightcolor=currentTheme["menuBorder"],
    )
    copyStatsButton.pack()

    createButtonBorder = tk.Frame(
        mainFrame,
        bg=currentTheme["menuBorder"],
        padx=1,
        pady=1,
    )
    createButtonBorder.grid(row=3, columnspan=3, pady=15)

    createButton = tk.Button(
        createButtonBorder,
        text="🎲🎲🎲 CREATE 🎲🎲🎲",
        command=handleCreateClick,
        width=30,
        height=2,
        bg=sharedUiColors["createButtonBg"],
        fg=sharedUiColors["buttonFg"],
        font=("Segoe UI", 13, "bold"),
        relief="flat",
        bd=0,
        cursor="hand2",
        highlightthickness=1,
        highlightbackground=currentTheme["menuBorder"],
        highlightcolor=currentTheme["menuBorder"],
    )
    createButton.pack()

    outputText = tk.Text(
        mainFrame,
        wrap="word",
        height=13,
        width=60,
        bg=dataPaneColors["outputBg"],
        fg=dataPaneColors["outputFg"],
        font=("Consolas", 13),
        insertbackground=dataPaneColors["outputFg"],
        relief="flat",
        bd=0,
        highlightthickness=1,
        highlightbackground=currentTheme["border"],
        highlightcolor=sharedUiColors["buttonBg"],
    )
    outputText.grid(row=4, column=0, columnspan=3, pady=10, sticky="nsew")


    def scrollOutput(event):
        outputText.yview_scroll(-1 if event.delta > 0 else 1, "units")
        return "break"


    outputText.bind("<MouseWheel>", scrollOutput)
    outputText.bind("<Button-4>", lambda event: outputText.yview_scroll(-1, "units"))
    outputText.bind("<Button-5>", lambda event: outputText.yview_scroll(1, "units"))

    mainFrame.grid_rowconfigure(4, weight=1)
    mainFrame.grid_columnconfigure(1, weight=1)

    copyButtonBorder = tk.Frame(
        mainFrame,
        bg=currentTheme["menuBorder"],
        padx=1,
        pady=1,
    )
    copyButtonBorder.grid(row=5, columnspan=2, pady=10)

    copyButton = tk.Button(
        copyButtonBorder,
        text="📋 Copy Output",
        command=copyOutputToClipboard,
        width=20,
        bg=sharedUiColors["disabledButtonBg"],
        disabledforeground=sharedUiColors["disabledButtonFg"],
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        bd=0,
        activebackground=sharedUiColors["buttonHoverBg"],
        activeforeground=sharedUiColors["buttonFg"],
        state=tk.DISABLED,
        cursor="hand2",
        highlightthickness=1,
        highlightbackground=currentTheme["menuBorder"],
        highlightcolor=currentTheme["menuBorder"],
    )
    copyButton.pack()


    def drawHeader(event=None):
        global headerCountTextId
        width = max(headerCanvas.winfo_width(), 2)
        height = max(headerCanvas.winfo_height(), 2)
        headerCanvas.delete("all")
        start = outerTheme["gradientStart"]
        end = outerTheme["gradientEnd"]
        startRgb = tuple(int(start[index:index + 2], 16) for index in (1, 3, 5))
        endRgb = tuple(int(end[index:index + 2], 16) for index in (1, 3, 5))

        for x in range(width):
            ratio = x / max(width - 1, 1)
            color = "#{:02X}{:02X}{:02X}".format(
                *(
                    round(first + (last - first) * ratio)
                    for first, last in zip(startRgb, endRgb)
                )
            )
            headerCanvas.create_line(x, 0, x, height, fill=color)

        headerCanvas.create_line(
            8, 4, width - 8, 4,
            fill=outerTheme["decoration"],
            dash=(5, 5),
            width=1,
        )
        headerCanvas.create_line(
            8, height - 4, width - 8, height - 4,
            fill=outerTheme["decoration"],
            dash=(5, 5),
            width=1,
        )
        headerCanvas.create_text(
            20,
            height / 2,
            anchor="w",
            text="🎲🎭🎰🎪👑 CHAOS ONE-TIME PROMPT (COTP) - AUTHOR: GRUNT 🎭🎰🎪👑🎲",
            fill=outerTheme["headerFg"],
            font=("Segoe UI", 13, "bold"),
        )
        headerCountTextId = headerCanvas.create_text(
            width - 20,
            height / 2,
            anchor="e",
            text=f"CREATE PRESSES  •  {createClickCount:02d}",
            fill=outerTheme["headerFg"],
            font=("Consolas", 9, "bold"),
        )

    headerCanvas.bind("<Configure>", drawHeader)

    def applyTheme():
        global outerTheme
        outerTheme = themePalettes[themeMode.get()]

        root.configure(bg=outerTheme["appBg"])
        headerCanvas.configure(bg=outerTheme["mainBg"])
        drawHeader()
        mainFrame.configure(
            bg=outerTheme["mainBg"],
            highlightbackground=outerTheme["border"],
        )
        statsFrame.configure(highlightbackground=outerTheme["border"])
        outputText.configure(highlightbackground=outerTheme["border"])
        controlsFrame.configure(bg=outerTheme["mainBg"])
        themeSwitch.configure(bg=outerTheme["mainBg"])
        themeSwitchBorder.configure(bg=outerTheme["menuBorder"])
        copyStatsBorder.configure(bg=outerTheme["menuBorder"])
        createButtonBorder.configure(bg=outerTheme["menuBorder"])
        copyButtonBorder.configure(bg=outerTheme["menuBorder"])
        themeLabel.configure(bg=outerTheme["mainBg"], fg=outerTheme["controlFg"])
        outputLabel.configure(bg=outerTheme["mainBg"], fg=outerTheme["controlFg"])
        infoLabel.configure(bg=outerTheme["mainBg"], fg=outerTheme["controlFg"])

        optionMenu.configure(
            bg=outerTheme["menuBg"],
            fg=outerTheme["menuFg"],
            activebackground=outerTheme["menuActiveBg"],
            activeforeground=outerTheme["menuFg"],
            cursor="hand2",
            highlightthickness=1,
            highlightbackground=outerTheme["menuBorder"],
            highlightcolor=outerTheme["menuBorder"],
        )
        optionMenu["menu"].configure(
            bg=outerTheme["menuBg"],
            fg=outerTheme["menuFg"],
            activebackground=outerTheme["menuActiveBg"],
            activeforeground=outerTheme["menuFg"],
            cursor="hand2",
        )
        infoMenu.configure(
            bg=outerTheme["menuBg"],
            fg=outerTheme["menuFg"],
            activebackground=outerTheme["menuActiveBg"],
            activeforeground=outerTheme["menuFg"],
            cursor="hand2",
            highlightthickness=1,
            highlightbackground=outerTheme["menuBorder"],
            highlightcolor=outerTheme["menuBorder"],
        )
        infoMenu["menu"].configure(
            bg=outerTheme["menuBg"],
            fg=outerTheme["menuFg"],
            activebackground=outerTheme["menuActiveBg"],
            activeforeground=outerTheme["menuFg"],
            cursor="hand2",
        )

        drawThemeSwitch()

        copyStatsButton.configure(
            bg=sharedUiColors["buttonBg"],
            fg=sharedUiColors["buttonFg"],
            activebackground=sharedUiColors["buttonHoverBg"],
            activeforeground=sharedUiColors["buttonFg"],
            highlightbackground=outerTheme["menuBorder"],
            highlightcolor=outerTheme["menuBorder"],
        )
        createButton.configure(
            bg=sharedUiColors["createButtonBg"],
            fg=sharedUiColors["buttonFg"],
            activebackground=sharedUiColors["createButtonBg"],
            activeforeground=sharedUiColors["buttonFg"],
            highlightbackground=outerTheme["menuBorder"],
            highlightcolor=outerTheme["menuBorder"],
        )
        copyButton.configure(
            bg=(
                sharedUiColors["disabledButtonBg"]
                if copyButton.cget("state") == tk.DISABLED
                else sharedUiColors["buttonBg"]
            ),
            fg=(
                sharedUiColors["disabledButtonFg"]
                if copyButton.cget("state") == tk.DISABLED
                else sharedUiColors["buttonFg"]
            ),
            activebackground=sharedUiColors["buttonHoverBg"],
            activeforeground=sharedUiColors["buttonFg"],
            disabledforeground=sharedUiColors["disabledButtonFg"],
            highlightbackground=outerTheme["menuBorder"],
            highlightcolor=outerTheme["menuBorder"],
        )
    def drawThemeSwitch():
        themeSwitch.delete("all")
        trackColor = (
            outerTheme["switchActiveBg"]
            if themeMode.get() == "Light"
            else outerTheme["switchTrackBg"]
        )
        themeSwitch.create_rectangle(12, 5, 42, 25, fill=trackColor, outline=trackColor)
        themeSwitch.create_oval(2, 5, 22, 25, fill=trackColor, outline=trackColor)
        themeSwitch.create_oval(32, 5, 52, 25, fill=trackColor, outline=trackColor)
        knobX = 31 if themeMode.get() == "Light" else 3
        themeSwitch.create_oval(
            knobX,
            3,
            knobX + 24,
            27,
            fill=outerTheme["switchKnobBg"],
            outline=outerTheme["switchKnobBg"],
        )
        themeSwitch.create_text(
            knobX + 12,
            15,
            text="☀" if themeMode.get() == "Light" else "☾",
            fill=outerTheme["switchIconFg"],
            font=("Segoe UI Symbol", 12),
        )


    def toggleTheme(event=None):
        themeMode.set("Light" if themeMode.get() == "Dark" else "Dark")
        applyTheme()


    themeSwitch.bind("<Button-1>", toggleTheme)
    themeSwitch.bind("<space>", toggleTheme)
    applyTheme()


def runApp():
    createInterface()
    root.mainloop()


if __name__ == "__main__":
    runApp()
