/* ------------------------- ACTIONS ------------------------- */

const LOAD_FAVORITES = "favorites/LOAD";
const CREATE_FAVORITE = "favorites/NEW";
const DELETE_FAVORITE = "favorites/DELETE";

export const loadFavorites = (favorites) => {
    return {
        type: LOAD_FAVORITES,
        favorites,
    };
};

export const createFavorite = (favorite) => {
    return {
        type: CREATE_FAVORITE,
        favorite,
    };
};

export const removeFavorite = (favoriteId) => {
    return {
        type: DELETE_FAVORITE,
        favoriteId,
    };
};

/* ------------------------- THUNKS ------------------------- */

export const addToFavorites = (productId) => async (dispatch) => {
    const response = await fetch("/api/favorites", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            productId: productId,
        }),
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(createFavorite(data));
        return data;
    }
    return response;
};

export const getFavorites = (userId) => async (dispatch) => {
    const response = await fetch(`/api/favorites/${userId}`);

    if (response.ok) {
        const favorites = await response.json();
        dispatch(loadFavorites(favorites));
        return favorites;
    };
};

export const deleteFavorite = (favoriteId) => async dispatch => {
    const response = await fetch(`/api/favorites/${favoriteId}`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
    });

    if (response.ok) {
        const deletedMessage = await response.json();
        dispatch(removeFavorite(favoriteId))
        return deletedMessage;
    };
};

/* ------------------------- REDUCER ------------------------- */

const initialState = {};

const allFavoritesReducer = (state = initialState, action) => {
    const newState = { ...state }
    switch (action.type) {
        case LOAD_FAVORITES:
            return action.favorites.Favorites.reduce((favorites, favorite) => {
                favorites[favorite.id] = favorite;
                return favorites;
            }, {});
        case DELETE_FAVORITE:
            delete newState[action.favoriteId];
            return newState;
        default:
            return state;
    }
};

export default allFavoritesReducer;
