import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom';

import { getSingleProduct, putSingleProduct } from '../../store/one_product';
import ProductForm from './ProductForm';
import SupplyNavBar from '../SingleProduct/SupplyNavBar/SupplyNavBar';
import { useEffect } from 'react';

const ProductUpdateForm = () => {
  const history = useHistory();
  const dispatch = useDispatch();
  const { id } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    (async function fetchProduct() {
      const res = await dispatch(getSingleProduct(id));
      setProduct(res);
    })();
  }, [dispatch, id]);

  const [title, setTitle] = useState(product?.title);
  const [description, setDescription] = useState(product?.description);
  const [detailed_description, set_detailed_description] = useState(product?.detailedDescription);
  const [category_id, set_category_id] = useState(product?.categoryId);
  const [price, setPrice] = useState(product?.price);
  const [preview_img_url, set_preview_img_url] = useState(
    JSON.stringify(product?.productImages[product.previewImgId].url)
  );
  const [errors, setErrors] = useState([]);

  const handleSubmit = async e => {
    e.preventDefault();

    const updatedProduct = await dispatch(
      putSingleProduct({
        id: product.id,
        title,
        description,
        detailed_description,
        category_id,
        price
      })
    );

    if (updatedProduct) {
      updatedProduct.errors ? setErrors(updatedProduct.errors) : history.push(`/profile`);
    }
  };

  if (!product) return null;

  return (
    <>
      <SupplyNavBar />
      {product && (
        <ProductForm
          product={product}
          formType={'update'}
          handleSubmit={handleSubmit}
          title={title}
          setTitle={setTitle}
          description={description}
          setDescription={setDescription}
          detailed_description={detailed_description}
          category_id={category_id}
          set_category_id={set_category_id}
          set_detailed_description={set_detailed_description}
          price={price}
          setPrice={setPrice}
          preview_img_url={preview_img_url}
          set_preview_img_url={set_preview_img_url}
          errors={errors}
          setErrors={setErrors}
        />
      )}
    </>
  );
};

export default ProductUpdateForm;
