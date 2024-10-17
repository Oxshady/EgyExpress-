import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import Plus from "../../assests/plus.png";
import Minus from "../../assests/minus-sign.png";
import { useDispatch } from "react-redux";
import { addItemToCart } from "../../state/cartSlice";
import { useSelector } from "react-redux";
import "./ProdcutDetials.css";
import { fetchWithAuth } from "../../http";
import Review from "../Review/Review";
import ShowReview from "../Review/ShowReview";

function ProductDtials() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const params = useParams();
  const dispatch = useDispatch();
  const cartItems = useSelector((state) => state.cart.cartItems);
  const api_url = "http://127.0.0.1:5000/api/product";
  const [product, setProduct] = useState({});
  const [counter, setCounter] = useState(1);
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
  const [isMessageVisible, setIsMessageVisible] = useState(false);
  const post_url = "http://localhost:5000/api/cart";

  useEffect(() => {
    fetch(`${api_url}/${params.productId}`)
      .then((res) => res.json())
      .then((data) => setProduct(data));
  }, []);

  useEffect(() => {
    console.log("cart item changed");
    console.log(cartItems);
  }, [cartItems]);

  const handleInc = () => {
    setCounter(counter + 1);
  };

  const handleDec = () => {
    if (counter > 1) {
      setCounter(counter - 1);
    }
  };

  const cartItem = {
    product_id: product.id,
    quantity: counter,
    price: product.price * counter,
  };

  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: cartItem,
  };

  const handleAddToCart = () => {
    dispatch(addItemToCart(cartItem));
    if (!isAuthenticated) {
      alert("You are not logged in");
      return;
    }
    fetchWithAuth(post_url, options)
      .then((data) => {
        console.log(data);
        setIsMessageVisible(true);
        setTimeout(() => {
          setIsMessageVisible(false);
        }, 3000);
      })
      .catch((error) => {
        console.error("error");
      });

  };

  const handleCloseMessage = () => {
    setIsMessageVisible(false);
  };

  const toggleModal = () => {
    setIsModalOpen(!isModalOpen);
  };

  console.log(product);
  console.log("-------");

  return (
    <div className="product_details">
      <h1>Product details {product.title}</h1>
      <div className="product_info">
        <img src={product.image} alt={product.title} />
        <div>
          <p>Category: {product.category}</p>
          <p>{product.description}</p>
          <div className="counter">
            <button onClick={handleDec}>
              <img src={Minus} alt="minus" />
            </button>
            <span>{counter}</span>
            <button onClick={handleInc}>
              <img src={Plus} alt="plus" />
            </button>
          </div>
          <button className="AddBtn" onClick={handleAddToCart}>
            Add to Cart
          </button>
          {isAuthenticated && (
            <button className="AddReviewBtn" onClick={toggleModal}>
              Add review
            </button>
          )}
          {isModalOpen && (
            <Review
              onClose={toggleModal}
              isOpen={isModalOpen}
              productId={product.id}
            />
          )}
          {isMessageVisible && (
            <div className="popout-message">
              <span>The product has been added to your cart successfully</span>
              <button className="close-btn" onClick={handleCloseMessage}>
                Close
                &times;
              </button>
            </div>
          )}
        </div>
      </div>
      <div className="review_section">
        <ShowReview product={product.id} />
      </div>
    </div>
  );
}

export default ProductDtials;
