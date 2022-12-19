/* ------------------------- ACTIONS ------------------------- */

const LOAD_SINGLE_PRODUCT = 'products/LOAD_SINGLE';
const UPDATE_SINGLE_PRODUCT = 'products/UPDATE_SINGLE';

export const loadSingleProduct = product => {
  return {
    type: LOAD_SINGLE_PRODUCT,
    product
  };
};

export const updateSingleProduct = updatedProduct => {
  return {
    type: UPDATE_SINGLE_PRODUCT,
    updatedProduct
  };
};

/* ------------------------- THUNKS -------------------------- */

export const getSingleProduct = productId => async dispatch => {
  const response = await fetch(`/api/products/${productId}`);

  if (response.ok) {
    const product = await response.json();
    dispatch(loadSingleProduct(product));
    return product;
  }
  if (response.ok) {
    const product = await response.json();
    dispatch(loadSingleProduct(product));
    return product;
  }
};

export const putSingleProduct = product => async dispatch => {
  const { title, description, detailed_description, category_id, price } = product;
  const response = await fetch(`/api/products/${product.id}/update`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, description, detailed_description, category_id, price })
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(updateSingleProduct(data));
    return data;
  }
  const data = await response.json();
  return data;
};

export const postProductImage = (productId, url) => async dispatch => {
  const response = await fetch(`/api/images/${productId}/new`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url })
  });

  if (response.ok) {
    const data = await response.json();
    return data;
  }
  const data = await response.json()
  return data;
};

export const deleteProductImage = productImageId => async dispatch => {
  const response = await fetch(`/api/images/${productImageId}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json'
    }
  });

  if (response.ok) {
    const deletedMsg = await response.json();
    return deletedMsg;
  }
};

export const putProductImage = (productImageId, url) => async dispatch => {
  const response = await fetch(`/api/images/${productImageId}/update`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ productImageId, url })
  });

  if (response.ok) {
    const data = await response.json();
    return data;
  }
  const data = await response.json()
  return data;
};

export const getProductById = id => state => state.products[id];

/* ------------------------- REDUCER ------------------------- */

const initialState = {};

const singleProductReducer = (state = initialState, action) => {
  switch (action.type) {
    case LOAD_SINGLE_PRODUCT:
      return {
        ...state,
        [action.product.id]: { ...action.product }
      };
    case UPDATE_SINGLE_PRODUCT:
      return {
        ...state,
        [action.updatedProduct.id]: { ...action.updatedProduct }
      };
    default:
      return state;
  }
};

export default singleProductReducer;
