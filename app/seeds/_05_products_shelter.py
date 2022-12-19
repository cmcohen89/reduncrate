from random import randint


products_shelter = [
    {
        "id": 45,
        "title": "SEIKO MAI ALARM CLOCK",
        "description": "Inspired by the design of legendary Seiko wrist watches, this portable clock has a silent seconds hand and beep + LED alarm. $45.",
        "detailed_description": "Seiko fanatics now have a way to further their collection, but not on the wrist. The Mai Alarm Clock from Seiko is a tribute to the design of its famous utilitarian and relatively accessible wristwatches, and notably these alarm clocks have elements pulled from the design of the famed SKX series. Its portable design is compact for travel, complete with a 60-minute bezel and near-silent sweeping seconds hand. Powered by a precise quartz movement, it also has a beeping and LED-flashing alarm to wake even deep sleepers, a snooze function, and light. Powered by a single included AA battery.",
        "category_id": 5,
        "owner_id": randint(1, 3),
        "price": 45,
        "preview_img_id": 45,
    },
    {
        "id": 46,
        "title": "HYPELEV LEVITATING SNEAKER DISPLAY STAND",
        "description": "Using a powerful magnet, current manipulation, and air, this stand suspends sneakers in mid-air. $249.",
        "detailed_description": "Over the last 30+ years, sneakers have gone from humble foot coverings to pop culture artifacts. Problem is, most of us aren't leaving shoeboxes out in our living areas for guests to enjoy. The Hypelev allows sneakers to be displayed and enjoyed like the works of art they are. A powerful magnet slides into the shoe against the heel, while the C-shaped levitator manipulates magnetic currents to suspend the shoe in mi-air, and a small air hole causes it to slowly spin. For added drama, white LEDs provide illumination to highlight small details and enable nighttime viewing. Available in black or white, it works with shoes up to size 15 with a weight up to 2.2 pounds.",
        "category_id": 5,
        "owner_id": randint(1, 3),
        "price": 249,
        "preview_img_id": 46,
    },
    {
        "id": 47,
        "title": "REIGNING CHAMP X PENDLETON STADIUM BLANKET",
        "description": "Ombre striped blanket made from premium virgin wool/cotton blend and a napped finish. $400.",
        "detailed_description": "Reigning Champ enlists the expertise of Pendleton for a cold-weather accessory. The limited-edition stadium blanket fuses the ethos of both brands, using the historic craftsmanship of the six-generation American mill and the signature colorway of the Canadian athletic brand. Made from a premium virgin wool/cotton blend, the twin-size blanket features an ombre stripe pattern in black, gray, and navy, a felt wool binding, and a napped finish for added softness. A co-branding logo is stitched to the corner to slate the collaboration.",
        "category_id": 5,
        "owner_id": randint(1, 3),
        "price": 400,
        "preview_img_id": 47,
    },
    {
        "id": 48,
        "title": "HERMAN MILLER NELSON FIREPLACE TOOL SET",
        "description": "Crafted with quality to last, this fire tool set will tame the flames for generations. $395.",
        "detailed_description": "George Nelson designed the Nelson® Fireplace Tool Set in 1951 with the principle that everything is there for a reason. The four-piece set includes all the items needed to command the flames from start to finish. Made to last, the poker, shovel, arenga-fiber brush, and floor stand are forged from powder-coated steel and finished with walnut handles. Pairs well with the Nelson® Fireplace Caddy.",
        "category_id": 5,
        "owner_id": randint(1, 3),
        "price": 395,
        "preview_img_id": 48,
    },
{
        "id": 49,
        "title": "PORSCHE 356 NOSE FRAMED PRINT",
        "description": "A black and white photo of a vintage Porsche 356 front end is ideal decor for motoring enthusists. $269.",
        "detailed_description": "Produced from 1948 to 1965, the Porsche 356 put the brand on the map and set the standard for what a rear-engine, rear-wheel-drive sports car could be. While not as iconic as its successor, the 911, the 356 was no slouch in the style department, as evidenced in this photo of a 356 front-end, taken by Huseyin Erturk in Los Angeles in 2017. The photo is printed on Fuji crystal archive paper, numbered and certified, and comes encased inside a hand-made solid wood white or black frame that's ready to hang. Limited edition of 495.",
        "category_id": 5,
        "owner_id": randint(1, 3),
        "price": 269,
        "preview_img_id": 49,
    },
    {
        "id": 50,
        "title": "FILSON MACKINAW WOOL BLANKET",
        "description": "Soft virgin wool sourced from the US delivers a warm layer of insulation during crisp, autumn outings. $295.",
        "detailed_description": "At stadiums, campsites, and fireside sofas, a blanket is the ideal fall accessory. The Filson Mackinaw Wool Blanket keeps the cool off inside or out. It's made from 100% virgin wool sourced from the USA and provides a soft layer of insulation that is naturally water-repellent. Finished with serged edges, it won't fray and will withstand years of use.",
        "category_id": 5,
        "owner_id": randint(1, 3),
        "price": 295,
        "preview_img_id": 50,
    },
    {
        "id": 51,
        "title": "URSULA ANDRESS AT CASINO ROYALE FRAMED PRINT",
        "description": "The original Bond girl, Ursula Andress, is pictured here on the set of the 1967 film Casino Royale. $269.",
        "detailed_description": "Ursula Andress is famous for being the first Bond girl, setting a precedent as she came out of the water. As such, she was hired on for the forgettable parody adaptation of Casino Royale. This photo shows her in a scene from the film, laying back on a roulette table surrounded by money and markers. Printed to order on Fuji crystal archive paper, numbered and certified, and comes encased inside a hand-made solid wood black that's ready to hang. Limited edition of 495.",
        "category_id": 5,
        "owner_id": randint(1, 3),
        "price": 269,
        "preview_img_id": 51,
    },
    {
        "id": 52,
        "title": "SEAN CONNERY PLAYS GOLF FRAMED PRINT",
        "description": "The orignal James Bond plays a round of golf near his Acton home in 1962. $269.",
        "detailed_description": "Sean Connery famously played a round of golf with notorious villain Goldfinger in the 1964 Bond film. But his skills weren't just for show. The original 007 was an avid golfer off-screen, also. His love for the game is captured in this picture taken at a course near his home in Acton in 1962. The photo is printed on Fuji crystal archive paper, numbered and certified, and comes encased inside a hand-made solid wood white or black frame that's ready to hang. Limited edition of 495.",
        "category_id": 5,
        "owner_id": randint(1, 3),
        "price": 269,
        "preview_img_id": 52,
    },
    {
        "id": 53,
        "title": "ANDY WARHOL IN VENICE FRAMED PRINT",
        "description": "Photographer Graziano Arici camptures the Pop Art icon sitting at a cafe in Venice. $269.",
        "detailed_description": "Andy Warhol is one of the most iconic artists of the 20th century and pioneered the Pop Art era with his paintings of Campbell's soup cans and celebrities like Marilyn Monroe and Elvis Presley. In this pint, photographer Graziano Arici captures the legend at a cafe in Venice in 1977. The photo is printed on Fuji crystal archive paper, numbered and certified, and comes encased inside a hand-made solid wood white or black frame that's ready to hang. Limited edition of 495.",
        "category_id": 5,
        "owner_id": randint(1, 3),
        "price": 269,
        "preview_img_id": 53,
    },
    {
        "id": 54,
        "title": "ONSEN X UNCRATE TOWEL SET",
        "description": "Onsen's relaxed, minimalist towels were already our go-to, and now we've taken their hue... $75.",
        "detailed_description": "Onsen's relaxed, minimalist towels were already our go-to, and now we've taken their hue to our preferred end of the spectrum. Made with American-grown Supima cotton, these special edition black towels are made with longer fibers in a weave pattern that provides an exceptionally soft texture that's also fast-drying. But the key to this obsessively designed towel set isn't what Onsen added, but rather what they eliminated. Standard bath towels go through a chemical bathing process so they feel fluffy — at least at first. Instead of short-lived softness that washes away, Onsen builds in softness from the beginning and utilizes no chemical processes. Bypassing these common treatments eliminates the artificial fluff, resulting instead in a naturally plush surface that just gets better and better, making this quite possibly the last towel set you'll need.",
        "category_id": 5,
        "owner_id": randint(1, 3),
        "price": 75,
        "preview_img_id": 54,
    },
    {
        "id": 55,
        "title": "SPACE SHUTTLE DISCOVERY LIFTOFF FRAMED PRINT",
        "description": "This framed print captures the Space Shuttle Discovery at lift-off on its final mission in 2011. $269.",
        "detailed_description": "On February 11, 2011, the space shuttle Discovery lifted off on its final mission, STS-133. It was Discovery's 39th launch, with the orbiter spending exactly 365 days in space over its 27-year career. Captured at the moment of lift-off, this full-color print shows Discovery racing for the stars on that final flight. Printed on Fuji crystal paper and mounted in a hand-made black or white wooden frame.",
        "category_id": 5,
        "owner_id": randint(1, 3),
        "price": 269,
        "preview_img_id": 55,
    },
]


products_shelter_imgs = [
    {
        "id": 45,
        "product_id": 45,
        "url": "https://uncrate.com/assets_c/2022/12/seiko-mai-alarm-clock-blue-23-thumb-960xauto-155169.jpg",
    },
    {
        "id": 46,
        "product_id": 46,
        "url": "https://uncrate.com/assets_c/2021/12/hype-lev-levitator-1-thumb-960xauto-141302.jpg",
    },
    {
        "id": 47,
        "product_id": 47,
        "url": "https://uncrate.com/assets_c/2022/11/reigning-champ-pendleton-stadium-blanket-1-thumb-960xauto-154676.jpg",
    },
    {
        "id": 48,
        "product_id": 48,
        "url": "https://uncrate.com/assets_c/2022/10/herman-miller-nelson-fireplace-toolkit-2-thumb-960xauto-152264.jpg",
    },
    {
        "id": 49,
        "product_id": 49,
        "url": "https://uncrate.com/assets_c/2022/11/porsche-356-nose-print-black-1-thumb-960xauto-154585.jpg",
    },
    {
        "id": 50,
        "product_id": 50,
        "url": "https://uncrate.com/assets_c/2022/10/filson-plaid-wool-blanket-1-thumb-960xauto-152360.jpg",
    },
    {
        "id": 51,
        "product_id": 51,
        "url": "https://uncrate.com/assets_c/2022/11/Ursula-TFSK-bond-print-black-1-thumb-960xauto-154346.jpg",
    },
    {
        "id": 52,
        "product_id": 52,
        "url": "https://uncrate.com/assets_c/2022/11/sean-connery-golfing-IPPI-black-1-thumb-960xauto-154315.jpg",
    },
    {
        "id": 53,
        "product_id": 53,
        "url": "https://uncrate.com/assets_c/2022/11/warhol-kpzn-print-black-1-thumb-960xauto-154181.jpg",
    },
    {
        "id": 54,
        "product_id": 54,
        "url": "https://uncrate.com/assets_c/2018/11/onsen-uncrate-00-thumb-960xauto-92183.jpg",
    },
    {
        "id": 55,
        "product_id": 55,
        "url": "https://uncrate.com/assets_c/2022/11/nasa-ipwk-rocket-print-black-1-thumb-960xauto-153854.jpg",
    },
    {
        "id": 271,
        "product_id": 45,
        "url": "https://uncrate.com/assets_c/2022/12/seiko-mai-alarm-clock-black-and-gold-23-thumb-960xauto-155168.jpg"
    },
    {
        "id": 272,
        "product_id": 45,
        "url": "https://uncrate.com/assets_c/2022/12/seiko-mai-alarm-clock-black-and-gold-22-thumb-960xauto-155166.jpg"
    },
    {
        "id": 273,
        "product_id": 45,
        "url": "https://uncrate.com/assets_c/2022/12/seiko-mai-alarm-clock-black-and-gold-24-thumb-960xauto-155170.jpg"
    },
    {
        "id": 274,
        "product_id": 45,
        "url": "https://uncrate.com/assets_c/2022/12/seiko-mai-alarm-clock-blue-24-thumb-960xauto-155171.jpg"
    },
    {
        "id": 275,
        "product_id": 45,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/seiko-mai-alarm-clock-blue-25.jpg?v=1670604897"
    },
    {
        "id": 276,
        "product_id": 46,
        "url": "https://uncrate.com/assets_c/2021/12/hype-lev-levitator-2-thumb-960xauto-141303.jpg"
    },
    {
        "id": 277,
        "product_id": 46,
        "url": "https://uncrate.com/assets_c/2021/12/hypelev-white-1-thumb-960xauto-141301.jpg"
    },
    {
        "id": 278,
        "product_id": 46,
        "url": "https://uncrate.com/assets_c/2021/12/hypelev-white-2-thumb-960xauto-141304.jpg"
    },
    {
        "id": 279,
        "product_id": 46,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/hype-lev-levitator-3.jpg?v=1670008619"
    },
    {
        "id": 280,
        "product_id": 47,
        "url": "https://uncrate.com/assets_c/2022/11/reigning-champ-pendleton-stadium-blanket-2-thumb-960xauto-154677.jpg"
    },
    {
        "id": 281,
        "product_id": 47,
        "url": "https://uncrate.com/assets_c/2022/11/reigning-champ-pendleton-stadium-blanket-3-thumb-960xauto-154678.jpg"
    },
    {
        "id": 282,
        "product_id": 47,
        "url": "https://uncrate.com/assets_c/2022/11/reigning-champ-pendleton-stadium-blanket-4-thumb-960xauto-154679.jpg"
    },
    {
        "id": 283,
        "product_id": 47,
        "url": "https://uncrate.com/assets_c/2022/11/reigning-champ-pendleton-stadium-blanket-5-thumb-960xauto-154681.jpg"
    },
    {
        "id": 284,
        "product_id": 47,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/reigning-champ-pendleton-stadium-blanket-6.jpg?v=1669043563"
    },
    {
        "id": 285,
        "product_id": 48,
        "url": "https://uncrate.com/assets_c/2022/10/herman-miller-nelson-fireplace-toolkit-1-thumb-960xauto-152265.jpg"
    },
    {
        "id": 286,
        "product_id": 48,
        "url": "https://uncrate.com/assets_c/2022/10/herman-miller-nelson-fireplace-toolkit-3-thumb-960xauto-152267.jpg"
    },
        {
        "id": 287,
        "product_id": 48,
        "url": "https://uncrate.com/assets_c/2022/10/herman-miller-nelson-fireplace-toolkit-4-thumb-960xauto-152266.jpg"
    },
        {
        "id": 288,
        "product_id": 48,
        "url": "https://uncrate.com/assets_c/2022/10/herman-miller-nelson-fireplace-toolkit-5-thumb-960xauto-152268.jpg"
    },
    {
        "id": 289,
        "product_id": 48,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/herman-miller-nelson-fireplace-toolkit-6.jpg?v=1664810003"
    },
    {
        "id": 290,
        "product_id": 49,
        "url": "https://uncrate.com/assets_c/2022/11/porsche-356-nose-print-white-1-thumb-960xauto-154584.jpg"
    },
    {
        "id": 291,
        "product_id": 49,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/porsche-356-nose-print-black-2.jpg?v=1668782455"
    },
    {
        "id": 292,
        "product_id": 50,
        "url": "https://uncrate.com/assets_c/2022/10/filson-black-checkered-wool-blanket-1-thumb-960xauto-152357.jpg"
    },
        {
        "id": 293,
        "product_id": 50,
        "url": "https://uncrate.com/assets_c/2022/10/filson-black-checkered-wool-blanket-21-thumb-960xauto-152363.jpg"
    },
        {
        "id": 294,
        "product_id": 50,
        "url": "https://uncrate.com/assets_c/2022/10/filson-black-checkered-wool-blanket-3-thumb-960xauto-152359.jpg"
    },
    {
        "id": 295,
        "product_id": 50,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/filson-plaid-wool-blanket-2.jpg?v=1668803655"
    },
    {
        "id": 296,
        "product_id": 51,
        "url": "https://uncrate.com/assets_c/2022/11/Ursula-TFSK-bond-print-white-1-thumb-960xauto-154347.jpg"
    },
    {
        "id": 297,
        "product_id": 51,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/Ursula-TFSK-bond-print-black-2.jpg?v=1668456324"
    },
        {
        "id": 298,
        "product_id": 52,
        "url": "https://uncrate.com/assets_c/2022/11/sean-connery-golfing-IPPI-white-1-thumb-960xauto-154316.jpg"
    },
    {
        "id": 299,
        "product_id": 52,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/sean-connery-golfing-IPPI-black-2.jpg?v=1668093935"
    },
        {
        "id": 300,
        "product_id": 53,
        "url": "https://uncrate.com/assets_c/2022/11/warhol-kpzn-print-white-1-thumb-960xauto-154182.jpg"
    },
    {
        "id": 301,
        "product_id": 53,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/warhol-kpzn-print-black-2.jpg?v=1668094807"
    },
    {
        "id": 302,
        "product_id": 54,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/onsen-x-uncrate-towel-set-1280.jpg?v=1543084220"
    },
    {
        "id": 303,
        "product_id": 54,
        "url": "https://uncrate.com/assets_c/2018/11/onsen-x-uncrate-towel-set-7-thumb-960xauto-92172.jpg"
    },
    {
        "id": 304,
        "product_id": 54,
        "url": "https://uncrate.com/assets_c/2018/11/onsen-uncrate-01-thumb-960xauto-92182.jpg"
    },
    {
        "id": 305,
        "product_id": 54,
        "url": "https://uncrate.com/assets_c/2018/11/onsen-x-uncrate-towel-set-6-thumb-960xauto-92168.jpg"
    },
    {
        "id": 306,
        "product_id": 54,
        "url": "https://uncrate.com/assets_c/2018/11/onsen-x-uncrate-towel-set-2-thumb-960xauto-92164.jpg"
    },
    {
        "id": 307,
        "product_id": 55,
        "url": "https://uncrate.com/assets_c/2022/11/nasa-ipwk-rocket-print-white-1-thumb-960xauto-153855.jpg"
    },
    {
        "id": 308,
        "product_id": 55,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/nasa-ipwk-rocket-print-black-2.jpg?v=1667571656"
    },
]
