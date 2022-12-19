import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { getProducts } from '../../store/all_products';
import { putProductImage, postProductImage } from '../../store/one_product';

const ImageForm = ({ modalData, setShowEditModal, setShowEditMainModal, setShowAddModal, formType }) => {
  const dispatch = useDispatch();
  const [url, setUrl] = useState('');
  const [errors, setErrors] = useState([]);

  const handleEdit = async e => {
    e.preventDefault();
    const updatedProductImage = await dispatch(putProductImage(modalData, url));
    if (updatedProductImage) {
      updatedProductImage.errors
        ? setErrors(updatedProductImage.errors)
        : await dispatch(getProducts()).then(() =>
          formType === 'edit' ? setShowEditModal(false) : setShowEditMainModal(false)
        );
    }
  };

  const handleCreate = async e => {
    e.preventDefault();
    const newProductImage = await dispatch(postProductImage(modalData, url));
    if (newProductImage) {
      newProductImage.errors
        ? setErrors(newProductImage.errors)
        : await dispatch(getProducts()).then(() => setShowAddModal(false));
    }
  };

  return (
    <form
      className='image-form'
      onSubmit={formType === 'create' ? handleCreate : handleEdit}
    >
      {errors.length > 0 ? (
        <ul className='image-form-header-errors'>
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>
      ) : (
        <h2 className='image-form-header'>
          {formType === 'create' ? 'Enter an image URL' : 'Enter a new image URL'}
        </h2>
      )}
      <div className='url-container'>
        <label htmlFor='url-input'>URL</label>
        <input
          className='url-input'
          onChange={e => setUrl(e.target.value)}
          name='url-input'
          placeholder='Enter a new image URL...'
          type='text'
          value={url}
        />
      </div>
      <button
        className='image-submit-btn'
        type='submit'
      >
        {formType === 'create' ? 'ADD IMAGE' : 'EDIT IMAGE'}
      </button>
    </form>
  );
};

export default ImageForm;
