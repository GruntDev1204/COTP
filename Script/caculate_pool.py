from data.data import *

# tính toán
def formatNumber(number, digits=2):
    if abs(number) < 1:
        return f"{number:.12f}".rstrip("0").rstrip(".")
    n = len(str(int(number))) - 1
    base = str(int(number))[:digits]
    base_float = round(int(base) / (10 ** (digits - 1)), 2)
    return f"{base_float}×10^{n}"


def returnIconRandom(number):
    iconLength = len(all_icons)
    return iconLength**number


def caculateQuantity():
    titleLen = len(starting)
    endingLen = len(ending)
    colorsLen = len(colors)
    quantityLen = len(quantities)
    shapesLen = len(shapes)
    commentLen = len(comment)
    statusLen = len(status)
    NPCActionLen = len(liveNPCActions)
    NPCLen = len(liveNPCs)
    NPCAdjLen = len(liveNPCApperances)

    indoorLocationLen = len(indoorLocations)
    indoorStatusLen = len(indoorStatus)
    indoorMaterialLen = len(indoorMaterials)
    indoorItemsLen = len(indoorItems)
    indoorItemsStatusLen = len(indoorItemStatus)
    indoorLightVerbLen = len(indoorLightVerb)
    indoorSourceLightLen = len(indoorItemLightningSource)
    indoorObjectLen = len(indoorObjectItems)

    indoor_total = (
        (len(liveNPCEmotions))
        * ((len(titleEmojis) ** 4) ** 2)
        * titleLen
        * indoorLocationLen
        * indoorStatusLen
        * indoorMaterialLen
        * (colorsLen**3)
        * (quantityLen**3)
        * (shapesLen**2)
        * indoorItemsLen
        * indoorItemsStatusLen
        * indoorLightVerbLen
        * indoorSourceLightLen
        * indoorObjectLen
        * NPCLen
        * NPCAdjLen
        * NPCActionLen
        * endingLen
        * statusLen
        * (len(emojiStatus) ** 3)
        * (len(emotionPunctuations) ** 4)
        * commentLen
        * (len(emojiMeme) ** 3)
        * returnIconRandom(7)
    )

    outdoorViewLen = len(outdoorView)
    outdoorStatusLen = len(outDoorStatus)
    weatherConditionsLen = len(weatherConditions)
    outDoorSkyStrongObjectsLen = len(outDoorSkyStrongObjects)
    outDoorSkyStrongObjectStatusLen = len(outDoorSkyStrongObjectStatus)
    outDoorSkyObjectsLen = len(outDoorSkyObjects)
    outdoorObjectDensityLen = len(outdoorObjectDensity)
    outdoorObjectsLen = len(outdoorObjects)

    outdoor_total = (
        (len(liveNPCEmotions))
        * ((len(titleEmojis) ** 4) ** 2)
        * titleLen
        * outdoorViewLen
        * outdoorStatusLen
        * weatherConditionsLen
        * (outDoorSkyStrongObjectsLen + 1)
        * (shapesLen**3)
        * outDoorSkyStrongObjectStatusLen
        * (quantityLen**3)
        * outDoorSkyObjectsLen
        * (colorsLen**2)
        * outdoorObjectDensityLen
        * outdoorObjectsLen
        * NPCLen
        * NPCAdjLen
        * NPCActionLen
        * endingLen
        * statusLen
        * (len(emojiStatus) ** 3)
        * (len(emotionPunctuations) ** 4)
        * commentLen
        * (len(emojiMeme) ** 3)
        * returnIconRandom(7)
    )

    story_total = (
        returnIconRandom(10)
        * returnIconRandom(7)
        * len(businesses)
        * len(magicTypes)
        * (outdoorViewLen**2)
        * outdoorStatusLen
        * outdoorObjectDensityLen
        * (outdoorObjectsLen**2)
        * (indoorMaterialLen**2)
        * indoorItemsLen
        * indoorItemsStatusLen
        * indoorLightVerbLen
        * indoorSourceLightLen
        * (NPCAdjLen**2)
        * (len(liveNPCEmotions) ** 5)
        * indoorLocationLen
        * indoorStatusLen
        * len(proverbs)
        * (len(NPCjobs) ** 3)
        * (900001**1)  # repeat_times mới
        * (90001**4)  # years_duration mới
        * (900000000001**14)  # distance mới
        * (indoorObjectLen**3)
        * (shapesLen**5)
        * (quantityLen**3)
        * (colorsLen**6)
        * (NPCLen**4)
        * (len(slogan))
        * (len(nameNPC) ** 4)
        * len(sourceInfo)
        * len(gpsLocations)
        * (NPCActionLen**7)
    )

    story2_total = (
        returnIconRandom(10)
        * returnIconRandom(7)
        * ((len(emojiStatus) ** 3) ** 2)
        * (len(colors) ** 2)
        * (9000000001**2)
        * 8  # số giờ có thể rảnh
        * 18  # số tuổi của ứng viên
        * len(outdoorView)
        * (900000000001**25)
        * len(weatherConditions)
        * (len(companies) ** 2)
        * (len(liveNPCs) ** 3)
        * len(liveNPCApperances)
        * (len(liveNPCEmotions) ** 3)
        * (len(liveNPCActions) ** 7)
        * (len(nameNPC) ** 3)
        * (len(indoorLocations) ** 2)
        * len(indoorStatus)
        * len(status)
        * (len(NPCjobs) ** 2)
        * len(buildings)
    )

    shortStory3Total = (
        (900000000001**23)
        * 9000000001
        * 18
        * len(indoorLocations)
        * (len(indoorMaterials) ** 2)
        * returnIconRandom(10)
        * returnIconRandom(7)
        * ((len(emojiStatus) ** 3) ** 2)
        * len(gpsLocations)
        * len(magicTypes)
        * len(businesses)
        * len(weatherConditions)
        * (len(outdoorView) ** 2)
        * len(outDoorStatus)
        * len(companies)
        * len(outDoorSkyStrongObjects)
        * (len(shapes) ** 3)
        * len(outDoorSkyStrongObjectStatus)
        * (len(status) ** 2)
        * len(outdoorObjectDensity)
        * len(outdoorObjects)
        * (len(colors) ** 9)
        * len(buildings)
        * (len(liveNPCEmotions) ** 2)
        * (len(liveNPCs) ** 4)
        * (len(liveNPCActions) ** 9)
        * (len(sourceInfo) ** 2)
        * (len(liveNPCApperances) ** 3)
        * len(indoorObjectItems)
        * (len(proverbs) ** 2)
        * (len(nameNPC) ** 3)
        * len(slogan)
    )

    shortStory4Total = (
        (1000000000000000 - 100000000000000 + 1)
        * ((10000000000 - 1000000000 + 1) ** 3)
        * (900000000001**46)
        * (18**3)
        * returnIconRandom(10)
        * returnIconRandom(7)
        * (len(indoorLocations) ** 3)
        * len(indoorStatus)
        * len(indoorMaterials)
        * (len(colors) ** 4)
        * (len(outdoorView) ** 3)
        * len(weatherConditions)
        * (len(shapes) ** 2)
        * (len(status) ** 2)
        * len(outDoorSkyStrongObjects)
        * len(outDoorSkyStrongObjectStatus)
        * (len(liveNPCActions) ** 15)
        * (len(liveNPCEmotions) ** 4)
        * (len(liveNPCs) ** 5)
        * (len(nameNPC) ** 6)
        * len(magicTypes)
        * ((len(emojiStatus) ** 3) ** 2)
        * (len(companies) ** 2)
        * (len(gpsLocations) ** 2)
        * (len(indoorObjectItems) ** 2)
        * len(liveNPCApperances)
    )
    
    L4D2caseTotal = (
        len(mapsL4D2) *
        len(charactersL4D2) *
        (100 - 1 + 1) *  # HP
        (len(weaponsL4D2) + 1) *  # có thể không có vũ khí
        (500 - 1 + 1) *  # ammo
        len(meleeL4D2) *
        len(grenadesL4D2) * (5 - 0 + 1) *  # số lượng lựu đạn
        len(pickupsL4D2) * (5 - 0 + 1) *  # số lượng đồ nhặt được
        len(medicineL4D2) * (5 - 0 + 1) *  # số lượng thuốc
        (3 - 0 + 1) *  # first aid kit
        (100 - 1 + 1) *  # số lượng common infected
        (5 - 2 + 1) *  # time limit
        (500 - 100 + 1) *  # step limit
        (100000000000 - 1000000000 + 1) *  # tank HP
        len(playerRulesL4D2) * (60 - 10 + 1) *  # time limit cho rule
        3  # objective
    )

    appDateTotal = (
        len(companies)
        * (20 - 1 + 1)  # số profile reject
        * (20 - 1 + 1)  # số profile like
        * len(optionsDateApp)  # các tùy chọn quẹt
    )

    lovelyPromptTotal = (
        len(BoyActions)
        * len(GirlActions)
        * len(LoveActions)
        * len(status)
        * (
            len(indoorLocations)
            * len(indoorStatus)
            * len(indoorMaterials)
            * len(colors)
            * len(quantities)
            * len(indoorItems)
            * len(indoorItemStatus)
            * len(shapes)
            * len(indoorLightVerb)
            * len(indoorItemLightningSource)
            * len(colors)
            * len(quantities)
            * len(indoorObjectItems)
            * len(shapes)
            * len(colors)
            * len(quantities)
            * len(liveNPCs)
            * len(liveNPCApperances)
            * len(liveNPCEmotions)
            * len(liveNPCActions)
            + len(outdoorView)
            * len(outDoorStatus)
            * len(weatherConditions)
            * (len(outDoorSkyStrongObjects) + 1)
            * len(shapes)
            * len(outDoorSkyStrongObjectStatus)
            * len(quantities)
            * len(outDoorSkyObjects)
            * len(shapes)
            * len(colors)
            * len(quantities)
            * len(liveNPCs)
            * len(liveNPCApperances)
            * len(liveNPCEmotions)
            * len(liveNPCActions)
        )
    )

    return (
        indoor_total,
        outdoor_total,
        story_total,
        story2_total,
        shortStory3Total,
        shortStory4Total,
        L4D2caseTotal,
        appDateTotal,
        lovelyPromptTotal,
    )