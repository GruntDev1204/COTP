import random

backgroundModeling = [
    # --- DANH MỤC: CÁNH ĐỒNG (FIELD & MEADOW) ---
    "softly blurred golden wheat field at sunset, warm cinematic lighting, minimal details",
    "out of focus green meadow under an overcast sky, soft natural daylight, minimalist backdrop",
    "blurred wildflower field with pastel colors, soft morning sun rays, clean composition",
    "out of focus lavender field with gentle purple hues, dreamy minimalist bokeh background",
    "softly blurred pampas grass field, earthy tones, minimalist and clean outdoor setup",
    "blurred rustic countryside hay bale field, muted colors, soft focus background",

    # --- DANH MỤC: TRONG NHÀ / STUDIO HẠU CẢNH (INDOOR & ARCHITECTURE) ---
    "softly blurred luxury hotel lobby with warm ambient light, minimalist structural lines",
    "out of focus minimalist museum interior, clean white marble textures, soft diffuse lighting",
    "blurred upscale apartment interior, floor-to-ceiling window, soft morning light, clean backdrop",
    "out of focus art gallery space, neutral concrete walls, dim artistic spotlighting",
    "softly blurred scandinavian style living room, muted tones, minimalist furniture layout",
    "blurred high-end studio interior with professional lighting setup, clean solid textures",

    # --- DANH MỤC: PHỐ THỊ & CÀ PHÊ (URBAN & CAFE) ---
    "blurred minimalist cafe interior with soft bokeh lighting",
    "out of focus modern urban street at daytime, minimal crowd",
    "softly blurred industrial loft wall, minimalist interior",
    "blurred contemporary fashion boutique backdrop with warm glowing lights",
    "out of focus clean architectural concrete wall, minimalist design",
    "softly blurred serene outdoor garden, natural daylight, clean composition"
]


backgroundModelingColors = [
    "solid deep navy blue",        # Xanh dương đậm (Màu kinh điển của ảnh thẻ cao cấp và suit doanh nhân)
    "solid luxury charcoal gray",  # Xám than đá (Màu quyền lực nhất trong chụp lookbook thời trang nam/nữ)
    "solid elegant olive green",   # Xanh rêu/ô-liu trầm (Cực tôn da và làm nổi bật đồ màu trắng/kem)
    "solid muted terracotta",      # Đất nung trầm (Tạo cảm giác nghệ thuật, ấm áp, trendy)
    "solid chocolate brown",       # Nâu đen/nâu chocolate (Tông màu cổ điển cho đồ thu đông, da thuộc)
    "solid midnight black",        # Đen tuyền (Ép AI đánh khối ánh sáng studio viền gáy - Rim light rất nghệ)
    "solid deep burgundy wine",    # Đỏ rượu vang chát (Sang trọng, huyền bí, hợp với đồ dạ hội/vest)
    "solid slate gray",            # Xám đá phiến (Màu trung tính lạnh, tạo cảm giác hiện đại, sạch sẽ)
    "solid dark forest green"      # Xanh lá cây sẫm/rừng sâu (Tạo chiều sâu tuyệt đối cho khung hình)
]

shoes = [
    # --- DANH MỤC: GIÀY CAO GÓT (HIGH HEELS) ---
    "wearing elegant high-heeled stiletto pumps",
    "wearing sexy strappy high-heeled sandals",
    "wearing classic pointed-toe kitten heels",
    "wearing chunky platform high heels",
    "wearing sophisticated slingback heels with pointed toes",
    "wearing luxury patent leather ankle-strap heels",
    "wearing stylish wedge heel sandals",
    "wearing open-toe mule heels",

    # --- DANH MỤC: BỐT NỮ (BOOTS) ---
    "wearing sleek black leather knee-high boots",
    "wearing premium suede over-the-knee thigh boots",
    "wearing elegant leather chelsea ankle boots",
    "wearing chunky combat platform boots",
    "wearing stylish pointed-toe stiletto ankle booties",
    "wearing western-style cowboy leather boots",
    "wearing luxury lace-up leather boots",

    # --- DANH MỤC: GIÀY BỆT & BÚP BÊ (FLATS & BALLERINAS) ---
    "wearing classic minimalist ballet flats",
    "wearing elegant mary jane shoes with instep straps",
    "wearing trendy leather loafers with metal hardware",
    "wearing comfortable slip-on leather mules",
    "wearing stylish pointed-toe flat shoes",
    "wearing classic leather oxfords",
    "wearing casual espadrille flat shoes",

    # --- DANH MỤC: GIÀY THỂ THAO & STREETWEAR (SNEAKERS) ---
    "wearing clean white minimalist fashion sneakers",
    "wearing trendy chunky platform dad sneakers",
    "wearing stylish canvas low-top skate shoes",
    "wearing sporty retro-style running sneakers",
    "wearing high-top streetwear sneakers"
]


backgrounds = backgroundModeling + backgroundModelingColors

modelSetup = [
    "Three-quarter thigh-up studio lookbook shot of a professional model, standing perfectly straight, symmetrical frontal pose, facing directly at the camera, clean e-commerce style, 8k resolution, crisp details, soft floor shadow, professional studio lighting.",
    "Knee-up fashion studio lookbook portrait of a professional model, standing perfectly straight, symmetrical frontal pose, facing directly at the camera, clean e-commerce style, 8k resolution, crisp details, soft floor shadow, professional studio lighting.",
    "Ankle-up fashion studio lookbook portrait of a professional model, standing perfectly straight, symmetrical frontal pose, facing directly at the camera, clean e-commerce style, 8k resolution, crisp details, soft floor shadow, professional studio lighting. The model is {shoe}.",
    "Full-body studio lookbook portrait of a professional model, standing perfectly straight, symmetrical frontal pose, facing directly at the camera, clean e-commerce style, 8k resolution, crisp details, soft floor shadow, professional studio lighting. The model is {shoe}."
]