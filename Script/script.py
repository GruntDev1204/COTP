import random
from Script.caculate_pool import *
from data.data import *

# common
def generateRandomIcons(quantity):
    return " ".join(random.choices(all_icons, k=quantity))

def generateNPC():
    return f"Xung quanh, {random.choice(quantities)} {random.choice(liveNPCs)} {random.choice(liveNPCApperances)}, nhìn thì trông có vẻ {random.choice(liveNPCEmotions)}, và đang {random.choice(liveNPCActions)}"

# tạo cảnh indoor
def generateIndoorObject():
    return f"có {random.choice(quantities)} {random.choice(indoorObjectItems)} có hình dạng là {random.choice(shapes)} và đang phát quang màu {random.choice(colors)}"

def generateIndoorItems():
    return f"Có {random.choice(quantities)} {random.choice(indoorItems)} {random.choice(indoorItemStatus)}, nó có hình dạng là {random.choice(shapes)} , và đang {random.choice(indoorLightVerb)} là {random.choice(indoorItemLightningSource)} màu {random.choice(colors)} từ bên ngoài"

def generateIndoorScene():
    NPCstr = generateNPC().strip()
    location = random.choice(indoorLocations).strip()
    indoorItemsStr = generateIndoorItems().strip()
    indoorObjectStr = generateIndoorObject().strip()
    endingStr = random.choice(ending).strip()
    scene = (
        f"{''.join(random.choices(titleEmojis, k=4))}- Một khung cảnh {random.choice(starting).strip()} -{''.join(random.choices(titleEmojis, k=4))}:\n"
        f"Bên trong {location} {random.choice(indoorStatus)} lâu năm , được xây bằng {random.choice(indoorMaterials)} và sơn màu {random.choice(colors)}. "
        f"{indoorItemsStr}. "
        f"Ở đây, {indoorObjectStr}. "
        f"{NPCstr}. "
        f"Cảm xúc của người đang quan sát có thể nói là {random.choice(status)} {''.join(random.choices(emojiStatus, k=3))}{''.join(random.choices(emotionPunctuations, k=4))}.\n"
        f"{random.choice(comment).strip()} {''.join(random.choices(cuteEmojis, k=3))}. {endingStr}{generateRandomIcons(7)}"
    )
    return scene


# tạo cảnh outdoor
def returnOutdoorSkyStrongObject():
    outDoorTime = random.choice(times).strip().upper()
    if outDoorTime == "ban ngày":
        return f"Bầu trời đang ban ngày, có Mặt trời có hình {random.choice(shapes)} {random.choice(outDoorSkyStrongObjectStatus)}"
    else:
        return f"Bầu trời đang ban đêm, có {random.choice(outDoorSkyStrongObjects)} có hình dạng là {random.choice(shapes)} {random.choice(outDoorSkyStrongObjectStatus)}"

def generateOutdoorObject():
    return f"Tại {random.choice(outdoorObjectDensity)} , {random.choice(quantities)} {random.choice(outdoorObjects)} có hình dạng là {random.choice(shapes)} đang phát ra ánh sáng màu {random.choice(colors)}"

def generateOutdoorSkyObject():
    return f"Có {random.choice(quantities)} {random.choice(outDoorSkyObjects)} hình dạng là {random.choice(shapes)} đang phát quang màu {random.choice(colors)} giữa không trung"

def generateOutdoorScene():
    NPCstr = generateNPC().strip()
    location = random.choice(outdoorView).strip()
    outDoorStatusStr = random.choice(outDoorStatus).strip()
    weatherStr = random.choice(weatherConditions).strip()
    skyStrongObjStr = returnOutdoorSkyStrongObject().strip()
    skyObjStr = generateOutdoorSkyObject().strip()
    outdoorObjStr = generateOutdoorObject().strip()
    endingStr = random.choice(ending).strip()
    scene = (
        f"{''.join(random.choices(titleEmojis, k=4))} - Một khung cảnh {random.choice(starting).strip()} - {''.join(random.choices(titleEmojis, k=4))}:\n"
        f"{location} đã {outDoorStatusStr} lâu năm, "
        f"thời tiết thì đang {weatherStr}. "
        f"{skyStrongObjStr}. "
        f"{skyObjStr}. "
        f"{outdoorObjStr}. "
        f"{NPCstr}. "
        f"Cảm xúc của người đang quan sát có thể nói là {random.choice(status)} {''.join(random.choices(emojiStatus, k=3))}{''.join(random.choices(emotionPunctuations, k=4))}.\n"
        f"{random.choice(comment).strip()} {''.join(random.choices(cuteEmojis, k=3))}. {endingStr}{generateRandomIcons(7)}"
    )
    return scene

# tạo câu chuyện ngắn mẫu 1
def generateShortStory1():
    repeat_times = random.randint(100000, 1000000)
    years_duration = random.randint(10000, 100000)

    shop_location = random.choice(outdoorView).upper()
    outdoor_shope_status = random.choice(outDoorStatus)
    outdoor_density = random.choice(outdoorObjectDensity)
    outdoor_object = random.choice(outdoorObjects)

    indoor_material = random.choice(indoorMaterials)
    indoor_item = random.choice(indoorItems)
    indoor_item_status = random.choice(indoorItemStatus)
    indoor_light_verb = random.choice(indoorLightVerb)
    indoor_light_source = random.choice(indoorItemLightningSource)
    indoor_location = random.choice(indoorLocations)
    indoor_location_status = random.choice(indoorStatus)

    shopkeeper_appearance = random.choice(liveNPCApperances)
    shopkeeper_emotion = random.choice(liveNPCEmotions)

    customer_status = random.choice(liveNPCEmotions)
    proverb = random.choice(proverbs)

    scene = (
        f"Dựa trên một câu chuyện được lấy từ {random.choice(sourceInfo)}!!! {generateRandomIcons(10)}\n"
        f"Có một {random.choice(businesses)} bán {random.choice(indoorObjectItems)}, nó tọa lạc ngay {shop_location} và trông có vẻ đã {outdoor_shope_status} lâu năm.\n\n"
        f"Ở {outdoor_density} nhìn từ phía tiệm, {random.choice(quantities)} {outdoor_object} có hình dạng là {random.choice(shapes)} đang phát ra ánh sáng màu {random.choice(colors)}.\n"
        f"Bên trong tiệm, nó được xây bằng {indoor_material} và được sơn màu {random.choice(colors)}. "
        f"Ở đây, {random.choice(quantities)} {indoor_item} {indoor_item_status}, nó có hình dạng là {random.choice(shapes)}, và đang {indoor_light_verb} là {indoor_light_source} màu {random.choice(colors)} từ bên ngoài. "
        f"Xung quanh tiệm, có {random.choice(quantities)} {random.choice(indoorObjectItems)} có hình dạng là {random.choice(shapes)} và đang phát quang màu {random.choice(colors)}. \n\n"
        f"Chủ tiệm, nhìn trông giống một {random.choice(liveNPCs)}, tên thật là {random.choice(nameNPC)} và năm nay đã {random.randint(10000, 100000)} tuổi.\n"
        f"Chủ tiệm cũng từng là 1 {random.choice(NPCjobs).upper()} đã về hưu. Chủ tiệm thì đang {shopkeeper_appearance}, vừa nhìn thì trông có vẻ {shopkeeper_emotion}, và đang {random.choice(liveNPCActions)}.\n"
        f"Chủ tiệm dù nhìn bên ngoài là một chủ tiệm bình thường, nhưng có một năng lực đặc biệt là {random.choice(magicTypes)}. \n\n"
        f"Rồi 1 ngày nọ, có một vị khách ghé vào tiệm, tên là {random.choice(nameNPC)}, nghề nghiệp là {random.choice(NPCjobs).upper()} và đã có {random.randint(10000, 100000)} năm kinh nghiệm. Nhìn vị khách thì đang trông có vẻ {customer_status}.\n"
        f'Vị khách đó hỏi chủ tiệm: "Tôi đang bị dính phải một lời nguyền vì đã lỡ đắc tội với {random.choice(liveNPCs)}. '
        f'Lời nguyền đó khiến tôi bây giờ phải có ngoại hình là {random.choice(shapes)} , và khi trúng nguyền thì phải {random.choice(liveNPCActions)} mãi mãi."\n\n'
        f'Chủ tiệm hỏi: "Vậy cậu đã làm gì để bị dính phải lời nguyền đó? Đừng có nói với ta là cái trò thách thức đó nhá?".\n\n'
        f'Vị khách đáp: "Ơ sao ngài... lại biết ạ? Tôi sống năm nay đã {random.randint(10000, 100000)} tuổi mà tôi chưa bao giờ gặp cái trường hợp nào mà... nó như này cả!!! "\n\n'
        f'Chủ tiệm đáp: "Đó là vì ta đã từng gặp đâu đó khoảng {random.randint(100000000000, 1000000000000):,} người bị dính lời nguyền như cậu, và ta đã giúp {random.randint(100000000000, 1000000000000):,} người khác phá giải lời nguyền đó. Nhưng tôi chưa thấy ai nghiêm trọng như cậu cả."\n\n'
        f'Vị khách đáp: "Tôi đúng đã thách thức họ trong cuộc thi {random.choice(liveNPCActions)} xem ai làm tốt hơn và đã thua cuộc, và tôi đã phải dính lời nguyền này! Bây giờ, tôi cần phải làm gì? \n\n'
        f'Chủ tiệm đáp: "Tôi biết tên đó, hắn ta cũng đã từng nguyền tôi mà thất bại. Tên này có {random.randint(100000000000, 1000000000000):,} kẻ khác là đàn em dưới trướng , tên đó có chút quyền năng cái là tâm tà bất chính. '
        f'Lại còn trợ ác hại thiện! Mà cậu đã thử tự giải lời nguyền à? Trông cậu tôi thấy có vẻ {random.choice(liveNPCEmotions)}"\n\n'
        f'Vị khách hỏi: "Vậy ngài có cách nào giúp tôi phá giải lời nguyền này không? Tôi đúng là đã thử giải nguyền bằng cách {random.choice(liveNPCActions)} hơn {random.randint(100000000000, 1000000000000):,} lần nhưng đều thất bại! Xin hãy cứu giúp tôi với thưa ngài!!!"\n\n'
        f'Chủ tiệm đáp: "Cũng không có gì khó đâu! Cậu hãy đến một {indoor_location}, nơi đó cách ở đây {random.randint(100000000000, 1000000000000):,}km về phía {random.choice(gpsLocations)}. '
        f'Để nhận biết đã đến đúng nơi cần đến hay chưa, thì cậu phải để ý là địa điểm đó tọa lạc tại {random.choice(outdoorView).upper()}, nơi mà ở đó có {random.randint(100000000000, 1000000000000):,} {random.choice(outdoorObjects)} có hình dạng là {random.choice(shapes)} và chúng hay phát ra ánh sáng màu {random.choice(colors)}."\n\n'
        f"Chủ tiệm, rút ra một điếu thuốc dài {random.randint(100000000000, 1000000000000):,}m ra, rít 1 hơi dài , rồi ông ta {random.choice(liveNPCActions)} một lúc.\n"
        f"Ông ta tiếp tục nhìn vào vị khách bằng ánh mắt {random.choice(liveNPCEmotions)} và nói: còn nữa , ở đó có {random.randint(100000000000, 1000000000000):,} {random.choice(liveNPCs)} đang sinh sống. Hãy gặp 1 kẻ nào đó trong số họ, và dùng tên giả của tôi và cứ nói với họ rằng ông chủ tiệm {random.choice(nameNPC)} đã bảo đến đó để phá giải lời nguyền.\n"
        f"Rồi sau đó, họ sẽ dẫn cậu đến một nơi khác gần đó, nơi mà có một người bạn của tôi đang sống. Anh ta trông giống 1 {random.choice(liveNPCs)}, và danh tính thật là {random.choice(nameNPC)}, là {random.choice(NPCjobs).upper()} có {random.randint(100000000000, 1000000000000):,} năm kinh nghiệm. Cậu sẽ dễ nhận ra vì anh ta có ngoại hình là {random.choice(liveNPCApperances)} và thường {random.choice(liveNPCActions)}.\n"
        f"Anh ta tuy câm điếc bẩm sinh nhưng anh ta sẽ nói rõ ràng chi tiết với cậu cách để giải lời nguyền của cậu. Nhưng với điều kiện là cậu phải đưa cho anh ta {random.randint(100000000000, 1000000000000):,}$ hoặc {random.randint(100000000000, 1000000000000):,} {random.choice(indoorObjectItems)} để làm phí giao dịch .\n"
        f"Anh ta ngoài ra còn bị cụt tứ chi, nên anh ta sẽ đi bộ cùng cậu để dẫn cậu đến 1 con đường mòn, sau đó cậu sẽ đi con đường đó thẳng một đoạn {random.randint(100000000000, 1000000000000):,}km nữa là sẽ đến đích. "
        f"Tôi nghĩ đây là một hành trình khá ngắn vì chỉ mất {random.randint(100000000000, 1000000000000):,} giờ đi xe taxi từ đây đến nơi mà địa điểm đó tọa lạc. "
        f"Tôi nghĩ cậu nên tranh thủ vì thời gian không còn nhiều nữa, vì cậu chỉ đang còn {formatNumber(1/random.randint(100000000000, 1000000000000) , 2)} giây để phá giải lời nguyền của cậu.\n"
        f"Và tôi nghe nói nơi cậu cần đến được xây bằng {random.choice(indoorMaterials)}, tường thì được sơn màu {random.choice(colors)} và nó thì đã {indoor_location_status} lâu năm rồi. Ngay khi vừa đến đó, cậu hãy lặp lại {repeat_times} lần việc {random.choice(liveNPCActions)} trong {years_duration} năm. "
        f'Nếu làm theo tất cả lời tôi dặn, lời nguyền của cậu sẽ được phá giải hoàn toàn."\n\n'
        f'Vị khách thắc mắc: "Nhưng tôi thực sự không hiểu, tại sao lại phải làm như vậy?".\n\n'
        f'Chủ tiệm chỉ im lặng, rồi sau đó chỉ đáp lại: "{random.choice(slogan)}".\n\n'
        f'Sau đó, vị khách cứ lúng túng mãi thì được chủ tiệm trao cho một tờ giấy có ghi nội dung là "{proverb}".\n'
        f"Vị khách như đã hiểu ra điều gì đó mà chủ tiệm truyền đạt, và ngay lập tức làm theo lời chủ tiệm nói. "
        f"Từ sau khi thực hiện xong lời chủ tiệm dặn dò, vị khách đó đã giải được hoàn toàn lời nguyền. Trông vị khách sau đó có vẻ rất {random.choice(liveNPCEmotions)}\n\n"
        f"Còn bạn? Nếu bạn thực sự hiểu được điều gì đó từ câu chuyện ngắn này, thì tôi không thể không chúc mừng bạn!!!! {generateRandomIcons(7)}"
    )
    return scene

# short story 2
def generateShortStory2():
    scene = (
        f"Một ngày {random.choice(weatherConditions)} tại {random.choice(companies)} Company!!! {generateRandomIcons(10)}\n\n"
        f"Nơi này đang diễn ra một buổi phỏng vấn ứng viên đặc biệt - Cuộc phỏng vấn không giới hạn , diễn ra tại sảnh chờ {random.randint(100000000000, 1000000000000):,}km2 của công ty.\n\n"
        f"Đang có tổng cộng {random.randint(100000000000, 1000000000000):,} ứng viên, họ đều là {random.choice(liveNPCs)} {random.choice(liveNPCApperances)}, nhìn bọn họ trông có vẻ {random.choice(liveNPCEmotions)}, và đang {random.choice(liveNPCActions)} trong lúc chờ đến lượt phỏng vấn của mình\n\n"
        f"Một lúc sau, có {random.randint(100000000000, 1000000000000):,} {random.choice(liveNPCs)} , họ là đại diện phòng nhân sự của công ty xuất hiện để tiến hành buổi phỏng vấn đặc biệt này.\n\n"
        f"CEO của công ty là 1 {random.choice(liveNPCs)}, tên thật là {random.choice(nameNPC)}, là người sáng lập công ty. Ông ta vừa đứng trên bục, vừa {random.choice(liveNPCActions)} và vừa phát biểu :\n"
        f" - Chào mừng mọi người đến với buổi phỏng vấn đặc biệt tại đây! Buổi phỏng vấn này đặc biệt ở chỗ 'Đây là buổi phỏng vấn nhân sự đầu tiên. Cái mà bạn có thể nhận mọi công việc bạn muốn làm nhất, deal mọi mức lương mà bạn muốn nhất!!!'\n\n"
        f"Sau đó , CEO lấy ly rượu {random.randint(100000000000, 1000000000000):,} lít ra và uống hết sạch trong {formatNumber(1/random.randint(100000000000, 1000000000000) , 2)} nano giây, rồi ông ta đã ợ {random.randint(100000000000, 1000000000000):,} hơi liên tục, rồi tiếp tục nói : \n"
        f" - Cuộc phỏng vấn này sẽ không có thi cử, không xét duyệt điều kiện. Chỉ cần với duy nhất điều kiện là bạn phải thành thật, và đó là điều kiện duy nhất bạn buộc phải làm.\n\n"
        f"Cuộc phỏng vấn sau đó được tiến hành theo như kế hoạch. Đâu đó ở trong các cuộc phỏng vấn, có một cuộc phỏng vấn đang được diễn ra khá suôn sẻ giữa ứng viên và HR. \n"
        f" - Chào anh , tôi là {random.choice(nameNPC)}, {random.randint(100000000000, 1000000000000):,} tuổi. Tôi đại diện cho phòng HR của công ty và tôi sẽ là người thực hiện việc phỏng vấn anh ở đây. Rất vui được gặp anh!! \n\n"
        f" - Vâng , tôi là {random.choice(nameNPC)}, {random.randint(100000000000, 1000000000000):,} tuổi. Tôi cũng rất vui khi được gặp cô ở đây, à mà... cô có bạn trai chưa? "
        f"...Tôi chỉ là muốn mời cô đi {random.choice(liveNPCActions)} cùng tôi tại 1 {random.choice(indoorLocations)} sau cuộc phỏng vấn này, tôi nghe bảo nơi đó đã {random.choice(indoorStatus)} lâu năm!!! \n\n"
        f"HR hơi đỏ mặt , ngượng ngùng rồi lí nhí đáp : \n\n"
        f" - Tôi... tôi đã từng trải qua {random.randint(100000000000, 1000000000000):,} mối tình cũ, mà chưa thấy ai vừa đẹp trai mà lãng mạn như anh đó!!!{''.join(random.choices(emojiStatus, k=3))} \n\n"
        f"Ứng viên ghé sát đôi môi vài tai HR và khẽ nói : \n\n"
        f" - Tôi thì... cũng đã từng hẹn hò với {random.randint(100000000000, 1000000000000):,} cô gái rồi... Cơ mà chưa thấy ai xinh đẹp như cô cả!!!{''.join(random.choices(emojiStatus, k=3))} \n\n"
        f"HR đỏ tím cả mặt , rồi dần chuyển sang {random.choice(colors)} và dịu nhẹ lại. Cô bỗng nghiêm giọng : \n\n"
        f" - À mà thôi... có gì thì nói sau nha! Bây giờ, ta tiến hành cuộc phỏng vấn nhé... Hmmm, trước mắt thì để tôi đọc qua hồ sơ cả anh. Tên tuổi anh đã giới thiệu rồi nên tôi sẽ không nhắc nữa! \n\n"
        f"Cô HR xăm soi một lúc, trông cô có vẻ {random.choice(liveNPCEmotions)} và {random.choice(status)}. Bỗng cô dừng lại :  \n\n"
        f" - Chà, anh cũng thật thú vị đó chứ. Anh từng là {random.choice(NPCjobs).upper()}, làm cho {random.choice(companies)} và đã có {random.randint(100000000000, 1000000000000):,} năm kinh nghiệm sao? Tại sao anh nghỉ việc bên đó vậy? \n\n"
        f"Ứng viên ngập ngừng đáp : Vâng, tôi đã từng làm việc bên đó. Và để trả lời cho câu hỏi của cô thì lí do tôi nghĩ là vì... bên này có cô HR xinh đẹp này làm tôi say đắm từ lâu =)))) "
        f"Tôi đùa đấy... thật ra thì tôi không còn hứng thú với công việc bên đó nữa nên tôi quyết định nghỉ việc và tạm thư giãn ở nhà {random.randint(100000000000, 1000000000000):,} năm. "
        f"Trước khi tôi đã nộp {random.randint(100000000000, 1000000000000):,} cái CV để có thể có được cơ hội vào vòng phỏng vấn ở công ty này!\n\n"
        f"Cô ứng viên 2 má tự dưng dần chuyển sang {random.choice(colors)} vì ngượng ngùng. Nhưng cô vẫn giữ được sự nghiêm túc và lại tiếp tục : \n\n"
        f" - Mồm miệng anh cũng ghê thật đó... Không biết tối nay ai đó có chịu đúng hẹn không mà bày đặt... À mà, lúc {random.randint(1, 18)} tuổi, anh đã từng hack thành công vào Ngân Hàng SIDA Liên Bang Quốc Tế để trộm đi {formatNumber(1/random.randint(100000000000, 1000000000000) , 2)}$ và {formatNumber(1/random.randint(100000000000, 1000000000000) , 2)} thỏi vàng sao? \n\n"
        f"Ứng viên thật thà đáp: - Phải, tôi cũng đã bị phán {random.randint(1000000000, 10000000000):,} năm tù ở 1 phiên tòa được diễn ra tại {random.choice(outdoorView)} và phải khổ sai bằng việc {random.choice(liveNPCActions)} liên tục {random.randint(100000000000, 1000000000000):,} lần. Và do tôi thực hiện cải tạo tốt nên được mãn hạn sớm. \n\n"
        f"Cô ứng viên mỉm cười : - Anh cũng thật thà phết nhỉ? Tôi thích anh rồi đó! ...Bây giờ, vào việc quan trọng chính nhé. Về việc thực hiện chủ trương của CEO trong buổi phỏng vấn này, anh hãy nói vị trí mà anh đang muốn vào nhất, công việc anh muốn làm nhất và mức lương anh muốn nhất? Hãy thành thật nha! \n\n"
        f"Ứng viên dõng dạc: - Được rồi, tôi sẽ thành thật và không giấu diếm gì cả! Yêu cầu của tôi khá là khắt khe nha. Tôi muốn vào vị trí {random.choice(NPCjobs).upper()} , công việc tôi muốn làm là {random.choice(liveNPCActions)}. Mức lương tôi muốn nhất là {formatNumber(1/random.randint(100000000000, 1000000000000) , 2)}$ , cô thấy sao? Yêu cầu này có quá cao không? \n\n"
        f"Cô ứng viên nhẹ nhàng : - Cá nhân tôi thì thấy anh cũng xứng đáng với điều đó chứ không thực sự quá cao. Được rồi, tôi bây giờ sẽ phải đi họp lại với ban nhân sự trước khi ra quyết định! Anh vui lòng chờ trong {random.randint(1000000000, 10000000000):,} phút nhá, tôi sẽ quay lại và cho anh biết kết quả sớm nhất!\n\n"
        f"Lúc cô HR rời đi, anh ứng viên đã lấy ra điếu thuốc dài {random.randint(100000000000, 1000000000000):,}m ra đốt và rít 1 hơi dài để giải tỏa áp lực. Xung quanh anh, các ứng viên khác đang {random.choice(liveNPCActions)} trong giờ giải lao giữa buổi phỏng vấn.\n\n"
        f"Sau khi họp xong, các đại diện nhân sự quay lại với ứng viên của mình để thông báo kết quả. Cô ứng viên kia cũng quay lại với anh HR của mình. \n\n"
        f"Cô HR mỉm cười và nói với anh ứng viên: - Xin được chúc mừng anh! kết quả thành công ngoài mong đợi, bên phía nhân sự của công ty đều bỏ {random.randint(100000000000, 1000000000000):,} phiếu để tuyển anh vào!! "
        f"Chưa kể là nếu anh làm việc đủ {random.randint(100000000000, 1000000000000):,} năm nữa thì lương của anh sẽ tăng thêm {formatNumber(1/random.randint(100000000000, 1000000000000) , 2)}% mức lương hiện tại anh yêu cầu! Ngày mai anh có thể bắt đầu đi làm rồi!\n\n"
        f"Anh ứng viên vui mừng : - Vậy thì quá tốt rồi! Vậy là...tôi sẽ được gặp cô mỗi này...nhỉ? À mà, còn lời mời của tôi trước đó thì...cô đồng ý chứ? \n\n"
        f"Cô ứng viên im lặng, chỉ mỉm cười. Và rồi cô vấp té cắm đầu vì không để ý và nhào lộn {random.randint(100000000000, 1000000000000):,} vòng rồi đứng dậy , sau đó bỏ đi. Nhưng cô cố tình làm rơi mảnh giấy nhỏ gần chân anh ứng viên. \n\n"
        f"Anh ứng viên cũng không nói gì thêm nữa, nhưng tò mò mở mảnh giấy đó ra đọc. Bên trong ghi :`Tối nay tôi tan làm lúc {random.randint(17, 24)}giờ, anh hãy đến công ty đón tôi. Ngoài ra, tôi cũng muốn tăng 2 cho cuộc hẹn của chúng ta là {random.choice(liveNPCActions)} ở {random.choice(indoorLocations)}. Số điện thoại của tôi kèm ở dưới nha! Còn nữa, tôi làm ở văn phòng nhân sự tại tầng {random.randint(100000000000, 1000000000000):,} tòa nhà {random.choice(buildings)} của công ty. "
        f"Tạm thời thì thang máy ở đó đang bảo trì {random.randint(100000000000, 1000000000000):,} năm nên anh chịu khó đi thang bộ nhé 😉!! Vào Buổi trưa thì tôi hay ăn trưa tại 1 quán quen cách ở đây {random.randint(100000000000, 1000000000000):,}km 😉` \n\n"
        f"Anh ứng viên vui vẻ cười lớn, sau đó thì bỏ mảnh giấy vào túi áo và ra về! Hôm đó , tâm trạng anh trông rất {random.choice(liveNPCEmotions)}. \n"
        f"Còn bạn? Bạn có đoán được mối quan hệ giữa 2 nhân vật này sẽ tiến triển như thế nào? {generateRandomIcons(7)}"
    )

    return scene

# generateShortStory3
def generateShortStory3():
    scene = (
        f"Một đêm thư giãn sau giờ làm việc, thời tiết thì {random.choice(weatherConditions)}. "
        f"Bầu trời đang {random.choice(status)}, có {random.choice(outDoorSkyStrongObjects)} có hình dạng là {random.choice(shapes)} và bị {random.choice(outDoorSkyStrongObjectStatus)} đang phát ra ánh sáng màu {random.choice(colors)}. {generateRandomIcons(10)}\n\n"
        f"Ở đâu đó, có {random.randint(100000000000, 1000000000000):,} cặp đôi đang thực hiện kết hoạch thực hiện lời hẹn ước từ lúc sáng, cái lúc mà họ hẹn trước khi ở sảnh công ty với tư cách là HR và ứng viên xin việc.\n\n"
        f"Ở ngay trước công ty {random.choice(companies)} tọa lạc tại {random.choice(outdoorView).upper()} đã {random.choice(outDoorStatus)} lâu năm. "
        f"Ngay tại {random.choice(outdoorObjectDensity)} của công ty, có {random.randint(100000000000, 1000000000000):,} {random.choice(outdoorObjects)} đều có hình dạng là {random.choice(shapes)} đang phát ra ánh sáng màu {random.choice(colors)} khiến cho nơi này lung linh hơn bao giờ hết.\n\n"
        f"Đâu đó tại tòa nhà {random.choice(buildings)} của công ty, có anh chàng {random.choice(liveNPCs)} , tên thật của anh là {random.choice(nameNPC)}. Đang {random.choice(liveNPCEmotions)} và đợi cô gái {random.choice(liveNPCs)} của mình tan ca khi cô đang làm việc ở phòng HR tại tầng  {random.randint(100000000000, 1000000000000):,}, và tên thật của cô là {random.choice(nameNPC)}. "
        f"Hôm nay anh có lẽ hơi nóng vội hơn mọi ngày, nên anh đã đến sớm hơn {random.randint(100000000000, 1000000000000):,} phút so với lịch đã hẹn trước với cô gái. "
        f"Vì anh đến hơi sớm, và cô gái kia thì vẫn đang còn trong ca nên anh hơi đói bụng. Anh đang thầm nghĩ, nên mua {random.randint(100000000000, 1000000000000):,} cái bánh mì để ăn nhẹ trước.\n\n"
        f"Có một quán quen của anh cách đó {random.randint(100000000000, 1000000000000):,}km. Nghĩ cũng gần đây thôi, chưa kể vẫn còn cách thời gian đã hẹn là {formatNumber(1/random.randint(100000000000, 1000000000000),2)} ns nữa, thời gian trông khá thoải mái. "
        f"Không nghĩ thêm vì bụng anh kêu ọc ọc rồi, anh lập tức phóng xe với tốc độ {formatNumber(1/random.randint(100000000000, 1000000000000),2)}nm/h đi mua vội bánh mì trước khi anh hết hứng hẹn hò vì đói. \n\n"
        f"Dọc đường, anh phải băng qua 1 ngã tư , và anh phải dừng đèn đỏ là {random.randint(100000000000, 1000000000000):,}s. "
        f"Lúc đợi cái cột đèn giao thông có hình là {random.choice(shapes)}, và đang từ đỏ sang {random.choice(colors)} rồi sang {random.choice(colors)} rồi sang {random.choice(colors)} rồi sang {random.choice(colors)} rồi sang {random.choice(colors)} rồi sang {random.choice(colors)} rồi mới xanh để anh được đi tiếp, thì anh nhìn ngắm cảnh vật xung quanh một chút, tâm trạng anh đang rất {random.choice(status)}.\n\n"
        f"Rồi bỗng anh thấy có {random.randint(100000000000, 1000000000000):,} cặp đôi {random.choice(liveNPCs)}-{random.choice(liveNPCs)} đang vừa {random.choice(liveNPCActions)} và vừa {random.choice(liveNPCActions)} bên đường. Sau đó, bọn họ nắm tay nhau băng qua vạch kẻ đường trông rất tình cảm. "
        f"Anh dõi nhìn theo bọn họ, sau đó {random.choice(liveNPCActions)} một lúc rồi quay lại xe của mình và cười thầm trong lòng - 'Phải chi cuộc hẹn hôm nay của mình cũng được như thế!' \n\n"
        f"Một lúc sau, anh đã quay lại công ty nơi bạn gái anh vẫn còn đang làm việc và kèm túi bánh mì nhỏ. Anh mừng trong lòng là vẫn còn kịp, chứ nếu không, anh sẽ bị block thẳng tay trên {random.choice(sourceInfo)} trước khi kịp giải thích là do anh mãi ngắm các cặp đôi hẹn hò ở ngã tư kia. "
        f"Anh nhanh chóng bỏ hết số bánh mì vừa mua được vào bụng trong chưa đến {formatNumber(1/random.randint(100000000000, 1000000000000),2)}ns. Và ngay khi anh vừa lau miệng xong thì cô bạn gái đã xuất hiện và đứng cách anh rất gần - {random.randint(100000000000, 1000000000000):,}m. \n\n"
        f"Anh có thể nhìn thấy rõ cô nàng xinh đẹp đó với diện mạo {random.choice(liveNPCApperances)} và dù có hơi rũ rượi do tăng ca. Anh vẫy tay để ra hiệu cho cô thấy, và rồi cô cũng nhìn thấy diện mạo {random.choice(liveNPCApperances)} của anh - trông rất đẹp trai. "
        f"Cô lập tức chạy thật nhanh {random.randint(100000000000, 1000000000000):,}km/s đến với anh để anh không phải đợi lâu thêm nữa.\n\n"
        f"- Chà, anh chàng đẹp trai? Đợi ta có lâu không chàng? Xin lỗi vì hôm nay nhiều việc nên em tăng ca quá, để xíu bé bù cho anh nha!{''.join(random.choices(emojiStatus, k=3))}\n\n"
        f"- Hổng sao đâu, anh chàng đẹp trai của em vừa đủ thời gian ăn bánh mì với ngắm người ta yêu nhau ở ngã tư đó nha! {''.join(random.choices(emojiStatus, k=3))}\n\n"
        f"- Mà bây giờ anh muốn đi đâu trước nhỉ? Em đi theo anh đó, muốn đưa em đi đâu thì cứ tự nhiên nhe.\n\n"
        f"- HMMM, anh vừa tìm ra chỗ này cũng hay. Anh lướt trên {random.choice(sourceInfo)}, thì thấy ở {random.choice(indoorLocations)} cách ở đây {random.randint(100000000000, 1000000000000):,}km về phía {random.choice(gpsLocations)}. "
        f"Có 1 ông chủ {random.choice(businesses)} tên là {random.choice(nameNPC)} bán {random.choice(indoorObjectItems)} cũng được {random.randint(100000000000, 1000000000000):,} năm rồi. Nghe đồn là ông ấy có năng lực {random.choice(magicTypes)}. Ông ta có thể bói toán được {random.randint(100000000000, 1000000000000):,} tiền kiếp đó. Em muốn thử không?\n\n"
        f"- Được thui nè, được ở bên anh thì đi đâu cũng được hết!\n\n"
        f"Một lúc sau, cặp đôi này đã có mặt tại địa điểm cần đến. Bước vào tiệm, một ông chú trung niên có diện mạo {random.choice(liveNPCApperances)}, đang {random.choice(liveNPCActions)}. "
        f"Lúc 2 người họ hỏi là có thể bói gì đó không thì ông chủ tiệm lấy một tẩu thuốc bằng {random.choice(indoorMaterials)} {random.randint(100000000000, 1000000000000):,}km ra rít một hơi dài. Sau đó ông ta đưa ra cho cặp 1 cái hộp thăm được làm bằng {random.choice(indoorMaterials)} gồm {random.randint(100000000000, 1000000000000):,} lá thăm.\n\n"
        f"- Mỗi người 1 lá thăm, mỗi lá sẽ có 1 câu. Nam trước, nữ sau. Nam tả nữ hữu. Cứ thế mà làm, rồi tôi sẽ cho 2 người biết kết quả.\n\n"
        f"Anh và cô khá hồi hộp. Và rồi, anh nhường cô bốc trước một lá thăm, sau đó đến lượt anh bốc 1 lá phần của mình. Sau một lúc, như lời ông chủ dặn, anh đọc trước: \n\n"
        f"- {random.choice(proverbs)}!.\n\n"
        f"- {random.choice(proverbs)}! - Rồi cô gái tiếp tục phần của mình. \n\n"
        f"Ông chủ im lặng một lúc, rồi {random.choice(liveNPCActions)} và {random.choice(liveNPCActions)} rồi lại {random.choice(liveNPCActions)}. Sau đó, ông đăm chiêu một lúc rồi phán: \n\n"
        f"- Mối lương duyên giữa 2 người không hề tầm thường đâu! 2 người đã có tiền duyên với nhau cũng {random.randint(100000000000, 1000000000000):,} kiếp rồi đó. "
        f"Kiếp trước, vì 2 người hiểu lầm nhau, nguyên nhân là chàng trai đã {random.choice(liveNPCActions)} {random.randint(100000000000, 1000000000000):,} lần trước mặt cô gái khiến cô trầm cảm mà tự vẫn. Chàng trai vì nhớ thương người mình yêu nên đã đi theo cô sau đó không lâu! "
        f"Kiếp này, vì 2 người vẫn còn mối nợ kiếp trước chưa trả hết. Nên kiếp này sẽ tiếp tục bên nhau thôi! Cơ mà, ta muốn nói trước 2 người biết, sẽ có họa kiếp đó. Này cậu trai trẻ? Cậu từng phạm phải tội gì phải không?\n\n"
        f"- Ơ sao ông lại,.... ??? Phải, tôi từng hack thành công vào Ngân Hàng SIDA Liên Bang Quốc Tế để trộm đi {formatNumber(1/random.randint(100000000000, 1000000000000),2)}$ và {formatNumber(1/random.randint(100000000000, 1000000000000),2)} thỏi vàng lúc tôi chỉ mới {random.randint(1, 18)} tuổi! "
        f"Và tôi cũng đã bị phán {random.randint(1000000000, 10000000000):,} năm tù ở 1 phiên tòa được diễn ra tại {random.choice(outdoorView).upper()} và phải khổ sai bằng việc {random.choice(liveNPCActions)} liên tục {random.randint(100000000000, 1000000000000):,} lần.\n\n"
        f"- Vì ta biết đó do nghiệp báo kiếp trước. Cơ mà quan trọng là chính cô gái trong tương lai cũng sẽ gặp tai họa tương tự, 2 người bây giờ chỉ cần làm theo tờ giấy {random.choice(colors)} này ghi, thì lập tức họa kiếp tiêu trừ. Vạn sự bình an!\n\n"
        f"Cặp đôi ra về và với tâm trạng hơi {random.choice(liveNPCEmotions)}. Một lúc sau, họ đi dạo ở gần đó, và lúc không có ai, họ lấy tờ giấy ông chủ đó đưa cho họ ra xem. Họ như hiểu ra điều gì đó và họ nhìn nhau như ngầm hiểu - 'Ohhh, thì ra là thế!'\n\n"
        f"Chàng trai nhìn sâu vào ánh mắt cô gái : - Em có hiểu không?\n\n"
        f"Cô gái đưa tay xoa mặt chàng trai : - Em hiểu rồi!!\n\n"
        f"Vậy là họ làm theo lời tờ giấy đó ghi - {random.choice(slogan)}. Và càng về sau, đúng như lời tiên tri của chủ tiệm bí ẩn, mọi việc đều rất suôn sẻ!\n\n"
        f"Vậy còn bạn? bạn thực sự đã hiểu ra gì chưa? {generateRandomIcons(7)} \n\n"
    )
    return scene

# generateShortStory4
def generateShortStory4():
    mainName = random.choice(nameNPC).upper()
    mainAction = random.choice(liveNPCActions)
    mainOfen = random.randint(100000000000, 1000000000000)
    scene = (
        f"Tọa lạc tại {random.choice(outdoorView).upper()}, thời tiết thì {random.choice(weatherConditions)}. Bầu trời đang trông có vẻ {random.choice(status)}, "
        f"có {random.choice(outDoorSkyStrongObjects)} có hình dạng là {random.choice(shapes)} và bị {random.choice(outDoorSkyStrongObjectStatus)} đang phát ra ánh sáng màu {random.choice(colors)}. "
        f"Đây quả thật là một khung cảnh {random.choice(status)}. {generateRandomIcons(10)}\n\n"
        f"Có một {random.choice(indoorLocations)} {random.choice(indoorStatus)} lâu năm, được xây dựng bằng {random.choice(indoorMaterials)} và được sơn màu {random.choice(colors)}. "
        f"Ở đây đang có {random.randint(100000000000, 1000000000000):,} cặp đôi {random.choice(liveNPCs)}-{random.choice(liveNPCs)} đang hẹn hò. Họ đang {random.choice(liveNPCActions)} và trông rất {random.choice(liveNPCEmotions)}.\n\n"
        f"Và ngay tại đó cũng có một cặp đôi đặc biệt {random.choice(liveNPCs)}-{random.choice(liveNPCs)} đang hẹn hò. Chàng trai tên thật là {mainName}, {random.randint(100000000000, 1000000000000):,} tuổi. "
        f"Còn bạn nữ thì tên là {random.choice(nameNPC).upper()}, {random.randint(100000000000, 1000000000000):,} tuổi.\n\n"
        f"Cặp đôi đặc biệt đang trò chuyện với nhau trông rất {random.choice(liveNPCEmotions)}.\n\n"
        f"- Anh không thể ngờ là chúng ta có {random.randint(100000000000, 1000000000000):,} tiền kiếp ở bên nhau đó. Ông thầy bói đó quả nhiên là cao thủ {random.choice(magicTypes)}. {''.join(random.choices(emojiStatus, k=3))} \n\n"
        f"- Em cũng thế, em không ngờ là sáng nay em mới gặp anh với tư cách là HR và ứng viên ở {random.choice(companies)}, mà bây giờ thì chúng ta... hihi ngại nói ghê. {''.join(random.choices(emojiStatus, k=3))} \n\n"
        f"- Cơ mà, về quá khứ của anh... Em đã biết rồi đó, em vẫn đồng ý hẹn hò với anh? Em không hề e ngại hay suy nghĩ lại sao?\n\n"
        f"- Không đâu, lúc đó anh còn quá trẻ, ai mà chả từng có sai lầm. Anh đừng lo, em không quan tâm anh đã làm những gì. Em chỉ quan tâm anh bây giờ là anh thôi! \n\n"
        f"- Qủa thật thời gian đó anh quá ham vui và thiếu suy nghĩ chính chắn. Cơ mà, thật may mắn vì em không hề trách anh hay e ngại và rời bỏ anh. "
        f"Thật ra, {random.randint(100000000000, 1000000000000):,} cô gái anh đã từng hẹn hò, sau khi họ biết về quá khứ anh từng phạm pháp, họ đều bỏ đi! Cho đến khi gặp em, em là người đầu tiên chịu ở lại.\n\n"
        f"- Ohhh, thì ra là thế. Cơ mà, em đang thấy anh rất tốt ở hiện tại, dù anh đã có hẹn hò {random.randint(100000000000, 1000000000000):,} hay {random.randint(100000000000, 1000000000000):,} cô gái khác đi nữa."
        f" Em vẫn tin là anh rất chung tình. Chỉ là họ vì e ngại quá khứ của anh, họ đã không hiểu anh, họ không chịu thông cảm cho anh! Cơ mà em thì khác, em không quan tâm gì cả, chỉ cần anh là phiên bản tốt nhất của chính mình là đủ rồi!"
        f" Cơ mà anh phải kể cho em nghe cái chuyện anh từng phạm phải đó! Em khá tò mò lắm nha... haha. \n\n"
        f"- Được rồi được rồi, anh sẽ kể chi tiết ngay đây, không giấu diếm. Lúc đó, anh chỉ mới {random.randint(1, 18)} tuổi thôi...\n\n"
        f"Chàng trai đang bắt đầu hồi tưởng...\n\n"
        f"Cách thời điểm hiện tại {random.randint(100000000000, 1000000000000):,} năm. Chàng trai ban đầu nãy ra ý tưởng hack và trộm đi một số tiền để test bảo mật Ngân Hàng SIDA Liên Bang Quốc Tế thuộc tập đoàn {random.choice(companies)} sau đó giúp họ cải tiến hệ thống và vá lổ hổng bảo mật. "
        f"Anh ấy đã rủ thêm {random.randint(100000000000, 1000000000000):,} {random.choice(liveNPCs)}, tất cả là đều đồng phạm chung trong vụ đó với anh. \n\n"
        f"Sau {random.randint(100000000000, 1000000000000):,} phút tính toán kế hoạch một cách nhanh chóng, họ bắt đầu thực hiện kế hoạch đó một cách bài bản. Trông tất cả bọn họ đều phối hợp ăn ý nhau và rất là {random.choice(liveNPCEmotions)}. \n\n"
        f"Họ quyết định chọn một chi nhánh ngân hàng gần đó cách {random.randint(100000000000, 1000000000000):,}km về hướng {random.choice(gpsLocations)}. "
        f"Cả bọn đều lên xe và phóng đi nhanh chóng với tốc độ là {formatNumber(1/random.randint(100000000000, 1000000000000),2)}nm/year đến đó.\n\n"
        f"Theo kế hoạch ban đầu, cả bọn sẽ chia làm 2 nhóm. Nhóm 1 sẽ vào sảnh chính của ngân hàng giả vờ thực hiện giao dịch như các khách hàng, sau đó họ sẽ {random.choice(liveNPCActions)} {random.randint(100000000000, 1000000000000):,} lần/ns để đánh lạc hướng bảo vệ và nhân viên là dàn dựng 1 vụ cướp có vũ trang giả ở sảnh. "
        f"Nhóm 2 bao gồm chàng trai chủ mưu sẽ đột nhật vào kho phòng máy chủ trung tâm của ngân hàng, họ buộc phải {random.choice(liveNPCActions)} {random.randint(100000000000, 1000000000000):,} lần/ns để qua mặt lớp bảo vệ của hệ thống ngân hàng.\n\n"
        f"Sau {random.randint(100000000000, 1000000000000):,}h thì nhóm 2 đã đột nhập vào kho tổng của ngân hàng thành công. Họ đã đánh ngất {random.randint(100000000000, 1000000000000):,} bảo vệ ở đó, và lúc đó thì các lực lượng bảo vệ lo mải mê {random.choice(liveNPCActions)} {random.randint(100000000000, 1000000000000):,} lần/ns và {random.choice(liveNPCActions)} {random.randint(100000000000, 1000000000000):,} lần/ns. "
        f"Nhanh chóng họ đã bỏ túi {formatNumber(1/random.randint(100000000000, 1000000000000),2)}$ và {formatNumber(1/random.randint(100000000000, 1000000000000),2)}nanogram vàng khối và rời đi bằng cửa sau.\n\n"
        f"Nhóm 1 sau khi được báo là là kế hoạch thành công và rút lui thông qua bộ đàm, bọn họ cũng bắt đầu {random.choice(liveNPCActions)} {random.randint(100000000000, 1000000000000):,} lần, "
        f"rồi tiếp tục {random.choice(liveNPCActions)} {random.randint(100000000000, 1000000000000):,} lần nữa để câu giờ cho nhóm 2 trước khi cả nhóm 1 cũng rời khỏi hiện trường.\n\n"
        f"Sau một lúc, ngân hàng mới phát hiện ra đã mất đi một số khoản tiền. Họ lập tức ấn chuông báo động. "
        f"Cảnh sát địa phương đã điều động 1 lực lượng đặc nhiệm gồm {random.randint(100000000000, 1000000000000):,} người, cùng với đó là {random.randint(100000000000, 1000000000000):,} xe tăng và {random.randint(100000000000, 1000000000000):,} chó nghiệp vụ. "
        f"Cả cảnh sát trưởng của địa phương {random.choice(nameNPC).upper()}, {random.randint(100000000000, 1000000000000):,} tuổi và cùng {random.randint(1, 18)} điều tra viên khác cũng có mặt tại hiện trường vụ án ngay sau đó.\n\n"
        f"- Ai mà dám liều mạng vậy chứ? Đây quả thật là 1 vụ cướp táo tợn mà! Tôi thề phải bắt được hết tất cả bọn này! - Cảnh sát trưởng đang tức tối.\n\n"
        f"Một điều tra viên có tên là {random.choice(nameNPC).upper()}, {random.randint(100000000000, 1000000000000):,} tuổi, tính cách anh liêm khiết, ngay thẳng. Sau khi quan sát kĩ hiện trường, ngay lập tức, anh ta nhận ra vấn đề và thẳng thắn : \n\n"
        f"- Tôi không nghĩ bọn họ có ý đồ cướp ngân hàng đâu. Vì tôi thấy họ có thể dễ dàng che giấu khiến ngân hàng không thể phát hiện, "
        f"nhưng họ đã cố tình để lại {random.randint(100000000000, 1000000000000):,} {random.choice(indoorObjectItems)} có hình dạng là {random.choice(shapes)} và phát quang màu {random.choice(colors)} để làm dấu vết. "
        f"Nhờ đó, ngân hàng mới phát hiện ra dấu vết đã bị cướp. Điều này trái với các vụ cướp hay khủng bố ngân hàng thông thường mà tôi từng điều tra. \n\n"
        f"Anh điều tra viên tiếp tục nói : \n\n"
        f"- Theo kinh nghiệm điều tra của tôi, có thể là họ đang cố tình làm thế với mục đích là giúp ngân hàng cải tiến hệ thống bảo mật và họ sẽ nhận 1 số tiền thưởng.\n\n"
        f"Cảnh sát trưởng bỏ ngoài tai những lời anh điều tra viên đó nói, đập bàn và lập tức mắng anh ta: \n\n"
        f"- Cái kiểu điều tra của anh là gì mà lạ thế hả? Thế nào là cải tiến? Tôi bảo đây là cướp, không có mục đích gì khác. Nhớ kĩ lời tôi, CƯỚP LÀ CƯỚP, KHÔNG CÓ GÌ KHÁC!!!\n\n"
        f"Anh điều tra viên vốn trung trực, liêm chính từ nhỏ, liền phản biện: \n\n"
        f"- Thưa cảnh sát trưởng, nếu làm vậy là không minh bạch, tôi chỉ muốn đảm bảo công bằng với pháp luật. Thứ lỗi cho tôi nói thẳng, tôi biết ngài đang áp lực vì cấp trên đang hối thúc điều tra. "
        f"Nhưng chúng ta không thể làm oan sai và thiếu công bằng minh bạch được. Xin ngài hãy nghe lời khuyên của tôi!\n\n"
        f"Cảnh sát trưởng rõ là đang lơ anh điều tra viên đó đi, trông ông ta rất {random.choice(liveNPCEmotions)}. Ngay lập tức, ông ta được báo cáo là xác định được danh tính của thủ phạm và nhanh chóng ra lệnh truy nã toàn quốc.\n\n"
        f"Sau {random.randint(100000000000, 1000000000000):,} ngày, chàng trai cố tình đến ngân hàng vì nghĩ là họ đã phát hiện ra toàn bộ vụ việc và đến để nhận thưởng. "
        f"Tuy nhiên, ngân hàng đã chuẩn bị giăng lưới, phối hợp với cảnh sát {random.choice(liveNPCActions)} {random.randint(100000000000, 1000000000000):,} lần/ns để dụ anh ta sa lưới và bắt giữ. Ban đầu, ngân hàng vẫn giả vờ là mời anh ta vào để nhận thưởng.\n\n"
        f"Sau khi anh ta bước vào trong ngân hàng. Ngay lập tức, thủ phạm đã bị bắt giữ tại chỗ. Cảnh sát nhanh chóng đưa anh ta về trụ sở làm việc. Ngay lập tức, anh ta được đưa vào phòng điều tra. "
        f"Cảnh sát trưởng đến gặp trực tiếp anh ta để hỏi cung: \n\n"
        f"- Mày liều nhỉ? dám cướp ngân hàng sao? Mày có quyền biện hộ! Có gì muốn thì nói đi? Chỉ cần nộp cho tao {random.randint(100000000000, 1000000000000):,}$. Tao sẽ dàn xếp ổn thỏa cho mày tự do thoát tội? Thấy sao?\n\n"
        f"Thủ phạm im lặng 1 lúc không nói gì hết. Cảnh sát trưởng nghi ngờ, một cảnh sát viên chạy vào báo : \n\n"
        f"- Thưa cảnh sát trưởng, đây không phải thủ phạm, đây là kẻ giả mạo. Chúng ta bắt nhầm kẻ giả mạo rồi!\n\n"
        f"Cảnh sát trưởng quát : 'Cái gì???'. Ngay lập tức ông ta ra lệnh cho toàn bộ lực lượng truy bắt thủ phạm thật. Cảnh sát trưởng ngồi xuống, quát vào mặt tên giả mạo : \n\n"
        f"- Rốt cuộc là sao đây? khai thật đi. \n\n"
        f"- Dạ, có người thuê tôi giả dạng anh ta để vào ngân hàng lấy tiền thưởng về. Anh ta hứa sẽ chia cho tôi 20% của tổng tiền thưởng... nên là tôi mới làm.\n\n"
        f"Cảnh sát trưởng đập bàn thật to: - Thật là tức chết đi mà! \n\n"
        f"Ngày {random.randint(1, 18)} sau khi triển khai truy bắt triệt để, thủ phạm thật đã bị bắt. Lúc đó, anh ta đang có diện mạo là {random.choice(liveNPCApperances)} và lẩn trốn tại tại 1 {random.choice(indoorLocations)}...\n\n"
        f"Quay trở lại hiện tại, cô gái đang mỉm cười và vỗ vào vai anh ta an ủi và bảo: \n\n"
        f"- Tính ra anh đâu có thực sự phạm pháp, động cơ gây án ban đầu của anh là ý tốt. Cơ mà tại sao anh bị phán án nặng quá vậy? Còn tên cảnh sát trưởng? Hắn ta đúng là 1 kẻ tham lam!! Còn anh điều tra viên đặc biệt đó? Anh ta có giúp anh không? \n\n"
        f"- Tên cảnh sát trưởng đó, anh biết. Hắn ta là kẻ biến chất và tham tiền, không biết bao nhiêu nạn nhân đã bị hắn hại? Còn anh điều tra viên đó, là người anh thấy duy nhất là người tốt, anh ta thì đã giúp anh nhiều lắm đó. Anh rất biết ơn anh ta... \n\n"
        f"...Vào năm {random.randint(100000000000000, 1000000000000000):,}TCN, tọa lạc tại {random.choice(outdoorView).upper()}. Tòa án liên bang `SIDA VKL QUỐC TẾ` đang xét xử 1 vụ án cướp ngân hàng. "
        f"Tòa án có sự tham gia của {random.randint(100000000000, 1000000000000):,} luật sư bào chữa, {random.randint(100000000000, 1000000000000):,} thẩm phán,{random.randint(100000000000, 1000000000000):,} đại diện bên cơ quan công tố và điều tra. "
        f"Và cũng góp mặt tham dự tại đây {random.randint(100000000000, 1000000000000):,} đại diện của bên bị hại và {random.randint(100000000000, 1000000000000):,} nhân chứng khác.\n\n"
        f"Sau {random.randint(100000000000, 1000000000000):,} phút thẩm vấn, chủ tọa tòa án {random.choice(nameNPC).upper()}, vừa {random.choice(liveNPCActions)}. Trong khi đó các thẩm phán khác đang {random.choice(liveNPCActions)} để hỗ trợ thẩm phán chính. Sau {random.randint(100000000000, 1000000000000):,} giây bàn luận trao đổi gay gắt giữa các bên lên quan. Phán quyết đã được đưa ra : \n\n"
        f"- Bị cáo đã thực hiện hành vi chủ mưu cướp ngân hàng, đã cướp đi {random.randint(100000000000, 1000000000000):,}$ và {random.randint(100000000000, 1000000000000):,} thỏi vàng nguyên khối. Bị cáo có gì để nói không?\n\n"
        f"- Ngay cả con số liệu điều tra mà cả thẩm phán như ông và bên phía cảnh sát cũng làm giả để tăng án cho tôi sao? Ông tưởng tôi không biết bên đại diện của cái ngân hàng chết tiệt đó đã hối lộ {random.randint(100000000000, 1000000000000):,}$ cho ông và cả bên cảnh sát điều tra à? "
        f"Bây giờ, ngay cả việc có thể phản biện thì tôi chịu thua thật rồi. Ông bảo tôi còn cách nào mà đấu lại mấy người chứ? 'Hệ thống pháp luật đô la' của các người đúng là làm tôi mở mang tầm mắt đó!! =)))\n\n"
        f"Thẩm phán như chột dạ, tức giận quát: \n\n"
        f"- Đề nghị bị cáo tôn trọng tòa án, đây là nơi thực thi pháp luật. Chúng tôi đại diện pháp luật và công lý. Anh không được phép hỗn láo xàm ngôn!!\n\n"
        f"Anh ta nói: - Thắng làm vua, thua làm {random.choice(indoorObjectItems)}. Muốn phán gì thì cứ phán, trên đầu các ông có {random.randint(1000000000, 10000000000):,} thần linh đang đứng nhìn đó! =)))\n\n"
        f"Tòa án ra phán quyết cuối cùng: \n\n"
        f"- Sau khi căn cứ vào các điều luật tại bộ luật liên bang và căn cứ vào các tình tiết tăng nặng, giảm nhẹ. Tòa quyết định tuyên phạt bị cáo {mainName} {random.randint(1000000000, 10000000000):,} năm tù giam vì tội chủ mưu cướp ngân hàng. \n\n"
        f"Ngoài ra bị cáo còn phải thực hiện 1 trong các hình phạt, thuộc lao động công ích sau: \n\n"
        f"   a/ Lặp lại việc {random.choice(liveNPCActions)} trong {random.randint(100000000000, 1000000000000):,} năm.\n\n"
        f"   b/ Lặp lại việc {random.choice(liveNPCActions)} trong {random.randint(100000000000, 1000000000000):,} năm.\n\n"
        f"   c/ Lặp lại việc {mainAction} trong {mainOfen:,} năm.\n\n"
        f"Về việc chọn 1 hình phạt trong các mục này sẽ do cái thẩm phán và bên công tố lựa chọn.\n\n"
        f"Sau một lúc việc bỏ phiếu từ các bên liên quan, tòa phán quyết cuối cùng về hình phạt lao động công ích là mục lặp lại việc {mainAction} trong {mainOfen:,} năm. Bản án sẽ hiệu lực tính từ thời gian lúc phán quyết....\n\n"
        f" - Tên thẩm phán và bọn công tố đều biến chất như vậy à?? Thật khổ cho anh rồi, em thấy thương anh quá à! Còn người điều tra viên tốt bụng kia? Anh ta đã cứu anh sao? đã cứu như thế nào vậy? - Cô gái tò mò và tiếp tục tập trung lắng nghe chàng trai kể.\n\n"
        f" - Về điều tra viên đó thì như thế này, lúc đó anh đã thụ án cũng được mới có {random.randint(1000000000, 10000000000):,} ngày,....\n\n"
        f"Tại nhà tù `SIDA VKL QUỐC TẾ`, tọa lạc tại một {random.choice(outdoorView)}. Các phạm nhân cũng sinh hoạt bình thường như mọi ngày.\n\n"
        f" - Phạm nhân {mainName}, có người muốn gặp anh! - 1 cai ngục hằn giọng. \n\n"
        f"Chàng trai đi theo cai ngục đó, anh ta được dẫn đến gặp anh điều tra viên chính trực kia. Hai người bắt đầu trò chuyện.\n\n"
        f" - Chào anh, chúng ta lại gặp nhau rồi! - Điều tra viên thân thiện đưa tay ra trước mặt chàng trai. \n\n"
        f" - Vâng, chào anh. Chúng ta đã gặp nhau nhiều rồi. Và người duy nhất tôi rất nể trọng trong vụ án này là anh, anh là người duy nhất không bị biến chất và còn hiểu được động cơ ban đầu thực sự của {mainName} tôi đây nữa! Haha!\n\n"
        f" - Tôi cảm thấy như vậy là chưa thực sự giúp anh đâu! Tôi hôm nay đến thăm anh, 1 là để thay mặt toàn bộ hệ thống tư pháp để tạ lỗi với anh!\n\n"
        f" - Còn 2 là gì? Anh cứ nói đi, tôi đang nghe đây!\n\n"
        f" - Tôi không tiện nói ra ở đây! anh hãy cầm lấy tờ giấy nhỏ này, mở ra đọc sẽ hiểu thôi. - Điều tra viên lấy trong túi áo ra 1 tờ giấy nhỏ {random.randint(100000000000, 1000000000000):,} dòng đưa cho chàng trai. \n\n"
        f"Lúc về lại phòng giam, anh ta mở ra đọc ngay. Nội dung ghi là: 'Anh thực sự không có phạm phải tội lớn gì! Bây giờ nếu tôi không thể giúp anh giảm nhẹ hình phạt thì tôi lại không đành lòng nhìn anh chịu khổ vì những cái anh không làm. "
        f"Nên là tôi sẽ giúp anh ...vượt ngục, hãy chạy trốn đi thật xa và đừng ngẩng đầu lại. Bên dưới là bản đồ bí mật của nhà tù này, anh chỉ cần canh lúc 18h ngày mai. "
        f"Lúc đó, các cai ngục sẽ giải lao và đi {random.choice(liveNPCActions)} theo thói quen sinh hoạt thường thấy. Đây là thời điểm tốt nhất, hãy theo bản đồ này và thoát ra ngoài. "
        f"Sau khi thoát được ra ngoài, anh hãy đi thêm {random.randint(100000000000, 1000000000000):,}km về hướng {random.choice(gpsLocations)}. "
        f"Một người bạn của tôi tên là {random.choice(nameNPC).upper()}, đi chiếc xe màu {random.choice(colors)}. Anh ta sẽ giúp anh đưa anh đi trốn ra nước ngoài. Xin anh hãy giữ bí mật chuyện này! Và hãy cẩn thận và bảo trọng nhé!!' \n\n"
        f"Vậy là mọi kế hoạch đều suôn sẻ, chàng trai đã được đưa đi bỏ trốn thành công....\n\n"
        f" - Vậy lí do anh bảo anh được ân xá chứ không phải là anh đã vượt ngục là muốn bảo vệ anh điều tra viên ân nhân đó sao? - Cô gái tựa đầu vào vai chàng trai. \n\n"
        f" - Phải! Anh chả cần giấu gì với em cả, trước giờ động cơ của anh luôn chỉ là cải tiến bảo mật giúp ngân hàng! Cơ mà anh muốn bảo vệ ân nhân nên mới che giấu mỗi cái việc này! "
        f"Anh chỉ hận bọn ngân hàng chết tiệt đó lấy oán báo ân, còn hệ thống tư pháp thì tham nhũng. Nếu biết trước như thế, anh đã không làm vụ này làm gì để rước họa vào thân cả.\n\n"
        f" - Không sao cả, em tin anh mà, anh là người tốt.\n\n"
        f"Thời gian nhanh chóng trôi qua, cặp đôi đặc biệt đó nhanh chóng về nhà. Lúc chàng trai đưa cô gái về đến trước cổng nhà. Cô gái thơm má chàng trai 1 cái, rồi bảo: \n\n"
        f" - Bye anh yêu nha!!! Cơ mà anh nhớ mai chúng ta sẽ hẹn hò ở đâu không đó??? =)))\n\n"
        f" - Anh nhớ chứ, mai chúng ta sẽ đi {random.choice(liveNPCActions)} ở một {random.choice(indoorLocations)} gần đây? Anh nhớ đúng phải hông ta??\n\n"
        f" - Đúng rùi đó, mai nhớ đúng giờ nha!! Em muốn ở bên anh cựu `tội phạm lương thiện` lâu hơn nè!!~ =))\n\n"
        f"Cặp đôi nhanh chóng tạm biệt nhau, tình cảm họ lúc này đã tăng lên đáng kể. Còn bạn? Bạn cảm thấy quá khứ của chàng trai thế nào? Bạn sẽ làm gì khi bị phán quyết khổ sai bằng cách `Lặp lại việc {mainAction} trong {mainOfen:,} năm`? {generateRandomIcons(7)}"
    )
    return scene


#prompt for AI romantic
def generateLovelyPromt():
    locationIndoor = random.choice(indoorLocations).strip()
    locationOutdoor = random.choice(outdoorView).strip()   
    typeLocation = random.randint(1,2)
    endingStatus = f"Đây thật là 1 khung cảnh {random.choice(status)}!"
    if typeLocation == 1:
        scene = (
            f"Hai người này là cặp đôi yêu nhau rất sâu đậm. Tóc của chàng trai sidepart ngắn gọn, chàng trai rất đẹp trai và có đôi mắt 2 mí rất đẹp, áo của chàng trai đóng thùng gọn gàng ( giữ nguyên outfit 2 ảnh gốc). \n"
            f"Chàng trai đang {random.choice(BoyActions)} và cô gái đang {random.choice(GirlActions)}. \n"
            f"Bọn họ đang {random.choice(LoveActions)} ở khung cảnh là bên trong {locationIndoor} {random.choice(indoorStatus)} lâu năm. \n"
            f"Nó được xây bằng {random.choice(indoorMaterials)} và sơn màu {random.choice(colors)}. \n"
            f"{generateIndoorItems().strip()}. \n"
            f"Ở đây, {generateIndoorObject().strip()}. \n"
            f"{generateNPC().strip()}. \n"
            f"{endingStatus}"
        )
    else:
        scene = (
            f"Hai người này là cặp đôi yêu nhau rất sâu đậm. Tóc của chàng trai sidepart ngắn gọn, chàng trai rất đẹp trai và có đôi mắt 2 mí rất đẹp, áo của chàng trai đóng thùng gọn gàng ( giữ nguyên outfit 2 ảnh gốc). \n"
            f"Chàng trai đang {random.choice(BoyActions)} và cô gái đang {random.choice(GirlActions)}. \n"
            f"Bọn họ đang {random.choice(LoveActions)} ở khung cảnh {locationOutdoor} đã {random.choice(outDoorStatus).strip()} lâu năm. \n"
            f"Khung cảnh đang có thời tiết {random.choice(weatherConditions).strip()}. \n"
            f"{returnOutdoorSkyStrongObject().strip()}. \n"
            f"{generateOutdoorSkyObject().strip()}. \n"
            f"{generateNPC().strip()}. \n"
            f"{endingStatus}"
        )
    return scene

# anything
def ruleL4D2():
    scene = (
        f"Rule of this game (L4D2) : Người chơi làm theo mục tiêu, Zombie cố định luôn là tank , trong 1 khoảng thời gian và số bước di chuyển đc giới hạn :\n\n"
        f"Map : {random.choice(mapsL4D2)} - Campain của map sẽ được random ( trừ map cuối) \n"
        f"Character : {random.choice(charactersL4D2)}\n"
        f"Player HP : {random.randint(1, 100):,}\n"
        + (
            f"Weapon : {random.choice(weaponsL4D2)} - ammo : {random.randint(1, 500)}\n"
            if random.randint(0, 1) == 1
            else "Weapon : None\n"
        )
        + f"Melee: {random.choice(meleeL4D2)}\n"
        f"Grenade : {random.choice(grenadesL4D2)} - quantity : {random.randint(0, 5)}\n"
        f"Pickups : {random.choice(pickupsL4D2)} - quantity : {random.randint(0, 5)}\n"
        f"Medicine : {random.choice(medicineL4D2)} - quantity : {random.randint(0, 5)}\n"
        f"First Aid Kits  : {random.randint(0, 3)}\n"   
        f"Tank Health : {random.randint(1000000000, 100000000000):,}\n"
        f"Common Infected : {random.randint(1, 100):,} zombies\n"
        f"Time limit: {random.randint(2, 5)} minutes\n"
        f"Step limit: {random.randint(100, 500)} steps\n"
        f"Player Rules : {random.choice(playerRulesL4D2)} - time limit: {random.randint(10, 60)} seconds\n"
        f"Objective : {random.choice(['kill the tank', 'survive', 'escape'])}\n"
    )
    return scene

def dateAppOptions():
    scene = (
        f"Chào mừng đến với ứng dụng tài xỉu sổ xố hẹn hò `SIDA VKL QUỐC TẾ ${random.choice(companies)}`. \n\n"
        f"Reject Number of Profiles (số lượt phải quẹt trái): {random.randint(1,20):,} profiles\n"
        f"Like Number of Profiles (số lượt phải quẹt phải): {random.randint(1,20):,} profiles\n"
        f"Options: {random.choice(optionsDateApp)} \n"
    )
    return scene