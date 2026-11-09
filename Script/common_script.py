import random
from data.data import *


# common
def generateRandomIcons(quantity):
    return " ".join(random.choices(allIcons, k=quantity))

def generateNPC():
    return f"Xung quanh, {random.choice(quantities)} {random.choice(liveNPCs)} {random.choice(liveNPCApperances)}, nhìn họ trông có vẻ {random.choice(liveNPCEmotions)} và họ đang {random.choice(liveNPCActions)}"

def generateOpenScene():
    return f"{generateRandomIcons(4)} - Đây là một khung cảnh {random.choice(starting).strip()} - {generateRandomIcons(4)}:\n"

def generateEnding():
    return (
        f"Cảm xúc của người đang quan sát có thể nói là {random.choice(status)} {generateRandomIcons(3)}{''.join(random.choices(emotionPunctuations, k=4))}.\n"
        f"{random.choice(comment).strip()} {generateRandomIcons(3)}. {random.choice(ending).strip()}{generateRandomIcons(7)}."
    )

# tạo cảnh indoor
def generateIndoorItems():
    return f"{random.choice(quantities)} {random.choice(indoorItems)} {random.choice(indoorItemStatus)}, nó có hình dạng là {random.choice(shapes)}, và đang {random.choice(indoorLightVerb)} là {random.choice(indoorItemLightningSource)} màu {random.choice(colors)} từ bên ngoài"

def generateIndoorObject():
    
    return f"{random.choice(quantities)} {random.choice(indoorObjectItems)} đang có hình dạng là {random.choice(shapes)} và đang phát quang màu {random.choice(colors)}"

def generateIndoorOutput():
    NPCstr = generateNPC().strip()
    location = random.choice(indoorLocations).strip()
    indoorItemsStr = generateIndoorItems().strip()
    indoorObjectStr = generateIndoorObject().strip()
    output = (
        f"{generateOpenScene()}\n"
        f"Bên trong {location}, trông rất {random.choice(indoorStatus)}, nó được xây bằng {random.choice(indoorMaterials)} và được sơn màu {random.choice(colors)}. \n"
        f"Có {indoorItemsStr}. \n"
        f"Ở đây, đang có {indoorObjectStr}. \n"
        f"{NPCstr}. \n\n"
        f"{generateEnding()}"
    )
    return output

# tạo cảnh outdoor
def returnOutdoorSkyStrongObject():
    outDoorTime = random.choice(times).strip()
    if outDoorTime == "ban ngày":
        return f"Bầu trời đang ban ngày, có Mặt trời có hình {random.choice(shapes)} và nó đang trong tình trạng {random.choice(outDoorSkyStrongObjectStatus)}"
    else:
        return f"Bầu trời đang ban đêm, có {random.choice(outDoorSkyStrongObjects)} có hình dạng là {random.choice(shapes)} và nó đang trong tình trạng {random.choice(outDoorSkyStrongObjectStatus)}"

def generateOutdoorObject():
    return f"{random.choice(outdoorObjectDensity)}, {random.choice(quantities)} {random.choice(outdoorObjects)} đang có hình dạng là {random.choice(shapes)} đang phát ra ánh sáng màu {random.choice(colors)}"

def generateOutdoorSkyObject():
    return f"{random.choice(quantities)} {random.choice(outDoorSkyObjects)} đang có hình dạng là {random.choice(shapes)} và nó đang phát quang màu {random.choice(colors)} giữa không trung"

def generateOutdoorOutput():
    NPCstr = generateNPC().strip()
    location = random.choice(outdoorView).strip()
    outDoorStatusStr = random.choice(outDoorStatus).strip()
    weatherStr = random.choice(weatherConditions).strip()
    skyStrongObjStr = returnOutdoorSkyStrongObject().strip()
    skyObjStr = generateOutdoorSkyObject().strip()
    outdoorObjStr = generateOutdoorObject().strip()
    output = (
        f"{generateOpenScene()}\n"
        f"{location} đã {outDoorStatusStr} lâu năm, "
        f"thời tiết thì đang {weatherStr}. \n"
        f"{skyStrongObjStr}. \n"
        f"Có {skyObjStr}. \n"
        f"Tại {outdoorObjStr}. \n"
        f"{NPCstr}. \n\n"
        f"{generateEnding()}"
    )
    return output
