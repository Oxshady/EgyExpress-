import { useState, useEffect } from "react";
import { fetchWithAuth } from "../http";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import "../css/Order.css"
function Order() {
  const url_api = "http://localhost:5000/order";
  const navigate = useNavigate();
  const orderitems = useSelector((state)=>state.cart.cartItems);
  const [error, setError] = useState(null);
  const [total, setTotal] = useState(0);
  const [paymentType, setPaymentType] = useState("");
  const [address, setAddress] = useState("");

    useEffect(() => {
    console.log(orderitems);
  }, [orderitems]);

    useEffect(() => {
      const calculatedTotal = orderitems.reduce(
        (acc, item) => acc + item.price * item.quantity,
        0
      );
      setTotal(calculatedTotal);
    }, [orderitems]);

      const HandleConfirm = () => {
        const order_mi_item = {
          payment_type: paymentType,
          delivery_address: address,
          total_price: total,
        };
        fetch(url_api, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(order_mi_item),
        })
          .then((res) => res.json())
          .then((data) => {
            console.log(data);
          })
          .catch((error) => {
            console.error("error");
          });
          alert("Order Confirmed");
          navigate("/tracking");
        };
  return (
    <>
      <div className="order_items">
        {error ? (
          <h2>{error}</h2>
        ) : orderitems.length === 0 ? (
          <h2>Cart is empty</h2>
        ) : (
          orderitems.map((item) => (
            <div className="cart_item" key={item.product_id}>
              <div>
                <h3>{item.product_id}</h3>
                <p>Price: ${item.price}</p>
                <p>Quantity: {item.quantity}</p>
              </div>
            </div>
          ))
        )}
        <div className="total">Total: ${total}</div>
        <div className="payment">
          <form onSubmit={HandleConfirm}>
            <label>Payment Type</label>
            <select
              value={paymentType}
              onChange={(e) => setPaymentType(e.target.value)}
            >
              <option value="cash">Cash</option>
              <option value="visa">visa</option>
            </select>
            <label> Shipping Adress</label>
            <input
              type="text"
              required
              onChange={(e) => setAddress(e.target.value)}
            />
            {error && <p>{error}</p>}
            <button type="submit" className="confirm">
              Confirm
            </button>
          </form>
        </div>
      </div>
    </>
  );
}
export default Order;
