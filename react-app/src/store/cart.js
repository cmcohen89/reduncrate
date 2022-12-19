const LOAD_CART = 'carts/LOAD';
const PURCHASE_CART = 'carts/PURCHASE';
const LOAD_HISTORY = 'carts/HISTORY';

export const loadCart = (cart) => {
  return {
    type: LOAD_CART,
    cart
  }
}

export const loadCartHistory = (carts) => {
  return {
    type: LOAD_HISTORY,
    carts
  }
}

export const purchaseCartAction = (cart) => {
  return {
    type: PURCHASE_CART,
    cart
  }
}

export const getCart = () => async dispatch => {
  const response = await fetch(`/api/carts`);

  if (response.ok) {
    const cart = await response.json();
    dispatch(loadCart(cart));
    return cart;
  }
}

export const getCartHistory = () => async dispatch => {
  const response = await fetch(`/api/carts/history`);

  if (response.ok) {
    const carts = await response.json();
    dispatch(loadCartHistory(carts));
    return carts;
  }
}

export const purchaseCart = (total) => async dispatch => {
  const response = await fetch('/api/carts', {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ "total": total })
  })

  if (response.ok) {
    const cart = await response.json();
    dispatch(purchaseCartAction(cart));
    return cart;
  }
}

export const getCartById = (id) => (state) => state.cart[id];

const initialState = {};

const cartReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOAD_CART:
      return { ...action.cart, 'orderHistory': state.orderHistory };
    case PURCHASE_CART:
      return { [action.cart.id]: action.cart };
    case LOAD_HISTORY:
      return { ...state, 'orderHistory': action.carts.OrderHistory };
    default:
      return state;
  };
};

export default cartReducer;
