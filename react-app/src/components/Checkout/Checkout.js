import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom';
import { purchaseCart } from '../../store/cart';
import CategoriesNav from '../Navigation/CategoriesNav';
import Navigation from '../Navigation/Navigation';
import './Checkout.css';

const Checkout = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const cart = useSelector(state => state.cart);

  let totalPrice = 0;
  const usDollar = Intl.NumberFormat('en-US');

  let cartItems;
  if (cart && cart.cartItems) {
    cartItems = Object.values(cart.cartItems);
  }

  if (!cart || !cartItems) return null;

  return (
    <>
      <Navigation />
      <CategoriesNav />
      <div className='checkout-page'>
        <h1 className='checkout-title'>CHECKOUT</h1>
        <div className='checkout-items-container'>
          <div className='checkout-items'>
            {cartItems.map(item => (
              <div
                key={item.id}
                className='one-checkout-item'
              >
                <NavLink to={`/products/${item.product.id}`}>
                  <img
                    className='cart-item-image'
                    src={item.product.cartImgUrl ? item.product.cartImgUrl : item.product.productImages[item.product.previewImgId].url}
                    alt='cart item'
                  />
                </NavLink>
                <div className='checkout-item-title'>{item.product.title}</div>
                <div className='checkout-item-quantity-and-price'>
                  <div className='checkout-item-price'>
                    ${usDollar.format(item.product.price * item.quantity)}.00
                    {(totalPrice += item.product.price * item.quantity) && false}
                  </div>
                  <div className='checkout-item-quantity'>
                    QTY: <span className='checkout-quantity'>{item.quantity}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
          <div className='checkout-total-container'>
            <span className='checkout-total'>TOTAL</span>
            <span className='checkout-price'>USD ${usDollar.format(totalPrice)}</span>
          </div>
          <div className='cart-checkout-button-container'>
            <button
              className='cart-checkout-button'
              onClick={() => {
                dispatch(purchaseCart(totalPrice));
                history.push('/checkout/complete');
              }}
            >
              PURCHASE
            </button>
          </div>
        </div>
      </div>
    </>
  );
};

export default Checkout;
