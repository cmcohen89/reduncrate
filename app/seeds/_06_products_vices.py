from random import randint

products_vices = [
    {
        "id": 56,
        "title": "KLARO MILITARY EDITION HUMIDOR",
        "description": "Store your best sticks in style with this cedar-lined, military-inspired matte black humidor. $300.",
        "detailed_description": "Not all humidors need to have classic wooden exteriors. This Military Edition Humidor from adopts a more modern look with a sleek matte black exterior and custom gunmetal hardware and handles. The interior is clad in thick 100% Spanish cedar, and outfitted with a recessed hydro system to keep sticks fresh, a sliding, removable storage tray for organization, and rubber gaskets for a tight seal. A digital hygrometer on the front lets you know when it's time to add more water, and a drawer on the bottom keeps lighters, cutters, and other accessories conveniently at hand.",
        "category_id": 6,
        "owner_id": randint(1, 3),
        "price": 300,
        "preview_img_id": 56,
    },
    {
        "id": 57,
        "title": "SAIL AWAY COLD BREW BOX TAP",
        "description": "A 96-ounce supply of organic cold brew coffee on tap for all-day fueling. $30.",
        "detailed_description": "Some mornings call for a cup of coffee while others require a keg. For the latter, there's the Sail Away Tap. The box holds 96 glorious ounces of organic cold brew that comes ready to drink. No mixing or measuring, just pour it straight into your cup, or mouth, We don't judge. Each 8-ounce serving delivers 120mg of caffeine to fuel you through the day. Once it's been opened, the slim box fits neatly in the fridge.",
        "category_id": 6,
        "owner_id": randint(1, 3),
        "price": 30,
        "preview_img_id": 57,
    },
    {
        "id": 58,
        "title": "ALESSI SPIRALE ASHTRAY",
        "description": "Created in 1970 by Italian designer Achille Castiglioni, the Spirale has a cig-holding metal spiral. $125.",
        "detailed_description": "Smoking was far more common when Italian designer Achille Castiglioni came up with the Spirale Ashtray in 1970, yet its design endures. It's crafted from 18/10 stainless steel and named for the signature spiral that goes around the inner edge and holds cigarettes for absent-minded smokers like its creator. The spiral can also be lifted out for cleaning, which also allows the object to serve as a catch-all tray for small items like change, keys, or earphones. Made in Italy.",
        "category_id": 6,
        "owner_id": randint(1, 3),
        "price": 125,
        "preview_img_id": 58,
    },
    {
        "id": 59,
        "title": "KINTO COFFEE BREWER STAND SET",
        "description": "Slow down and enjoy the brew with this minimalist pour-over coffee set. $150.",
        "detailed_description": "Emphasizing simplicity and aesthetics, Kinto encourages users to slow down and enjoy the process. Their coffee brewer set elevates the morning ritual with a minimalist stainless steel stand and sleek porcelain brewer that are made to be displayed. Ideal for pour-overs, the heat‐resistant glass carafe can hold two cups and is microwave and dishwasher safe. The set also includes 20 cotton paper filters that produce an exceptional cup of coffee every time.",
        "category_id": 6,
        "owner_id": randint(1, 3),
        "price": 150,
        "preview_img_id": 59,
    },
    {
        "id": 60,
        "title": "NUDE FUMO CIGAR ASHTRAY",
        "description": "Capable of handling ash and small trinkets alike, this handmade ashtray is a worthwhile addition. $77.",
        "detailed_description": "Carved from solid crystalline glass, Nude's Fumo ashtray is equally suited to accommodating cigars or trinkets. It's made by hand, giving each piece an artisan look. The deep groove keeps favorite sticks from moving around, while the generous bowl keeps ash intact, avoiding the dreaded split.",
        "category_id": 6,
        "owner_id": randint(1, 3),
        "price": 77,
        "preview_img_id": 60,
    },
    {
        "id": 61,
        "title": "NUDE ALTRUIST CIGAR ASHTRAY",
        "description": "Designed to be placed between two chairs, this sleek ashtray has dual slots that face each other. $77.",
        "detailed_description": "A fine cigar can be an enjoyable indulgence. Even more so when the experience is shared. Nude's Altruist Cigar Ashtray is made to accommodate two sticks at once, making it perfect for dual chair, relaxed conversations. It's handmade from lead-free crystal with a refined circular shape, two placement grooves that face each other, and generous ash bowls.",
        "category_id": 6,
        "owner_id": randint(1, 3),
        "price": 77,
        "preview_img_id": 61,
    },
    {
        "id": 62,
        "title": "HEMSON STEALTH BLACK CLASSIC PIPE",
        "description": "Inspired by the pipes of generations past, this pipe combines a classic profile with a ceramic bowl. $90.",
        "detailed_description": "It looks like the kind of pipe your granddad (or maybe great-grandad) might have smoked. Yet this model from Hemson hides modern convenience. The American ash wood body is carved by hand into a timeless silhouette, but fitted with a removable glazed ceramic bowl and filter screen for easier cleaning and a more enjoyable smoke. The body undergoes a multi-step polishing, tinting, and waxing process that gives it a handsome, durable black finish that will develop a unique patina over time. Finished with a removable, co-injected acrylic/nylon mouthpiece.",
        "category_id": 6,
        "owner_id": randint(1, 3),
        "price": 90,
        "preview_img_id": 62,
    },
    {
        "id": 63,
        "title": "TRAVEL CIGAR HUMIDOR",
        "description": "A hygrometer built into the lid ensures the cigars in this travel humidor arrive in prime condition. $75.",
        "detailed_description": "Cigars need a certain amount of humidity — generally somewhere between 62 percent and 72 percent — to stay at their best. The lid-mounted hygrometer of this travel humidor lets you see at a glance the conditions inside. Able to hold between three and five cigars, depending on ring gauge, its exterior has a silver checkered pattern at the top that provides an eye-catching transition from the black base to the aforementioned silver lid.",
        "category_id": 6,
        "owner_id": randint(1, 3),
        "price": 75,
        "preview_img_id": 63,
    },
    {
        "id": 64,
        "title": "CARBON FIBER CIGAR TUBE",
        "description": "Like a high-end wallet or case, this tube carries a single  cigar in carbon fiber-wrapped luxury. $75.",
        "detailed_description": "A fine cigar deserves better than being hauled around in a plastic wrapper, or worse, yet, nothing at all. Made from stainless steel with a black carbon fiber finish, this is an upscale carry option.",
        "category_id": 6,
        "owner_id": randint(1, 3),
        "price": 75,
        "preview_img_id": 64,
    },
    {
        "id": 65,
        "title": "CARBON FIBER HUMIDOR",
        "description": "Protect a small supply of your best sticks in style with this carbon fiber-covered humidor. $225.",
        "detailed_description": "Well-curated cigar collections deserve equally well-considered storage. While not sized to house a full collection, this model certainly looks the part. It's made from wood with and given a veneer of carbon fiber, with a checkered weave pattern on the base and a high gloss black finish on the top. A hygrometer and humidifying sponge are included for keeping ideal interior conditions, and the size is just right for use in a vehicle or as part of your gear for an extended trip.",
        "category_id": 6,
        "owner_id": randint(1, 3),
        "price": 225,
        "preview_img_id": 65,
    },
    {
        "id": 66,
        "title": "HERBAL GOODS PRE-ROLLED SMOKING CONES",
        "description": "100% natural, these cones offer the smooth burn of a pre-roll with the familiarity of personal flower. $25.",
        "detailed_description": "Enjoy the smooth, slow burn of a pre-roll with your leaf of choice by packing it into one of Herbal Goods' all natural Smoking Cones. Rolled and tied by hand without the use of additives, glues, or toxins, they're made using a natural corn husk filter and ebony leaves. Five 3/4 gram cones come in each box, individually packaged in a flat-bottom, air-tight glass vile with cork top.",
        "category_id": 6,
        "owner_id": randint(1, 3),
        "price": 25,
        "preview_img_id": 66,
    },
]

products_vices_imgs = [
    {
        "id": 56,
        "product_id": 56,
        "url": "https://uncrate.com/assets_c/2022/11/military-edition-humidor-1-thumb-960xauto-154713.jpg",
    },
    {
        "id": 57,
        "product_id": 57,
        "url": "https://uncrate.com/assets_c/2020/11/sail-away-box-cold-brew-1-thumb-960xauto-123343.jpg",
    },
    {
        "id": 58,
        "product_id": 58,
        "url": "https://uncrate.com/assets_c/2022/11/alessi-ashtray-1-thumb-960xauto-154382.jpg",
    },
    {
        "id": 59,
        "product_id": 59,
        "url": "https://uncrate.com/assets_c/2021/02/kinto-coffee-filter-set-1-thumb-960xauto-126993.jpg",
    },
    {
        "id": 60,
        "product_id": 60,
        "url": "https://uncrate.com/assets_c/2022/10/nude-cigar-tray-single-clear-glass-5-thumb-960xauto-152668.jpg",
    },
    {
        "id": 61,
        "product_id": 61,
        "url": "https://uncrate.com/assets_c/2022/10/nude-glass-black-double-cigar-tray-2-thumb-960xauto-152620.jpg",
    },
    {
        "id": 62,
        "product_id": 62,
        "url": "https://uncrate.com/assets_c/2022/01/hemson-black-pipe-2-thumb-960xauto-142902.jpg",
    },
    {
        "id": 63,
        "product_id": 63,
        "url": "https://uncrate.com/assets_c/2022/03/brouk-and-co-humidor-canister-1-thumb-960xauto-144274.jpg",
    },
    {
        "id": 64,
        "product_id": 64,
        "url": "https://uncrate.com/assets_c/2022/03/brouk-and-co-single-humidor-1-thumb-960xauto-144175.jpg",
    },
    {
        "id": 65,
        "product_id": 65,
        "url": "https://uncrate.com/assets_c/2022/03/broku-co-cf-humidor-1-thumb-960xauto-144141.jpg",
    },
    {
        "id": 66,
        "product_id": 66,
        "url": "https://uncrate.com/assets_c/2021/02/herbal-goods-new-packaging-3-thumb-960xauto-126935.jpg",
    },
    {
        "id": 309,
        "product_id": 56,
        "url": "https://uncrate.com/assets_c/2022/11/military-edition-humidor-8-thumb-960xauto-154720.jpg",
    },
    {
        "id": 310,
        "product_id": 56,
        "url": "https://uncrate.com/assets_c/2022/11/military-edition-humidor-3-thumb-960xauto-154715.jpg",
    },
    {
        "id": 311,
        "product_id": 56,
        "url": "https://uncrate.com/assets_c/2022/11/military-edition-humidor-2-thumb-960xauto-154714.jpg"
    },
    {
        "id": 312,
        "product_id": 56,
        "url": "https://uncrate.com/assets_c/2022/11/military-edition-humidor-5-thumb-960xauto-154717.jpg",
    },
    {
        "id": 313,
        "product_id": 56,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/klaro-humidor-black-9.jpg?v=1669060458"
    },
    {
        "id": 314,
        "product_id": 57,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/sail-away-box-cold-brew-9.jpg?v=1606152729"
    },
    {
        "id": 315,
        "product_id": 57,
        "url": "https://uncrate.com/assets_c/2020/11/sail-away-box-cold-brew-2-thumb-960xauto-123344.jpg"
    },
    {
        "id": 316,
        "product_id": 57,
        "url": "https://uncrate.com/assets_c/2020/11/sail-away-box-cold-brew-3-thumb-960xauto-123346.jpg"
    },
    {
        "id": 317,
        "product_id": 57,
        "url": "https://uncrate.com/assets_c/2020/11/sail-away-box-cold-brew-4-thumb-960xauto-123345.jpg"
    },
    {
        "id": 318,
        "product_id": 58,
        "url": "https://uncrate.com/assets_c/2022/11/alessi-ashtray-3-thumb-960xauto-154383.jpg",
    },
    {
        "id": 319,
        "product_id": 58,
        "url": "https://uncrate.com/assets_c/2022/11/alessi-ashtray-2-thumb-960xauto-154381.jpg",
    },
    {
        "id": 320,
        "product_id": 58,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/alessi-ashtray-4.jpg?v=1668529138"
    },
    {
        "id": 321,
        "product_id": 59,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/FI1i_eug.jpg?v=1612212484"
    },
    {
        "id": 322,
        "product_id": 59,
        "url": "https://uncrate.com/assets_c/2021/02/kinto-coffee-filter-set-2-thumb-960xauto-126996.jpg"
    },
    {
        "id": 323,
        "product_id": 59,
        "url": "https://uncrate.com/assets_c/2021/02/kinto-coffee-filter-set-3-thumb-960xauto-126994.jpg"
    },
    {
        "id": 324,
        "product_id": 59,
        "url": "https://uncrate.com/assets_c/2021/02/kinto-coffee-filter-set-4-thumb-960xauto-126995.jpg"
    },
    {
        "id": 325,
        "product_id": 59,
        "url": "https://uncrate.com/assets_c/2021/02/kinto-coffee-filter-set-5-thumb-960xauto-126997.jpg"
    },
    {
        "id": 326,
        "product_id": 60,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/nude-cigar-tray-single-clear-glass-21.jpg?v=1665409788"
    },
    {
        "id": 327,
        "product_id": 60,
        "url": "https://uncrate.com/assets_c/2022/10/nude-cigar-tray-single-clear-glass-1-thumb-960xauto-152671.jpg",
    },
    {
        "id": 328,
        "product_id": 60,
        "url": "https://uncrate.com/assets_c/2022/10/nude-cigar-tray-single-clear-glass-2-thumb-960xauto-152672.jpg",
    },
    {
        "id": 329,
        "product_id": 60,
        "url": "https://uncrate.com/assets_c/2022/10/nude-cigar-tray-single-clear-glass-3-thumb-960xauto-152674.jpg",
    },
    {
        "id": 330,
        "product_id": 60,
        "url": "https://uncrate.com/assets_c/2022/10/nude-cigar-tray-single-clear-glass-5-thumb-960xauto-152668.jpg"
    },

    {
        "id": 331,
        "product_id": 61,
        "url": "https://uncrate.com/assets_c/2022/10/cigar-lifestyle-shots-5-thumb-960xauto-152637.jpg"
    },
    {
        "id": 332,
        "product_id": 61,
        "url": "https://uncrate.com/assets_c/2022/10/nude-glass-black-double-cigar-tray-1-thumb-960xauto-152621.jpg",
    },
    {
        "id": 333,
        "product_id": 61,
        "url": "https://uncrate.com/assets_c/2022/10/nude-glass-black-double-cigar-tray-4-thumb-960xauto-152625.jpg",
    },
    {
        "id": 334,
        "product_id": 61,
        "url": "https://uncrate.com/assets_c/2022/10/nude-glass-black-double-cigar-tray-3-thumb-960xauto-152624.jpg",
    },
    {
        "id": 335,
        "product_id": 61,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/nude-glass-black-double-cigar-tray-21.jpg?v=1665409502"
    },

    {
        "id": 336,
        "product_id": 62,
        "url": "https://uncrate.com/assets_c/2022/01/hemson-black-pipe-3-thumb-960xauto-142903.jpg",
    },
    {
        "id": 337,
        "product_id": 62,
        "url": "https://uncrate.com/assets_c/2022/01/hemson-black-pipe-1-thumb-960xauto-142901.jpg",
    },
    {
        "id": 338,
        "product_id": 62,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/hemson-black-pipe-4.jpg?v=1643653839"
    },

    {
        "id": 339,
        "product_id": 63,
        "url": "https://uncrate.com/assets_c/2022/03/brouk-and-co-humidor-canister-3-thumb-960xauto-144276.jpg",
    },
    {
        "id": 340,
        "product_id": 63,
        "url": "https://uncrate.com/assets_c/2022/03/brouk-and-co-humidor-canister-2-thumb-960xauto-144275.jpg",
    },
    {
        "id": 341,
        "product_id": 63,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/brouk-and-co-humidor-canister-4.jpg?v=1646684172"
    },

    {
        "id": 342,
        "product_id": 64,
        "url": "https://uncrate.com/assets_c/2022/03/brouk-and-co-single-humidor-2-thumb-960xauto-144176.jpg",
    },
    {
        "id": 343,
        "product_id": 64,
        "url": "https://uncrate.com/assets_c/2022/03/brouk-and-co-single-humidor-3-thumb-960xauto-144177.jpg",
    },
    {
        "id": 344,
        "product_id": 64,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/brouk-and-co-single-humidor-4.jpg?v=1646683821"
    },

    {
        "id": 345,
        "product_id": 65,
        "url": "https://uncrate.com/assets_c/2022/03/broku-co-cf-humidor-3-thumb-960xauto-144142.jpg",
    },
    {
        "id": 346,
        "product_id": 65,
        "url": "https://uncrate.com/assets_c/2022/03/broku-co-cf-humidor-4-thumb-960xauto-144143.jpg",
    },
    {
        "id": 347,
        "product_id": 65,
        "url": "https://uncrate.com/assets_c/2022/03/broku-co-cf-humidor-5-thumb-960xauto-144144.jpg",
    },
    {
        "id": 348,
        "product_id": 65,
        "url": "https://uncrate.com/assets_c/2022/03/broku-co-cf-humidor-6-thumb-960xauto-144145.jpg",
    },
    {
        "id": 349,
        "product_id": 65,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/broku-co-cf-humidor-7.jpg?v=1646677267"
    },
    {
        "id": 350,
        "product_id": 66,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/herbal-goods-ebony-leaf-5.jpg?v=1612206163"
    },
    {
        "id": 351,
        "product_id": 66,
        "url": "https://uncrate.com/assets_c/2020/02/herbal-goods-ebony-leaf-3-thumb-960xauto-111647.jpg"
    },
    {
        "id": 352,
        "product_id": 66,
        "url": "https://uncrate.com/assets_c/2020/02/herbal-goods-ebony-leaf-1-thumb-960xauto-111645.jpg"
    },
    {
        "id": 353,
        "product_id": 66,
        "url": "https://uncrate.com/assets_c/2021/02/herbal-goods-new-packaging-1-thumb-960xauto-126933.jpg"
    },
    {
        "id": 354,
        "product_id": 66,
        "url": "https://uncrate.com/assets_c/2021/02/herbal-goods-new-packaging-2-thumb-960xauto-126934.jpg"
    },

]
