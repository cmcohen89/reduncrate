import { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux';
import { getCart } from '../../store/cart';
import { editCartItem } from '../../store/cart_items';

const SelectField = ({ currentItem }) => {
  const dispatch = useDispatch();
  const [quantity, setQuantity] = useState(currentItem.quantity);
  const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  useEffect(() => {
    (async function fetchQuantity() {
      await dispatch(editCartItem(currentItem, quantity));
      dispatch(getCart());
    })()
  }, [quantity, dispatch]);

  return (
    <>
      <form>
        <label htmlFor='quantity-input'></label>
        <select
          className='cart-quantity-form'
          required
          onChange={e => setQuantity(e.target.value)}
          name='quantity-input'
          value={currentItem.quantity}
        >
          {nums.map((num, idx) => (
            <option
              key={idx}
              value={num}
            >
              {num}
            </option>
          ))}
        </select>
        <br />
      </form>
    </>
  );
};
export default SelectField;
