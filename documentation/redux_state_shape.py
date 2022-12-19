# "reduncrate" REDUX STORE STATE SHAPE

{
    # CARTS SLICE OF REDUX STATE:
    cart: {
        1: {
            id: 1,
            user_id: 1,
            total: 100,
            purchased: True,
            cartItems: {...},
            cartUser: (...),
            orderHistory: {...}
        },
        2: {
            id: 2,
            user_id: 2,
            total: 200,
            purchased: False,
            cartItems: {...},
            cartUser: (...),
            orderHistory: {...}
        },
    },

    # CART_ITEMS SLICE OF REDUX STATE:
    cart_items: {
        1: {
            id: 1,
            cart_id: 1,
            product_id: 1,
            quantity: 1,
            product: {...},
            cartImg: 'https://www.imageurl.com/img'
        },
        2: {
            id: 2,
            cart_id: 2,
            product_id: 2,
            quantity: 2,
            product: {...},
            cartImg: 'https://www.imageurl.com/img'
        },
    },

    # FAVORITES SLICE OF REDUX STATE:
    favorites: {
        1: {
            id: 1,
            title: 'Item title',
            categoryId: 7,
            description: "Item description",
            detailedDescription: "Detailed item description",
            previewImgId: 5,
            price: 65,
            productCategory: {...},
            productImages: {...},
            productOwner: {...}
        },
        2: {
            id: 2,
            title: 'Item title',
            categoryId: 4,
            description: "Item description",
            detailedDescription: "Detailed item description",
            previewImgId: 3,
            price: 530,
            productCategory: {...},
            productImages: {...},
            productOwner: {...}
        }
    },

    # PRODUCTS SLICE OF REDUX STATE:
    products: {
        1: {
            id: 1,
            title: 'Item title',
            categoryId: 7,
            description: "Item description",
            detailedDescription: "Detailed item description",
            previewImgId: 5,
            price: 65,
            productCategory: {...},
            productImages: {...},
            productOwner: {...}
        },
        2: {
            id: 2,
            title: 'Item title',
            categoryId: 4,
            description: "Item description",
            detailedDescription: "Detailed item description",
            previewImgId: 32,
            price: 234,
            productCategory: {...},
            productImages: {...},
            productOwner: {...}
        },
    },

    # SINGLE_PRODUCT SLICE OF REDUX STATE:
    product: {
        1: {
            id: 1,
            title: 'Item title',
            categoryId: 7,
            description: "Item description",
            detailedDescription: "Detailed item description",
            previewImgId: 5,
            price: 65,
            productCategory: {...},
            productImages: {...},
            productOwner: {...}
        },
    },

    # SESSION SLICE OF STATE:
    session: {
        user: {
            id: 1,
            first_name: "first_name",
            last_name: "last_name",
            username: "user_name",
            hashed_password: "password",
            email: "user@email.io",
        }
    },
