import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { fetchWithAuth } from "../../http.js";
import Logout from "../Register/Logout.jsx";
import "./Profile.css";
const Profile = () => {
  const [userData, setUserData] = useState({});
  const navigate = useNavigate();
  const api_url = "http://localhost:5000/api/profile";
  const options = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  };
  // Fetch user profile data from API
  useEffect(() => {
    fetchWithAuth(api_url, options).then((data) => setUserData(data));
  }, []);

  if (!userData) {
    return <div>Loading...</div>; // Show a loading state while data is being fetched
  }
  console.log("User data:");
  console.log(userData);
  // Navigate to orders page
  const handleOrdersClick = () => {
    navigate("/tracking");
  };

  // Navigate to change password page
  const handleChangePasswordClick = () => {
    navigate("/change-password");
  };

  // Navigate to edit account page
  const handleEditAccountClick = () => {
    navigate("/edit-account");
  };
  const deleteacount = () => {
    navigate("/delete-acount");
  };
  return (
    <div className="profile-container">
      <div className="profile-continer-centered">
      <h1>Profile</h1>

      {/* Display User Information */}
      <div className="profile-info">
        <h2>
          {userData.first_name} {userData.last_name}
        </h2>
        <p>
          <strong>Email:</strong> {userData.email}
        </p>
        <p>
          <strong>Phone Number:</strong> {userData.phone_number}
        </p>
        <p>
          <strong>Address:</strong> {userData.address}
        </p>
      </div>

      {/* Orders Button */}
      <div className="profile-actions">
        <button className="profile-btn" onClick={handleOrdersClick}>
          View Current Orders
        </button>

        {/* Change Password Button */}
        <button className="profile-btn" onClick={handleChangePasswordClick}>
          Change Password
        </button>

        {/* Edit Account Information Button */}
        <button className="profile-btn" onClick={handleEditAccountClick}>
          Edit Account Info
        </button>
        <Logout />
        <button className="delete" onClick={deleteacount}>
          Delete Account
        </button>
      </div>
      </div>
    </div>
  );
};

export default Profile;
