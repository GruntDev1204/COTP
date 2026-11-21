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
    dayCount = sum(1 for time in times if time.strip() == "ban ngày")
    nightCount = sum(1 for time in times if time.strip() != "ban ngày")

    indoorBackgroundPool = (
        len(inDoorPreposition) ** 3
        * len(indoorLocations)
        * len(indoorStatus)
        * len(indoorMaterials)
        * len(colors) ** 3
        * len(quantities) ** 3
        * len(indoorItems)
        * len(indoorItemStatus)
        * len(shapes) ** 2
        * len(indoorLightVerb)
        * len(indoorItemLightningSource)
        * len(indoorObjectItems)
        * len(liveNPCs)
        * len(liveNPCApperances)
        * len(liveNPCEmotions)
        * len(liveNPCActions)
    )
    outdoorSkyStrongObjectPool = (
        len(shapes)
        * len(outDoorSkyStrongObjectStatus)
        * (dayCount + nightCount * len(outDoorSkyStrongObjects))
    )
    outdoorBackgroundPool = (
        len(outDoorPreposition) ** 3
        * len(outdoorView)
        * len(outDoorStatus)
        * len(weatherConditions)
        * outdoorSkyStrongObjectPool
        * len(quantities)
        * len(outDoorSkyObjects)
        * len(shapes)
        * len(colors)
        * len(colors)
        * len(outdoorObjectDensity)
        * len(quantities)
        * len(outdoorObjects)
        * len(shapes)
        * len(colors)
        * len(liveNPCs)
        * len(liveNPCApperances)
        * len(liveNPCEmotions)
        * len(liveNPCActions)
    )
    backgroundPool = len(backgrounds) + indoorBackgroundPool + outdoorBackgroundPool

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

    maleTotal = backgroundPool * len(maleHair) * maleSetupPool
    femaleTotal = backgroundPool * len(femaleHair) * femaleSetupPool

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
        * (shapesLen**3)
        * outDoorSkyStrongObjectStatusLen
        * colorsLen
        * (quantityLen**3)
        * outDoorSkyObjectsLen
        * (colorsLen**2)
        * outdoorObjectDensityLen
        * (outdoorObjectsLen)
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

    dayCount = sum(1 for time in times if time.strip() == "ban ng\u00e0y")
    nightCount = sum(1 for time in times if time.strip() != "ban ng\u00e0y")
    storySkyPool = dayCount + nightCount * len(outDoorSkyStrongObjects)
    storyLargeNumberPool = (
        randomLargeNumberRange[1] - randomLargeNumberRange[0] + 1
    ) * numberTypePool
    storyAgePool = 18 * numberTypePool

    storyTotal = (
        returnIconRandom(17)
        * (storyLargeNumberPool**20)
        * caculateDatePool()
        * caculateClockPool()
        * len(UpperText)
        * (len(LowerText)**5)
        * len(sourceInfo)
        * len(businesses)
        * (len(indoorObjectItems)**4)
        * (len(outDoorPreposition)**3)
        * len(outDoorStatus)
        * len(weatherConditions)
        * len(outdoorObjectDensity)
        * (len(quantities)**4)
        * (len(outdoorObjects)**2)
        * (len(shapes)**7)
        * (len(colors)**7)
        * (len(indoorMaterials)**2)
        * len(indoorItems)
        * len(indoorItemStatus)
        * len(indoorLightVerb)
        * len(indoorItemLightningSource)
        * (len(liveNPCs)**5)
        * (len(status)**2)
        * (len(nameNPC)**4)
        * (len(liveNPCApperances)**2)
        * (len(liveNPCEmotions)**5)
        * (len(liveNPCActions)**11)
        * len(magicTypes)
        * (len(NPCjobs)**5)
        * len(companies)
        * len(indoorLocations)
        * (len(gpsLocations)**2)
        * len(outDoorSkyObjects)
        * (len(outdoorView)**3)
        * len(indoorStatus)
        * len(slogan)
        * len(proverbs)
        * storySkyPool
        * (len(inDoorPreposition)**2)
        * len(Vehicle)
    )

    story2Total = (
        returnIconRandom(23)
        * (storyLargeNumberPool**30)
        * storyAgePool
        * caculateDatePool()
        * (caculateClockPool()**2)
        * len(UpperText)
        * (len(LowerText)**5)
        * len(weatherConditions)
        * (len(inDoorPreposition)**4)
        * (len(status)**3)
        * len(quantities)
        * len(outDoorSkyObjects)
        * (len(shapes)**3)
        * (len(colors)**6)
        * (len(companies)**3)
        * (len(liveNPCActions)**15)
        * len(indoorObjectItems)
        * len(outDoorPreposition)
        * len(slogan)
        * (len(liveNPCs)**3)
        * len(liveNPCApperances)
        * (len(liveNPCEmotions)**4)
        * (len(nameNPC)**3)
        * len(proverbs)
        * (len(indoorLocations)**2)
        * len(indoorStatus)
        * len(sourceInfo)
        * (len(outdoorView)**3)
        * len(buildings)
        * len(outdoorObjects)
        * storySkyPool
        * (len(NPCjobs)**2)
        * len(Vehicle)
    )

    shortStory3Total = (
        returnIconRandom(23)
        * (storyLargeNumberPool**28)
        * storyAgePool
        * caculateDatePool()
        * (caculateClockPool()**3)
        * len(UpperText)
        * (len(LowerText)**5)
        * (len(status)**10)
        * len(weatherConditions)
        * len(quantities)
        * len(outDoorSkyObjects)
        * (len(shapes)**4)
        * (len(colors)**11)
        * (len(gpsLocations)**2)
        * (len(companies)**2)
        * (len(liveNPCActions)**15)
        * (len(indoorObjectItems)**3)
        * len(outDoorPreposition)
        * len(outDoorStatus)
        * (len(inDoorPreposition)**2)
        * len(outdoorObjectDensity)
        * (len(outdoorObjects)**2)
        * len(buildings)
        * (len(liveNPCs)**4)
        * (len(nameNPC)**3)
        * (len(liveNPCEmotions)**7)
        * len(LoveActions)
        * (len(slogan)**2)
        * (len(sourceInfo)**2)
        * (len(liveNPCApperances)**3)
        * len(indoorLocations)
        * len(businesses)
        * len(magicTypes)
        * (len(indoorMaterials)**2)
        * (len(proverbs)**2)
        * storySkyPool
        * (len(BoyActions)**2)
        * (len(GirlActions)**2)
        * (len(outdoorView)**2)
        * len(Vehicle)
    )

    shortStory4Total = (
        returnIconRandom(23)
        * (storyLargeNumberPool**62)
        * storyAgePool
        * caculateDatePool()
        * (caculateClockPool()**4)
        * len(UpperText)
        * (len(LowerText)**5)
        * (len(liveNPCActions)**23)
        * (len(nameNPC)**6)
        * storySkyPool
        * (len(outDoorPreposition)**2)
        * len(outDoorStatus)
        * len(weatherConditions)
        * len(quantities)
        * len(outDoorSkyObjects)
        * (len(shapes)**4)
        * (len(colors)**6)
        * (len(status)**8)
        * (len(indoorLocations)**3)
        * len(indoorStatus)
        * len(indoorMaterials)
        * (len(liveNPCs)**5)
        * (len(liveNPCEmotions)**7)
        * (len(inDoorPreposition)**3)
        * len(magicTypes)
        * (len(companies)**2)
        * (len(gpsLocations)**2)
        * (len(Vehicle)**2)
        * (len(liveNPCApperances)**2)
        * (len(indoorObjectItems)**2)
        * (len(outdoorView)**3)
        * len(outdoorObjects)
        * len(GirlActions)
        * len(BoyActions)
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

    boyFlaggedActionLen = sum(action[1] != 0 for action in BoyActions)
    girlFlaggedActionLen = sum(action[1] != 0 for action in GirlActions)
    coupleActionPairPool = (
        len(BoyActions) * len(GirlActions)
        + (2 * boyFlaggedActionLen * girlFlaggedActionLen)
    )

    couplePromptSharedPool = (
        coupleActionPairPool
        * len(LoveActions)
        * len(coupleCall)
        * (len(status)**2)
        * len(adjApperanceBoys)
        * len(adjAppearanceGirls)
        * ((len(loveIcons)**4)**3)
        * len(liveNPCEmotions)
        * len(fashionHairMale)
        * len(fashionHairFemale)
    )

    coupleEnglishScenePool = len(coupleCall) * len(backgrounds)

    coupleIndoorScenePool = (
        len(coupleCall)
        * len(indoorLocations)
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
    )

    coupleOutdoorScenePool = (
        len(coupleCall)
        * len(outdoorView)
        * (outDoorPrepositionLen**3)
        * len(outDoorStatus)
        * len(weatherConditions)
        * (len(outDoorSkyStrongObjects) + 1)
        * len(shapes)
        * len(outDoorSkyStrongObjectStatus)
        * len(quantities)
        * len(outDoorSkyObjects)
        * len(shapes)
        * len(colors)
        * len(colors)
        * len(outdoorObjectDensity)
        * len(quantities)
        * len(outdoorObjects)
        * len(shapes)
        * len(colors)
        * len(quantities)
        * len(liveNPCs)
        * len(liveNPCApperances)
        * len(liveNPCEmotions)
        * len(liveNPCActions)
    )

    couplePromptTotal = couplePromptSharedPool * (
        coupleEnglishScenePool
        + coupleIndoorScenePool
        + coupleOutdoorScenePool
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
