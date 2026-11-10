import random
from data.data import *
from Script.common_script import *

#prompt for AI Art

#Indoor scene prompt
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

# Outdoor scene prompt
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

# Romantic prompt
def generateLovelyPrompt():
    typeLocation = random.randint(1,2)
    
    commonSence = (
        f"[Note: Strictly preserve 100% facial features, facial structures, and original outfits from both source images. Crucial: directly transplant the original faces and clothes from the input photos without altering them or adding any extra clothing/accessories]. \n\n"
        f"Hai người này là cặp đôi yêu nhau rất sâu đậm. Chàng trai rất đẹp trai và có đôi mắt 2 mí rất đẹp, áo của chàng trai đóng thùng gọn gàng. Còn cô gái thì có nhan sắc xinh đẹp tuyệt trần. \n"
        f"Tóc của chàng trai để kiểu {random.choice(fashionHairMale)}, cô gái thì có kiểu tóc {random.choice(fashionHairFemale)}. \n"
        f"Chàng trai đang {random.choice(BoyActions)}. Còn cô gái thì đang {random.choice(GirlActions)}. \n"
        f"Bọn họ đang {random.choice(LoveActions)} và trông họ có vẻ {random.choice(liveNPCEmotions)}. \n\n"
        f"Và khung cảnh cặp đôi này đang hẹn hò là: \n"
    )
    
    endingStatus = ( f"Đây thật là khung cảnh {random.choice(status)}! \n"
                     f"Cảm xúc chung của cặp đôi có thể nói là: {''.join(random.choices(loveIcons, k=4))}" ) 
    
    if typeLocation == 1:
        output = (
            f"{commonSence}"
            f"Ở bên trong {random.choice(indoorLocations).strip()} {random.choice(indoorStatus)} lâu năm. \n"
            f"Nó được xây bằng {random.choice(indoorMaterials)} và sơn màu {random.choice(colors)}. \n"
            f"Tại đó, {generateIndoorItems().strip()}. \n"
            f"Và cũng đang có {generateIndoorObject().strip()} ở đây. \n"
            f"{generateNPC().strip()}. \n\n"
            f"{endingStatus}"
        )
    else:
        output = (
            f"{commonSence}"
            f"{random.choice(outdoorView).strip()} đã {random.choice(outDoorStatus).strip()} lâu năm. \n"
            f"Và ở đây, đang có thời tiết {random.choice(weatherConditions).strip()}. \n"
            f"{returnOutdoorSkyStrongObject().strip()}. \n"
            f"Và cũng đang có {generateOutdoorSkyObject().strip()}. \n"
            f"{generateNPC().strip()}. \n\n"
            f"{endingStatus}"
        )
    return output

# Modeling prompt
def generateModelingPrompt():
    gender = random.choice(["male", "female"])
    selectedPose, gazeFlag = random.choice(globals()[f"{gender}Poses"])
    selectedArmPose = random.choice(globals()[f"{gender}ArmPoses"])
    selectedGaze = random.choice(modelGazes)[gazeFlag]
    selectedExpression = random.choice(globals()[f"{gender}Expressions"])
    framingText, hasShoe = random.choice(modelFramings)
    
    if hasShoe:
        shoeChoice = random.choice(globals()[f"{gender}Shoes"])
        setupText = framingText.format(
            pose=selectedPose, 
            armPose=selectedArmPose, 
            gaze=selectedGaze,
            expression=selectedExpression,
            shoe=shoeChoice
        )
    else:
        setupText = framingText.format(
            pose=selectedPose, 
            armPose=selectedArmPose,
            gaze=selectedGaze,
            expression=selectedExpression
        )

    return (
        f"[Note: Strictly maintain 100% accurate facial recognition, bone structure, and unique facial features of the subject from the source reference photo, "
        f"ensuring it is unmistakably the exact same person, while naturally adapting the head angle, gaze direction, and facial expression as described in the prompt. "
        f"Strictly preserve 100% of the original outfit and existing accessories without altering or redesigning them. "
        f"However, if the prompt explicitly requests new items or accessories that conflict with or replace existing ones in the reference photo, prioritize and apply the prompt's instructions over the source photo. "
        f"Output must be a realistic photograph]. \n\n"
        f"This is a {gender.upper()} MODEL: \n"
        f" - {setupText} \n"
        f" - The hairstyle is: {random.choice(globals()[f'{gender}Hair'])}. \n"
        f" - The background is: {random.choice(backgrounds)}."
    )