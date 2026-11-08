import random
from data.data import *


# common
def generateRandomIcons(quantity):
    return " ".join(random.choices(allIcons, k=quantity))

def generateRandomReciprocal():
    denominator = random.randint(100_000_000_000, 1_000_000_000_000)
    return f"1/{denominator}"

def generateRandomWord():
    return random.choice(UpperText) + "".join(random.choices(LowerText, k=5))

def generateNPC():
    return f"Xung quanh, {random.choice(quantities)} {random.choice(liveNPCs)} {random.choice(liveNPCApperances)}, nhìn thì trông có vẻ {random.choice(liveNPCEmotions)}, và đang {random.choice(liveNPCActions)}"

# tạo cảnh indoor
def generateIndoorObject():
    return f"có {random.choice(quantities)} {random.choice(indoorObjectItems)} có hình dạng là {random.choice(shapes)} và đang phát quang màu {random.choice(colors)}"

def generateIndoorItems():
    return f"Có {random.choice(quantities)} {random.choice(indoorItems)} {random.choice(indoorItemStatus)}, nó có hình dạng là {random.choice(shapes)} , và đang {random.choice(indoorLightVerb)} là {random.choice(indoorItemLightningSource)} màu {random.choice(colors)} từ bên ngoài"

def generateIndoorOutput():
    NPCstr = generateNPC().strip()
    location = random.choice(indoorLocations).strip()
    indoorItemsStr = generateIndoorItems().strip()
    indoorObjectStr = generateIndoorObject().strip()
    endingStr = random.choice(ending).strip()
    output = (
        f"{generateRandomIcons(4)}- Một khung cảnh {random.choice(starting).strip()} -{generateRandomIcons(4)}:\n"
        f"Bên trong {location} {random.choice(indoorStatus)} lâu năm , được xây bằng {random.choice(indoorMaterials)} và sơn màu {random.choice(colors)}. "
        f"{indoorItemsStr}. "
        f"Ở đây, {indoorObjectStr}. "
        f"{NPCstr}. "
        f"Cảm xúc của người đang quan sát có thể nói là {random.choice(status)} {generateRandomIcons(3)}{''.join(random.choices(emotionPunctuations, k=4))}.\n"
        f"{random.choice(comment).strip()} {generateRandomIcons(3)}. {endingStr}{generateRandomIcons(7)}"
    )
    return output


# tạo cảnh outdoor
def returnOutdoorSkyStrongObject():
    outDoorTime = random.choice(times).strip()
    if outDoorTime == "ban ngày":
        return f"Bầu trời đang ban ngày, có Mặt trời có hình {random.choice(shapes)} {random.choice(outDoorSkyStrongObjectStatus)}"
    else:
        return f"Bầu trời đang ban đêm, có {random.choice(outDoorSkyStrongObjects)} có hình dạng là {random.choice(shapes)} {random.choice(outDoorSkyStrongObjectStatus)}"

def generateOutdoorObject():
    return f"Tại {random.choice(outdoorObjectDensity)} , {random.choice(quantities)} {random.choice(outdoorObjects)} có hình dạng là {random.choice(shapes)} đang phát ra ánh sáng màu {random.choice(colors)}"

def generateOutdoorSkyObject():
    return f"Có {random.choice(quantities)} {random.choice(outDoorSkyObjects)} hình dạng là {random.choice(shapes)} đang phát quang màu {random.choice(colors)} giữa không trung"

def generateOutdoorOutput():
    NPCstr = generateNPC().strip()
    location = random.choice(outdoorView).strip()
    outDoorStatusStr = random.choice(outDoorStatus).strip()
    weatherStr = random.choice(weatherConditions).strip()
    skyStrongObjStr = returnOutdoorSkyStrongObject().strip()
    skyObjStr = generateOutdoorSkyObject().strip()
    outdoorObjStr = generateOutdoorObject().strip()
    endingStr = random.choice(ending).strip()
    output = (
        f"{generateRandomIcons(4)} - Một khung cảnh {random.choice(starting).strip()} - {generateRandomIcons(4)}:\n"
        f"{location} đã {outDoorStatusStr} lâu năm, "
        f"thời tiết thì đang {weatherStr}. "
        f"{skyStrongObjStr}. "
        f"{skyObjStr}. "
        f"{outdoorObjStr}. "
        f"{NPCstr}. "
        f"Cảm xúc của người đang quan sát có thể nói là {random.choice(status)} {generateRandomIcons(3)}{''.join(random.choices(emotionPunctuations, k=4))}.\n"
        f"{random.choice(comment).strip()} {generateRandomIcons(3)}. {endingStr}{generateRandomIcons(7)}"
    )
    return output
