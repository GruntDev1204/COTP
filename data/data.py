from data.dataNPC import *
from data.dataIndoor import *
from data.dataOutdoor import *
from data.dataStory import *
from data.dataLove import *
from data.dataL4D2 import *
from data.dataIcon import *
from data.dataModelingPrompt import *

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
    # Đồ vật
    "hình bánh donut(🍩)",
    "hình bánh răng(⚙️)",
    "hình bát quái(☯)",
    "hình bì thư(✉️)",
    "hình bóng đèn(💡)",
    "hình bookmark(🔖)",
    "hình bông tuyết(❄️)",
    "hình cái chuông(🔔)",
    "hình cái khiên(🛡️)",
    "hình cái răng(🦷)",
    "hình cây thông(🌲)",
    "hình cây xương rồng(🌵)",
    "hình chìa khóa(🔑)",
    "hình con bướm(🦋)",
    "hình con cá(🐟)",
    "hình con cua(🦀)",
    "hình cỏ 4 lá(🍀)",
    "hình dấu chân(👣)",
    "hình đám mây(☁️)",
    "hình đồng hồ cát(⏳)",
    "hình giọt nước(💧)",
    "hình GPS(📍)",
    "hình hoa hồng(🌹)",
    "hình hoa sen(🪷)",
    "hình kem ốc quế(🍦)",
    "hình kẹp giấy(📎)",
    "hình kính lúp(🔍)",
    "hình lá bồ đề(🍃)",
    "hình lá phong(🍁)",
    "hình mặt cười(😊)",
    "hình lưỡi liềm(🌙)",
    "hình móng ngựa(🧲)",
    "hình mỏ neo(⚓)",
    "hình mũi tên(➔)",
    "hình ngọn lửa(🔥)",
    "hình ngôi sao(⭐)",
    "hình ổ khóa(🔒)",
    "hình quả táo(🍎)",
    "hình sóng wifi(🛜)",
    "hình tia chớp(⚡)",
    "hình trái tim(❤️)",
    "hình viên kẹo(🍬)",
    "hình viên kim cương(💎)",
    "hình vương miện(👑)",
    "hình lò xo(➰)",
    "hình con mèo(🐱)",
    "hình con chó(🐶)",
    "hình con thỏ(🐰)",
    "hình con cáo(🦊)",
    "hình con gấu(🐻)",
    "hình con cú mèo(🦉)",
    "hình con đại bàng(🦅)",
    "hình con chim cánh cụt(🐧)",
    "hình con dơi(🦇)",
    "hình con rắn(🐍)",
    "hình con rùa(🐢)",
    "hình con bạch tuộc(🐙)",
    "hình con cá voi(🐳)",
    "hình con cá heo(🐬)",
    "hình con cá mập(🦈)",
    "hình con ốc sên(🐌)",
    "hình con nhện(🕷️)",
    "hình con ong(🐝)",
    "hình con bọ cạp(🦂)",
    "hình con khủng long(🦖)",
    "hình đầu lâu(💀)",
    "hình bàn tay(✋)",
    "hình con mắt(👁️)",
    "hình đôi môi(👄)",
    "hình bộ não(🧠)",
    "hình chiếc lá(🍃)",
    "hình cây nấm(🍄)",
    "hình quả anh đào(🍒)",
    "hình quả dứa(🍍)",
    "hình quả chuối(🍌)",
    "hình miếng dưa hấu(🍉)",
    "hình chiếc cúp(🏆)",
    "hình thanh kiếm(🗡️)",
    "hình cây cung tên(🏹)",
    "hình cây búa(🔨)",
    "hình chiếc kéo(✂️)",
    "hình chiếc ô(☂️)",
    "hình chiếc mũ phù thủy(🧙)",
    "hình chiếc đàn guitar(🎸)",
    "hình nốt nhạc(🎵)",
    "hình chiếc máy ảnh(📷)",
    "hình chiếc đồng hồ(⏰)",
    "hình tên lửa(🚀)",
    "hình quân cờ vua - Vua(♔)",
    "hình quân cờ vua - Hậu(♕)",
    "hình quân cờ vua - Mã(♘)",
    "hình quân cờ vua - Tốt(♙)",
    "hình quân cờ vua - Xe(♖)",
    "hình quân cờ vua - Tượng(♗)",
    "hình chiếc cờ lê(🔧)",
    "hình cây tua vít(🪛)",
    "hình cái cưa(🪚)",
    "hình cây rìu(🪓)",
    "hình con ốc vít",
    "hình bu-lông",
    "hình cái thang(🪜)",
    "hình cuộn băng dính(🩹)",
    "hình thước kẻ(📏)",
    "hình thước ê ke(📐)",
    "hình chiếc compa(🧭)",
    "hình cục nam châm(🧲)",
    "hình viên pin(🔋)",
    "hình phích cắm điện(🔌)",
    "hình sợi dây xích(⛓️)",
    "hình cái xẻng(⛏️)",
    "hình biểu tượng like (👍)",
    "hình mặt hề (🤡)",

    # Biểu tượng toán học
    "hình biểu tượng vô cực(∞)",
    "hình bán nguyệt(◗)",
    "hình chóp đều(▲)",
    "hình dấu cộng(✚)",
    "hình elip(⬭)",
    "hình lục giác(⬡)",
    "hình ngũ giác(⬠)",
    "hình bát giác(⯃)",
    "hình tam giác(△)",
    "hình thang(⏢)",
    "hình thoi(◇)",
    "hình tròn(○)",
    "hình vuông(□)",
    "hình bình hành(▱)",
    "hình tứ diện đều",
    "hình bát diện đều",
    "hình thập nhị diện đều",
    "hình nhị thập diện đều",
    "hình khối trụ",
    "hình khối nón",
    "hình khối cầu",
    "hình bán cầu",
    "hình lăng trụ tam giác",
    "hình lăng trụ lục giác",
    "hình chóp cụt",
    "hình nón cụt",
    "hình vòng xuyến Torus",
    "hình xoắn kép DNA",
    "hình xoắn ốc Fibonacci",
    "hình tam giác bất khả thi Penrose",
    "hình khối lập phương bất khả thi",
    "hình khối siêu lập phương Tesseract",
    "hình chai Klein",
    "hình sao 6 cánh(✡)",
    "hình sao 8 cánh(✴)",
    "hình bông tuyết Koch",
    "hình tam giác Sierpinski",
    "hình thảm Sierpinski",
    "hình mạng lưới Voronoi",
    "hình xoắn ốc(🌀)",
    "hình biểu tượng dấu tích phân(∫)",
    "hình biểu tượng tích phân kỳ(∏)",
    "hình biểu tượng sigma(∑)",
    "hình biểu tượng sóng sin(∿)",
    "hình biểu tượng parabol(∪)",
    "hình biểu tượng parabol úp(∩)",
    "hình biểu tượng Mobius(♾️)",
    "hình biểu tượng Pi(π)",
    "hình biểu tượng Omega(Ω)",
    "hình biểu tượng Delta(Δ)",
    "hình biểu tượng Alpha(α)",
    "hình biểu tượng Beta(β)",
    "hình biểu tượng Lambda(λ)",
    "hình biểu tượng Phi(Φ)",
    "hình biểu tượng Psi(Ψ)",
    "hình dấu căn bậc hai(√)",
    "hình dấu xấp xỉ(≈)",
    "hình dấu đồng dạng(∽)",
    "hình dấu vô cùng bé(∂)",
    "hình tam giác ngược Nabla(∇)",
    "hình dấu vuông góc(⊥)",
    "hình dấu song song(∥)",
    "hình dấu góc nhọn(∠)",
    "hình dấu giao thoa(⋈)",
    "hình dấu hợp nhất(⊕)",
    "hình dấu nhân tâm(⊗)",
    "hình dấu chấm tròn tâm(⊙)",
    "hình dấu rỗng(∅)",
    "hình dấu tồn tại(∃)",
    "hình dấu với mọi(∀)",
    "hình dấu thuộc về(∈)",
    "hình dấu ba chấm tam giác(∴)",
    "hình dấu phần trăm(%)",
    "hình dấu thăng(#)",
    "hình dấu sao hoa thị(*)",
    "hình dấu ngoặc nhọn({)",
    "hình khối lập phương(🧊)",
    "hình cầu",
    "hình kim tự tháp(🔺)",
    "hình mạng lưới tọa độ(⊞)",

    # Biểu tượng chữ cái
    "hình dấu hỏi(❓)",
    "hình dấu tick(✔️)",
    "hình đô la($)",
    "hình chữ A",
    "hình chữ B",
    "hình chữ C",
    "hình chữ D",
    "hình chữ E",
    "hình chữ F",
    "hình chữ G",
    "hình chữ H",
    "hình chữ I",
    "hình chữ J",
    "hình chữ K",
    "hình chữ L",
    "hình chữ M",
    "hình chữ N",
    "hình chữ O",
    "hình chữ P",
    "hình chữ Q",
    "hình chữ R",
    "hình chữ S",
    "hình chữ T",
    "hình chữ U",
    "hình chữ V",
    "hình chữ W",
    "hình chữ X",
    "hình chữ Y",
    "hình chữ Z",
    "hình chữ vạn",
    "hình chữ thập",
    
    # Biểu tượng chữ số
    "hình số 0",
    "hình số 1",
    "hình số 2",
    "hình số 3",
    "hình số 4",
    "hình số 5",
    "hình số 6",
    "hình số 7",
    "hình số 8",
    "hình số 9",
    
    # Biểu tượng cung hoàng đạo
    "hình biểu tượng cung Bạch Dương(♈)",
    "hình biểu tượng cung Kim Ngưu(♉)",
    "hình biểu tượng cung Song Tử(♊)",
    "hình biểu tượng cung Cự Giải(♋)",
    "hình biểu tượng cung Sư Tử(♌)",
    "hình biểu tượng cung Xử Nữ(♍)",
    "hình biểu tượng cung Thiên Bình(♎)",
    "hình biểu tượng cung Bọ Cạp(♏)",
    "hình biểu tượng cung Nhân Mã(♐)",
    "hình biểu tượng cung Ma Kết(♑)",
    "hình biểu tượng cung Bảo Bình(♒)",
    "hình biểu tượng cung Song Ngư(♓)",

    # Biểu tượng bài Tây
    "hình trái tim bài cơ(♥)",
    "hình viên kim cương bài rô(♦)",
    "hình cỏ ba lá bài chuồn(♣)",
    "hình lá bích(♠)",
]

status = [
    "đáng yêu",
    "dễ thương",
    "bối rối",
    "bất đồng",
    "bất đối xứng",
    "đanh thép",
    "đặc sắc",
    "hào hứng",
    "hòa hợp",
    "chúa hề",
    "hề hước",
    "hài hước",
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
    "hòa thuận",
    "khó nói",
    "không thể nói gì",
    "không thể nói gì hơn",
    "không nói nên lời",
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
    "siêu thực",
    "trầm tư",
    "xa xăm",
    "kỳ quặc",
    "kỳ cục",
    "kỳ bí",
    "chớt quớt",
    "lag lag",
    "khùng điên",
    "cam chịu",
    "không xác định",
    "bí ẩn",
    "bình dị",
    "bình yên",
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
    "ngây thơ",
    "tạm ổn",
    "thơ mộng",
    "thường ngày",
    "yêu thương",
    "tuyệt vời",
    "vui vẻ",
    "vô định",
    "vô sở trụ",
    "vô nghiệm",
    "vô vị",
    "vi diệu",
    "tuyệt vời ông mặt trời",
    "sặc sỡ",
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

randomLargeNumberRange = (100_000_000_000, 1_000_000_000_000)
clockPeriods = ["sáng", "trưa", "chiều", "tối", "đêm"]
dateEras = [
    "TCN",
    "SCN",
    "AH",  # Anno Hegirae / Hijri era
    "BE",  # Buddhist Era
    "AM",  # Anno Mundi
    "HE",  # Holocene Era
]

typeNumber = ["i", ""]
typeValueNumber = ["-" , ""]


