import { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { BiArrowBack } from 'react-icons/bi';
import './ProductForm.css';

const ProductForm = ({
  product,
  formType,
  handleSubmit,
  title,
  setTitle,
  description,
  setDescription,
  detailed_description,
  set_detailed_description,
  category_id,
  set_category_id,
  price,
  setPrice,
  preview_img_url,
  set_preview_img_url,
  errors,
  setErrors
}) => {
  const history = useHistory();
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    formType === 'update' ? product && setIsLoaded(true) : setIsLoaded(true);
    formType === 'update' && setTitle(product?.title);
    formType === 'update' && setDescription(product?.description);
    formType === 'update' && set_detailed_description(product?.detailedDescription);
    formType === 'update' && product && set_category_id(product?.categoryId);
    formType === 'update' && setPrice(product?.price);
  }, [
    product?.title,
    product?.description,
    product?.detailedDescription,
    product?.categoryId,
    product?.price,
    setTitle,
    setDescription,
    set_detailed_description,
    set_category_id,
    setPrice,
    product,
    formType
  ]);

  if (!isLoaded) return null;

  return (
    <>
      {isLoaded && (
        <div className='product-form-container'>
          <form
            className='product-form'
            onSubmit={handleSubmit}
          >
            {errors.length > 0 ? (
              <ul className='product-form-header-errors'>
                {errors.map((error, idx) => (
                  <li key={idx}>{error}</li>
                ))}
              </ul>
            ) : (
              <div className='product-form-header'>
                <button
                  onClick={() => history.goBack()}
                  className='back-btn'
                >
                  <BiArrowBack size={25} />
                </button>
                <h2>{formType === 'create' ? 'Product Details' : 'Change Product Details'}</h2>
                <div className='hidden-spacer'></div>
              </div>
            )}

            <div className='inputs-container'>
              <div className='title-container'>
                <label htmlFor='title-input'>TITLE</label>
                <input
                  className='title-input'
                  onChange={e => setTitle(e.target.value)}
                  name='title-input'
                  placeholder='Give your product a title here.'
                  required
                  type='text'
                  value={title}
                />
              </div>
              <div className='description-container'>
                <label htmlFor='desctiption-input'>DESCRIPTION</label>
                <input
                  className='description-input'
                  onChange={e => setDescription(e.target.value)}
                  name='description-input'
                  placeholder='Tell us a little bit about it.'
                  required
                  type='text'
                  value={description}
                />
              </div>
              <div className='detailed-description-container'>
                <label htmlFor='detailed-description-input'>DETAILS</label>
                <textarea
                  className='detailed-description-input'
                  onChange={e => set_detailed_description(e.target.value)}
                  name='detailed-description-input'
                  placeholder='Now tell us a lot more about it.'
                  value={detailed_description}
                />
              </div>
              <div className='category-container'>
                <label htmlFor='category-input'>CATEGORY</label>
                <select
                  className='category-input'
                  onChange={e => set_category_id(e.target.value)}
                  name='category-input'
                  required
                  value={category_id}
                >
                  <option
                    value={category_id === 0 ? category_id : ''}
                    disabled
                    hidden
                  >
                    Select a Category
                  </option>
                  <option value='1'>Gear</option>
                  <option value='2'>Style</option>
                  <option value='3'>Cars</option>
                  <option value='4'>Tech</option>
                  <option value='5'>Shelter</option>
                  <option value='6'>Vices</option>
                  <option value='7'>Body</option>
                  <option value='8'>Etc</option>
                </select>
              </div>
              <div className='price-container'>
                <label htmlFor='price-input'>PRICE</label>
                <input
                  className='price-input'
                  min={0}
                  onChange={e => setPrice(e.target.value)}
                  placeholder="Don't be afraid to price gouge."
                  required
                  type='number'
                  value={price}
                />
              </div>
              {formType === 'create' && (
                <div className='preview-img-container'>
                  <label htmlFor='preview-img-input'>MAIN IMAGE</label>
                  <input
                    className='preview-img-input'
                    onChange={e => set_preview_img_url(e.target.value)}
                    placeholder='Show us a pretty picture.'
                    required
                    type='text'
                    value={preview_img_url}
                  />
                </div>
              )}
              <button
                className='product-form-submit'
                type='submit'
              >
                SUBMIT
              </button>
            </div>
          </form>
        </div>
      )}
    </>
  );
};
export default ProductForm;
