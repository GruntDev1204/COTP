from data.dataNPC import *
from data.dataIndoor import *
from data.dataOutdoor import *
from data.dataStory import *
from data.dataLove import *
from data.dataL4D2 import *

ending = [
    "Cảnh vật ở đây trông rất bình thường và thơ mộng.",
    "Cảnh vật ở đây trông rất yên bình và dễ thương.",
    "Cảnh vật ở đây trông rất quen thuộc và khó quên.",
    "Cảnh vật ở đây trông rất dễ thương và quen thuộc.",
    "Cảnh vật ở đây trông rất hạnh phúc và dễ thương.",
    "Cảnh vật ở đây trông rất dễ thương và ngọt ngào.",
    "Cảnh vật ở đây trông rất hài hước và thường ngày.",
    "Cảnh vật ở đây trông rất vui vẻ và thường ngày.",
    "Cảnh vật ở đây trông rất ấn tượng và quen thuộc.",
    "Cảnh vật ở đây trông rất nhộn nhịp và quen thuộc.",
    "Cảnh vật ở đây trông rất bồi hồi và thường thấy.",
    "Cảnh vật ở đây trông rất mơ mộng và thường thấy.",
    "Cảnh vật ở đây trông rất thường thấy và bồi hồi.",
    "Cảnh vật ở đây trông rất xúc động và dễ mến.",
    "Cảnh vật ở đây trông rất bình yên và dễ thương.",
    "Cảnh vật ở đây trông rất thân quen nhưng lạ lẫm."
    "Cảnh vật ở đây trông rất hồn nhiên và kì lạ.",
    "Cảnh vật ở đây trông rất như đùa nhưng rất thật.",
    "Cảnh vật ở đây trông rất như 1 giấc mơ nhưng rất cuốn.",
    "Cảnh vật ở đây trông rất khó tả và rất cuốn.",
    "Cảnh vật ở đây trông rất khó tả và kì lạ.",
    "Cảnh vật ở đây trông rất dễ nhớ và bình thường.",
    "Cảnh vật ở đây trông rất dễ thương và bình dị.",
    "Cảnh vật ở đây trông rất tạm ổn và dễ thương.",
]

comment = [
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó khó gọi tên",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái ánh nhìn lạc vào cơn gió cũ",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái cảm giác như đã từng ở đây",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái cảm giác như rất bình dị ở đây",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó hơi khó quên",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó như giấc mơ",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó hơi mơ hồ",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó như mơ màng",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó như lạ lùng",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó hơi quen thuộc",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó hơi kì lạ",
]

starting = [
    "lãng mạn",
    "hơi kì cục",
    "mơ màng",
    "thơ mộng",
    "hồn nhiên",
    "kì lạ",
    "mộng mơ",
    "tuyệt vời",
    "dễ thương",
    "vui vẻ",
    "gần gũi",
    "thường ngày",
    "nhộn nhịp",
    "bình yên",
    "bình dị",
    "tạm ổn"
]

# Emojis
emojiMeme = [
    "🌚", "💀", "🫥", "🤯", "😣", "🥳", "😨", "🤢", "🤒", "🤕", 
    "🥹", "🫨", "🧐", "🤡", "🚨", "🛒", "🎉", "🥰", "😪", "🥱", 
    "🥺", "👻", "👌", "✌️", "🫶", "🤝", "🤟", "👀" , "💍" , "☃️" , "👍" , "🦾"
]

cuteEmojis = ["😫", "😵", "😀", "😵‍💫", "😁", "🫠", "😚", "🤣", "😝", "🥴" , "🤪"]
foodEmojis = [
    "🍕", "🍔", "🍟",  "🌭",  "🍿", "🍗", "🍣",  "🍦", "🍩", "🍰", "🍭"
]

emojiStatus = [
    "😇",  # Thiện lành
    "😈",  # Tinh quái
    "🤝",  # Bắt tay
    "🤔",  # Suy nghĩ
    "😬",  # Gượng gạo
    "🙃",  # Lộn ngược
    "😴",  # Ngủ gật
    "🤗",  # Ôm
    "😎",  # Ngầu
    "😢",  # Buồn nhẹ
    "😖",  # Cáu giận
    "😮",  # Ngạc nhiên
    "😆",  # Cười lớn
    "😭",  # Khóc to
    "😑",
    "🙄"
]

animalsEmojis = [
    "🐀",  # Tý - Chuột
    "🐂",  # Sửu - Trâu
    "🐅",  # Dần - Hổ
    "🐈",  # Mão - Mèo
    "🐉",  # Thìn - Rồng
    "🐍",  # Tỵ - Rắn
    "🐎",  # Ngọ - Ngựa
    "🐐",  # mời - Dê
    "🐒",  # Thân - Khỉ
    "🐓",  # Dậu - Gà
    "🐕",  # Tuất - Chó
    "🐖",  # Hợi - Heo
]

NPCEmojis = [
    "🤖",  # Robot kiểu default AI
    "👾",  # NPC bug
    "📺",  # NPC xem TV 24/7
    "✅",  # Checkmark thay ☑️
    "🐌",  # Nông dân (cây lúa)
    "💻",  # Dev dính bug
    "📢",  # NPC la hét glitch
    "🔧",  # Fix bug = búa
    "🧙",  # Pháp sư bán thuốc xổ
    "🧛",  # Hút máu người chơi AFK
    "🧞",  # Bị nhốt 500 năm
    "🧜",  # Trong hệ thống thoát nước
    "📚",  # NPC thuyết triết học
    "👮",  # Cảnh sát bắt gà
    "💡",  # Thám tử giấu mặt
]

titleEmojis = [
  "🌳", 
  "🌲", 
  "🌴", 
  "🌵",  
  "🌾", 
  "🌿", 
  "🍃", 
  "🍂", 
  "🍁", 
  "🌻",
  "🌼", 
  "🌸",
  "🌺", 
  "🌍", 
  "🌋", 
  "🌄", 
  "🌅", 
  "🌌", 
  "🌈", 
  "🌧",  
  "❄",  
  "🔥",  
  "💧",   
  "🎡",
  "🛝",
  "🎢",
  "📡",
  "🚨",
  "🪐",
  "🌥️",
  "🌤️",
  "🌠",
  "🌊", 
  "🎊",
  "🎉",
  "🎭"
]

entertainmentIcons = [
    "🎬",  
    "🎤", 
    "🎧", 
    "🎸", 
    "🎹", 
    "🎮",  
    "🎲",  
    "🎯", 
    "📺", 
    "🎰",
    "🎪", 
    "🎻",  
]
sportsIcons = [
    "⚽",  
    "🏀", 
    "🏈",  
    "⚾", 
    "🎾", 
    "🏐",
    "🏉",  
    "🥊", 
    "🎱", 
    "🏆", 
    "⛳", 
]

chaosEmojis = ['🧠', '🪅', '⌛', '🎈', '✨', '⚡', '🔥', '🫧', '🌀', '☠️', '🍵']

colors = [
    "đỏ", "cyan", "xanh lam", "vàng", "xanh lục", "hồng", "tím", "cam", "trắng",
    "bạc", "ngọc bích", "vàng kim", "bạch kim", "cam vàng", "neon", "xám bạc",
    "huyết nguyệt", "cam xanh", "hồng lục",

    # 🌟 MÀU SÁNG THÊM VÀO
    "trắng ngọc trai",            # hơi óng ánh mịn da
    "hồng pastel",                # dịu dịu mà sáng vcl
    "xanh mint",                  # màu kem bạc hà mát lạnh
    "vàng chanh",                 # chói sáng như đèn pin xe tải
    "xanh băng",                  # sáng như mắt robot băng giá
    "cam neon",                   # đập vô mặt
    "tím ánh kim",                # tím nhưng sáng như vàng
    "hồng đào sáng",              # màu mlem công chúa
    "trắng ánh kim",             # trắng + lấp lánh
    "xanh thiên thanh",          # màu trời xanh cực sáng
    "vàng ánh hồng",             # màu hoàng hôn rich kid
    "xanh điện",                 # bright điện giật 🟦⚡
    "tím pastel",                # ngọt như trà sữa
    "vàng pastel",               # dễ thương mà chói
    "xanh ánh bạc",              # ánh metal siêu nhiên
    "đỏ son",
    "nâu sáng",
    "xám sáng",
    "hồng cánh sen",
    "hồng đào",
    "trắng xanh",
    "vàng lục",
    "nâu đất",
    "xám khói",
    "đỏ gạch",
    "đỏ tươi",
    "xám tối màu"
]

quantities = ["vài", "các" , "một số", "nhiều",  "một vài" , "1" ,"3" , "lác đác vài" , "đôi ba" , "rải rác vài" , "một số ít" , "rải rác đều có" , "lác đác có vài" ,"rải đều có"]

shapes = [
    "hình cây",
    "hình cái khiên",
    "hình bookmark",
    "hình trái tim",
    "hình chìa khóa",
    "hình ngôi sao",
    "hình cây xương rồng",
    "hình bông tuyết",
    "hình cỏ 4 lá",
    "hình hoa hồng",
    "hình trái bóng rổ",
    "hình lục giác",
    "hình tam giác",
    "hình cái chuông",
    "hình viên kim cương",
    "hình con cua",
    "hình con cá",
    "hình giọt nước",
    "hình tròn",
    "hình vuông",
    "hình chóp đều",
    "hình kẹp giấy",
    "hình lá phong",
    "hình quả táo",
    "hình cái răng",
    "hình lá bồ đề",
    "hình elip",
    "hình kem ốc quế",
    "hình mặt cười",
    "hình viên kẹo",
    "hình bánh răng",
    "hình đồng hồ cát",
    "hình bánh donut",
    "hình máy bay giấy",
    "hình ổ khóa",
    "hình móng ngựa",
    "hình hạt đậu",
    "hình quả trứng",
    "biểu tượng vô cực",
    "hình ngọn lửa",
    "hình dấu cộng",
    "hình bát quái",
    "hình dấu chân",
    "hình cây thông",
    "hình bì thư",
    "hình xoắn ốc",
    "hình GPS",
    "hình hoa sen",
    "hình sóng wifi",
    "hình dấu tick",
    "hình cây son",
    "hình đồng xu",
    "hình đô la",
    "hình chữ S",
    "hình số 8"
]

emotionPunctuations = [
    "!",   # Cảm xúc mạnh, ngạc nhiên, vui vẻ
    "?",   # Bối rối, tò mò, hoang mang
    "@",   # Gợi liên kết, gọi tên, hoặc meme hóa
    "~",   # Mơ màng, lơ lửng, chill
    "*",   # Nhấn nhá, lấp lánh, đặc biệt
    "#",   # Meme, tag, hoặc cảm xúc mạng
    "$",   # Gợi giá trị, hoặc meme kiểu "giấc mơ đắt giá"
    "%",   # Rối loạn, hỗn hợp, chaos
    "^",   # Mơ màng, lơ lửng, chill
    "-.-!",
]

status = [
    "dễ thương",
    "hơi bối rối",
    "rất mơ",
    "trầm tư",
    "mơ hồ",
    "hào hứng",
    "quá thân thuộc",
    "hơi cô đơn",
    "quá chill",
    "hơi buồn",
    "rất suy tư",
    "quá sáng",
    "hơi ấm",
    "hơi bơ vơ",
    "rất deep",
    "rất lãng mạn",
    "quá dễ thương",
    "hơi xa",
    "rất gần",
    "quá êm",
    "hơi lạ",
    "rất dịu",
    "quá lạ",
    "hơi quen",
    "rất quen",
    "hơi mộng",
    "rất mộng",
    "rất bối rối",
    "quá mộng",
    "hơi thơ",
    "rất đáng nhớ",
    "quá thơ",
    "hơi lặng",
    "rất lặng",
    "quá lặng",
    "hơi vui",
    "rất vui",
    "quá vui",
    "khó nói",
    "rất ngẫu hứng",
    "rất khác lạ",
    "lo âu",
    "rất bình thường",
]

units = ["kg", "nm" , "km2" , "m3", "cm", "m", "mm", "dm", "hm", "cân", "tấn", "lít", "ml", "gallon", "feet", "inch", "yard", "mile" , "dBm" , "dB" , "kg/s" , "km/s" , "dBm/s" , "knot" , "km3/ns" , "kg/ns" ]

all_icons = sportsIcons + entertainmentIcons + cuteEmojis + foodEmojis + chaosEmojis + animalsEmojis + NPCEmojis + emojiMeme + titleEmojis + loveIcons
