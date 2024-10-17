import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./ChangePassword.css";
import { fetchWithAuth } from "../../http";

function ChangePassword() {
  const navigate = useNavigate();
  const api_url = "http://localhost:5000/api/profile/edit";
  const [error, setError] = useState("");
  const [passwd, setPasswd] = useState({
    old_password: "",
    new_password: "",
    confirm_password: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setPasswd({
      ...passwd,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (
      !passwd.old_password ||
      !passwd.new_password ||
      !passwd.confirm_password
    ) {
      setError("All fields are required.");
      return;
    }
    if (passwd.new_password !== passwd.confirm_password) {
      setError("Password doesn't match.");
      return;
    }
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: passwd,
    };
    fetchWithAuth(api_url, options)
      .then((data) => {
        if (data.error) {
          setError(data.error);
        } else {
          setError("");
          navigate("/profile");
        }
      })
      .catch((data) => setError("old password is incorrect"));
  };

  const handleCancel = () => {
    navigate(-1); // Go back to the previous page
  };

  return (
    <>
      <form onSubmit={handleSubmit} className="change-password-form">
        <div className="change-password-form-group">
          <label htmlFor="old_password">Old Password</label>
          <input
            type="password"
            id="old_password"
            name="old_password"
            required
            value={passwd.old_password}
            onChange={handleChange}
          />
        </div>
        <div className="change-password-form-group">
          <label htmlFor="new_password">New Password</label>
          <input
            type="password"
            id="new_password"
            name="new_password"
            required
            value={passwd.new_password}
            onChange={handleChange}
          />
        </div>
        <div className="change-password-form-group">
          <label htmlFor="confirm_password">Confirm Password</label>
          <input
            type="password"
            id="confirm_password"
            name="confirm_password"
            required
            value={passwd.confirm_password}
            onChange={handleChange}
          />
        </div>
        {error && <div className="change-password-error-message">{error}</div>}
        <div className="change-password-button-group">
          <button type="submit" className="change-password-btn">
            Change Password
          </button>
          <button
            type="button"
            className="change-password-btn cancel"
            onClick={handleCancel}
          >
            Cancel
          </button>
        </div>
      </form>
    </>
  );
}

export default ChangePassword;
