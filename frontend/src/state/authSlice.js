import { createSlice } from "@reduxjs/toolkit";


const token = localStorage.getItem("token");
const refreshToken = localStorage.getItem("refreshToken");

const initialState = {
  isAuthenticated: !!token,
  token: token,
  refreshToken: refreshToken,
};

const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    login(state, action) {
      console.log("Action Payload:", action.payload); // Log the entire payload
      state.isAuthenticated = true;
      localStorage.setItem("token", action.payload.token);
      localStorage.setItem("refreshToken", action.payload.refreshToken);
      state.token = action.payload.token;
      state.refreshToken = action.payload.refreshToken;
    },
    logout(state) {
      state.isAuthenticated = false;
      state.token = null;
      state.refreshToken = null;
      localStorage.removeItem("token");
      localStorage.removeItem("refreshToken");
    },
  },
});

export const { login, logout } = authSlice.actions;
export default authSlice.reducer;
