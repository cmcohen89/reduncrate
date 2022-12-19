from random import randint

products_cars = [
    {
        "id": 23,
        "title": "CAKE MAKKA FLEX ELECTRIC COMMUTER BIKE",
        "description": "Mopeds are ideal short-haul urban commute vehicles... $4,470.",
        "detailed_description": "Mopeds are ideal short-haul urban commute vehicles. While ICE-powered models are easy on gas, they still noisily spew emissions. That's not a problem for Cake's all-electric Makka Flex. Its powerful motor has a top speed of 28 mph and a range of 34 miles — plenty for in-town trips — while the proprietary suspension system and all-weather tires can handle both pothole-riddled streets and the occasional off-road adventure. A host of accessories let it adapt to many different uses, a built-in electronic braking system helps recharge the battery when slowing down. Since it's removable, it can easily be carried inside for a quick top-off.",
        "category_id": 3,
        "owner_id": randint(1, 3),
        "price": 4470,
        "preview_img_id": 23,
    },
    {
        "id": 24,
        "title": "CAKE KALK INK & STREET LEGAL ELECTRIC BIKE",
        "description": "Cake takes its trail-ready model to the pavement with this road-legal version of the Kalk INK. $12,580.",
        "detailed_description": "Rugged enough for the trail yet refined enough for the road, Cake's Kalk INK& e-Bike is here to transform your commute and time off. It's powered by an electric powertrain with a lithium battery and a powerful motor to deliver instant torque and a top speed of 56 mph. The proprietary suspension system has a direct mount rear chock and spring front fork with 200mm of travel, which handle both potholes and bumpy paths with aplomb. Up front is a digital dashboard that provides essential info like speed and battery life and access to the three braking and ride modes. It sits on custom-designed 19\" motorcycle rims and dual sport motorcycle tires, which transition effortlessly from city streets to backcountry trails. And as a road-legal model, it has all the necessary lights, indicators, and mirrors, and can be registered as a 125cc equivalent in the EU and USA.",
        "category_id": 3,
        "owner_id": randint(1, 3),
        "price": 12580,
        "preview_img_id": 24,
    },
    {
        "id": 25,
        "title": "MOONBIKES X UNCRATE ELECTRIC SNOWMOBILE",
        "description": "Everything is going electric, and that now extends to snowmobiles. We've partnered with the pioneer of the electric snow sports industry, MoonBikes...$10,900.",
        "detailed_description": "Everything is going electric, and that now extends to snowmobiles. We've partnered with the pioneer of the electric snow sports industry, MoonBikes, to offer their standard electric snowmobile in murdered-out fashion, and the result is something that could easily be pulled straight off the set of a Bond film action sequence. Nearly entirely black with subtle, tonal branding, it offers the same specs as the standard model, including a top speed of 26 mph and the ability to handle powder up to 12 inches deep. The low center gravity and light weight — under 200 lbs with a single battery — make it extremely easy to ride, while the 28-inch width makes it easy to transport. It can run up to 1.5 hours with a single battery in temperatures as low as -13°F and is assembled in France by Bosch. In short, it's equally as capable in the French Alps as it is in the Rockies, or just cruising through a snow covered field.",
        "category_id": 3,
        "owner_id": randint(1, 3),
        "price": 10900,
        "preview_img_id": 25,
    },
    {
        "id": 26,
        "title": "MUSTANG MACH-E FIRST EDITION",
        "description": "When it was first revealed last year, the Mustang Mach-E First Edition was so popular that most consumers were unable to reserve a vehicle due to demand...$59,900.",
        "detailed_description": "When it was first revealed last year, the Mustang Mach-E First Edition was so popular that most consumers were unable to reserve a vehicle due to demand. To give Reduncrate readers a final shot at grabbing what will certainly become a highly sought-after trim level and first year-model edition of the all-electric Mustang, we've partnered with Ford to make a limited number of the Carbonized Gray First Edition available for order once again. Unique to Uncrate in Carbonized Gray, the First Edition trim-level is paired with red brake calipers, brushed aluminum pedal covers and \"First Edition\" scuff plates, as well as black onyx perforated ActiveX upholstery with unique ST-Red line accent stitching. As with all First Edition models, it will sport eAWD, 346-horsepower†, and a targeted EPA estimated range of 270 miles‡. If you missed out the first time, be sure to claim one for yourself by proceeding to the order page below, before this limited-edition model is gone forever.",
        "category_id": 3,
        "owner_id": randint(1, 3),
        "price": 59900,
        "preview_img_id": 26,
    },
    {
        "id": 27,
        "title": "CAKE KALK INK OFF-ROAD ELECTRIC BIKE",
        "description": "Cake's Kalk INK model provides the nimble handling and maneuverability of traditional options with a whisper-quiet electric powertrain... $11,580.",
        "detailed_description": "Dirt bikes are a great way to explore the wilderness, but ICE-powered models are typically quite loud, scaring away wildlife while releasing nature-killing emissions. Cake's Kalk INK model provides the nimble handling and maneuverability of traditional options with a whisper-quiet electric powertrain. Combining a premium lithium battery with a powerful motor, it provides instant torque and a top speed of 56 mph. It has a proprietary suspension system comprised of a direct mount rear chock and spring front fork with 200mm of travel to easily absorb the bumps inherent to uneven terrain, while custom designed 19\" motorcycle rims and dual sport motorcycle tires provide plenty of grip on all surfaces.",
        "category_id": 3,
        "owner_id": randint(1, 3),
        "price": 11580,
        "preview_img_id": 27,
    },
    {
        "id": 28,
        "title": "DROOG MOTO MINI-FIGHTER MOTORCYCLE",
        "description": "Droog Moto's angular, distinct designs are now available in a smaller package with the DM-018 Mini-Fighter... $25,000.",
        "detailed_description": "Droog Moto's angular, distinct designs are now available in a smaller package with the DM-018 Mini-Fighter. The reduced size doesn't mean Droog skimped on features, as engine choices range from 125cc to 190cc, with a custom intake, exhaust, and digital fuel injection. This makes for a top speed of at least 65 mph, with all engine parameters available in a compact digital instrument cluster. Styling takes Droog's unique vision and downscales it perfectly for the platform, with trademark cues like solid wheels and scrambler tires present. Each DM-018 is built to order with nearly any option on the table that the customer can think up. The final price will be determined by the upgrades and changes the customer selects; all modifications and upgrades are available post-purchase as each bike is built in collaboration with Droog.",
        "category_id": 3,
        "owner_id": randint(1, 3),
        "price": 25000,
        "preview_img_id": 28,
    },
    {
        "id": 29,
        "title": "DROOG MOTO E-FIGHTER ELECTRIC MOTORCYCLE",
        "description": "The instant torque provided by electric motors is exhilarating in a car, and even more so on two wheels...$32,500.",
        "detailed_description": "The instant torque provided by electric motors is exhilarating in a car, and even more so on two wheels. Propelled by a high-performance brushless motor producing up to 46 hp and 78 ft. lbs of peak torque, the Droog Moto E-Fighter is an all-electric screamer. Power is supplied by either a base modular 3.6-kilowatt-hour battery that can be swapped on the fly or a more permanent, optional 7.2 pack. Zero's 550 Amp high-efficiency controller handles distribution and enables regenerative braking, while also powering the LED head and tail lights, LED turn signals, and blue backlit digital speedometer. Each one is built to suit the buyer's needs and specs, which means the suspension setup is suited to matching their riding style, the seat height to their body dimensions, and even the tires, wheels — there's both a solid wheel and tubeless custom spoke options — and fork color can be customized. As such, the final price will be determined by the upgrades and changes the customer selects; all modifications and upgrades are available post-purchase as each bike is built in collaboration with Droog.",
        "category_id": 3,
        "owner_id": randint(1, 3),
        "price": 32500,
        "preview_img_id": 29,
    },
    {
        "id": 30,
        "title": "TARFORM X UNCRATE LUNA ELECTRIC MOTORCYCLE",
        "description": "After 5 years of development, Brooklyn-based Tarform is now ready to begin production of their first street-legal consumer models...$32,000.",
        "detailed_description": "After 5 years of development, Brooklyn-based Tarform is now ready to begin production of their first street-legal consumer models. The previous prototype Scrambler and the new Racer. For the launch of the first production run, we've partnered with Tarform to release the limited edition Tarform Luna Black. Limited to 20 examples available for made-to-order reservation in either the Racer (shown) or Scrambler model, the Luna Black is customized in an all-black color scheme, unique seat stitching pattern, custom display graphic animation, numbered Uncrate Edition engraving, and can be further customized by the owner after the reservation is placed. Each is built one-by-one by hand at the Tarfrom headquartered in the Brooklyn Navy Yard, of which you'll have a private visit to once your reservation is confirmed.",
        "category_id": 3,
        "owner_id": randint(1, 3),
        "price": 32000,
        "preview_img_id": 30,
    },
    {
        "id": 31,
        "title": "RONIN X UNCRATE 47 MOTORCYCLE",
        "description": "Designed by Reduncrate and built by Ronin, our collaboration includes two identical blacked-out motorcycles...$46,000.",
        "detailed_description": "Designed by Reduncrate and built by Ronin, our collaboration includes two identical blacked-out motorcycles. Offering a 160 MPH top speed and 130 rear-wheel HP, the limited Uncrate versions receive a satin black airbox cover and black paint on the front and rear main springs, front fork links, and subframe. Smoke gray was used to replace the taillight lens, the cast rearsets replaced with black anodized billet parts from vintage racers, the muffler endcaps repainted in black cerakote, and the entire exhaust wrapped with black header tape. As a finishing touch, the seat was reupholstered in black leather by Clint Wilkinson, giving this unique, limited bike a menacing look worthy of its fierce namesake. Each bike weighs in at 425 lbs. One of the two identical bikes is still available for purchase.",
        "category_id": 3,
        "owner_id": randint(1, 3),
        "price": 46000,
        "preview_img_id": 31,
    },
    {
        "id": 32,
        "title": "SUPER73 S2 SERIES ELECTRIC BIKE",
        "description": "Urban adventurers, take note: Super73's second-generation S2 e-Bike was built with you in mind...$2,445.",
        "detailed_description": "Urban adventurers, take note: Super73's second-generation S2 e-Bike was built with you in mind. The high-performance, street-legal machine has a sport cruiser-style design, with an aircraft-grade aluminum alloy frame, fully adjustable air spring suspension fork, and powerful motor. That 2000-watt brushless DC hub is attached to an advanced 960 watt-hour battery that lets it hit speeds up to 28 mph while also serving as a low-key pedal-assist system. A monochromatic LCD display keeps you updated on things like range and ride modes, while a Bluetooth connection with the companion iOS/Android app enables further functionality. It sits on 5\"-wide, all-terrain BDGR tires, has a two-person extended seat, and has a triple LED headlight as well as internal cable routing to maintain the sleek look. Also, note that pre-ordered bikes are being offered at a $500 discount and will return to the full price of $2,695 in late Spring 2020.",
        "category_id": 3,
        "owner_id": randint(1, 3),
        "price": 2445,
        "preview_img_id": 32,
    },
    {
        "id": 33,
        "title": "SUPER73 R SERIES ELECTRIC BIKE",
        "description": "Requiring no motorcycle license to ride and capable both on- and off-road Super73's R Series e-Bike offers the best of both worlds...$2,795.",
        "detailed_description": "Requiring no motorcycle license to ride and capable both on- and off-road Super73's R Series e-Bike offers the best of both worlds. Its aircraft-grade 6065/7071 aluminum alloy frame supports a best-in-class 960 watt-hour battery and an internally geared, 2000-watt brushless DC hub motor, a combination that's good for up to 40 miles of unassisted, 20mph biking, or up to 75 miles in pedal-assist mode. Three other riding modes are available, including an \"unlimited\" mode that can reach speeds over 28 mph. An inverted coil-spring fork and a rear Coilover mono-shock provide agile handling and a smooth ride, and its 5-inch-wide BDGR tires are the widest, most aggressive 20\" all-terrain fat tires available. Interaction with the bike's electronics is handled via a monochromatic LCD display and a Bluetooth connection that supports a companion iOS and Android app. It's finished with internal cable routing that keeps the minimal design looking clean and a cafe racer-style seat.",
        "category_id": 3,
        "owner_id": randint(1, 3),
        "price": 2795,
        "preview_img_id": 33,
    },
]


products_cars_imgs = [
    {
        "id": 23,
        "product_id": 23,
        "url": "https://uncrate.com/assets_c/2022/12/ridecake-makka-flex-white-1-thumb-960xauto-155478.jpg",
    },
    {
        "id": 24,
        "product_id": 24,
        "url": "https://uncrate.com/assets_c/2022/12/cake-inkand-road-bike-1-thumb-960xauto-155118.jpg",
    },
    {
        "id": 25,
        "product_id": 25,
        "url": "https://uncrate.com/assets_c/2021/08/packshot-uncrate-moonbike-1-thumb-960xauto-136228.jpg",
    },
    {
        "id": 26,
        "product_id": 26,
        "url": "https://uncrate.com/assets_c/2020/08/ford-mustang-mach-e-9-thumb-960xauto-119654.jpg",
    },
    {
        "id": 27,
        "product_id": 27,
        "url": "https://uncrate.com/assets_c/2022/11/ridecake-kalk-ink-bike-1-thumb-960xauto-154857.jpg",
    },
    {
        "id": 28,
        "product_id": 28,
        "url": "https://uncrate.com/assets_c/2021/03/droog-moto-mini-fighter-1-thumb-960xauto-129456.jpg",
    },
    {
        "id": 29,
        "product_id": 29,
        "url": "https://uncrate.com/assets_c/2020/03/droog-motorcycle-1-thumb-960xauto-113107.jpg",
    },
    {
        "id": 30,
        "product_id": 30,
        "url": "https://uncrate.com/assets_c/2021/06/tarform-uncrate-motorcycle-1-thumb-960xauto-133691.jpg",
    },
    {
        "id": 31,
        "product_id": 31,
        "url": "https://uncrate.com/assets_c/2018/09/ronin-2-thumb-960xauto-89277.jpg",
    },
    {
        "id": 32,
        "product_id": 32,
        "url": "https://uncrate.com/assets_c/2020/02/super-73-electric-bike-1-thumb-960xauto-111232.jpg",
    },
    {
        "id": 33,
        "product_id": 33,
        "url": "https://uncrate.com/assets_c/2020/02/super-73-electric-bike-4-thumb-960xauto-111222.jpg",
    },
    {
        "id": 182,
        "product_id": 23,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/ridecake-makka-flex-white-4.jpg?v=1670781973"
    },
    {
        "id": 183,
        "product_id": 23,
        "url": "https://uncrate.com/assets_c/2022/12/ridecake-makka-flex-white-2-thumb-960xauto-155477.jpg"
    },
    {
        "id": 184,
        "product_id": 23,
        "url": "https://uncrate.com/assets_c/2022/12/ridecake-makka-flex-white-3-thumb-960xauto-155479.jpg"
    },
    {
        "id": 185,
        "product_id": 24,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/cake-inkand-road-bike-sq.jpg?v=1670000921"
    },
    {
        "id": 186,
        "product_id": 24,
        "url": "https://uncrate.com/assets_c/2022/12/cake-inkand-road-bike-2-thumb-960xauto-155117.jpg"
    },
    {
        "id": 187,
        "product_id": 25,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/packshot-uncrate-moonbike-11.jpg?v=1630594092"
    },
    {
        "id": 188,
        "product_id": 25,
        "url": "https://uncrate.com/assets_c/2021/08/packshot-uncrate-moonbike-2-thumb-960xauto-136229.jpg"
    },
    {
        "id": 189,
        "product_id": 25,
        "url": "https://uncrate.com/assets_c/2021/08/packshot-uncrate-moonbike-9-thumb-960xauto-136235.jpg"
    },
    {
        "product_id": 25,
        "url": "https://uncrate.com/assets_c/2021/08/packshot-uncrate-moonbike-8-thumb-960xauto-136234.jpg"
    },
    {
        "product_id": 25,
        "url": "https://uncrate.com/assets_c/2021/08/packshot-uncrate-moonbike-10-thumb-960xauto-136236.jpg"
    },
    {
        "product_id": 25,
        "url" : "https://cdn.shopify.com/s/files/1/0248/6216/products/packshot-uncrate-moonbike-11.jpg?v=1630594092"
    },
    {
        "id": 190,
        "product_id": 26,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/image_14aa6f3b-cdd8-4ac7-9f91-937a8d59346e.jpg?v=1597938862"
    },
    {
        "id": 191,
        "product_id": 26,
        "url": "https://uncrate.com/assets_c/2020/08/ford-mustang-mach-e-9-thumb-960xauto-119654.jpg"
    },
    {
        "id": 192,
        "product_id": 26,
        "url": "https://uncrate.com/assets_c/2020/08/ford-mustang-mach-e-6-thumb-960xauto-119658.jpg"
    },
    {
        "id": 193,
        "product_id": 26,
        "url": "https://uncrate.com/assets_c/2020/08/ford-mustang-mach-e-7-thumb-960xauto-119657.jpg"
    },
    {
        "id": 194,
        "product_id": 26,
        "url": "https://uncrate.com/assets_c/2020/08/ford-mustang-mach-e-50-thumb-960xauto-119922.jpg"
    },
    {
        "id": 195,
        "product_id": 27,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/ridecake-kalk-ink-bike-3.jpg?v=1669389684"
    },
    {
        "id": 196,
        "product_id": 27,
        "url": "https://uncrate.com/assets_c/2022/11/ridecake-kalk-ink-bike-2-thumb-960xauto-154856.jpg"
    },
    {
        "id": 197,
        "product_id": 28,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/droog-moto-mini-fighter-5.jpg?v=1617113611"
    },
    {
        "id": 198,
        "product_id": 28,
        "url": "https://uncrate.com/assets_c/2021/03/droog-moto-mini-fighter-2-thumb-960xauto-129455.jpg"
    },
    {
        "id": 199,
        "product_id": 28,
        "url": "https://uncrate.com/assets_c/2021/03/droog-moto-mini-fighter-3-thumb-960xauto-129457.jpg"
    },
    {
        "id": 200,
        "product_id": 28,
        "url": "https://uncrate.com/assets_c/2021/03/droog-moto-mini-fighter-4-thumb-960xauto-129458.jpg"
    },
    {
        "id": 201,
        "product_id": 29,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/droog-moto-efighter-electric-motorcycle-1.jpg?v=1624995288"
    },
    {
        "id": 202,
        "product_id": 29,
        "url": "https://uncrate.com/assets_c/2020/03/droog-motorcycle-2-thumb-960xauto-113108.jpg"
    },
    {
        "id": 203,
        "product_id": 29,
        "url": "https://uncrate.com/assets_c/2020/03/droog-motorcycle-3-thumb-960xauto-113109.jpg"
    },
    {
        "id": 204,
        "product_id": 29,
        "url": "https://uncrate.com/assets_c/2020/03/droog-motorcycle-4-thumb-960xauto-113111.jpg"
    },
    {
        "id": 205,
        "product_id": 29,
        "url": "https://uncrate.com/assets_c/2020/03/droog-motorcycle-5-thumb-960xauto-113110.jpg"
    },
    {
        "id": 206,
        "product_id": 30,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/tarform-uncrate-motorcycle-10.jpg?v=1624991927"
    },
    {
        "id": 207,
        "product_id": 30,
        "url": "https://uncrate.com/assets_c/2021/06/tarform-uncrate-motorcycle-2-thumb-960xauto-133692.jpg"
    },
    {
        "id": 208,
        "product_id": 30,
        "url": "https://uncrate.com/assets_c/2021/06/tarform-uncrate-motorcycle-5-thumb-960xauto-133695.jpg"
    },
    {
        "id": 209,
        "product_id": 30,
        "url": "https://uncrate.com/assets_c/2021/06/tarform-uncrate-motorcycle-3-thumb-960xauto-133693.jpg"
    },
    {
        "id": 210,
        "product_id": 30,
        "url": "https://uncrate.com/assets_c/2021/06/tarform-uncrate-motorcycle-7-thumb-960xauto-133697.jpg"
    },
    {
        "id": 211,
        "product_id": 31,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/ronin-1280.jpg?v=1536163015"
    },
    {
        "id": 212,
        "product_id": 31,
        "url": "https://uncrate.com/assets_c/2018/09/ronin-3-thumb-960xauto-89276.jpg"
    },
    {
        "id": 213,
        "product_id": 31,
        "url": "https://uncrate.com/assets_c/2018/09/ronin-1-thumb-960xauto-89278.jpg"
    },
    {
        "id": 214,
        "product_id": 31,
        "url": "https://uncrate.com/assets_c/2018/09/ronin-4-thumb-960xauto-89275.jpg"
    },
    {
        "id": 215,
        "product_id": 31,
        "url": "https://uncrate.com/assets_c/2018/09/ronin-5-thumb-960xauto-89289.jpg"
    },
    {
        "id": 216,
        "product_id": 32,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/super-73-electric-bike-7.jpg?v=1581028693"
    },
    {
        "id": 217,
        "product_id": 32,
        "url": "https://uncrate.com/assets_c/2020/02/super-73-electric-bike-2-thumb-960xauto-111233.jpg"
    },
    {
        "id": 218,
        "product_id": 32,
        "url": "https://uncrate.com/assets_c/2020/02/super-73-electric-bike-3-thumb-960xauto-111234.jpg"
    },
    {
        "id": 219,
        "product_id": 33,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/super-73-electric-bike-8.jpg?v=1581028674"
    },
    {
        "id": 220,
        "product_id": 33,
        "url": "https://uncrate.com/assets_c/2020/02/super-73-electric-bike-5-thumb-960xauto-111223.jpg"
    },
    {
        "id": 221,
        "product_id": 33,
        "url": "https://uncrate.com/assets_c/2020/02/super-73-electric-bike-6-thumb-960xauto-111224.jpg"
    },
]
#     {
#         "id": 182,
#         "product_id": 26,
#         "url": "https://uncrate.com/p/2022/12/land-rover-lightweight-88-2.jpg",
#     },
#     {
#         "id": 183,
#         "product_id": 26,
#         "url": "https://uncrate.com/p/2022/12/land-rover-lightweight-88-3.jpg",
#     },
#     {
#         "id": 184,
#         "product_id": 26,
#         "url": "https://uncrate.com/p/2022/12/land-rover-lightweight-88-4.jpg",
#     },
#     {
#         "id": 185,
#         "product_id": 27,
#         "url": "https://uncrate.com/p/2022/12/bentley-surgeon-flying-spur-2.jpg",
#     },
#     {
#         "id": 186,
#         "product_id": 27,
#         "url": "https://uncrate.com/p/2022/12/bentley-surgeon-flying-spur-3.jpg",
#     },
#     {
#         "id": 187,
#         "product_id": 27,
#         "url": "https://uncrate.com/p/2022/12/bentley-surgeon-flying-spur-4.jpg",
#     },
#     {
#         "id": 188,
#         "product_id": 27,
#         "url": "https://uncrate.com/p/2022/12/bentley-surgeon-flying-spur-5.jpg",
#     },
#     {
#         "id": 189,
#         "product_id": 28,
#         "url": "https://uncrate.com/p/2022/06/lightyear-0-2.jpg",
#     },
#     {
#         "id": 190,
#         "product_id": 28,
#         "url": "https://uncrate.com/p/2022/06/lightyear-0-3.jpg",
#     },
#     {
#         "id": 191,
#         "product_id": 30,
#         "url": "https://uncrate.com/p/2022/12/hookie-cake-osa-flex-2.jpg",
#     },
#     {
#         "id": 192,
#         "product_id": 30,
#         "url": "https://uncrate.com/p/2022/12/hookie-cake-osa-flex-3.jpg",
#     },
#     {
#         "id": 193,
#         "product_id": 31,
#         "url": "https://uncrate.com/p/2022/11/lamborghini-urraco-2.jpg",
#     },
#     {
#         "id": 194,
#         "product_id": 31,
#         "url": "https://uncrate.com/p/2022/11/lamborghini-urraco-4.jpg",
#     },
#     {
#         "id": 195,
#         "product_id": 31,
#         "url": "https://uncrate.com/p/2022/11/lamborghini-urraco-3.jpg",
#     },
#     {
#         "id": 196,
#         "product_id": 32,
#         "url": "https://uncrate.com/p/2022/11/de-tomaso-p900-2.jpg",
#     },
#     {
#         "id": 197,
#         "product_id": 32,
#         "url": "https://uncrate.com/p/2022/11/de-tomaso-p900-4.jpg",
#     },
# ]
