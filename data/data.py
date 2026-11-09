from data.dataNPC import *
from data.dataIndoor import *
from data.dataOutdoor import *
from data.dataStory import *
from data.dataLove import *
from data.dataL4D2 import *
from data.dataIcon import *
from data.dataModelingPrompt import *

ending = [
    "Cảnh vật ở đây trông rất ấn tượng và quen thuộc.",
    "Cảnh vật ở đây trông rất bình thường và thơ mộng.",
    "Cảnh vật ở đây trông rất bình yên và dễ thương.",
    "Cảnh vật ở đây trông rất bồi hồi và thường thấy.",
    "Cảnh vật ở đây trông rất dễ nhớ và bình thường.",
    "Cảnh vật ở đây trông rất dễ thương và bình dị.",
    "Cảnh vật ở đây trông rất dễ thương và ngọt ngào.",
    "Cảnh vật ở đây trông rất dễ thương và quen thuộc.",
    "Cảnh vật ở đây trông rất dễ thương và quyết liệt.",
    "Cảnh vật ở đây trông rất dễ thương và tạm ổn.",
    "Cảnh vật ở đây trông rất hài hước và thường ngày.",
    "Cảnh vật ở đây trông rất hạnh phúc và dễ thương.",
    "Cảnh vật ở đây trông rất hồn nhiên và kì lạ.",
    "Cảnh vật ở đây trông rất khó tả và khó quên.",
    "Cảnh vật ở đây trông rất khó tả và kì lạ.",
    "Cảnh vật ở đây trông rất khó tả và rất cuốn.",
    "Cảnh vật ở đây trông rất khó tả và rõ ràng.",
    "Cảnh vật ở đây trông rất mơ mộng và thường thấy.",
    "Cảnh vật ở đây trông rất nhộn nhịp và quen thuộc.",
    "Cảnh vật ở đây trông rất như đùa nhưng rất thật.",
    "Cảnh vật ở đây trông rất như 1 giấc mơ nhưng rất cuốn.",
    "Cảnh vật ở đây trông rất quen thuộc và khó quên.",
    "Cảnh vật ở đây trông rất quyết liệt và bình thường.",
    "Cảnh vật ở đây trông rất tạm ổn và dễ thương.",
    "Cảnh vật ở đây trông rất thân quen nhưng lạ lẫm.",
    "Cảnh vật ở đây trông rất thường thấy và bồi hồi.",
    "Cảnh vật ở đây trông rất vui vẻ và thường ngày.",
    "Cảnh vật ở đây trông rất xúc động và dễ mến.",
    "Cảnh vật ở đây trông rất yên bình và dễ thương.",
]

comment = [
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái ánh nhìn lạc vào cơn gió cũ",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái cảm giác như đã từng ở đây",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái cảm giác như rất bình dị ở đây",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó hơi khó quên",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó hơi kì lạ",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó hơi mơ hồ",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó hơi quen thuộc",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó khó gọi tên",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó như giấc mơ",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó như lạ lùng",
    "Tổng quan thì chả có gì đặc biệt, chỉ là có một chút cái gì đó như mơ màng",
]

starting = [
    "bình dị",
    "bình yên",
    "dễ thương",
    "gần gũi",
    "hồn nhiên",
    "hơi kì cục",
    "kì cục",
    "kì lạ",
    "kì quặc",
    "lãng mạn",
    "mộng mơ",
    "mơ màng",
    "nhộn nhịp",
    "tạm ổn",
    "thơ mộng",
    "thường ngày",
    "tuyệt vời",
    "vui vẻ",
]

colors = [
    "bạc",  # #C0C0C0 - Màu bạc metallic truyền thống
    "bạch kim",  # #E5E4E2 - Màu bạch kim sang chảnh
    "bạc xước phần cứng",  # #8B8D8F - Màu vỏ laptop nhôm nguyên khối
    "cam",  # #FFA500 - Màu cam tiêu chuẩn
    "cam neon",  # #FF6700 - Màu cam neon đập vô mặt
    "cam vàng",  # #FF8C00 - Màu cam thiên vàng
    "cam xanh",  # #FF7F50 - Màu lai giữa cam và xanh (coral/phản phản)
    "crôm bóng gương",  # #E6E6E6 - Màu bạc bóng loáng phản chiếu
    "cyan",  # #00FFFF - Màu xanh cyan sáng
    "đen hố đen",  # #050505 - Màu đen tuyệt đối hút ánh sáng
    "đỏ",  # #FF0000 - Màu đỏ tiêu chuẩn
    "đỏ gạch",  # #8B0000 - Màu đỏ gạch trầm
    "đỏ son",  # #E34234 - Màu đỏ son rực rỡ
    "đỏ tươi",  # #FF2400 - Màu đỏ tươi cháy máy
    "đồng cyberpunk",  # #B87333 - Màu đồng đỏ pha hiệu ứng mạch điện
    "hồng",  # #FFC0CB - Màu hồng tiêu chuẩn
    "hồng cánh sen",  # #FF007F - Màu hồng cánh sen gắt
    "hồng dạ quang",  # #FF1493 - Màu bút dạ nhớ dòng nhìn xa 1km
    "hồng đào",  # #FFD1DC - Màu hồng đào dịu
    "hồng đào sáng",  # #FFB7C5 - Màu mlem công chúa
    "hồng hoàng hôn",  # #E0115F - Màu hồng pha tím sẫm lúc tắt nắng
    "hồng lục",  # #E6A8D7 - Màu hồng ánh xanh lục độc lạ
    "hồng pastel",  # #FFD1DC - Dịu dịu mà sáng vcl
    "huyết nguyệt",  # #4A0404 - Màu đỏ nguyệt thực huyền bí
    "nâu đất",  # #964B00 - Màu nâu đất trầm mộc
    "nâu sáng",  # #CD7F32 - Màu nâu sáng ấm
    "neon",  # #00FF00 - Màu xanh neon phát quang
    "ngọc bích",  # #00A86B - Màu xanh ngọc bích quý phái
    "tím",  # #800080 - Màu tím tiêu chuẩn
    "tím ánh kim",  # #9966FF - Tím nhưng sáng như vàng
    "tím khoai môn",  # #C3B1E1 - Đặc béo như trà sữa khoai môn
    "tím pastel",  # #DCD0FF - Ngọt như trà sữa
    "tím tinh vân",  # #660099 - Màu mây bụi vũ trụ Hubble
    "titan cháy",  # #5D3FD3 - Màu chuyển sắc khò nhiệt xanh tím vàng
    "trắng",  # #FFFFFF - Màu trắng tinh khiết
    "trắng ánh kim",  # #F8F8FF - Trắng + lấp lánh
    "trắng ngọc trai",  # #F0EAE1 - Hơi óng ánh mịn da
    "trắng xanh",  # #F0FFFF - Trắng thiên xanh
    "vàng",  # #FFFF00 - Màu vàng tiêu chuẩn
    "vàng ánh hồng",  # #FEE12B - Màu hoàng hôn rich kid
    "vàng chanh",  # #CCFF00 - Chói sáng như đèn pin xe tải
    "vàng kim",  # #FFD700 - Màu vàng kim quý tộc
    "vàng lục",  # #ADFF2F - Màu vàng chanh pha lục
    "vàng pastel",  # #FFFDD0 - Dễ thương mà chói
    "vàng phong tỏa",  # #FFCC00 - Vàng băng rôn cảnh báo nguy hiểm
    "vàng pudding",  # #F3E5AB - Màu vàng nhạt mềm mại, béo ngậy
    "xám bạc",  # #C0C0C0 - Màu xám ánh bạc
    "xám khói",  # #708090 - Màu xám khói ma mị
    "xám sáng",  # #D3D3D3 - Màu xám sáng thanh lịch
    "xám tối màu",  # #A9A9A9 - Màu xám tối đậm đà
    "xanh ánh bạc",  # #5F9EA0 - Ánh metal siêu nhiên
    "xanh băng",  # #71A6D2 - Sáng như mắt robot băng giá
    "xanh bơ creamy",  # #CBE86B - Màu xanh quả bơ xay sữa đặc
    "xanh chuối neon",  # #39FF14 - Xanh đọt chuối phát quang chói lòa
    "xanh cực quang",  # #00FF87 - Màu xanh lục lam Aurora Bắc Cực
    "xanh điện",  # #0066FF - Bright điện giật 🟦⚡
    "xanh lam",  # #0000FF - Màu xanh lam gốc
    "xanh lục",  # #008000 - Màu xanh lá cây gốc
    "xanh matcha",  # #74A12E - Màu xanh trà sữa Nhật Bản
    "xanh mint",  # #98FF98 - Màu kem bạc hà mát lạnh
    "xanh thiên thanh",  # #87CEEB - Màu trời xanh cực sáng
    "xanh tím laser",  # #4D00FF - Màu tia laser quán bar cyberpunk
]

quantities = [
    "các",
    "đôi ba",
    "lác đác có vài",
    "lác đác vài",
    "một số",
    "một số ít",
    "nhiều",
    "rải đều có",
    "rải rác đều có",
    "rải rác vài",
    "vài",
    "1",
    "3",
    "một vài", 
    "một nhóm", 
    "một đám",
    "hàng loạt", 
    "đầy rẫy", 
    "vài đám",
]

shapes = [
    # --- Hình học & Nét cơ bản ---
    "biểu tượng vô cực",
    "hình bánh donut",       # Vòng tròn có lỗ
    "hình bánh răng",        # Tròn có răng cưa
    "hình bán nguyệt",
    "hình bát quái",         # Bàn cờ bát quái/Thái cực
    "hình bì thư",           # Hình chữ nhật có nắp tam giác
    "hình bóng đèn",
    "hình bookmark",         # Dải băng có đuôi cá
    "hình bông tuyết",       # Đối xứng 6 góc phức tạp
    "hình cái chuông",
    "hình cái khiên",

    # --- Ký hiệu & Biểu tượng đường nét ---
    "hình cái răng",         # Răng có chân
    "hình cây thông",        # Dáng tam giác tầng
    "hình cây xương rồng",   # Dáng nhánh đặc trưng
    "hình chìa khóa",
    "hình chóp đều",
    "hình chữ S",
    "hình con bướm",         # Đối xứng cánh
    "hình con cá",
    "hình con cua",

    # --- Biểu tượng Đời sống & Đồ vật (Hình dáng đặc trưng) ---
    "hình cỏ 4 lá",
    "hình dấu chân",
    "hình dấu cộng",
    "hình dấu hỏi",
    "hình dấu tick",
    "hình đám mây",
    "hình đồng hồ cát",
    "hình đô la",
    "hình elip",
    "hình giọt nước",
    "hình GPS",
    "hình hoa hồng",
    "hình hoa sen",
    "hình kem ốc quế",       # Tam giác ngược kèm khối tròn phía trên
    "hình kẹp giấy",
    "hình kính lúp",

    # --- Thiên nhiên, Thời tiết & Thực vật ---
    "hình lá bồ đề",         # Dáng tim ngược có đuôi nhọn
    "hình lá phong",         # Lá nhiều răng cưa sâu
    "hình lục giác",
    "hình máy bay giấy",
    "hình mặt cười",
    "hình mặt trăng lưỡi liềm",
    "hình móng ngựa",        # Hình chữ U ngược
    "hình mỏ neo",
    "hình mũi tên",
    "hình ngọn lửa",
    "hình ngôi sao",
    "hình ngũ giác",
    "hình ổ khóa",
    "hình quả táo",          # Khối tròn có hõm và cuống

    # --- Động vật & Con người ---
    "hình sóng wifi",
    "hình tam giác",
    "hình thang",
    "hình thoi",
    "hình tia chớp",

    # --- Ẩn thực & Khác ---
    "hình trái tim",
    "hình tròn",
    "hình viên kẹo",         # Khối tròn/chữ nhật có 2 đuôi xoắn
    "hình viên kim cương",   # Khối đa giác lấp lánh
    "hình vuông",
    "hình vương miện",
    "hình xoắn ốc",
]

status = [
    "đáng yêu",
    "dễ thương",
    "bối rối",
    "đanh thép",
    "hào hứng",
    "hoang mang",
    "hấp tấp",
    "hơi ấm",
    "hơi bối rối",
    "hơi bơ vơ",
    "hơi buồn",
    "hơi cô đơn",
    "hơi lạ",
    "hơi lặng",
    "hơi mộng",
    "hơi nhạt",
    "hơi quen",
    "hơi sầu",
    "hơi thơ",
    "hơi tối",
    "hơi trầm",
    "hơi vui",
    "hơi xa",
    "khó nói",
    "không thể nói gì",
    "hơi lag",
    "hơi chớt quớt",
    "hơi cool",
    "quá là lag",
    "quá là cool",
    "quá chớt quớt",
    "quá lạ",
    "quá lặng",
    "quá mộng",
    "quá khùng",
    "mơ hồ",
    "ngộ nghĩnh",
    "quá chill",
    "quá dễ thương",
    "quá đăm chiêu",
    "quá êm",
    "quá mơ màng",
    "quá sáng",
    "quá thân thuộc",
    "quá thơ",
    "quá trầm tư",
    "quá vui",
    "quyết liệt",
    "rất bình thường",
    "rất bối rối",
    "rất deep",
    "rất dịu",
    "rất đáng nhớ",
    "rất gần",
    "rất khác lạ",
    "rất lãng mạn",
    "rất lặng",
    "rất mộng",
    "rất mơ",
    "rất ngẫu hứng",
    "rất quen",
    "rất suy tư",
    "rất u sầu",
    "rất vui",
    "rất là chill",
    "rất là deep",
    "rất là mê",
    "rắn rỏi",
    "sung túc",
    "sầu muộn",
    "trầm tư",
    "xa xăm",
]


units = [
"cân",
"cm",
"dB",
"dBm",
"dBm/s",
"dm",
"feet",
"gallon",
"hm",
"inch",
"kg",
"kg/ns",
"kg/s",
"km/s",
"km2",
"km3/ns",
"knot",
"lít",
"m",
"mile",
"ml",
"mm",
"m3",
"nm",
"tấn",
"yard",
]
