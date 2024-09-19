import React from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { logout } from "../../state/authSlice";
import { clearUser } from "../../state/userSlice";

function Logout() {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleLogout = () => {
    dispatch(logout());
    dispatch(clearUser());
    navigate("/");
  };

  return <button onClick={handleLogout}>Logout</button>;
}

export default Logout;
