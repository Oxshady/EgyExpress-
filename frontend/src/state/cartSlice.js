import { createSlice } from "@reduxjs/toolkit";

const initialState ={
    cartItems: [],
    total: 0,
};
const cartSlice = createSlice({
    name:'cart',
    initialState,
    reducers:{
        addItemToCart:(state, action)=>{
            state.cartItems.push(action.payload);
            state.total += 1;
                  console.log("Item added to cart:", action.payload);
                  console.log("Updated cart items:", state.cartItems);
        },
        removeCartItems:(state)=>{
            state.cartItems = [];
        state.total = 0;
        },
    }
})
export const { addItemToCart, removeCartItems } = cartSlice.actions;
export default cartSlice.reducer;
