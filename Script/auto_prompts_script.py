import random
from data.data import *
from Script.common_script import *

#prompt for AI Art
def generateLovelyPrompt():
    typeLocation = random.randint(1,2)
    
    commonSence = (
        f"[Note: Strictly preserve 100% facial features, facial structures, and original outfits from both source images. Crucial: directly transplant the original faces and clothes from the input photos without altering them or adding any extra clothing/accessories]. \n\n"
        f"Hai người này là cặp đôi yêu nhau rất sâu đậm. Chàng trai rất đẹp trai và có đôi mắt 2 mí rất đẹp, áo của chàng trai đóng thùng gọn gàng. Còn cô gái thì có nhan sắc xinh đẹp tuyệt trần. \n"
        f"Tóc của chàng trai để kiểu {random.choice(fashionHairMale)}, cô gái thì có kiểu tóc {random.choice(fashionHairFemale)}. \n"
        f"Chàng trai đang {random.choice(BoyActions)}. Còn cô gái thì đang {random.choice(GirlActions)}. \n"
        f"Bọn họ đang {random.choice(LoveActions)} và trông họ có vẻ {random.choice(liveNPCEmotions)}. \n"
    )
    
    endingStatus = ( f"Đây thật là khung cảnh {random.choice(status)}! \n"
                     f"Cảm xúc chung có thể nói là : {''.join(random.choices(loveIcons, k=4))}" ) 
    
    if typeLocation == 1:
        output = (
            f"{commonSence}\n"
            f"Và khung cảnh bọn họ đang hẹn hò là: Ở bên trong {random.choice(indoorLocations).strip()} {random.choice(indoorStatus)} lâu năm. \n"
            f"Nó được xây bằng {random.choice(indoorMaterials)} và sơn màu {random.choice(colors)}. \n"
            f"Tại đó, {generateIndoorItems().strip()}. \n"
            f"Và cũng đang có {generateIndoorObject().strip()} ở đây. \n"
            f"{generateNPC().strip()}. \n\n"
            f"{endingStatus}"
        )
    else:
        output = (
            f"{commonSence}\n"
            f"Và bọn họ đang hẹn hò ở khung cảnh là : {random.choice(outdoorView).strip()} đã {random.choice(outDoorStatus).strip()} lâu năm \n"
            f"và đang có thời tiết {random.choice(weatherConditions).strip()}. \n"
            f"{returnOutdoorSkyStrongObject().strip()}. \n"
            f"Và cũng đang có {generateOutdoorSkyObject().strip()}. \n"
            f"{generateNPC().strip()}. \n\n"
            f"{endingStatus}"
        )
    return output


def generateModelingPrompt():
    gender = random.choice(["male", "female"])
    selectedPose = random.choice(globals()[f"{gender}Poses"])
    selectedArmPose = random.choice(globals()[f"{gender}ArmPoses"])
    framingText, hasShoe = random.choice(modelFramings)
    
    if hasShoe:
        shoeChoice = random.choice(globals()[f"{gender}Shoes"])
        setupText = framingText.format(
            pose=selectedPose, 
            armPose=selectedArmPose, 
            shoe=shoeChoice
        )
    else:
        setupText = framingText.format(
            pose=selectedPose, 
            armPose=selectedArmPose
        )

    return (
        f"[Note: Strictly preserve 100% of the facial features, facial structure, identity, and original outfits from the source reference photo. " 
        f"Do not alter the face or clothing, and do not add extra accessories. Output must be a realistic photograph]. \n\n"
        f"This is a {gender.upper()} MODEL: \n"
        f" - {setupText} \n"
        f" - The hairstyle is: {random.choice(globals()[f'{gender}Hair'])}. \n"
        f" - The background is: {random.choice(backgrounds)}."
    )