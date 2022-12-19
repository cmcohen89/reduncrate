from random import randint

products_style = [
    {
        "id": 12,
        "title": "HOLDEN DOWN CREW SWEATER",
        "description": "The classic crewneck sweater gets a winter-weather upgrade. $390.",
        "detailed_description": "Holden reimagines the crew neck with puffer-style details to create a performance hybrid. The Down Grew Sweater features a classic silhouette cut from Polartec Powerstretch Pro for warmth and mobility during winter activities. For a cold-weather upgrade, its core is crafted from color-contrasting 7D Japanese nylon and insulated with responsibly sourced 600-fill power down. A side zipper makes for easy on and off, while a water-repellent coating protects from rain and snow.",
        "category_id": 2,
        "owner_id": randint(1, 3),
        "price": 390,
        "preview_img_id": 12,
    },
    {
        "id": 13,
        "title": "HOLDEN KNIT HOODIE",
        "description": "Superfine Italian wool elevates this streetwear staple. $450.",
        "detailed_description": "With its moisture-wicking and temperature-regulating properties, wool is a natural performance material. This and its luxe feel make it a perfect choice for the Holden Knit Hoodie. Handmade in Italy, the pullover is crafted from 100% \superfine traceable wool offering an elevated take on the loungewear staple. It's cut with a modern silhouette and finished with rib cuffs and hem and an adjustable hood. Tonal branding across the back shoulder completes the look.",
        "category_id": 2,
        "owner_id": randint(1, 3),
        "price": 450,
        "preview_img_id": 13,
    },
    {
        "id": 14,
        "title": "ROUGE TERRITORY TAN WAX PATROL SHIRT",
        "description": "Crafted from USA-made waxed cotton canvas, this shirt pulls double-duty as a light outer layer. $295.",
        "detailed_description": "Landing somewhere between a shirt, shacket, and raincoat, the Tan Wax Patrol Shirt from Rogue Territory is a versatile garment. It's crafted using USA-made 7oz waxed sail cloth 100% cotton canvas that provides some protection against the elements, its relaxed cut fits easily over tees and other base layers, and its lower front welt pockets give it jacket-like utility. The front also has two large chest pockets and antique brass snaps down the center, with large elbow patches finishing off the utilitarian look. Handmade in downtown Los Angeles.",
        "category_id": 2,
        "owner_id": randint(1, 3),
        "price": 295,
        "preview_img_id": 14,
    },
    {
        "id": 15,
        "title": "BAD BIRDIE ARIZONA NIGHTS GOLF POLO",
        "description": "Inspired by the nighttime skies above the Arizona desert, this polo is designed for daytime wear. $72.",
        "detailed_description": "Inspired by the clear nighttime skies above the Arizona desert, this polo from Bad Birdie is designed for on-course daytime wear. It's made with a moisture-wicking poly/spandex blend imbued with swing-friendly 4-way stretch, odor-fighting properties, wrinkle resistance, and SPF 50 protection from harmful UV rays. It's finished with a stay-right collar and Bad Birdie branding on the placket and sleeve.",
        "category_id": 2,
        "owner_id": randint(1, 3),
        "price": 72,
        "preview_img_id": 15,
    },
    {
        "id": 16,
        "title": "BARBOUR BEACONSFIELD JACKET",
        "description": "A workhorse of a jacket, the Barbour Beaconsfield is inspired by legacy hunting coats. $650.",
        "detailed_description": "Inspired by Barbour's history of producing upland bird hunting jackets, but updated and refined to a more modern fabrication and cut, the Beaconsfield jacket is a workhouse of a jacket. A detachable hood ensures you're covered in a bit of rain. Large bellowed pockets provide a wealth of storage while side hand slot pockets provide a place for your hands when needed, but away from the clutter of what's needing to be stored in the bellowed pockets. Speaking of pockets and storage, there are rear zipper pockets (yes, actually on the back of the jacket) for additional space. While those rear pockets are inspired by the game pockets on legacy hunting jackets used to store dead birds, you can make the call on what to put in them. The cotton/poly blend outer provides water resistance and the Thermore insulation provides just the right amount of warmth when the weather calls for a medium-heavy jacket.",
        "category_id": 2,
        "owner_id": randint(1, 3),
        "price": 650,
        "preview_img_id": 16,
    },
    {
        "id": 17,
        "title": "NAVAL WATCH CO. FRXC001 CHRONOGRAPH WATCH",
        "description": "Billed as an \"urban military watch\", the FRXC001 has straightforward looks and a reverse panda dial. $250.",
        "detailed_description": "Yoshikage Kajiwara, creative director of Lowercase, decided to work with Naval Watch Co. on an \"urban military watch\". The FRXC001 Chronograph is the result. It draws inspiration from British Air Force 6BB specification timepieces of the 1970s but adds a subdial to the mix for a total of three. The reverse panda dial is also home to LumiNova-painted indexes and hands and sits within a 42mm 316L stainless steel beneath an acrylic dome crystal. Powered by a reliable Japan-built Seiko Cal. VK63 quartz movement, it sits on a 20mm black nylon NATO strap.",
        "category_id": 2,
        "owner_id": randint(1, 3),
        "price": 250,
        "preview_img_id": 17,
    },
    {
        "id": 18,
        "title": "REGINING CHAMP CABIN FLEECE ROBE",
        "description": "Triple layer fleece and boxing-inspired details elevate this loungewear staple. $220.",
        "detailed_description": "Reigning Champ gives its signature boxing robe a cozy update. Built for downtime, they've handcrafted the Cabin Fleece Robe from custom triple-layer fleece with a quilted lining for lightweight warmth. A three-piece hood, front patch pockets, rib cuffs, and a self-fabric waist belt complete the athletic-inspired details. Made in Canada.",
        "category_id": 2,
        "owner_id": randint(1, 3),
        "price": 220,
        "preview_img_id": 18,
    },
    {
        "id": 19,
        "title": "TAYLOR STITCH BLACK SELVEDGE LONG HAUL JACKET",
        "description": "Rugged selvedge denim and a vintage finished elevate the classic outerwear staple. $228.",
        "detailed_description": "A timeless classic, a denim jacket is a wardrobe stable. Taylor Stich delivers a quality option with its Black Selvedge Long Haul Jacket. It's crafted from hard-wearing 13-ounce organic selvage denim giving the piece rugged structure and durability, and it's pre-washed for a worn-in vintage look. The traditional design is enhanced with details to support everyday wear, including pockets, a pen slot, and a stand-up collar.",
        "category_id": 2,
        "owner_id": randint(1, 3),
        "price": 228,
        "preview_img_id": 19,
    },
    {
        "id": 20,
        "title": "TIMEX Q GMT WATCH",
        "description": "Combining classic looks and size with a useful complication, this is an affordable way to get a GMT. $219.",
        "detailed_description": "Since their invention, GMT watches have been linked to travelers — and traveling across time zones normally requires a significant sum of money. As do the complications required to keep track of time in two places at once. Timex is democratizing the feature with its Q GMT. Powered by a Swiss-made GMT movement, it has classic looks, with a 38mm stainless steel case, matching bracelet, black face, and \"Batman\" black and blue rotating bezel. Based on the 1979 Reissue, it also has a domed acrylic crystal, red-tipped GMT hand, a date window at 3 o'clock, and is water-resistant to 50 meters.",
        "category_id": 2,
        "owner_id": randint(1, 3),
        "price": 219,
        "preview_img_id": 20,
    },
    {
        "id": 21,
        "title": "HARD GRAFT ALPINE DUCK BOOTS",
        "description": "Modernized duck boot presents the classic silhouette with a tonal upper and chunky sole. $515.",
        "detailed_description": "Hard Graft updates a winter classic for modern wear. Made in Italy, The Alpine Duck Boots reimagine the timeless silhouette with a black vegetable-tanned leather upper and tonal rubberized calfskin detailing for protection from the elements. A lining made from Italian wool shearling wraps feet in warmth, while a robust Vibram lug outsole keeps feet steady on snow-covered streets. They're finished with tan laces, a reinforced toe kick, and artisanal cement construction.",
        "category_id": 2,
        "owner_id": randint(1, 3),
        "price": 515,
        "preview_img_id": 21,
    },
    {
        "id": 22,
        "title": "HOLDEN MERINO WOOL BALACLAVA",
        "description": "Keep your head and face covered and warm this winter with this merino wool balaclava. $150.",
        "detailed_description": "Made from a 90% merino wool and nylon blend, this balaclava keeps your head and neck covered while wicking away moisture on the coldest days. Perforations around the mouth allow for easy breathing. Made from sustainably sourced materials. Available in Carbon Blue and Stone Green.",
        "category_id": 2,
        "owner_id": randint(1, 3),
        "price": 150,
        "preview_img_id": 22,
    },
]


products_style_imgs = [
    {
        'id': 12,
        'product_id': 12,
        'url': "https://uncrate.com/assets_c/2022/12/holden-outerwear-crew-sweatshirt-slate-grey-1-thumb-960xauto-155705.jpg"
    },
    {
        'id': 13,
        'product_id': 13,
        'url': "https://uncrate.com/assets_c/2022/12/holden-knit-hoodie-grey-1-thumb-960xauto-155717.jpg"
    },
    {
        'id': 14,
        'product_id': 14,
        'url': "https://uncrate.com/assets_c/2022/12/rgt-waxed-shirt-jacket-tan-21-thumb-960xauto-155669.jpg"
    },
    {
        'id': 15,
        'product_id': 15,
        'url': "https://uncrate.com/assets_c/2022/12/bad-birdie-arizona-nights-1-thumb-960xauto-155635.jpg"
    },
    {
        'id': 16,
        'product_id': 16,
        'url': "https://uncrate.com/assets_c/2022/11/barbour-beaconsfield-jacket-olive-4-thumb-960xauto-153955.jpg"
    },
    {
        'id': 17,
        'product_id': 17,
        'url': "https://uncrate.com/assets_c/2022/12/naval-watch-chrono-black-1-thumb-960xauto-155519.jpg"
    },
    {
        'id': 18,
        'product_id': 18,
        'url': "https://uncrate.com/assets_c/2022/12/reigning-champ-cabin-fleece-hooded-robe-black-1-thumb-960xauto-155469.jpg"
    },
    {
        'id': 19,
        'product_id': 19,
        'url': "https://uncrate.com/assets_c/2022/12/taylor-stitch-black-wash-long-haul-jacket-4-thumb-960xauto-155433.jpg"
    },
    {
        'id': 20,
        'product_id': 20,
        'url': "https://uncrate.com/assets_c/2022/04/timex-batman-gmt-1-thumb-960xauto-146128.jpg"
    },
    {
        'id': 21,
        'product_id': 21,
        'url': "https://uncrate.com/assets_c/2022/12/hardgraft-alpine-duck-boot-1-thumb-960xauto-155398.jpg"
    },
    {
        'id': 22,
        'product_id': 22,
        'url': "https://uncrate.com/assets_c/2022/12/holden-balaclava-blue-1-thumb-960xauto-155245.jpg"
    },
    {
        "id": 129,
        "product_id": 12,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/holden-outerwear-crew-sweatshirt-black-4.jpg?v=1671218935"
    },
    {
        "id": 130,
        "product_id": 12,
        "url": "https://uncrate.com/assets_c/2022/12/holden-outerwear-crew-sweatshirt-black-1-thumb-960xauto-155708.jpg"
    },
    {
        "id": 131,
        "product_id": 12,
        "url": "https://uncrate.com/assets_c/2022/12/holden-outerwear-crew-sweatshirt-slate-grey-2-thumb-960xauto-155704.jpg"
    },
    {
        "id": 132,
        "product_id": 12,
        "url": "https://uncrate.com/assets_c/2022/12/holden-outerwear-crew-sweatshirt-slate-grey-3-thumb-960xauto-155706.jpg"
    },
    {
        "id": 133,
        "product_id": 12,
        "url": "https://uncrate.com/assets_c/2022/12/holden-outerwear-crew-sweatshirt-black-2-thumb-960xauto-155707.jpg"
    },
    {
        "id": 134,
        "product_id": 13,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/holden-wool-knit-hoodie-stone-green-5.jpg?v=1671225413"
    },
    {
        "id": 135,
        "product_id": 13,
        "url": "https://uncrate.com/assets_c/2022/12/holden-wool-knit-hoodie-stone-green-1-thumb-960xauto-155721.jpg"
    },
    {
        "id": 136,
        "product_id": 13,
        "url": "https://uncrate.com/assets_c/2022/12/holden-wool-knit-hoodie-stone-green-2-thumb-960xauto-155722.jpg"
    },
    {
        "id": 137,
        "product_id": 13,
        "url": "https://uncrate.com/assets_c/2022/12/holden-wool-knit-hoodie-stone-green-3-thumb-960xauto-155723.jpg"
    },
    {
        "id": 138,
        "product_id": 13,
        "url": "https://uncrate.com/assets_c/2022/12/holden-wool-knit-hoodie-stone-green-4-thumb-960xauto-155724.jpg"
    },
    {
        "id": 139,
        "product_id": 14,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/rgt-waxed-shirt-jacket-tan-4.jpg?v=1671201367"
    },
    {
        "id": 140,
        "product_id": 14,
        "url": "https://uncrate.com/assets_c/2022/12/rgt-waxed-shirt-jacket-tan-5-thumb-960xauto-155668.jpg"
    },
    {
        "id": 141,
        "product_id": 14,
        "url": "https://uncrate.com/assets_c/2022/12/rgt-waxed-shirt-jacket-tan-1-thumb-960xauto-155663.jpg"
    },
    {
        "id": 142,
        "product_id": 14,
        "url": "https://uncrate.com/assets_c/2022/12/rgt-waxed-shirt-jacket-tan-2-thumb-960xauto-155664.jpg"
    },
    {
        "id": 143,
        "product_id": 14,
        "url": "https://uncrate.com/assets_c/2022/12/rgt-waxed-shirt-jacket-tan-3-thumb-960xauto-155665.jpg"
    },
    {
        "id": 144,
        "product_id": 15,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/bad-birdie-arizona-nights-5.jpg?v=1671137417"
    },
    {
        "id": 145,
        "product_id": 15,
        "url": "https://uncrate.com/assets_c/2022/12/bad-birdie-arizona-nights-2-thumb-960xauto-155636.jpg"
    },
    {
        "id": 146,
        "product_id": 15,
        "url": "https://uncrate.com/assets_c/2022/12/bad-birdie-arizona-nights-3-thumb-960xauto-155637.jpg"
    },
    {
        "id": 147,
        "product_id": 15,
        "url": "https://uncrate.com/assets_c/2022/12/bad-birdie-arizona-nights-4-thumb-960xauto-155638.jpg"
    },
    {
        "id": 148,
        "product_id": 16,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/barbour-beaconsfield-jacket-olive-6.jpg?v=1667838356"
    },
    {
        "id": 149,
        "product_id": 16,
        "url": "https://uncrate.com/assets_c/2022/11/barbour-beaconsfield-jacket-olive-5-thumb-960xauto-153956.jpg"
    },
    {
        "id": 150,
        "product_id": 16,
        "url": "https://uncrate.com/assets_c/2022/11/barbour-beaconsfield-jacket-olive-1-thumb-960xauto-153952.jpg"
    },
    {
        "id": 151,
        "product_id": 16,
        "url": "https://uncrate.com/assets_c/2022/11/barbour-beaconsfield-jacket-olive-2-thumb-960xauto-153953.jpg"
    },
    {
        "id": 152,
        "product_id": 16,
        "url": "https://uncrate.com/assets_c/2022/11/barbour-beaconsfield-jacket-olive-3-thumb-960xauto-153954.jpg"
    },
    {
        "id": 153,
        "product_id": 17,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/naval-watch-chrono-black-6.jpg?v=1670879939"
    },
    {
        "id": 154,
        "product_id": 17,
        "url": "https://uncrate.com/assets_c/2022/12/naval-watch-chrono-black-2-thumb-960xauto-155520.jpg"
    },
    {
        "id": 155,
        "product_id": 17,
        "url": "https://uncrate.com/assets_c/2022/12/naval-watch-chrono-black-3-thumb-960xauto-155521.jpg"
    },
    {
        "id": 156,
        "product_id": 17,
        "url": "https://uncrate.com/assets_c/2022/12/naval-watch-chrono-black-4-thumb-960xauto-155522.jpg"
    },
    {
        "id": 157,
        "product_id": 17,
        "url": "https://uncrate.com/assets_c/2022/12/naval-watch-chrono-black-5-thumb-960xauto-155523.jpg"
    },
    {
        "id": 158,
        "product_id": 18,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/reigning-champ-cabin-fleece-hooded-robe-black-6.jpg?v=1670712967"
    },
    {
        "id": 159,
        "product_id": 18,
        "url": "https://uncrate.com/assets_c/2022/12/reigning-champ-cabin-fleece-hooded-robe-black-2-thumb-960xauto-155470.jpg"
    },
    {
        "id": 160,
        "product_id": 18,
        "url": "https://uncrate.com/assets_c/2022/12/reigning-champ-cabin-fleece-hooded-robe-black-3-thumb-960xauto-155471.jpg"
    },
    {
        "id": 161,
        "product_id": 18,
        "url": "https://uncrate.com/assets_c/2022/12/reigning-champ-cabin-fleece-hooded-robe-black-4-thumb-960xauto-155472.jpg"
    },
    {
        "id": 162,
        "product_id": 18,
        "url": "https://uncrate.com/assets_c/2022/12/reigning-champ-cabin-fleece-hooded-robe-black-5-thumb-960xauto-155473.jpg"
    },
    {
        "id": 163,
        "product_id": 19,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/taylor-stitch-black-wash-long-haul-jacket-7.jpg?v=1670619893"
    },
    {
        "id": 164,
        "product_id": 19,
        "url": "https://uncrate.com/assets_c/2022/12/taylor-stitch-black-wash-long-haul-jacket-5-thumb-960xauto-155437.jpg"
    },
    {
        "id": 165,
        "product_id": 19,
        "url": "https://uncrate.com/assets_c/2022/12/taylor-stitch-black-wash-long-haul-jacket-1-thumb-960xauto-155431.jpg"
    },
    {
        "id": 166,
        "product_id": 19,
        "url": "https://uncrate.com/assets_c/2022/12/taylor-stitch-black-wash-long-haul-jacket-6-thumb-960xauto-155436.jpg"
    },
    {
        "id": 167,
        "product_id": 19,
        "url": "https://uncrate.com/assets_c/2022/12/taylor-stitch-black-wash-long-haul-jacket-2-thumb-960xauto-155432.jpg"
    },
    {
        "id": 168,
        "product_id": 20,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/timex-batman-gmt-5.jpg?v=1651171540"
    },
    {
        "id": 169,
        "product_id": 20,
        "url": "https://uncrate.com/assets_c/2022/04/timex-batman-gmt-2-thumb-960xauto-146129.jpg"
    },
    {
        "id": 170,
        "product_id": 20,
        "url": "https://uncrate.com/assets_c/2022/04/timex-batman-gmt-3-thumb-960xauto-146130.jpg"
    },
    {
        "id": 171,
        "product_id": 20,
        "url": "https://uncrate.com/assets_c/2022/04/timex-batman-gmt-3-thumb-960xauto-146130.jpg"
    },
    {
        "id": 172,
        "product_id": 20,
        "url": "https://uncrate.com/assets_c/2022/04/timex-batman-gmt-4-thumb-960xauto-146131.jpg"
    },
    {
        "id": 173,
        "product_id": 21,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/hardgraft-alpine-duck-boot-6.jpg?v=1670611454"
    },
    {
        "id": 174,
        "product_id": 21,
        "url": "https://uncrate.com/assets_c/2022/12/hardgraft-alpine-duck-boot-5-thumb-960xauto-155402.jpg"
    },
    {
        "id": 175,
        "product_id": 21,
        "url": "https://uncrate.com/assets_c/2022/12/hardgraft-alpine-duck-boot-4-thumb-960xauto-155401.jpg"
    },
    {
        "id": 176,
        "product_id": 21,
        "url": "https://uncrate.com/assets_c/2022/12/hardgraft-alpine-duck-boot-2-thumb-960xauto-155399.jpg"
    },
    {
        "id": 177,
        "product_id": 21,
        "url": "https://uncrate.com/assets_c/2022/12/hardgraft-alpine-duck-boot-3-thumb-960xauto-155400.jpg"
    },
    {
        "id": 178,
        "product_id": 22,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/holden-balaclava-blue-3.jpg?v=1670255507"
    },
    {
        "id": 179,
        "product_id": 22,
        "url": "https://uncrate.com/assets_c/2022/12/holden-balaclava-blue-2-thumb-960xauto-155246.jpg"
    },
    {
        "id": 180,
        "product_id": 22,
        "url": "https://uncrate.com/assets_c/2022/12/holden-balaclava-stone-green-1-thumb-960xauto-155247.jpg"
    },
    {
        "id": 181,
        "product_id": 22,
        "url": "https://uncrate.com/assets_c/2022/12/holden-balaclava-stone-green-2-thumb-960xauto-155248.jpg"
    },
]
#     {
#         'id': 120,
#         'product_id': 12,
#         'url': "https://uncrate.com/assets_c/2022/11/rze-orange-thumb-960xauto-153706.jpg"
#     },
#     {
#         'id': 121,
#         'product_id': 12,
#         'url': "https://uncrate.com/assets_c/2022/11/rze-white-thumb-960xauto-153707.jpg"
#     },
#     {
#         'id': 122,
#         'product_id': 12,
#         'url': "https://uncrate.com/assets_c/2022/11/rze-black-thumb-960xauto-153708.jpg"
#     },
#     {
#         'id': 123,
#         'product_id': 12,
#         'url': "https://uncrate.com/assets_c/2022/11/rze-green-thumb-960xauto-153709.jpg"
#     },
#     {
#         'id': 127,
#         'product_id': 14,
#         'url': "https://uncrate.com/assets_c/2022/12/sunspel-fleeceback-sweatpants-white-melange-3-thumb-960xauto-155259.jpg"
#     },
#     {
#         'id': 128,
#         'product_id': 14,
#         'url': "https://uncrate.com/assets_c/2022/12/sunspel-fleeceback-sweatpants-white-melange-1a-thumb-960xauto-155257.jpg"
#     },
#     {
#         'id': 131,
#         'product_id': 16,
#         'url': "https://uncrate.com/assets_c/2022/12/holden-puffy-slides-black-2-thumb-960xauto-155216.jpg"
#     },
#     {
#         'id': 132,
#         'product_id': 16,
#         'url': "https://uncrate.com/assets_c/2022/12/holden-puffy-slides-black-3-thumb-960xauto-155218.jpg"
#     },
#     {
#         'id': 134,
#         'product_id': 17,
#         'url': "https://uncrate.com/assets_c/2022/12/filling-pieces-hightop-sneakers-2-thumb-960xauto-155191.jpg"
#     },
#     {
#         'id': 135,
#         'product_id': 17,
#         'url': "https://uncrate.com/assets_c/2022/12/filling-pieces-hightop-sneakers-3-thumb-960xauto-155193.jpg"
#     },
#     {
#         'id': 136,
#         'product_id': 17,
#         'url': "https://uncrate.com/assets_c/2022/12/filling-pieces-hightop-sneakers-4-thumb-960xauto-155192.jpg"
#     },
#     {
#         'id': 137,
#         'product_id': 17,
#         'url': "https://uncrate.com/assets_c/2022/12/filling-pieces-hightop-sneakers-5-thumb-960xauto-155194.jpg"
#     },
#     {
#         'id': 139,
#         'product_id': 18,
#         'url': "https://uncrate.com/assets_c/2022/10/faherty-black-sweater-shirt-21-thumb-960xauto-153443.jpg"
#     },
#     {
#         'id': 140,
#         'product_id': 18,
#         'url': "https://uncrate.com/assets_c/2022/10/faherty-black-sweater-shirt-24-thumb-960xauto-153422.jpg"
#     },
#     {
#         'id': 143,
#         'product_id': 20,
#         'url': "https://uncrate.com/assets_c/2022/12/new-balance-974h-hikers-2-thumb-960xauto-155097.jpg"
#     },
#     {
#         'id': 144,
#         'product_id': 20,
#         'url': "https://uncrate.com/assets_c/2022/12/new-balance-974h-hikers-3-thumb-960xauto-155099.jpg"
#     },
#     {
#         'id': 145,
#         'product_id': 20,
#         'url': "https://uncrate.com/assets_c/2022/12/new-balance-974h-hikers-4-thumb-960xauto-155100.jpg"
#     },
#     {
#         'id': 146,
#         'product_id': 20,
#         'url': "https://uncrate.com/assets_c/2022/12/new-balance-974h-hikers-5-thumb-960xauto-155101.jpg"
#     },
#     {
#         'id': 148,
#         'product_id': 21,
#         'url': "https://uncrate.com/assets_c/2021/11/onsen-bath-robe-2-thumb-960xauto-140167.jpg"
#     },
#     {
#         'id': 149,
#         'product_id': 21,
#         'url': "https://uncrate.com/assets_c/2021/11/onsen-bath-robe-3-thumb-960xauto-140168.jpg"
#     },
#     {
#         'id': 151,
#         'product_id': 22,
#         'url': "https://uncrate.com/assets_c/2020/11/reigning-champ-terry-joggers-5-thumb-960xauto-124676.jpg"
#     },
#     {
#         'id': 152,
#         'product_id': 22,
#         'url': "https://uncrate.com/assets_c/2020/11/reigning-champ-terry-joggers-2-thumb-960xauto-124674.jpg"
#     },
#     {
#         'id': 153,
#         'product_id': 22,
#         'url': "https://uncrate.com/assets_c/2020/11/reigning-champ-terry-joggers-4-thumb-960xauto-124677.jpg"
#     },
# ]
