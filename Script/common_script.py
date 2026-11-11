import random
from data.data import *


# common
def generateRandomIcons(quantity):
    return " ".join(random.choices(allIcons, k=quantity))

def generateNPC():
    return f"Xung quanh, {random.choice(quantities)} {random.choice(liveNPCs)} {random.choice(liveNPCApperances)}, nhìn họ trông có vẻ {random.choice(liveNPCEmotions)}, và đang {random.choice(liveNPCActions)}"

def generateOpenScene():
    return f"{generateRandomIcons(4)} - Đây là một khung cảnh {random.choice(status).strip()} - {generateRandomIcons(4)}:\n"

def generateRandomReciprocal():
    denominator = random.randint(*randomLargeNumberRange)
    return f"(1/{denominator})"

def generateRandomLargeNumber():
    return f"{random.randint(*randomLargeNumberRange):,}"

def generateRandomWord():
    return random.choice(UpperText) + "".join(random.choices(LowerText, k=5))

def generateEnding():
    return (
        f"Cảm xúc của người đang quan sát có thể nói là {random.choice(status)} {generateRandomIcons(3)}{''.join(random.choices(emotionPunctuations, k=4))}.\n"
        f"{random.choice(comment).strip()} {generateRandomIcons(3)}. Cảnh vật ở đây trông rất {random.choice(status)} và {random.choice(status)} {generateRandomIcons(7)}."
    )


def generateIndoorItems():
    return f"{random.choice(quantities)} {random.choice(indoorItems)} {random.choice(indoorItemStatus)}, nó có hình dạng là {random.choice(shapes)}, và đang {random.choice(indoorLightVerb)} là {random.choice(indoorItemLightningSource)} màu {random.choice(colors)} từ bên ngoài"

def generateIndoorObject():
    return f"{random.choice(quantities)} {random.choice(indoorObjectItems)} đang có hình dạng là {random.choice(shapes)} và đang phát quang màu {random.choice(colors)}"


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


def generateClock():
    return f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d} {random.choice(clockPeriods)}"
