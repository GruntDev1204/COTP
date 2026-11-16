from data.dataNPC import *
from data.dataIndoor import *
from data.dataOutdoor import *
from data.dataStory import *
from data.dataLove import *
from data.dataL4D2 import *
from data.dataIcon import *
from data.dataModelingPrompt import *

comment = (
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
)

colors = (
    "bạc",  # #C0C0C0 - Màu bạc metallic truyền thống
    "bạc ánh trăng",  # #E2E5DE - Màu bạc sáng mờ ảo dưới trăng
    "bạc xước phần cứng",  # #8B8D8F - Màu vỏ laptop nhôm nguyên khối
    "bạch kim",  # #E5E4E2 - Màu bạch kim sang chảnh
    "be",  # #F5F5DC - Màu beige kinh điển của giới UI/UX tối giản
    "be cát sa mạc",  # #EDC9AF - Màu cát nóng bỏng vùng Trung Đông
    "be sữa yến mạch",  # #EAE0C8 - Màu nền web aesthetic chuẩn Pinterest
    "bích ngọc lục bảo",  # #50C878 - Màu emerald xanh ngọc sáng lấp lánh
    "bơ lạt",  # #FFF8DC - Màu cornsilk vàng kem nhạt
    "cam",  # #FFA500 - Màu cam tiêu chuẩn
    "cam bí ngô",  # #FF7518 - Màu pumpkin đặc trưng mùa Halloween
    "cam cháy",  # #CC5500 - Màu burnt orange trầm ấm, đậm chất retro
    "cam đào",  # #FFE5B4 - Màu peachpuff ngọt ngào dịu mắt
    "cam đất",  # #E2725B - Màu terracotta gạch nung thủ công
    "cam hoàng hôn",  # #FD5E53 - Màu sunset rực lửa cuối chân trời
    "cam hổ phách",  # #FFBF00 - Màu amber sáng rực như nhựa thông hóa thạch
    "cam san hô",  # #FF7F50 - Màu coral chuẩn CSS của dân FE
    "cam sáng",  # #FFA07A - Màu lightsalmon cá hồi tươi
    "cam quýt",  # #F28500 - Màu tangerine tươi rói mọng nước
    "cam neon",  # #FF6700 - Màu cam neon đập vô mặt
    "cam vàng",  # #FF8C00 - Màu cam thiên vàng
    "cam xanh",  # #FF7F50 - Màu lai giữa cam và xanh (coral/phản phản)
    "chàm",  # #4B0082 - Màu indigo sâu thẳm trên dải cầu vồng
    "chàm điện tử",  # #6F00FF - Màu electric indigo chói lòa màn hình OLED
    "crôm bóng gương",  # #E6E6E6 - Màu bạc bóng loáng phản chiếu
    "cyan",  # #00FFFF - Màu xanh cyan sáng
    "cyan đậm",  # #008B8B - Màu darkcyan trầm lạnh
    "dạ quang",  # #CCFF00 - Màu phát sáng trong bóng tối
    "đen",  # #000000 - Màu đen tuyền nguyên bản chuẩn Hex #000
    "đen hố đen",  # #050505 - Màu đen tuyệt đối hút ánh sáng
    "đen nhám",  # #28282B - Màu matte black của siêu xe và vỏ phím cơ
    "đen than chì",  # #36454F - Màu charcoal xám đen hiện đại
    "đen tuyền",  # #0A0A0A - Màu onyx đen bóng sang trọng
    "đỏ",  # #FF0000 - Màu đỏ tiêu chuẩn
    "đỏ anh đào",  # #DE3163 - Màu cerise đỏ hồng chín mọng
    "đỏ bầm",  # #800000 - Màu maroon truyền thống của CSS
    "đỏ burgundy",  # #800020 - Màu đỏ rượu vang Pháp cổ điển
    "đỏ cánh kiến",  # #960018 - Màu carmine đậm đà quyền lực
    "đỏ cam",  # #FF4500 - Màu orangeredy rực lửa thông báo lỗi
    "đỏ đô",  # #8B0000 - Màu darkred đậm đặc
    "đỏ đồng",  # #CB6D51 - Màu copper red kim loại ấm
    "đỏ gạch",  # #8B0000 - Màu đỏ gạch trầm
    "đỏ hồng ngọc",  # #E0115F - Màu ruby lấp lánh đắt giá
    "đỏ máu",  # #660000 - Màu blood red rùng rợn
    "đỏ san hô",  # #F88379 - Màu coral pink pha đỏ dịu
    "đỏ son",  # #E34234 - Màu đỏ son rực rỡ
    "đỏ thẫm",  # #DC143C - Màu crimson sắc sảo
    "đỏ tươi",  # #FF2400 - Màu đỏ tươi cháy máy
    "đồng cyberpunk",  # #B87333 - Màu đồng đỏ pha hiệu ứng mạch điện
    "đồng điếu",  # #CD7F32 - Màu bronze cổ vật nghìn năm
    "đồng thau",  # #B5A642 - Màu brass vàng ánh kim loại
    "hổ phách",  # #FF7E00 - Màu amber rực sáng
    "hồng",  # #FFC0CB - Màu hồng tiêu chuẩn
    "hồng cánh sen",  # #FF007F - Màu hồng cánh sen gắt
    "hồng dạ quang",  # #FF1493 - Màu bút dạ nhớ dòng nhìn xa 1km
    "hồng đào",  # #FFD1DC - Màu hồng đào dịu
    "hồng đào sáng",  # #FFB7C5 - Màu mlem công chúa
    "hồng đất",  # #C08081 - Màu old rose trầm cổ điển
    "hồng fuchsia",  # #FF00FF - Màu hồng tím chuẩn hệ màu CMYK/CSS
    "hồng hoàng hôn",  # #E0115F - Màu hồng pha tím sẫm lúc tắt nắng
    "hồng lục",  # #E6A8D7 - Màu hồng ánh xanh lục độc lạ
    "hồng magenta",  # #FF0090 - Màu hồng cánh sen đậm hệ in ấn
    "hồng nhạt",  # #FFB6C1 - Màu lightpink nhẹ nhàng
    "hồng pastel",  # #FFD1DC - Dịu dịu mà sáng vcl
    "hồng phấn",  # #FADADD - Màu pale pink mịn màng
    "hồng san hô",  # #F88379 - Màu hồng cam tươi tắn
    "hồng thạch anh",  # #F7CAC9 - Màu rose quartz từng làm mưa làm gió Pantone
    "hồng trà sữa",  # #D8A1C4 - Màu hồng pha nâu tím ngọt lịm
    "huyết nguyệt",  # #4A0404 - Màu đỏ nguyệt thực huyền bí
    "kem",  # #FFFDD0 - Màu cream mềm mại
    "lam ngọc",  # #00CED1 - Màu darkturquoise xanh biển sâu
    "lục bảo",  # #50C878 - Màu xanh đá quý hoàng gia
    "be nhạt",  # #FAF0E6 - linen vải lanh tự nhiên
    "cà phê",  # #6F4E37 - nâu hạt cà phê rang
    "chàm cổ",  # #3F00FF - ultramarine xanh chàm rực rỡ
    "chì",  # #2F4F4F - darkslategray xám xanh tối
    "da người",  # #FFE0BD - peach skin tự nhiên
    "gỗ gụ",  # #C04000 - mahogany đỏ nâu sang trọng
    "hạt dẻ",  # #954535 - chestnut nâu đỏ ấm áp
    "khói sương",  # #F5F5F5 - whitesmoke huyền thoại của CSS
    "lông chuột",  # #808080 - gray tiêu chuẩn hệ thập lục phân
    "mận chín",  # #DDA0DD - plum tím hồng dịu
    "ngà voi",  # #FFFFF0 - ivory trắng ngà cổ điển
    "ô liu",  # #808000 - olive xanh rêu quân đội
    "rỉ sét",  # #B7410E - rust nâu cam kim loại oxy hóa
    "sô cô la",  # #D2691E - chocolate chuẩn CSS
    "than đá",  # #1C1C1C - đen xám lì
    "tuyết",  # #FFFAFA - snow trắng tinh khôi của CSS
    "vỏ trứng",  # #F0EAD6 - Màu eggshell trắng ngà nhẹ
    "nâu",  # #A52A2A - Màu brown chuẩn CSS (thiên đỏ gạch)
    "nâu cánh gián",  # #654321 - Màu nâu đậm bóng bẩy
    "nâu đất",  # #964B00 - Màu nâu đất trầm mộc
    "nâu đồng",  # #804A00 - Màu nâu ánh kim loại
    "nâu hạt phỉ",  # #8E7618 - Màu hazel nâu vàng
    "nâu quế",  # #D2691E - Màu cinnamon thơm nồng
    "nâu sáng",  # #CD7F32 - Màu nâu sáng ấm
    "nâu tây",  # #BC8F8F - Màu rosybrown nâu pha hồng
    "nâu trầm",  # #5C4033 - Màu dark brown sâu lắng
    "neon",  # #00FF00 - Màu xanh neon phát quang
    "ngọc bích",  # #00A86B - Màu xanh ngọc bích quý phái
    "ngọc lam",  # #40E0D0 - Màu turquoise xanh biển nhiệt đới
    "tím",  # #800080 - Màu tím tiêu chuẩn
    "tím ánh kim",  # #9966FF - Tím nhưng sáng như vàng
    "tím bằng lăng",  # #B57EDC - Màu lavender floral nhẹ nhàng
    "tím cà",  # #614051 - Màu eggplant tím sẫm
    "tím hoa cà",  # #C8A2C8 - Màu lilac tím nhạt thơ mộng
    "tím hoàng gia",  # #7851A9 - Màu royal purple quyền quý
    "tím huế",  # #9932CC - Màu darkorchid mộng mơ
    "tím khoai môn",  # #C3B1E1 - Đặc béo như trà sữa khoai môn
    "tím lavender",  # #E6E6FA - Màu tím oải hương chuẩn CSS
    "tím mộng mơ",  # #9370DB - Màu mediumpurple dịu dàng
    "tím pastel",  # #DCD0FF - Ngọt như trà sữa
    "tím phong lan",  # #DA70D6 - Màu orchid tươi sáng
    "tím than",  # #301934 - Màu dark purple gần như đen
    "tím tinh vân",  # #660099 - Màu mây bụi vũ trụ Hubble
    "tím violet",  # #EE82EE - Màu violet chuẩn hệ màu quang phổ
    "titan cháy",  # #5D3FD3 - Màu chuyển sắc khò nhiệt xanh tím vàng
    "trắng",  # #FFFFFF - Màu trắng tinh khiết
    "trắng ánh kim",  # #F8F8FF - Trắng + lấp lánh
    "trắng ngà",  # #FAEBD7 - Màu antiquewhite cổ kính
    "trắng ngọc trai",  # #F0EAE1 - Hơi óng ánh mịn da
    "trắng sứ",  # #F8F9FA - Màu nền trắng xám cực nhẹ của Bootstrap/Tailwind
    "trắng sữa",  # #FDFFF5 - Màu milk white mềm mịn
    "trắng xanh",  # #F0FFFF - Trắng thiên xanh
    "vàng",  # #FFFF00 - Màu vàng tiêu chuẩn
    "vàng ánh hồng",  # #FEE12B - Màu hoàng hôn rich kid
    "vàng nghệ",  # #FFDB58 - Màu mustard vàng mù tạt
    "vàng chanh",  # #CCFF00 - Chói sáng như đèn pin xe tải
    "vàng đồng",  # #DAA520 - Màu goldenrod vàng kim trầm
    "vàng hổ phách",  # #FFBF00 - Màu vàng cam rực rỡ
    "vàng kem",  # #FFFACD - Màu lemonchiffon vàng nhạt dịu mắt
    "vàng kim",  # #FFD700 - Màu vàng kim quý tộc
    "vàng lục",  # #ADFF2F - Màu vàng chanh pha lục
    "vàng mơ",  # #FBCEB1 - Màu apricot cam vàng nhạt
    "vàng mật ong",  # #FFB300 - Màu vàng sóng sánh ngọt ngào
    "vàng nắng",  # #FFF44F - Màu lemon yellow rực rỡ ban trưa
    "vàng nhạt",  # #FFFFE0 - Màu lightyellow thanh thoát
    "vàng pastel",  # #FFFDD0 - Dễ thương mà chói
    "vàng phong tỏa",  # #FFCC00 - Vàng băng rôn cảnh báo nguy hiểm
    "vàng pudding",  # #F3E5AB - Màu vàng nhạt mềm mại, béo ngậy
    "xám",  # #808080 - Màu xám trung tính chuẩn CSS
    "xám bạc",  # #C0C0C0 - Màu xám ánh bạc
    "xám chì",  # #778899 - Màu lightslategray xám xanh thép
    "xám đá phiến",  # #6A5ACD - Màu slate xám tím hiện đại của Tailwind
    "xám khói",  # #708090 - Màu xám khói ma mị
    "xám lông chồn",  # #483C32 - Màu taupe xám pha nâu sang trọng
    "xám nhạt",  # #DCDCDC - Màu gainsboro xám sáng nhẹ
    "xám sáng",  # #D3D3D3 - Màu xám sáng thanh lịch
    "xám tối màu",  # #A9A9A9 - Màu xám tối đậm đà
    "xám tro",  # #B2BEB5 - Màu ash gray bụi bặm
    "xám xi măng",  # #8D918D - Màu bê tông công nghiệp tối giản
    "xanh ánh bạc",  # #5F9EA0 - Ánh metal siêu nhiên
    "xanh băng",  # #71A6D2 - Sáng như mắt robot băng giá
    "xanh bạc hà",  # #3EB489 - Màu mint đậm tươi mát
    "xanh biển",  # #0077BE - Màu ocean blue đại dương sâu
    "xanh biển sâu",  # #000080 - Màu navy kinh điển
    "xanh bơ creamy",  # #CBE86B - Màu xanh quả bơ xay sữa đặc
    "xanh cổ vịt",  # #008080 - Màu teal thần thánh của dân thiết kế UI
    "xanh chuối neon",  # #39FF14 - Xanh đọt chuối phát quang chói lòa
    "xanh coban",  # #0047AB - Màu cobalt xanh lam đậm rực rỡ
    "xanh cực quang",  # #00FF87 - Màu xanh lục lam Aurora Bắc Cực
    "xanh dương",  # #1E90FF - Màu dodgerblue chuẩn CSS
    "xanh dương nhạt",  # #ADD8E6 - Màu lightblue dịu nhẹ
    "xanh da trời",  # #00BFFF - Màu deepskyblue trong vắt
    "xanh đen",  # #191970 - Màu midnightblue tối sẫm
    "xanh điện",  # #0066FF - Bright điện giật 🟦⚡
    "xanh lam",  # #0000FF - Màu xanh lam gốc
    "xanh lá mạ",  # #7CFC00 - Màu lawngreen xanh non mơn mởn
    "xanh lơ",  # #00FFFF - Màu aqua xanh nước biển sáng
    "xanh lục",  # #008000 - Màu xanh lá cây gốc
    "xanh lục bảo",  # #2E8B57 - Màu seagreen xanh rừng rậm
    "xanh matcha",  # #74A12E - Màu xanh trà sữa Nhật Bản
    "xanh mint",  # #98FF98 - Màu kem bạc hà mát lạnh
    "xanh ngọc",  # #00A86B - Màu jade xanh cẩm thạch
    "xanh ngọc bích",  # #0D98BA - Màu blue-green quý phái
    "xanh pastel",  # #AEC6CF - Màu xanh phấn dịu mắt
    "xanh rêu",  # #556B2F - Màu darkolivegreen trầm mặc
    "xanh thép",  # #4682B4 - Màu steelblue kim loại lạnh
    "xanh thiên thanh",  # #87CEEB - Màu trời xanh cực sáng
    "xanh tím laser",  # #4D00FF - Màu tia laser quán bar cyberpunk
    "xanh vịt trời",  # #006D5B - Màu deep teal sang trọng
)

quantities = (
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
    "một đám đông",
    "hàng loạt", 
    "đầy rẫy", 
    "vài đám",
    "xuất hiện vài",
)

shapes = (
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
    "hình chìa khóa(🗝️)",
    "hình con bướm(🦋)",
    "hình con cá(🐟)",
    "hình con cua(🦀)",
    "hình cỏ 4 lá(🍀)",
    "hình dấu chân(👣)",
    "hình đám mây(☁️)",
    "hình đồng hồ cát(⏳)",
    "hình giọt nước(💧)",
    "hình biểu tượng GPS",
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
    "hình tia sét(⚡)",
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
    "hình cây lúa (🌾)",
    "hình chiếc bóng bay (🎈)",
    "hình đồng xu (🪙)",
    "hình cái cuốc (⛏️)",
    "hình đùi gà (🍗)",
    "hình Puzzle Piece (🧩)",
    "hình cái micro (🎤)",
    "hình cái micro phòng thu (🎙️)",
    "hình biển báo cấm (🚫)",
    "hình biển báo cấm đi ngược chiều (⛔)",
    "hình biển báo cảnh báo (⚠️)",
    "hình sóng điện thoại (📶)",
    "hình kính lúp (🔎)",
    "hình biểu tượng tái chế (♻️)",
    "hình biểu tượng BitCoin (₿)",

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
    "hình dấu chấm than (❗)",
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
)

status = (
    "đáng yêu",
    "dễ thương",
    "bối rối",
    "bất đồng",
    "bất lực",
    "bất đối xứng",
    "đanh thép",
    "đặc sắc",
    "hào hứng",
    "hòa hợp",
    "chúa hề",
    "chớt quớt",
    "cam chịu",
    "cà chớn",
    "cà nhây",
    "cù nhây",
    "chảnh chọe",
    "cảnh giác",
    "cau có",
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
    "sến súa",
    "sầu muộn",
    "siêu thực",
    "trầm tư",
    "xa xăm",
    "kỳ quặc",
    "kỳ cục",
    "kỳ bí",
    "lag lag",
    "lầy lội",
    "khùng điên",
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
    "mê muội",
    "mộng mơ",
    "mơ màng",
    "nhộn nhịp",
    "ngây thơ",
    "tạm ổn",
    "thơ mộng",
    "thường ngày",
    "yêu thương",
    "vui vẻ",
    "vô định",
    "vô sở trụ",
    "vô nghiệm",
    "vô vị",
    "vi diệu",
    "tuyệt vời",
    "tuyệt vời ông mặt trời",
    "tưng tửng",
    "sặc sỡ",
)


units = (
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
)

randomLargeNumberRange = (100_000_000_000, 1_000_000_000_000)
clockPeriods = ("sáng", "trưa", "chiều", "tối", "đêm")
dateEras = (
    "TCN",
    "SCN",
    "AH",
    "BE",
    "AM",
    "HE",
)

typeNumber = ("i", "")
typeValueNumber = ("-", "")



