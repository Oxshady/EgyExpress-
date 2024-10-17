import React, { useState, useEffect } from "react";
import { fetchWithAuth } from "../../http";
import "./Tracking.css";

function Tracking() {
  const [orders, setOrders] = useState([]);
  const url = "http://localhost:5000/api/tracking";
  const options = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };
  useEffect(() => {
    fetchWithAuth(url, options).then((data) => setOrders(data)).then((data)=>console.log(data)).catch((error) => {
      console.error('Error fetching orders:', error);});
  }, []);

  return (
    <div className="tracking-container">
      <h1>Tracking</h1>
      {orders.map((order) => (
        <div key={order.order_id} className="order-card">
          <p>
            <strong>Order ID:</strong> {order.order_id}
          </p>
          <p>
            <strong>Shipping Adress:</strong> ${order.delivery_address}
          </p>
          <p
            className={`status ${
              order.status === "delivered" ? "delivered" : "not-delivered"
            }`}
          >
            <strong>Status:</strong> {order.status}
          </p>
        </div>
      ))}
    </div>
  );
}

export default Tracking;
