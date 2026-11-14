from data.data import *
from Script.common_script import clockPeriods

numberTypePool = len(typeValueNumber) * len(typeNumber)

# tính toán
def formatNumber(number, digits=2):
    if abs(number) < 1:
        return f"{number:.12f}".rstrip("0").rstrip(".")
    n = len(str(int(number))) - 1
    base = str(int(number))[:digits]
    baseFloat = round(int(base) / (10 ** (digits - 1)), 2)
    return f"{baseFloat}×10^{n}"


def returnIconRandom(number):
    iconLength = len(allIcons)
    return iconLength**number


def caculateModelingPromptPool():
    noShoeCount = sum(1 for _, hasShoe in modelFramings if not hasShoe)
    hasShoeCount = sum(1 for _, hasShoe in modelFramings if hasShoe)

    maleSetupPool = (
        len(malePoses)
        * len(maleArmPoses)
        * len(modelGazes)
        * len(maleExpressions)
        * (noShoeCount + hasShoeCount * len(maleShoes))
    )
    femaleSetupPool = (
        len(femalePoses)
        * len(femaleArmPoses)
        * len(modelGazes)
        * len(femaleExpressions)
        * (noShoeCount + hasShoeCount * len(femaleShoes))
    )

    maleTotal = len(backgrounds) * len(maleHair) * maleSetupPool
    femaleTotal = len(backgrounds) * len(femaleHair) * femaleSetupPool

    return maleTotal, femaleTotal


def caculateClockPool():
    return 24 * 60 * 60 * len(clockPeriods) * (numberTypePool**3)


def caculateDatePool():
    return (
        (31 - 1 + 1)  # day
        * (12 - 1 + 1)  # month
        * (1000000000000000 - 100000000000000 + 1)  # year
        * len(dateEras)  # available date eras
        * (numberTypePool**3)  # day, month, year
    )


def caculateQuantity():
    openSceneStatusLen = len(status)
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
    inDoorPrepositionLen = len(inDoorPreposition)

    indoorTotal = (
        (len(liveNPCEmotions))
        * returnIconRandom(8)
        * openSceneStatusLen
        * indoorLocationLen
        * (inDoorPrepositionLen**2)
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
        * (statusLen**3)
        * returnIconRandom(3)
        * (len(emotionPunctuations) ** 4)
        * commentLen
        * returnIconRandom(3)
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
    outDoorPrepositionLen = len(outDoorPreposition)

    outdoorTotal = (
        (len(liveNPCEmotions))
        * returnIconRandom(8)
        * openSceneStatusLen
        * outdoorViewLen
        * (outDoorPrepositionLen**2)
        * outdoorStatusLen
        * weatherConditionsLen
        * (outDoorSkyStrongObjectsLen + 1)
        * (shapesLen**4)
        * outDoorSkyStrongObjectStatusLen
        * (quantityLen**4)
        * outDoorSkyObjectsLen
        * (colorsLen**3)
        * (outdoorObjectDensityLen**2)
        * (outdoorObjectsLen**2)
        * NPCLen
        * NPCAdjLen
        * NPCActionLen
        * (statusLen**3)
        * returnIconRandom(3)
        * (len(emotionPunctuations) ** 4)
        * commentLen
        * returnIconRandom(3)
        * returnIconRandom(7)
    )

    storyTotal = (
        returnIconRandom(10)
        * returnIconRandom(7)
        * len(businesses)
        * len(magicTypes)
        * len(UpperText)
        * (len(LowerText)**5)
        * (outdoorViewLen**3)
        * (outDoorPrepositionLen**3)
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
        * (len(status) ** 2)
        * indoorLocationLen
        * (inDoorPrepositionLen**2)
        * indoorStatusLen
        * len(proverbs)
        * (len(NPCjobs) ** 4)
        * (900000000001**20)  # 19 large numbers + 1 reciprocal denominator
        * (numberTypePool**20)
        * caculateClockPool()
        * caculateDatePool()
        * (indoorObjectLen**4)
        * (shapesLen**5)
        * (quantityLen**3)
        * (colorsLen**6)
        * (NPCLen**5)
        * (len(slogan))
        * (len(nameNPC) ** 4)
        * len(sourceInfo)
        * (len(gpsLocations) ** 2)
        * len(Vehicle)
        * (NPCActionLen**11)
    )

    story2Total = (
        returnIconRandom(10)
        * returnIconRandom(7)
        * (returnIconRandom(3) ** 2)
        * (len(colors) ** 4)
        * (18 * numberTypePool)  # số tuổi của ứng viên
        * (900000000001**29)  # 24 large numbers + 5 reciprocal denominators
        * (numberTypePool**29)
        * (caculateClockPool() ** 2)
        * caculateDatePool()
        * len(Vehicle)
        * len(weatherConditions)
        * (len(companies) ** 3)
        * len(sourceInfo)
        * (inDoorPrepositionLen**4)
        * outDoorPrepositionLen
        * (len(liveNPCs) ** 3)
        * len(liveNPCApperances)
        * (len(liveNPCEmotions) ** 4)
        * (len(liveNPCActions) ** 15)
        * (len(nameNPC) ** 3)
        * (len(indoorLocations) ** 2)
        * len(indoorStatus)
        * (len(status)**2)
        * (len(NPCjobs) ** 2)
        * len(buildings)
        * len(UpperText)
        * (len(LowerText)**5)
        *len(slogan)
        *len(proverbs)
        *(len(outdoorView)**3)
        * len(indoorObjectItems)
    )

    shortStory3Total = (
        (900000000001**27)  # 22 large numbers + 5 reciprocal denominators
        * (numberTypePool**27)
        * (caculateClockPool() ** 3)
        * caculateDatePool()
        * (18 * numberTypePool)
        * len(indoorLocations)
        * (inDoorPrepositionLen**2)
        * outDoorPrepositionLen
        * (len(indoorMaterials) ** 2)
        * returnIconRandom(10)
        * returnIconRandom(7)
        * (returnIconRandom(3)**2)
        * len(Vehicle)
        * (len(gpsLocations)**2)
        * len(magicTypes)
        * len(businesses)
        * len(weatherConditions)
        * (len(outdoorView) ** 2)
        * len(outDoorStatus)
        * (len(companies)**2)
        * len(outDoorSkyStrongObjects)
        * (len(shapes) ** 3)
        * len(outDoorSkyStrongObjectStatus)
        * (len(status) ** 9)
        * len(outdoorObjectDensity)
        * (len(outdoorObjects)**2)
        * (len(colors) ** 9)
        * len(buildings)
        * (len(liveNPCEmotions) ** 7)
        * (len(liveNPCs) ** 4)
        * (len(liveNPCActions) ** 15)
        * (len(sourceInfo) ** 2)
        * (len(liveNPCApperances) ** 3)
        * (len(indoorObjectItems)**3)
        * (len(proverbs) ** 2)
        * (len(nameNPC) ** 3)
        * (len(slogan)**2)
        * len(UpperText)
        * (len(LowerText)**5)
        * (len(GirlActions)**2)
        * (len(BoyActions)**2)
        * len(LoveActions)
    )

    shortStory4Total = (
        (900000000001**61)  # 54 large numbers + 7 reciprocal denominators
        * (numberTypePool**61)
        * (caculateClockPool() ** 4)
        * caculateDatePool()
        * (18 * numberTypePool)
        * returnIconRandom(10)
        * returnIconRandom(7)
        * (len(Vehicle)**2)
        * (len(indoorLocations) ** 3)
        * (inDoorPrepositionLen**3)
        * (outDoorPrepositionLen**2)
        * len(indoorStatus)
        * len(indoorMaterials)
        * (len(colors) ** 4)
        * (len(outdoorView) ** 3)
        * len(weatherConditions)
        * (len(shapes) ** 2)
        * (len(status) ** 7)
        * len(outDoorSkyStrongObjects)
        * len(outDoorSkyStrongObjectStatus)
        * (len(liveNPCActions) ** 23)
        * (len(liveNPCEmotions) ** 7)
        * (len(liveNPCs) ** 5)
        * (len(nameNPC) ** 6)
        * len(magicTypes)
        * (returnIconRandom(3)**2)
        * (len(companies) ** 2)
        * (len(gpsLocations) ** 2)
        * (len(indoorObjectItems) ** 2)
        * (len(liveNPCApperances)**2)
        * len(UpperText)
        * (len(LowerText)**5)
        * len(GirlActions)
        * len(BoyActions)
        * len(quantities)
        * len(outDoorStatus)
    )
    
    L4D2caseTotal = (
        len(mapsL4D2) *
        len(charactersL4D2) *
        (100 - 1 + 1) *  # HP
        (len(weaponsL4D2) * (500 - 1 + 1) + 1) *  # weapon + ammo, or no weapon
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

    couplePromptTotal = (
        len(BoyActions)
        * len(GirlActions)
        * len(LoveActions)
        *(len(coupleCall)**2)
        * (len(status)**2)
        * len(adjApperanceBoys)
        * len(adjAppearanceGirls)
        * ((len(loveIcons)**4)**2)
        * len(liveNPCEmotions)
        *len(fashionHairMale)
        * len(fashionHairFemale)
        * (
            len(indoorLocations)
            * (inDoorPrepositionLen**3)
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
            * (outDoorPrepositionLen**2)
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
    
    modelingPromptMaleTotal, modelingPromptFemaleTotal = caculateModelingPromptPool()
    modelingPromptTotal = modelingPromptMaleTotal + modelingPromptFemaleTotal

    return (
        indoorTotal,
        outdoorTotal,
        storyTotal,
        story2Total,
        shortStory3Total,
        shortStory4Total,
        L4D2caseTotal,
        appDateTotal,
        couplePromptTotal,
        modelingPromptTotal,
    )
