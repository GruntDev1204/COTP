import random
from data.data import *
from Script.common_script import *

#prompt for AI Art
def createNoteArt(mode=0):
    identityRules = [
        #couple
        "Keep the natural facial identity and recognizable features of both individuals from the reference photos without artificially remixing, blending, or over-stylizing their faces, allowing flexible head angles, natural eye contact, and organic expressions that fit their interaction. ",
        #single
        "Strictly maintain 100% accurate facial recognition, bone structure, and unique facial features of the subject from the source reference photos, ensuring it is unmistakably the exact same person, while naturally adapting the head angle, gaze direction, and facial expression as described in the prompt. ",
    ]
    
    return (
        f"[Note: {identityRules[mode]}"
        f"Strictly preserve 100% of the original outfits and existing accessories without altering or redesigning them, "
        f"unless the prompt explicitly introduces new items that conflict with or replace existing ones in the reference photos, "
        f"in which case prioritize the prompt's instructions. "
        f"Output must be a realistic photograph.]\n\n"
    )

#Indoor scene prompt
def generateIndoorOutput():
    output = (
        f"{generateOpenScene()}\n"
        f"This is a Indoor Scene: \n"
        f"Ngay {random.choice(inDoorPreposition).upper()} thuộc bên trong {random.choice(indoorLocations).strip()}, trông rất {random.choice(indoorStatus)}, nó được xây bằng {random.choice(indoorMaterials)} và được sơn màu {random.choice(colors)}. \n"
        f"Có {generateIndoorItems().strip()}. \n"
        f"{random.choice(inDoorPreposition).upper()}, đang có {generateIndoorObject().strip()}. \n"
        f"{generateNPC().strip()}. \n\n"
        f"{generateEnding()}"
    )
    return output

# Outdoor scene prompt
def generateOutdoorOutput():
    output = (
        f"{generateOpenScene()}\n"
        f"This is a Outdoor Scene: \n"
        f"Ngay {random.choice(outDoorPreposition).upper()} tại {random.choice(outdoorView).strip()} đã {random.choice(outDoorStatus).strip()} lâu năm, "
        f"thời tiết thì đang {random.choice(weatherConditions).strip()}. \n"
        f"{returnOutdoorSkyStrongObject().strip()}. \n"
        f"Có {generateOutdoorSkyObject().strip()}. \n"
        f"{random.choice(outDoorPreposition).upper()}, đang có {generateOutdoorObject().strip()} {generateOutdoorObject().strip()}. \n"
        f"{generateNPC().strip()}. \n\n"
        f"{generateEnding()}"
    )
    return output

# Romantic prompt
def generateCouplePrompt():
    
    commonSence = (
        f"{createNoteArt(0)}"
        f" - {''.join(random.choices(loveIcons, k=4))} This is a Romantic Scene: \n"
        f"Hai người này, vốn là {random.choice(coupleCall)} đang yêu nhau rất {random.choice(status)}. "
        f"Chàng trai rất {random.choice(adjApperanceBoys)} và có đôi mắt 2 mí, áo của chàng trai đóng thùng gọn gàng. "
        f"Còn cô gái thì có đôi mắt long lanh quyến rũ và nhan sắc {random.choice(adjAppearanceGirls)}. \n"
        f"Tóc của chàng trai để kiểu {random.choice(fashionHairMale)}, cô gái thì có kiểu tóc {random.choice(fashionHairFemale)}. \n"
        f"Chàng trai đang {random.choice(BoyActions)}. Đáp lại chàng trai, cô gái thì đang {random.choice(GirlActions)}. \n"
        f"Bọn họ đang {random.choice(LoveActions)} và trông họ có vẻ {random.choice(liveNPCEmotions)}. \n\n"
        f"Và khung cảnh {random.choice(coupleCall)} này đang hẹn hò là: \n"
    )
    
    endingStatus = ( f"Đây quả thật là khung cảnh {random.choice(status)}! \n"
                     f"Cảm xúc chung có thể nói là: {''.join(random.choices(loveIcons, k=4))}" ) 
  
    return random.choice((
        lambda:(
            f"{commonSence}"
            f"{random.choice(inDoorPreposition).upper()} {random.choice(indoorLocations).strip()} {random.choice(indoorStatus)} lâu năm. \n"
            f"Nó được xây bằng {random.choice(indoorMaterials)} và sơn màu {random.choice(colors)}. \n"
            f"{random.choice(inDoorPreposition).upper()}, {generateIndoorItems().strip()}. \n"
            f"Và cũng đang có {generateIndoorObject().strip()} {random.choice(inDoorPreposition)}. \n"
            f"{generateNPC().strip()}. \n\n"
            f"{endingStatus}"
        ),
        lambda:(
            f"{commonSence}"
            f"{random.choice(outDoorPreposition).upper()} {random.choice(outdoorView).strip()} đã {random.choice(outDoorStatus).strip()} lâu năm. \n"
            f"Và {random.choice(outDoorPreposition).upper()}, đang có thời tiết {random.choice(weatherConditions).strip()}. \n"
            f"{returnOutdoorSkyStrongObject().strip()}. \n"
            f"Và cũng đang có {generateOutdoorSkyObject().strip()}. \n"
            f"{generateNPC().strip()}. \n\n"
            f"{endingStatus}"
        ),
    ))()

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
        f"{createNoteArt(1)}"
        f"This is a {gender.upper()} MODEL: \n"
        f" - {setupText} \n"
        f" - The hairstyle is: {random.choice(globals()[f'{gender}Hair'])}. \n"
        f" - The background is: {random.choice(backgrounds)}."
    )
