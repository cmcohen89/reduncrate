from random import randint

products_etc = [
    {
        "id": 78,
        "title": "VINTAGE TENT FABRIC PET BED",
        "description": "Recycled military tents give these pet beds a utilitarian aesthetic. $90.",
        "detailed_description": "For the Vintage Tent Fabric Pet Bed, not only are the materials repurposed but so is the design. The shape is inspired by cloth buckets soldiers laid down when taking showers outside. It's handmade using old tents sold by the military, giving it a worn, utilitarian look. Due to the reclaimed nature of the fabric, the product may show slight imperfections and color differences, giving each piece its own unique character.",
        "category_id": 8,
        "owner_id": randint(1, 3),
        "price": 90,
        "preview_img_id": 78,
    },
    {
        "id": 79,
        "title": "TINKERING LABS ELECTRIC MOTORS TOY KIT",
        "description": "Over 50 pieces, 10 challenges, and illustrated instructions make this STEM kit ideal for kids 8+. $65.",
        "detailed_description": "Get the younglings in your life a gift that will occupy their time as well as their brain with this kit from Tinkering Labs. It includes over 50 wooden parts, connectors, and motors, as well as a storage bag, safety goggles, and batteries. 10 challenge cards give kids specific things to try and build, while the 21-page guide provides step-by-step instructions for younger builders. Suitable for ages 8 and up.",
        "category_id": 8,
        "owner_id": randint(1, 3),
        "price": 65,
        "preview_img_id": 79,
    },
    {
        "id": 80,
        "title": "INVESTING IN WRISTWATCHES: ROLEX",
        "description": "Written by experts with pricing info gleaned from Sotheby's, this reference covers 385 Rolex models. $95.",
        "detailed_description": "The value of watches has exploded in recent years, leading many to explore vintage examples as investment vehicles. Investing in Wristwatches: Rolex is an excellent intro for anyone looking to start buying into the Crown. It covers the most popular and important Rolex references, with each description accompanied by a photo and sales history — the latter compiled with help from Sotheby's. Written by experts Osvaldo Patrizzi and Mara Cappelletti, it covers 385 models in total, with an introduction from Daryn F. Schnipper, Chairman of Sotheby's International Watch Division.",
        "category_id": 8,
        "owner_id": randint(1, 3),
        "price": 95,
        "preview_img_id": 80,
    },
    {
        "id": 81,
        "title": "1000 DESIGN CLASSICS",
        "description": "A exploration of iconic items, objects, and products of the last three centuries. $90.",
        "detailed_description": "From everyday items to innovative pieces, 1000 Design Classics highlights the iconic objects of the last three hundred years. It starts in 1663 and works its way to the present day, featuring influential products from legends like Charles and Ray Eames, Dieter Rams, and Florence Knoll, modern designers Le Corbusier, Alvar and Aino Aalto, and Isamu Noguchi, and unknown creators. Each item is accompanied by vivid imagery and a thoughtful description that details the product, its history, and its maker. Equal parts insightful and inspiring, the book is an ideal give for design enthusiasts and creatives alike.",
        "category_id": 8,
        "owner_id": randint(1, 3),
        "price": 90,
        "preview_img_id": 81,
    },
    {
        "id": 82,
        "title": "THOMAS KELLER K+M HOT CHOCOLATE",
        "description": "Rich, intense, and nutty in flavor, this bean-to-cup hot chocolate is a new winter tradition. $24.",
        "detailed_description": "First, Michelin-star chef Thomas Keller and olive oil producer Armando Manni took the chocolate bar to another level. Now, they're using that same formula to elevate a holiday tradition with their bean-to-cup hot chocolate. Made with the same high-quality cocoa beans used in the Extravirgin bars, the K+M chocolatiers have crafted a cozy blend that delivers intense chocolate flavor with a rich creaminess and light nuttiness that's primed for nights sitting fireside.",
        "category_id": 8,
        "owner_id": randint(1, 3),
        "price": 24,
        "preview_img_id": 82,
    },
    {
        "id": 83,
        "title": "POPCORN ON THE COB",
        "description": "Start a new holiday tradition with an age old technique of popping popcorn straight from the cob. $25.",
        "detailed_description": "Grown fresh in Utah, this old-fashioned popcorn on the cob delivers the classic snack in its simplest form. The corn is raised in four varieties — red, blue, yellow, or calico — and hand-picked during the fall harvest after the sweet kernels have dried to perfection. Unlike the loose varieties, each ear is packaged with the popcorn kernels intact until you're ready to enjoy it. To prepare, place one entire whole cob into the included popping bag and then microwave into a satisfying snack that's just different enough from the regular popcorn experience to make movie night even better. We highly suggest having some real butter and salt handy after popping to enhance the flavor.",
        "category_id": 8,
        "owner_id": randint(1, 3),
        "price": 25,
        "preview_img_id": 83,
    },
    {
        "id": 84,
        "title": "PRIDE & GROOM LUXE GIFT SET",
        "description": "A coat-specific assortment of all-natural grooming products to keep pets fresh and clean. $70.",
        "detailed_description": "For the furrier friends on your list, there's the Pride & Groom Luxe Gift Set. The sleek, black box includes an assortment of shampoo, conditioner, and a signature scent that leaves pups so fresh and so clean. Available in two coat-specific formulas — The Shedder is for dogs fur and The Non-Shedder for those with hair — each product is chemical-free and made with natural ingredients, including flaxseed, avocado oil, and jojoba seed, to nourish your pup's coat, while calendula extract, marshmallow root, and coconut oil hydrate the skin, soothes irritation, and kills bacteria.",
        "category_id": 8,
        "owner_id": randint(1, 3),
        "price": 70,
        "preview_img_id": 84,
    },
    {
        "id": 85,
        "title": "ERNEST HEMINGWAY BOOK SET",
        "description": "Produced exclusively for Reduncrate, this 10-book set freatures the legendary author's most famous works. $475.",
        "detailed_description": "One of the greatest novelists of the 20th Century, Ernest Hemingway's straightforward, no-nonsense style paved the way for a generation of writers who followed in his footsteps. This Uncrate-only ten-volume collection, updated to now include Hemingway's arguably most classic work, The Old Man and The Sea, is designed with the author's iconic signature and all black jackets that are sure to stand out on any bookshelf. Each book is from Scribner Classics, Hemingway's publisher while he was alive and publisher's of the best editions of his works to this day.",
        "category_id": 8,
        "owner_id": randint(1, 3),
        "price": 475,
        "preview_img_id": 85,
    },
    {
        "id": 86,
        "title": "PORSCHE 959",
        "description": "Explore the rich history of one of the greatest sports cars of the 1980s in this three-book set. $135.",
        "detailed_description": "It started as a Group B rally car. It became the world's fastest street-legal production car. The Porsche 959 is one of the Stuttgart-based firm's finest achievements, and it's celebrated in this set of three books. Penned by journalist Jürgen Lewandowski, each covers a separate topic. One covers technical data, like the specs of the twin-turbo flat-six engine and all-wheel-drive system, while another concerns its history, including its development, win at the Paris-Dakar rally, and production run. Those are joined by a large-format illustrated book packed with photos of its genesis, all its various derivatives, and one of the most well-preserved examples.",
        "category_id": 8,
        "owner_id": randint(1, 3),
        "price": 135,
        "preview_img_id": 86,
    },
    {
        "id": 87,
        "title": "SHINGLE AND STONE",
        "description": "A 280-page monograph dedicated to the work of architect Thomas Kligerman. $75.",
        "detailed_description": "Thomas Kligerman grew up in Connecticut and New Mexico, then spent time in France and England while studying at Columbia and Yale. His time in these unique locations influences his interest in vernacular architecture, leading him to create his own style. His designs fuse the high desert designs of the Southwest and the shingle-clad residences of New England. Shingle and Stone examines the renowned architect's signature aesthetic and its evolution throughout his career. Featuring plans, renderings, and sketches, the book showcases 13 of Kligerman's projects, ranging from seaside dwelling on Martha's Vineyard and the Hamptons to the rural retreats in the Pacific Northwest. It's written by the architect himself in collaboration with design editor Mitchell Owens and includes over 200 inspiring images.",
        "category_id": 8,
        "owner_id": randint(1, 3),
        "price": 75,
        "preview_img_id": 87,
    },
    {
        "id": 88,
        "title": "BUILD YOUR OWN SKELETON",
        "description": "This self-explanatory title gives you the precut pieces and instructions needed to build a life-size skeleton. $40.",
        "detailed_description": "It's appropriate Halloween decor, to be sure, but the rack of bones that comes out of Build Your Own Skeleton is useful for more than just decoration. Each life-size piece is precut, so all that's needed to assemble the skeleton is some folding and instruction-following. The joints are bendable, the parts are anatomically labeled in both English and Latin, and the result is a full-size human ready for posing, staging, or study.",
        "category_id": 8,
        "owner_id": randint(1, 3),
        "price": 40,
        "preview_img_id": 88,
    },
]

products_etc_imgs = [
    {
        "id": 78,
        "product_id": 78,
        "url": "https://uncrate.com/assets_c/2022/12/vintage-tent-fabric-pet-bed-1-thumb-960xauto-155229.jpg",
    },
    {
        "id": 79,
        "product_id": 79,
        "url": "https://uncrate.com/assets_c/2020/11/tinkering-labs-electric-motor-catalyst-3-thumb-960xauto-124743.jpg",
    },
    {
        "id": 80,
        "product_id": 80,
        "url": "https://uncrate.com/assets_c/2021/12/investing-in-wristwatches-1-thumb-960xauto-141082.jpg",
    },
    {
        "id": 81,
        "product_id": 81,
        "url": "https://uncrate.com/assets_c/2022/11/phaidon-1000-design-classics-1-thumb-960xauto-155043.jpg",
    },
    {
        "id": 82,
        "product_id": 82,
        "url": "https://uncrate.com/assets_c/2021/11/thomas-keller-hot-chocolate-1-thumb-960xauto-139813.jpg",
    },
    {
        "id": 83,
        "product_id": 83,
        "url": "https://uncrate.com/assets_c/2021/05/petersens-microwavable-corn-cob-5-thumb-960xauto-132106.jpg",
    },
    {
        "id": 84,
        "product_id": 84,
        "url": "https://uncrate.com/assets_c/2021/11/Pride-and-Groom-Shedder-Shampoo-1-thumb-960xauto-140118.jpg",
    },
    {
        "id": 85,
        "product_id": 85,
        "url": "https://uncrate.com/assets_c/2020/03/hemingway-custom-book-set-1-thumb-960xauto-112802.jpg",
    },
    {
        "id": 86,
        "product_id": 86,
        "url": "https://uncrate.com/assets_c/2022/11/porsche-959-book-1-thumb-960xauto-154560.jpg",
    },
    {
        "id": 87,
        "product_id": 87,
        "url": "https://uncrate.com/assets_c/2022/11/shingles-and-stones-1-thumb-960xauto-154519.jpg",
    },
    {
        "id": 88,
        "product_id": 88,
        "url": "https://uncrate.com/assets_c/2019/10/build-your-own-skeleton-21-thumb-960xauto-106488.jpg",
    },
    {
        "id": 399,
        "product_id": 78,
        "url": "https://uncrate.com/assets_c/2022/12/vintage-tent-fabric-pet-bed-4-thumb-960xauto-155232.jpg"
    },
    {
        "id": 400,
        "product_id": 78,
        "url": "https://uncrate.com/assets_c/2022/12/vintage-tent-fabric-pet-bed-2-thumb-960xauto-155230.jpg"
    },
    {
        "id": 401,
        "product_id": 78,
        "url": "https://uncrate.com/assets_c/2022/12/vintage-tent-fabric-pet-bed-3-thumb-960xauto-155231.jpg"
    },
    {
        "id": 402,
        "product_id": 78,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/vintage-tent-fabric-pet-bed-5.jpg?v=1670343945"
    },
        {
        "id": 403,
        "product_id": 79,
        "url": "https://uncrate.com/assets_c/2020/11/tinkering-labs-electric-motor-catalyst-4-thumb-960xauto-124742.jpg"
    },
        {
        "id": 404,
        "product_id": 79,
        "url": "https://uncrate.com/assets_c/2020/11/tinkering-labs-electric-motor-catalyst-2-thumb-960xauto-124741.jpg"
    },
        {
        "id": 405,
        "product_id": 79,
        "url": "https://uncrate.com/assets_c/2020/11/tinkering-labs-electric-motor-catalyst-1-thumb-960xauto-124740.jpg"
    },
    {
        "id": 406,
        "product_id": 79,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/tinkering-labs-electric-motor-catalyst-21.jpg?v=1669066557"
    },
    {
        "id": 407,
        "product_id": 80,
        "url": "https://uncrate.com/assets_c/2021/12/investing-in-wristwatches-3-thumb-960xauto-141085.jpg"
    },
    {
        "id": 408,
        "product_id": 80,
        "url": "https://uncrate.com/assets_c/2021/12/investing-in-wristwatches-4-thumb-960xauto-141084.jpg"
    },
    {
        "id": 409,
        "product_id": 80,
        "url": "https://uncrate.com/assets_c/2021/12/investing-in-wristwatches-2-thumb-960xauto-141083.jpg"
    },
    {
        "id": 410,
        "product_id": 80,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/investing-in-wristwatches-5.jpg?v=1638980095"
    },
    {
        "id": 411,
        "product_id": 81,
        "url": "https://uncrate.com/assets_c/2022/11/phaidon-1000-design-classics-2-thumb-960xauto-155044.jpg"
    },
    {
        "id": 412,
        "product_id": 81,
        "url": "https://uncrate.com/assets_c/2022/11/phaidon-1000-design-classics-3-thumb-960xauto-155046.jpg"
    },
    {
        "id": 413,
        "product_id": 81,
        "url": "https://uncrate.com/assets_c/2022/11/phaidon-1000-design-classics-4-thumb-960xauto-155047.jpg"
    },
    {
        "id": 414,
        "product_id": 81,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/phaidon-1000-design-classics-5.jpg?v=1669832484"
    },
    {
        "id": 415,
        "product_id": 82,
        "url": "https://uncrate.com/assets_c/2021/11/thomas-keller-hot-chocolate-2-thumb-960xauto-139814.jpg"
    },
    {
        "id": 416,
        "product_id": 82,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/thomas-keller-hot-chocolate-3.jpg?v=1636652156"
    },
    {
        "id": 417,
        "product_id": 83,
        "url": "https://uncrate.com/assets_c/2021/05/petersens-microwavable-corn-cob-2-thumb-960xauto-132105.jpg"
    },
    {
        "id": 418,
        "product_id": 83,
        "url": "https://uncrate.com/assets_c/2021/05/petersens-microwavable-corn-cob-6-thumb-960xauto-132107.jpg"
    },
    {
        "id": 419,
        "product_id": 83,
        "url": "https://uncrate.com/assets_c/2021/05/petersens-microwavable-corn-cob-3-thumb-960xauto-132103.jpg"
    },
    {
        "id": 420,
        "product_id": 83,
        "url": "https://uncrate.com/assets_c/2021/05/petersens-microwavable-corn-cob-4-thumb-960xauto-132104.jpg"
    },
    {
        "id": 421,
        "product_id": 83,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/petersens-microwavable-corn-cob-7.jpg?v=1622129379"
    },
    {
        "id": 422,
        "product_id": 84,
        "url": "https://uncrate.com/assets_c/2021/11/Pride-and-Groom-non-Shedder-Shampoo-1-thumb-960xauto-140120.jpg"
    },
    {
        "id": 423,
        "product_id": 84,
        "url": "https://uncrate.com/assets_c/2021/11/Pride-and-Groom-Shedder-Shampoo-2-thumb-960xauto-140117.jpg"
    },
    {
        "id": 424,
        "product_id": 84,
        "url": "https://uncrate.com/assets_c/2021/11/Pride-and-Groom-non-Shedder-Shampoo-2-thumb-960xauto-140119.jpg"
    },
    {
        "id": 425,
        "product_id": 84,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/Pride-and-Groom-Shedder-Shampoo-3.jpg?v=1637079283"
    },
    {
        "id": 426,
        "product_id": 85,
        "url": "https://uncrate.com/assets_c/2020/03/hemingway-custom-book-set-2-thumb-960xauto-112801.jpg"
    },
    {
        "id": 427,
        "product_id": 85,
        "url": "https://uncrate.com/assets_c/2020/03/hemingway-custom-book-set-12-thumb-960xauto-112812.jpg"
    },
    {
        "id": 428,
        "product_id": 85,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/hemingway-custom-book-set-13.jpg?v=1583791157"
    },
    {
        "id": 429,
        "product_id": 86,
        "url": "https://uncrate.com/assets_c/2022/11/porsche-959-book-2-thumb-960xauto-154561.jpg"
    },
    {
        "id": 430,
        "product_id": 86,
        "url": "https://uncrate.com/assets_c/2022/11/porsche-959-book-3-thumb-960xauto-154562.jpg"
    },
    {
        "id": 431,
        "product_id": 86,
        "url": "https://uncrate.com/assets_c/2022/11/porsche-959-book-4-thumb-960xauto-154563.jpg"
    },
    {
        "id": 432,
        "product_id": 86,
        "url": "https://uncrate.com/assets_c/2022/11/porsche-959-book-5-thumb-960xauto-154564.jpg"
    },
    {
        "id": 433,
        "product_id": 86,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/porsche-959-book-7.jpg?v=1668704045"
    },
    {
        "id": 434,
        "product_id": 87,
        "url": "https://uncrate.com/assets_c/2022/11/shingles-and-stones-2-thumb-960xauto-154520.jpg"
    },
    {
        "id": 435,
        "product_id": 87,
        "url": "https://uncrate.com/assets_c/2022/11/shingles-and-stones-3-thumb-960xauto-154521.jpg"
    },
    {
        "id": 436,
        "product_id": 87,
        "url": "https://uncrate.com/assets_c/2022/11/shingles-and-stones-4-thumb-960xauto-154522.jpg"
    },
    {
        "id": 437,
        "product_id": 87,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/shingles-and-stones-5.jpg?v=1668695265"
    },
    {
        "id": 438,
        "product_id": 88,
        "url": "https://uncrate.com/assets_c/2019/10/build-your-own-skeleton-1-thumb-960xauto-106467.jpg"
    },
    {
        "id": 439,
        "product_id": 88,
        "url": "https://uncrate.com/assets_c/2019/10/build-your-own-skeleton-3-thumb-960xauto-106468.jpg"
    },
    {
        "id": 440,
        "product_id": 88,
        "url": "https://uncrate.com/assets_c/2019/10/build-your-own-skeleton-4-thumb-960xauto-106469.jpg"
    },
    {
        "id": 441,
        "product_id": 88,
        "url": "https://uncrate.com/assets_c/2019/10/build-your-own-skeleton-5-thumb-960xauto-106471.jpg"
    },
    {
        "id": 442,
        "product_id": 88,
        "url": "https://cdn.shopify.com/s/files/1/0248/6216/products/build-your-own-skeleton-8.jpg?v=1571413426"
    },
]
