from random import randint

products_tech = [
    {
        "id": 34,
        "title": "NOCS MONOLITH SPEAKER",
        "description": "Hand-built in Sweden, this minimalist speaker combines powerful audio with display-worthy design. $1,200.",
        "detailed_description": "Over two years in development, Nocs' Monolith is a hand-built speaker of the highest quality. It starts with local birch plywood, which is precisely CNC'd and then treated with oil and wax for a deep matte black finish. Custom-tuned Scan-Speak drivers — two woofers and three full-range — are then added, augmented by a newly-invented vent design inspired by car exhaust systems that increases bass response while reducing distortion. The resulting speaker is powerful and detailed, with display-worthy looks and the convenience of ​Spotify Connect & Tidal Connect support, Bluetooth 5.0, upcoming AirPlay 2 support, and optional multi-room playback, linking together up to eight units. Proudly designed and crafted in Sweden, it arrives with stainless steel floor stands.",
        "category_id": 4,
        "owner_id": randint(1, 3),
        "price": 1200,
        "preview_img_id": 34,
    },
    {
        "id": 35,
        "title": "U-TURN ORBIT PLUS TURNTABLE",
        "description": "The Orbit Plus adds some important features to the turntable's modern, minimalist look. $399.",
        "detailed_description": "Turntables that bring to mind vinyl's heyday are special, but most of the time we prefer a modern, minimalist deck like this one. The Orbit Plus from U-Turn keeps it simple, with a new acrylic platter for improved speed consistency and clearer, more detailed playback. Each one comes with a precision OA2 gimbal tonearm for accurate tracking and low distortion, while the external belt drive eliminates noise and keeps speeds right where you need them. Available in black or white, the Orbit Plus arrives with a built-in Pluto preamp to connect directly and an Ortofon OM5E cartridge for a balanced and neutral sound profile.",
        "category_id": 4,
        "owner_id": randint(1, 3),
        "price": 399,
        "preview_img_id": 35,
    },
    {
        "id": 36,
        "title": "NIGHTWATCH MAGNIFYING APPLE WATCH DOTCH",
        "description": "Domed charging station turns the Apple Watch into a full-sized alarm clock. $69.",
        "detailed_description": "Apple Watches are loaded with features, but when charging, they're mostly just taking up space on the nightstand. The NightWatch Magnifying Apple Watch Dock adds another layer to its functionality by transforming the dormant timepiece into an alarm clock. Made from a single piece of solid lucite, your watch slides perfectly behind the domed base. Its curved design magnifies the watch's face and displays it like a bedside clock. While docked, patented tap functions allow owners to wake up the watch with a single touch, while built-in sound channels amplify alarms to keep you running on time. Lastly, your existing Apple Watch magnetic charging cable neatly fits in to the back of the dock so your watch automatically begins charging once placed in the dock, and you're done fumbling around with finding your cord behind the nightstand for good. Horological ahfficiando's will appreciate that the design of NightWatch is based on a collectors item called the \"eye of time\" produced by an anonymous watch maker in Regency, London, making this the only ball clock made for the Apple Watch.",
        "category_id": 4,
        "owner_id": randint(1, 3),
        "price": 69,
        "preview_img_id": 36,
    },
    {
        "id": 37,
        "title": "MASTER & DYNAMIC MW08 SPORT ANC TRUE WIRELESS EARPHONES",
        "description": "Master & Dynamic enhances their excellent MW08 earphones with a Kevlar case and water resistance. $219.",
        "detailed_description": "Master & Dynamic's standard MW08 earphones are quite good, with 11mm beryllium drivers for accurate, powerful sound and Hybrid Active Noise-Cancellation with six microphones for both effective sound-blocking and clear calls. The MW08 Sport earphones offer the same features in a workout-friendly package. Instead of ceramic, their jewel-like exteriors are made from shatter-resistant sapphire glass, while the charging case is made from Kevlar and has an IPX4 water resistance rating. They use Bluetooth 5.2 with aptX, AAC, and SBC support for a strong wireless connection and run for up to 10 hours per charge with ANC on, combining with the aforementioned case for a total playtime of 40 hours.",
        "category_id": 4,
        "owner_id": randint(1, 3),
        "price": 219,
        "preview_img_id": 37,
    },
    {
        "id": 38,
        "title": "GEARBOX TRANSPARENT TURNTABLE",
        "description": "Compact and transparent, this turntable channels the design ethos of Dieter Rams. $545.",
        "detailed_description": "Drawing inspiration from Dieter Rams' iconic 1955 Braun PC 3 SV record player, Gearbox's MKII turntable brings back the compact, transparent aesthetic that helped their previous model stand out, but adds an upgraded belt drive with an aluminum pulley for better speed stability as well as upgraded electronics throughout for a performance boost. The plug and play table is made with a high-fidelity built-in phono stage which is specifically designed for cartridges like the included Ortofon OM10 that's pre-fitted to an ultra-low-mass tonearm. Each MKII also includes a wireless transmitter that allows you to stream vinyl songs to Bluetooth speakers, as well as on-board music recognition tech that can identify and add tracks from your vinyl collection to your Spotify playlist.",
        "category_id": 4,
        "owner_id": randint(1, 3),
        "price": 545,
        "preview_img_id": 38,
    },
    {
        "id": 39,
        "title": "NITECORE NPS600 POWER STATION",
        "description": "With a capacity of nearly 600Wh and an output of 300W, this power station can keep your gear running. $900.",
        "detailed_description": "Portable battery stations can be used as backup power during an outage or emergency, for off-grid living, or just for short camping trips. Nitecore's NPS600 a sensible choice for any of those. It has a 594Wh capacity and a pure sine wave output of 300W with support for surges of 600W, or in layman's terms, enough to power a 200W blender for two hours, a 40W fan for 12.5 hours, or recharge an iPhone 12 Pro 51 times. Charging options include 110V AC, 4x USB-A with one QC 3.0, PD USB-C port, 12V DC, and 12V cigarette lighter outputs, while it can recharge via an AC adapter, car charger, or by solar panel via a dedicated port. A real-time backlit LCD display makes checking on its status easy even at night, and multiple safety measures guard against overcharging, overcurrent, short circuits, and over-discharge. Its ABS and aluminum shell is fireproof and is easy to move about thanks to a robust built-in handle.",
        "category_id": 4,
        "owner_id": randint(1, 3),
        "price": 900,
        "preview_img_id": 39,
    },
    {
        "id": 40,
        "title": "IT'S OK NIGHT EDITION BLUETOOTH CASETTE PLAYER",
        "description": "Bluetooth, a built-in mic, and physical controls make this tape player a great blend of old and new. $120.",
        "detailed_description": "Inspired by the darkness of night, It's OK's latest cassette player is a sleek way to enjoy your legacy media. Bluetooth 5.0 support lets it play nice with modern wireless headphones and speakers, while a built-in mic lets you record your thoughts to the included blank tape. Alongside the playback controls, you'll find a physical volume wheel, sliding power switch, and 3.5mm headphone jack, as well as a detachable belt clip and a transparent black cover to offer a view of the currently playing selection.",
        "category_id": 4,
        "owner_id": randint(1, 3),
        "price": 120,
        "preview_img_id": 40,
    },
    {
        "id": 41,
        "title": "PUNKT MP 02 GEN II PHONE",
        "description": "Punkt's minimalist phone returns with the same distraction-free setup while adding 4G coverage, tethering support, and more. $350.",
        "detailed_description": "The Punkt MP-01 phone made offline the new luxury. Now, the minimalist communication tool from Punkt is back as the MP-02 Gen 2 — still without apps, GPS, and everything that distracts — while adding a few important upgrades. One of the most significant changes is the 4G LTE modem, a bump up from the 2G offering from the first generation, which is being phased out across the globe. The Punkt MP-02 also adds tethering support, so you can use it as a hotspot for your laptop or tablet when you need it, and has BlackBerry's security suite to keep everything secure when it's in hotspot mode. The security also keeps the Android 8.1 operating system protected. The design is essentially the same as the MP-01: sleek and straightforward with a 2-inch LCD display reinforced with Gorilla Glass and finished with a tough, abrasion-resistant coating. It only needs to be charged every couple of weeks and is an ideal choice for vacations, date nights, and even movie sets where smart phones are banned. A far cry from the improper dumb phone tag, it's now available in compatible versions for North America, Japan, and Europe.",
        "category_id": 4,
        "owner_id": randint(1, 3),
        "price": 350,
        "preview_img_id": 41,
    },
    {
        "id": 42,
        "title": "KEYSMART WIRELESS CHARGING NOTEBOOK",
        "description": "Take notes and charge nearly any device wirelessly or wired with this slick notebook. $120.",
        "detailed_description": "Taking notes the old-fashioned way — by putting pen to paper — isn't quite dead yet. But no one is giving up their devices either. KeySmart's wireless charging notebook brings the manual and the digital together in one smartly designed package that includes wireless and wired charging. A slim 8,000mAh battery integrated into the front cover wirelessly charges iPhone, Andriod, and tablet devices and has a secret USB flash drive in the magnetic clasp. A six-ring binder, dedicated wired charging cable storage, and multiple pockets will satisfy any obsessive organizer.",
        "category_id": 4,
        "owner_id": randint(1, 3),
        "price": 120,
        "preview_img_id": 42,
    },
    {
        "id": 43,
        "title": "BARISIEUR BREWING ALARM CLOCK",
        "description": "Having a warm cup of coffee or tea sitting on your nightstand the moment... $445.",
        "detailed_description": "Having a warm cup of coffee or tea sitting on your nightstand the moment your eyes open sounds more like a dream than a wake-up call. This machine lures you into consciousness with the aroma of a fresh brew and the sound of bubbling water. Using induction heating and stainless steel ball bearings, water boils and is siphoned over grounds or leaves to drip into the included cup while you sleep. The wood and steel base also houses a cooler for cream or milk that's activated by an infrared sensor so as to not waste power if there's nothing inside. The brewer components are crafted from stainless steel and laboratory-grade borosilicate glass, a material befitting its chemistry kit aesthetic. A complimentary, matching wireless device charging is also included with each purchase.",
        "category_id": 4,
        "owner_id": randint(1, 3),
        "price": 440,
        "preview_img_id": 43,
    },
    {
        "id": 44,
        "title": "TIVOLI PAL BLUETOOTH RADIO",
        "description": "Controlled with just three knobs, the Pal BT mixes retro looks with Bluetooth wireless convenience. $219.",
        "detailed_description": "Tivoli Audio is known for its classically-styled radios. The Pal BT distills that same design sense down into a portable package. As one would expect, it has a robust AM/FM radio built in, as well as Bluetooth for modern streaming services and a pair of 3.5mm jacks for input/headphones. It's controlled with just three knobs, with nary a screen to be seen, and the rechargeable battery lasts at least 16 hours between charges. None of that matters if it doesn't sound good, so its 2.5 inch full-range speaker works with the compact cabinet to create surprisingly full sound, and its weather-resistant body means it's up to outdoor use, as well.",
        "category_id": 4,
        "owner_id": randint(1, 3),
        "price": 219,
        "preview_img_id": 44,
    },
]


products_tech_imgs = [
    {
        "id": 34,
        "product_id": 34,
        "url": "https://uncrate.com/assets_c/2022/12/nocs-monolith-speaker-1-thumb-960xauto-155293.jpg",
    },
    {
        "id": 35,
        "product_id": 35,
        "url": "https://uncrate.com/assets_c/2020/11/uturn-orbit-pro-1-thumb-960xauto-123582.jpg",
    },
    {
        "id": 36,
        "product_id": 36,
        "url": "https://uncrate.com/assets_c/2021/07/nightwatch-magnifying-apple-watch-dock-1-thumb-960xauto-134881.jpg",
    },
    {
        "id": 37,
        "product_id": 37,
        "url": "https://uncrate.com/assets_c/2022/01/master-dynamic-mw08-black-1-thumb-960xauto-142471.jpg",
    },
    {
        "id": 38,
        "product_id": 38,
        "url": "https://uncrate.com/assets_c/2020/01/gear-box-turntable-1-thumb-960xauto-110560.jpg",
    },
    {
        "id": 39,
        "product_id": 39,
        "url": "https://uncrate.com/assets_c/2021/06/nitecore-nps600-powerstation-1-thumb-960xauto-132693.jpg",
    },
    {
        "id": 40,
        "product_id": 40,
        "url": "https://uncrate.com/assets_c/2021/02/its-ok-cassette-player-black-1-thumb-960xauto-127301.jpg",
    },
    {
        "id": 41,
        "product_id": 41,
        "url": "https://uncrate.com/assets_c/2019/07/punkt-mp02-11-thumb-960xauto-102296.jpg",
    },
    {
        "id": 42,
        "product_id": 42,
        "url": "https://uncrate.com/assets_c/2022/11/keysmart-chargebook-7-thumb-960xauto-154178.jpg",
    },
    {
        "id": 43,
        "product_id": 43,
        "url": "https://uncrate.com/assets_c/2018/07/barisiuer-coffee-clock-1-thumb-960xauto-87530.jpg",
    },
    {
        "id": 44,
        "product_id": 44,
        "url": "https://uncrate.com/assets_c/2022/06/tivoli-audio-portable-radio-1-thumb-960xauto-148651.jpg",
    },
    {
        "id": 222,
        "product_id": 34,
        "url": "https://uncrate.com/assets_c/2022/12/nocs-monolith-speaker-2-thumb-960xauto-155292.jpg",
    },
    {
        "id": 223,
        "product_id": 34,
        "url": "https://uncrate.com/assets_c/2022/12/nocs-monolith-speaker-3-thumb-960xauto-155294.jpg",
    },
    {
        "id": 224,
        "product_id": 34,
        "url": "https://uncrate.com/assets_c/2022/12/nocs-monolith-speaker-4-thumb-960xauto-155296.jpg",
    },
    {
        "id": 225,
        "product_id": 34,
        "url": "https://uncrate.com/assets_c/2022/12/nocs-monolith-speaker-6-thumb-960xauto-155297.jpg",
    },
    {
        "id": 226,
        "product_id": 34,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/nocs-design-monolith-speaker-21.jpg?v=1670451015"
    },
    {
        "id": 227,
        "product_id": 35,
        "url": "https://uncrate.com/assets_c/2020/11/uturn-orbit-pro-3-thumb-960xauto-123584.jpg",
    },
    {
        "id": 228,
        "product_id": 35,
        "url": "https://uncrate.com/assets_c/2020/11/uturn-orbit-pro-4-thumb-960xauto-123585.jpg",
    },
    {
        "id": 229,
        "product_id": 35,
        "url": "https://uncrate.com/assets_c/2020/11/uturn-orbit-pro-5-thumb-960xauto-123586.jpg",
    },
    {
        "id": 230,
        "product_id": 35,
        "url": "https://uncrate.com/assets_c/2020/11/uturn-orbit-pro-2-thumb-960xauto-123583.jpg",
    },
    {
        "id": 231,
        "product_id": 35,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/uturn-orbit-pro-10.jpg?v=1604940280"
    },
    {
        "id": 232,
        "product_id": 36,
        "url": "https://uncrate.com/assets_c/2021/12/night-watch-apple-watch-stand-1-thumb-960xauto-140923.jpg",
    },
    {
        "id": 233,
        "product_id": 36,
        "url": "https://uncrate.com/assets_c/2021/12/night-watch-apple-watch-stand-2-thumb-960xauto-140924.jpg",
    },
    {
        "id": 234,
        "product_id": 36,
        "url": "https://uncrate.com/assets_c/2021/12/night-watch-apple-watch-stand-35-thumb-960xauto-140926.jpg",
    },
    {
        "id": 235,
        "product_id": 36,
        "url": "https://uncrate.com/assets_c/2021/12/night-watch-apple-watch-stand-4-thumb-960xauto-140925.jpg",
    },
    {
        "id": 236,
        "product_id": 36,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/night-watch-apple-watch-stand-5.jpg?v=1638724614"
    },
    {
        "id": 237,
        "product_id": 37,
        "url": "https://uncrate.com/assets_c/2022/01/master-dynamic-mw08-black-2-thumb-960xauto-142472.jpg",
    },
    {
        "id": 238,
        "product_id": 37,
        "url": "https://uncrate.com/assets_c/2022/01/master-dynamic-mw08-black-3-thumb-960xauto-142474.jpg",
    },
    {
        "id": 239,
        "product_id": 37,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/master-dynamic-mw08-silver-4.jpg?v=1642538327"
    },
    {
        "id": 240,
        "product_id": 38,
        "url": "https://uncrate.com/assets_c/2020/01/gear-box-turntable-4-thumb-960xauto-110562.jpg",
    },
    {
        "id": 241,
        "product_id": 38,
        "url": "https://uncrate.com/assets_c/2020/01/gear-box-turntable-3-thumb-960xauto-110563.jpg",
    },
    {
        "id": 242,
        "product_id": 38,
        "url": "https://uncrate.com/assets_c/2020/01/gear-box-turntable-6-thumb-960xauto-110565.jpg",
    },
    {
        "id": 243,
        "product_id": 38,
        "url": "https://uncrate.com/assets_c/2020/01/gear-box-turntable-2-thumb-960xauto-110561.jpg",
    },
    {
        "id": 244,
        "product_id": 38,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/gear-box-turntable-7.jpg?v=1579554831"
    },
    {
        "id": 245,
        "product_id": 39,
        "url": "https://uncrate.com/assets_c/2021/06/nitecore-nps600-powerstation-2-thumb-960xauto-132694.jpg",
    },
    {
        "id": 246,
        "product_id": 39,
        "url": "https://uncrate.com/assets_c/2021/06/nitecore-nps600-powerstation-3-thumb-960xauto-132695.jpg",
    },
    {
        "id": 247,
        "product_id": 39,
        "url": "https://uncrate.com/assets_c/2021/06/nitecore-nps600-powerstation-6-thumb-960xauto-132698.jpg",
    },
    {
        "id": 248,
        "product_id": 39,
        "url": "https://uncrate.com/assets_c/2021/06/nitecore-nps600-powerstation-5-thumb-960xauto-132697.jpg",
    },
    {
        "id": 249,
        "product_id": 39,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/nitecore-nps600-powerstation-7.jpg?v=1623248273"
    },
    {
        "id": 250,
        "product_id": 40,
        "url": "https://uncrate.com/assets_c/2021/02/its-ok-cassette-player-black-2-thumb-960xauto-127302.jpg",
    },
    {
        "id": 251,
        "product_id": 40,
        "url": "https://uncrate.com/assets_c/2021/02/its-ok-cassette-player-black-3-thumb-960xauto-127303.jpg",
    },
    {
        "id": 252,
        "product_id": 40,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/its-ok-cassette-player-black-4.jpg?v=1612809301"
    },
    {
        "id": 253,
        "product_id": 41,
        "url": "https://uncrate.com/assets_c/2019/07/punkt-mp02-12-thumb-960xauto-102294.jpg",
    },
    {
        "id": 254,
        "product_id": 41,
        "url": "https://uncrate.com/assets_c/2019/07/punkt-mp02-13-thumb-960xauto-102295.jpg",
    },
    {
        "id": 255,
        "product_id": 41,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/punkt-mp02-4.jpg?v=1562592856"
    },
    {
        "id": 256,
        "product_id": 42,
        "url": "https://uncrate.com/assets_c/2022/11/keysmart-chargebook-1-thumb-960xauto-154224.jpg",
    },
    {
        "id": 257,
        "product_id": 42,
        "url": "https://uncrate.com/assets_c/2022/11/keysmart-chargebook-2-thumb-960xauto-154173.jpg",
    },
    {
        "id": 258,
        "product_id": 42,
        "url": "https://uncrate.com/assets_c/2022/11/keysmart-chargebook-3-thumb-960xauto-154174.jpg",
    },
    {
        "id": 259,
        "product_id": 42,
        "url": "https://uncrate.com/assets_c/2022/11/keysmart-chargebook-6-thumb-960xauto-154177.jpg",
    },
    {
        "id": 260,
        "product_id": 42,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/keysmart-chargebook-9.jpg?v=1668178406"
    },
    {
        "id": 261,
        "product_id": 43,
        "url": "https://uncrate.com/assets_c/2018/07/barisiuer-coffee-clock-5-thumb-960xauto-87533.jpg",
    },
    {
        "id": 262,
        "product_id": 43,
        "url": "https://uncrate.com/assets_c/2018/07/barisiuer-coffee-clock-7-thumb-960xauto-87536.jpg",
    },
    {
        "id": 263,
        "product_id": 43,
        "url": "https://uncrate.com/assets_c/2022/11/joy-wireless-charger-1-thumb-960xauto-154342.jpg",
    },
    {
        "id": 264,
        "product_id": 43,
        "url": "https://uncrate.com/assets_c/2022/11/joy-wireless-charger-2-thumb-960xauto-154341.jpg",
    },
    {
        "id": 265,
        "product_id": 43,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/barisiuer-coffee-clock-8.jpg?v=1532367542"
    },
    {
        "id": 266,
        "product_id": 44,
        "url": "https://uncrate.com/assets_c/2022/06/tivoli-audio-portable-radio-2-thumb-960xauto-148650.jpg",
    },
    {
        "id": 267,
        "product_id": 44,
        "url": "https://uncrate.com/assets_c/2022/06/tivoli-audio-portable-radio-3-thumb-960xauto-148652.jpg",
    },
    {
        "id": 268,
        "product_id": 44,
        "url": "https://uncrate.com/assets_c/2022/06/tivoli-audio-portable-radio-4-thumb-960xauto-148653.jpg",
    },
    {
        "id": 269,
        "product_id": 44,
        "url": "https://uncrate.com/assets_c/2022/06/tivoli-audio-portable-radio-5-thumb-960xauto-148654.jpg",
    },
    {
        "id": 270,
        "product_id": 44,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/tivoli-audio-portable-radio-6.jpg?v=1656613428"
    },
]
