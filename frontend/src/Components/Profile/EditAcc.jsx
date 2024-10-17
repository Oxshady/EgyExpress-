import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./EditAcc.css";
import { fetchWithAuth } from "../../http";

function EditAcc() {
  const options = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };
  const navigate = useNavigate();
  const [accountInfo, setAccountInfo] = useState({
    first_name: "",
    last_name: "",
    email: "",
    address: "",
    phoneNumber: "",
  });
  const [originalInfo, setOriginalInfo] = useState({});

  useEffect(() => {
    // Fetch the current account information and set it to state
    const fetchAccountInfo = async () => {
      const data = await fetchWithAuth(
        "http://localhost:5000/api/profile",
        options
      );
      setAccountInfo(data);
      setOriginalInfo(data);
    };

    fetchAccountInfo();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setAccountInfo((prevInfo) => ({
      ...prevInfo,
      [name]: value,
    }));
  };
  console.log("accoutn ingo");
  console.log();
  console.log(accountInfo);
  const handleSubmit = async (e) => {
    e.preventDefault();
    const options2 = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: accountInfo,
    };
    // Submit the updated account information
    const response = await fetchWithAuth(
      "http://localhost:5000/api/profile/edit",
      options2
    );
    navigate("/profile");
  };

  const isModified = (field) => accountInfo[field] !== originalInfo[field];

  return (
    <div className="edit-account-container">
      <h1>Edit Account Information</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="firstName">First Name</label>
          <input
            type="text"
            id="firstName"
            name="first_name"
            value={accountInfo.first_name}
            onChange={handleChange}
            className={isModified("firstName") ? "modified" : ""}
          />
        </div>
        <div className="form-group">
          <label htmlFor="lastName">Last Name</label>
          <input
            type="text"
            id="lastName"
            name="last_name"
            value={accountInfo.last_name}
            onChange={handleChange}
            className={isModified("lastName") ? "modified" : ""}
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            value={accountInfo.email}
            onChange={handleChange}
            className={isModified("email") ? "modified" : ""}
          />
        </div>
        <div className="form-group">
          <label htmlFor="address">Address</label>
          <input
            type="text"
            id="address"
            name="address"
            value={accountInfo.address}
            onChange={handleChange}
            className={isModified("address") ? "modified" : ""}
          />
        </div>
        <div className="form-group">
          <label htmlFor="phone">Phone</label>
          <input
            type="text"
            id="phone"
            name="phone_number"
            value={accountInfo.phone_number}
            onChange={handleChange}
            className={isModified("phone") ? "modified" : ""}
          />
        </div>
        <button type="submit" className="btn-edit-account">
          Save Changes
        </button>
      </form>
    </div>
  );
}

export default EditAcc;
