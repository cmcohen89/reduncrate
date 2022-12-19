from random import randint

products_gear = [
    {
        "id": 1,
        "title": "HIGH CAMP TORCH FLASK",
        "description": "Easy to clean and fill, this 6 oz. pocket flask has a removable bottom cap and built-in shot glass. $99.",
        "detailed_description": "Old-time pocket flasks were designed for concealing booze. High Camp's Torch was designed for enjoying it. Made from 18/8 kitchen-grade stainless steel, the double-walled tumbler has a generous, sharing-friendly 6 oz. capacity and an electropolished interior that keeps flavor intact. The removable bottom cap spans the entire width of the flask, making it easy to fill and clean, and allowing ice to be added for chilled drinks. At the other end are a pouring spout and a magnetically-attached 3 fl. oz. sipping shot glass for a more refined on-the-go tipple.",
        "category_id": 1,
        "owner_id": randint(1, 3),
        "price": 99,
        "preview_img_id": 1,
    },
    {
        "id": 2,
        "title": "WIHA CLASSIC PLIERS & CUTTER TRAY SET",
        "description": "Wiha's Classic pliers and cutter set bring German-made quality to three of the most-used hand tools. $85.",
        "detailed_description": "Wiha's Classic pliers and cutter set is the last set you'll buy. The set comes with a nine-inch pair of lineman's pliers, eight-inch needle nose pliers, and an eight-inch angle cutter with oil and solvent-resistant vinyl grips. Wiha's patented DynamicJoint has 40% more cutting and gripping strength, and doesn't fail or loosen like lesser tools. These premium made-in-Germany tools feature induction-hardened jaws and cutting edges with a manganese phosphate finish to resist corrosion, all in a form-fitting, high-quality tray to keep them organized in any toolbox.",
        "category_id": 1,
        "owner_id": randint(1, 3),
        "price": 85,
        "preview_img_id": 2,
    },
    {
        "id": 3,
        "title": "OFF GRID SURVIVAL AXE ELITE",
        "description": "If you had to stash just one emergency tool in your pack or glove... $70.",
        "detailed_description": "If you had to stash just one emergency tool in your pack or glove compartment, the Survival Axe Elite would be the right choice. In addition to a resharpenable hatchet blade, it has a hammer with a reinforced claw, a 6-inch replaceable metal saw integrated into the handle, a gas valve shut off wrench, a handful of hex sockets, a seat belt cutter, and, of course, a bottle opener. Plus, there's a sharpened hook, nail puller, pry bar, box cutter, and glass breaker, among the many other uses you can find for the edges and nooks of the axe. It's crafted from sturdy, black oxide-coated 420 stainless steel with a full tang that extends down the length of the glass-filled nylon handle, yet weighs just 1.5 pounds and measures under a foot from top to bottom. Blade sheath included. Made in the USA.",
        "category_id": 1,
        "owner_id": randint(1, 3),
        "price": 70,
        "preview_img_id": 3,
    },
    {
        "id": 3,
        "title": "VICTORINOX SWISS ARMY ONYX RANGER KNIFE",
        "description": "A special polispectral process gives the 12 implements of this knife a durable glossy black finish. $120.",
        "detailed_description": "Not satisfied to simply make the grippy, ergonomic polyamide scales black, the Onyx Ranger from Victorinox blacks out the tools, as well. More specifically, they use a special polispectral process to coat each stainless steel tool in chromium oxide, giving it a smooth, glossy black finish. 12 functions in all are offered, including 3mm and 5mm screwdrivers, a wood saw, wire stripper, reamer, punch, and sewing awl, a locking main blade, corkscrew, can opener, keyring, black lanyard, and the ever-present bottle opener. Arrives in a handsome presentation box.",
        "category_id": 1,
        "owner_id": randint(1, 3),
        "price": 120,
        "preview_img_id": 4,
    },
    {
        "id": 5,
        "title": "HARDCORE HAMMER BLACKOUT EDITION",
        "description": "Hardcore Hammers' Blackout Edition adds a tough new FNC coating and a slick all-black look. $119.",
        "detailed_description": "Hardcore Hammers has answered customer demand for a Blackout edition of its acclaimed Hardcore Hammer. The Blackout Edition features an investment cast 21-ounce head and Hardcore Hammers' unique head design, while the new 2.0 version adds a Ferritic Nitrocarburizing process that further strengthens the 4104 steel, for even better durability and corrosion resistance. A matte black 18-inch American hickory handle compliments the dark-finished head for the best hammer you can put your hands on.",
        "category_id": 1,
        "owner_id": randint(1, 3),
        "price": 119,
        "preview_img_id": 5,
    },
    {
        "id": 6,
        "title": "SNOW PEAK SHIMO BEER TANK",
        "description": "Designed for lightly carbonated beverages, this 4.7L growler has a handy one-touch spout system. $299.",
        "detailed_description": "It looks a little like a mini-keg, but in fact, Snow Peak's Shimo Beer Tank is a vacuum-insulated growler. Its stainless steel body can hold up to 4.7 liters of suds, with an intelligent lid that helps to preserve carbonation while integrating a one-touch plug and spout. A bamboo handle helps with pouring, while legs on the other side serve as a horizontal stand. Thanks to the vacuum insulation, it also works to keep hot drinks hot, making it suitable for everything from tailgating to camping trips.",
        "category_id": 1,
        "owner_id": randint(1, 3),
        "price": 299,
        "preview_img_id": 6,
    },
    {
        "id": 7,
        "title": "007 X PENFOLD GOLDFINGER GOLF GIFT SET",
        "description": "Hit the course like 007 with this multi-piece, gift-worthy golf ball, marker, towel, and tee set. $75+.",
        "detailed_description": "The golfing scene in Goldfinger is one of the more memorable in what's arguably the best Bond film. While it won't guarantee you can catch your opponent cheating, this 007 x Penfold Goldfinger Golf Gift Set can help set you apart on the course. Included is a sleeve of 3 Penfold Hearts golf balls — the modern-day version of the ball Bond plays in the film — as well as a 007-branded golf towel, 50 black 007 tees, a stainless 007 ball marker, and two custom, collectible postcards. The set arrives in a custom 007 box with 007 tissue paper, making it a perfect gift for yourself, or the Bond aficionado in your life. Available as a standalone set or with an additional dozen Penfold Hearts golf balls, it's limited to just 200 sets.",
        "category_id": 1,
        "owner_id": randint(1, 3),
        "price": 75,
        "preview_img_id": 7,
    },
    {
        "id": 8,
        "title": "POWERUP 4.0 POWERED PAPER AIRPLANE",
        "description": "A childhood staple becomes far more engaging with this lightweight app-enabled propeller system. $69.",
        "detailed_description": "We're all looking for fun ways to pass the time at home. Making paper airplanes is fun; giving them an actual engine is even more so. PowerUp's 4.0 paper airplane propeller can turn any piece of paper into an advanced flying machine. The lightweight motor has an onboard computer and stabilizers that let you fly even in the wind, Bluetooth for wireless control via smartphone, and up to 10 minutes of flight time per charge. It comes with four paper templates in the box, can work with both Balsa wood and foam models weighing up to 20 grams, and offers flight analytics like heading, thrust levels, and turn angles in real-time so you can use the data to help improve future flights.",
        "category_id": 1,
        "owner_id": randint(1, 3),
        "price": 69,
        "preview_img_id": 8,
    },
    {
        "id": 9,
        "title": "TROVA GOPLUS BIOMETRIC PERSONAL VAULT",
        "description": "Keep valuables, cash, or any other small items safe from prying eyes with this portable safe. $249.",
        "detailed_description": "Whether it's valuables, cash and cards, or items in need of more clandestine transportation, they'll be safe inside this box. CNC'd from stout aluminum alloy, it uses Bluetooth to access a smartphone's biometric authentication, preventing unwanted access. In the meantime, it's designed to be unassuming while offering enough room inside for watches, rings, pipes, or anything else that needs to be hidden away.",
        "category_id": 1,
        "owner_id": randint(1, 3),
        "price": 249,
        "preview_img_id": 9,
    },
    {
        "id": 10,
        "title": "CAKE KALK INK& STREET LEGAL ELECTRIC BIKE",
        "description": "Cake takes its trail-ready model to the pavement with this road-legal version of the Kalk INK. $12,580.",
        "detailed_description": "Rugged enough for the trail yet refined enough for the road, Cake's Kalk INK& e-Bike is here to transform your commute and time off. It's powered by an electric powertrain with a lithium battery and a powerful motor to deliver instant torque and a top speed of 56 mph. The proprietary suspension system has a direct mount rear chock and spring front fork with 200mm of travel, which handle both potholes and bumpy paths with aplomb. Up front is a digital dashboard that provides essential info like speed and battery life and access to the three braking and ride modes. It sits on custom-designed 19\" motorcycle rims and dual sport motorcycle tires, which transition effortlessly from city streets to backcountry trails. And as a road-legal model, it has all the necessary lights, indicators, and mirrors, and can be registered as a 125cc equivalent in the EU and USA.",
        "category_id": 1,
        "owner_id": randint(1, 3),
        "price": 12580,
        "preview_img_id": 10,
    },
    {
        "id": 11,
        "title": "CANVAS FIREWOOD CARRIER",
        "description": "Recycled canvas and a handmade process give this log carrier a sturdy construction and unique traits. $40.",
        "detailed_description": "Crafted from recycled canvas, this log carrier will make light work of your load. Its rugged construction and sturdy handles wrap logs tight to keep the job neat as you travel from the pile to the hearth. Made by hand using repurposed materials, each piece has its own individual character.",
        "category_id": 1,
        "owner_id": randint(1, 3),
        "price": 40,
        "preview_img_id": 11,
    },
]

products_gear_imgs = [
    {
        "id": 1,
        "product_id": 1,
        "url": "https://uncrate.com/assets_c/2022/12/highcamp-torch-flask-gunmetal-1-thumb-960xauto-155324.jpg",
    },
    {
        "id": 2,
        "product_id": 2,
        "url": "https://uncrate.com/assets_c/2022/07/wiha-classic-pliers-1-thumb-960xauto-148715.jpg",
    },
    {
        "id": 3,
        "product_id": 3,
        "url": "https://uncrate.com/assets_c/2018/02/off-grid-axe-13-thumb-960xauto-81005.jpg",
    },
    {
        "id": 4,
        "product_id": 4,
        "url": "https://uncrate.com/assets_c/2020/10/victorinox-onyx-ranger-grip-1-thumb-960xauto-122922.jpg",
    },
    {
        "id": 5,
        "product_id": 5,
        "url": "https://uncrate.com/assets_c/2022/05/hardcore-hammer-blackout-2-thumb-960xauto-147224.jpg",
    },
    {
        "id": 6,
        "product_id": 6,
        "url": "https://uncrate.com/assets_c/2022/12/snow-peak-shimo-tank-160-oz-1a-thumb-960xauto-155547.jpg",
    },
    {
        "id": 7,
        "product_id": 7,
        "url": "https://uncrate.com/assets_c/2022/11/penfold-007-gift-set-1-thumb-960xauto-154320.jpg",
    },
    {
        "id": 8,
        "product_id": 8,
        "url": "https://uncrate.com/assets_c/2020/11/powerup-4-remote-plane-11-thumb-960xauto-124520.jpg"},
    {
        "id": 9,
        "product_id": 9,
        "url": "https://uncrate.com/assets_c/2021/03/trova-go-plus-2-thumb-960xauto-128592.jpg",
    },
    {
        "id": 10,
        "product_id": 10,
        "url": "https://uncrate.com/assets_c/2022/12/cake-inkand-road-bike-1-thumb-960xauto-155118.jpg",
    },
    {
        "id": 11,
        "product_id": 11,
        "url": "https://uncrate.com/assets_c/2020/05/canvas-firewood-carrier-10-thumb-960xauto-115643.jpg",
    },
    {
        "id": 89,
        "product_id": 1,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/highcamp-torch-flask-gunmetal-5.jpg?v=1670510868",
    },
    {
        "id": 90,
        "product_id": 1,
        "url": "https://uncrate.com/assets_c/2022/12/highcamp-torch-flask-gunmetal-2-thumb-960xauto-155323.jpg",
    },
    {
        "id": 91,
        "product_id": 1,
        "url": "https://uncrate.com/assets_c/2022/12/highcamp-torch-flask-gunmetal-3-thumb-960xauto-155325.jpg",
    },
    {
        "id": 92,
        "product_id": 1,
        "url": "https://uncrate.com/assets_c/2022/12/highcamp-torch-flask-gunmetal-4-thumb-960xauto-155326.jpg",
    },
    {
        "id": 93,
        "product_id": 2,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/wiha-classic-pliers-3.jpg?v=1656703935",
    },
    {
        "id": 94,
        "product_id": 2,
        "url": "https://uncrate.com/assets_c/2022/07/wiha-classic-pliers-2-thumb-960xauto-148714.jpg",
    },
    {
        "id": 95,
        "product_id": 3,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/axe-shop1.jpg?v=1573161615",
    },
    {
        "id": 96,
        "product_id": 3,
        "url": "https://uncrate.com/assets_c/2018/02/off-grid-axe-1-thumb-960xauto-81000.jpg",
    },
    {
        "id": 97,
        "product_id": 3,
        "url": "https://uncrate.com/assets_c/2018/02/off-grid-axe-2-thumb-960xauto-80999.jpg",
    },
    {
        "id": 98,
        "product_id": 3,
        "url": "https://uncrate.com/assets_c/2018/02/off-grid-axe-3-thumb-960xauto-80998.jpg",
    },
    {
        "id": 99,
        "product_id": 3,
        "url": "https://uncrate.com/assets_c/2018/02/off-grid-axe-9-thumb-960xauto-80993.jpg",
    },
    {
        "id": 100,
        "product_id": 4,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/victorinox-onyx-ranger-grip-4.jpg?v=1603828614",
    },
    {
        "id": 101,
        "product_id": 4,
        "url": "https://uncrate.com/assets_c/2020/10/victorinox-onyx-ranger-grip-2-thumb-960xauto-122923.jpg",
    },
    {
        "id": 102,
        "product_id": 4,
        "url": "https://uncrate.com/assets_c/2020/10/victorinox-onyx-ranger-grip-3-thumb-960xauto-122924.jpg",
    },
    {
        "id": 103,
        "product_id": 5,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/hardcore-hammer-blackout-7.jpg?v=1653502315",
    },
    {
        "id": 104,
        "product_id": 5,
        "url": "https://uncrate.com/assets_c/2022/05/hardcore-hammer-blackout-5-thumb-960xauto-147221.jpg",
    },
    {
        "id": 105,
        "product_id": 5,
        "url": "https://uncrate.com/assets_c/2022/05/hardcore-hammer-blackout-4-thumb-960xauto-147222.jpg",
    },
    {
        "id": 106,
        "product_id": 5,
        "url": "https://uncrate.com/assets_c/2022/05/hardcore-hammer-blackout-3-thumb-960xauto-147223.jpg",
    },
    {
        "id": 107,
        "product_id": 6,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/snow-peak-shimo-tank-160-oz-8.jpg?v=1670943723",
    },
    {
        "id": 108,
        "product_id": 6,
        "url": "https://uncrate.com/assets_c/2022/12/snow-peak-shimo-tank-160-oz-2-thumb-960xauto-155548.jpg",
    },
    {
        "id": 109,
        "product_id": 6,
        "url": "https://uncrate.com/assets_c/2022/12/snow-peak-shimo-tank-160-oz-3-thumb-960xauto-155549.jpg",
    },
    {
        "id": 110,
        "product_id": 6,
        "url": "https://uncrate.com/assets_c/2022/12/snow-peak-shimo-tank-160-oz-5-thumb-960xauto-155551.jpg",
    },
    {
        "id": 111,
        "product_id": 6,
        "url": "https://uncrate.com/assets_c/2022/12/snow-peak-shimo-tank-160-oz-6-thumb-960xauto-155552.jpg",
    },
    {
        "id": 112,
        "product_id": 7,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/penfold-007-gift-set-6.jpg?v=1668009343",
    },
    {
        "id": 113,
        "product_id": 7,
        "url": "https://uncrate.com/assets_c/2022/11/penfold-007-gift-set-2-thumb-960xauto-154321.jpg",
    },
    {
        "id": 114,
        "product_id": 7,
        "url": "https://uncrate.com/assets_c/2022/11/penfold-007-gift-set-3-thumb-960xauto-154323.jpg",
    },
    {
        "id": 115,
        "product_id": 7,
        "url": "https://uncrate.com/assets_c/2022/11/penfold-007-gift-set-4-thumb-960xauto-154322.jpg",
    },
    {
        "id": 116,
        "product_id": 7,
        "url": "https://uncrate.com/assets_c/2022/11/penfold-007-gift-set-5-thumb-960xauto-154324.jpg",
    },
    {
        "id": 117,
        "product_id": 8,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/powerup-4-remote-plane-6.jpg?v=1606234163",
    },
    {
        "id": 118,
        "product_id": 8,
        "url": "https://uncrate.com/assets_c/2020/11/powerup-4-remote-plane-2-thumb-960xauto-124485.jpg",
    },
    {
        "id": 119,
        "product_id": 8,
        "url": "https://uncrate.com/assets_c/2020/11/powerup-4-remote-plane-4-thumb-960xauto-124486.jpg",
    },
    {
        "id": 120,
        "product_id": 9,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/trova-go-plus-5.jpg?v=1615212872",
    },
    {
        "id": 121,
        "product_id": 9,
        "url": "https://uncrate.com/assets_c/2021/03/trova-go-plus-1-thumb-960xauto-128591.jpg",
    },
    {
        "id": 122,
        "product_id": 9,
        "url": "https://uncrate.com/assets_c/2021/03/trova-go-plus-3-thumb-960xauto-128593.jpg",
    },
    {
        "id": 123,
        "product_id": 9,
        "url": "https://uncrate.com/assets_c/2021/03/trova-go-plus-4-thumb-960xauto-128594.jpg",
    },
    {
        "id": 124,
        "product_id": 10,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/cake-inkand-road-bike-sq.jpg?v=1670000921",
    },
    {
        "id": 125,
        "product_id": 10,
        "url": "https://uncrate.com/assets_c/2022/12/cake-inkand-road-bike-2-thumb-960xauto-155117.jpg",
    },
    {
        "id": 126,
        "product_id": 11,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/canvas-firewood-carrier-13.jpg?v=1589385240",
    },
    {
        "id": 127,
        "product_id": 11,
        "url": "https://uncrate.com/assets_c/2020/05/canvas-firewood-carrier-11-thumb-960xauto-115644.jpg",
    },
    {
        "id": 128,
        "product_id": 11,
        "url": "https://uncrate.com/assets_c/2020/05/canvas-firewood-carrier-12-thumb-960xauto-115645.jpg",
    },
]

#     {
#         "id": 89,
#         "product_id": 1,
#         "url": "https://uncrate.com/p/2022/12/atech-airtag-7-tool-multitool-21.jpg"
#     },
#     {
#         "id": 90,
#         "product_id": 1,
#         "url": "https://uncrate.com/p/2022/12/atech-airtag-7-tool-multitool-2.jpg"
#     },
#     {
#         "id": 91,
#         "product_id": 1,
#         "url": "https://uncrate.com/p/2022/12/atech-airtag-7-tool-multitool-6.jpg"
#     },
#     {
#         "id": 92,
#         "product_id": 1,
#         "url": "https://uncrate.com/p/2022/12/atech-airtag-7-tool-multitool-5.jpg"
#     },

#     {
#         "id": 94,
#         "product_id": 2,
#         "url": "https://uncrate.com/p/2022/12/2023-taylormade-p770-irons-2.jpg"
#     },
#     {
#         "id": 97,
#         "product_id": 4,
#         "url": "https://uncrate.com/p/2020/11/powerup-4-remote-plane-2.jpg"
#     },
#     {
#         "id": 98,
#         "product_id": 4,
#         "url": "https://uncrate.com/p/2020/11/powerup-4-remote-plane-4.jpg"
#     },
#     {
#         "id": 99,
#         "product_id": 4,
#         "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/powerup-4-remote-plane-6.jpg?v=1606234163"
#     },
#     {
#         "id": 101,
#         "product_id": 5,
#         "url": "https://uncrate.com/p/2021/03/trova-go-plus-1.jpg"
#     },
#     {
#         "id": 102,
#         "product_id": 5,
#         "url": "https://uncrate.com/p/2021/03/trova-go-plus-3.jpg"
#     },
#     {
#         "id": 103,
#         "product_id": 5,
#         "url": "https://uncrate.com/p/2021/03/trova-go-plus-4.jpg"
#     },
#     {
#         "id": 108,
#         "product_id": 9,
#         "url": "https://uncrate.com/p/2022/12/elvis-lockheed-1329-2.jpg"
#     },
#     {
#         "id": 109,
#         "product_id": 9,
#         "url": "https://uncrate.com/p/2022/12/elvis-lockheed-1329-4.jpg"
#     },
#     {
#         "id": 110,
#         "product_id": 9,
#         "url": "https://uncrate.com/p/2022/12/elvis-lockheed-1329-5.jpg"
#     },
#     {
#         "id": 112,
#         "product_id": 10,
#         "url": "https://uncrate.com/p/2020/05/canvas-firewood-carrier-11.jpg"
#     },
#     {
#         "id": 113,
#         "product_id": 10,
#         "url": "https://uncrate.com/p/2020/05/canvas-firewood-carrier-12.jpg"
#     },
#     {
#         "id": 114,
#         "product_id": 10,
#         "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/canvas-firewood-carrier-13.jpg?v=1589385240"
#     },
#     {
#         "id": 116,
#         "product_id": 11,
#         "url": "https://uncrate.com/p/2022/12/rimowa-pine-raspberry-2.jpg"
#     },
#     {
#         "id": 117,
#         "product_id": 11,
#         "url": "https://uncrate.com/p/2022/12/rimowa-pine-raspberry-3.jpg"
#     },
#     {
#         "id": 118,
#         "product_id": 11,
#         "url": "https://uncrate.com/p/2022/12/rimowa-pine-raspberry-4.jpg"
#     },
# ]
