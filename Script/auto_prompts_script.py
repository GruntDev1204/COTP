import random
from data.data import *
from Script.common_script import *

#prompt for AI Art
def generateLovelyPrompt():
    typeLocation = random.randint(1,2)
    
    commonSence = (
            f"Hai người này là cặp đôi yêu nhau rất sâu đậm. Tóc của chàng trai có kiểu {random.choice(fashionHairMale)}, cô gái thì có kiểu tóc {random.choice(fashionHairFemale)}. \n"
            f"Chàng trai rất đẹp trai và có đôi mắt 2 mí rất đẹp, áo của chàng trai đóng thùng gọn gàng. Cô gái có nhan sắc xinh đẹp tuyệt trần (giữ nguyên outfit 2 ảnh gốc). \n"
            f"Chàng trai đang {random.choice(BoyActions)}. Còn cô gái thì đang {random.choice(GirlActions)}. \n"
            f"Bọn họ đang {random.choice(LoveActions)} và trông họ có vẻ {random.choice(liveNPCEmotions)}. \n"
    )
    
    endingStatus = ( f"Đây thật là 1 khung cảnh {random.choice(status)}! \n"
                     f"Cảm xúc chung có thể nói là : {''.join(random.choices(loveIcons, k=4))}" ) 
    
    if typeLocation == 1:
        output = (
            f"{commonSence}\n"
            f"Và khung cảnh hẹn hò đang là bên trong {random.choice(indoorLocations).strip()} {random.choice(indoorStatus)} lâu năm. \n"
            f"Nó được xây bằng {random.choice(indoorMaterials)} và sơn màu {random.choice(colors)}. \n"
            f"{generateIndoorItems().strip()}. \n"
            f"Ở đây, {generateIndoorObject().strip()}. \n"
            f"{generateNPC().strip()}. \n\n"
            f"{endingStatus}"
        )
    else:
        output = (
            f"{commonSence}\n"
            f"Và khung cảnh hẹn hò đang là {random.choice(outdoorView).strip()} đã {random.choice(outDoorStatus).strip()} lâu năm. \n"
            f"Khung cảnh đang có thời tiết {random.choice(weatherConditions).strip()}. \n"
            f"{returnOutdoorSkyStrongObject().strip()}. \n"
            f"{generateOutdoorSkyObject().strip()}. \n"
            f"{generateNPC().strip()}. \n\n"
            f"{endingStatus}"
        )
    return output

def generateModelingPrompt():
    gender = random.choice(["male", "female"])

    return (
        f"This is a {gender.upper()} MODEL. \n"
        f" - {(random.choice(modelSetup)).format(shoe=random.choice(globals()[f'{gender}Shoes']))} \n"
        f" - The hairstyle is : {random.choice(globals()[f'{gender}Hair'])}. \n"
        f" - The background is : {random.choice(backgrounds)}."
    )