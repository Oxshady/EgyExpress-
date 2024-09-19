import '../../css/auth.css'
import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { Link, useNavigate } from "react-router-dom";
import { login } from "../../http";
import { login as loginAction } from "../../state/authSlice";
import { setUser } from "../../state/userSlice";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await login({ email, password });
      dispatch(loginAction({ token: data.access_token, refreshToken: data.refresh_token}));
      dispatch(setUser({ username: data.username }));
      navigate("/about");
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <>
      <div className="page">
        <div className="center">
          <h1>Login</h1>
          <form onSubmit={handleSubmit}>
            <div className="txt_felid">
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Email"
                required
              />
              <span></span>
              <label htmlFor="">Email</label>
            </div>
            <div className="txt_felid">
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
                required
              />
              <span></span>
              <label htmlFor="">Password</label>
            </div>
            {error && <p>{error}</p>}
            <button type="submit" className="submitBtn">
              Login
            </button>
            <p>
              Don't have an account? register <Link to="/register">Here</Link>
            </p>
          </form>
        </div>
      </div>
    </>
  );
}

export default Login;
