import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { AiTwotoneEdit } from "react-icons/ai";
import { AiOutlinePlusCircle } from "react-icons/ai";
import { BiArrowBack } from "react-icons/bi";
import { MdDelete } from "react-icons/md";
import { getProducts } from "../../store/all_products";
import { Modal } from "../../context/Modal";
import ImageForm from "./ImageForm";
import SupplyNavBar from "../SingleProduct/SupplyNavBar/SupplyNavBar";

import "./UserProductsImages.css";
import { deleteProductImage } from "../../store/one_product";

const UserProductsImages = () => {
  const history = useHistory();
  const dispatch = useDispatch();
  const { id } = useParams();
  const products = useSelector((state) => state.products);
  const product = products[id];
  const [showEditMainModal, setShowEditMainModal] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);
  const [showAddModal, setShowAddModal] = useState(false);
  const [modalData, setModalData] = useState(null);

  useEffect(() => {
    dispatch(getProducts());
  }, [dispatch]);

  if (!product) return null;

  // Add all but the main image into an array:
  let productImageUrls = [];
  for (const image in product.productImages) {
    if (
      product.productImages[image].id !== product.previewImgId &&
      !product.productImages[image].url.includes("shopify")
    ) {
      productImageUrls.push(product.productImages[image]);
    }
  }

  return (
    <>
      <SupplyNavBar />
      <div className="add-edit-image-form">
        <div className="add-edit-image-header">
          <button onClick={() => history.goBack()} className="back-btn">
            <BiArrowBack size={25} />
          </button>
          <header>Add or Edit an Image</header>
          <button
            className="add-image-btn"
            onClick={() => {
              setModalData(product.id);
              setShowAddModal(true);
            }}
          >
            <AiOutlinePlusCircle size={30} />
          </button>
          {showAddModal && (
            <Modal onClose={() => setShowAddModal(false)}>
              <ImageForm
                modalData={modalData}
                formType={"create"}
                setShowAddModal={setShowAddModal}
              />
            </Modal>
          )}
        </div>

        <div
          className="main-image"
          style={{
            backgroundImage: `url("${product.productImages[product.previewImgId].url
              }")`,
          }}
        >
          <p className="title">Main Product Image</p>
          <div className="overlay"></div>
          <button
            className="main-image-edit-btn"
            onClick={() => {
              setModalData(product.productImages[product.previewImgId].id);
              setShowEditMainModal(true);
            }}
          >
            <AiTwotoneEdit size={45} className="edit-icon" />
          </button>
          {showEditMainModal && (
            <Modal onClose={() => setShowEditMainModal(false)}>
              <ImageForm
                modalData={modalData}
                formType={"edit-main"}
                setShowEditMainModal={setShowEditMainModal}
              />
            </Modal>
          )}
        </div>

        <div className="product-images-container">
          {product ? (
            productImageUrls.map((image, idx) => (
              <div
                className="single-image-container"
                key={idx}
                style={{
                  backgroundImage: `url("${image.url}")`,
                }}
              >
                <div className="overlay"></div>
                <div className="buttons">
                  <button
                    className="delete-btn"
                    onClick={async () => {
                      await dispatch(deleteProductImage(image.id));
                      dispatch(getProducts());
                    }}
                  >
                    <MdDelete size={45} className="delete-icon" />
                  </button>
                  <button
                    className="edit-btn"
                    onClick={() => {
                      setModalData(image.id);
                      setShowEditModal(true);
                    }}
                  >
                    <AiTwotoneEdit size={45} className="edit-icon" />
                  </button>
                </div>
                {showEditModal && (
                  <Modal onClose={() => setShowEditModal(false)}>
                    <ImageForm
                      modalData={modalData}
                      formType={"edit"}
                      setShowEditModal={setShowEditModal}
                    />
                  </Modal>
                )}
              </div>
            ))
          ) : (
            <div>Loading...</div>
          )}
        </div>
      </div>
    </>
  );
};

export default UserProductsImages;
