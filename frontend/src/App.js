import "./App.css";
import About from "./Components/About";
import ProductDtials from "./Components/Product/ProductDetials";
import Login from "./Components/Register/Login";
import Register from "./Components/Register/Register";
import Logout from "./Components/Register/Logout";
import PrivateRoute from "./Components/PrivateRoute";
import Cart from "./Components/Cart/Cart";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import RootPage from "./pages/RootPage";
import Home from "./pages/Home";
import Profile from "./Components/Profile/Profile";
import Order from "./Components/Cart/Order";
import Tracking from "./Components/Cart/Tracking";
import CategroiesList from "./Components/Product/CategroiesList";
import EditAcc from "./Components/Profile/EditAcc";
import ChangePassword from "./Components/Profile/ChangePassword";
import DeleteAcount from "./Components/Register/DeleteAcount";
import Review from "./Components/Review/Review";
const router = createBrowserRouter([
  {
    path: "/",
    element: <RootPage />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "about",
        element: <About />,
      },
      {
        path: "cart",
        element: (
          <PrivateRoute>
            <Cart />
          </PrivateRoute>
        ),
      },
      {
        path: "order",
        element: (
          <PrivateRoute>
            <Order />
          </PrivateRoute>
        ),
      },
      {
        path: "profile",
        element: (
          <PrivateRoute>
            <Profile />
          </PrivateRoute>
        ),
      },
      {
        path: "register",
        element: <Register />,
      },
      {
        path: "login",
        element: <Login />,
      },
      {
        path: "logout",
        element: <Logout />,
      },
      {
        path: "product/:productId",
        element: <ProductDtials />,
      },
      {
        path: "tracking",
        element: (
          <PrivateRoute>
            <Tracking />
          </PrivateRoute>
        ),
      },
      {
        path: "categories",
        element: <CategroiesList />,
      },
      {
        path: "edit-account",
        element: (
          <PrivateRoute>
            <EditAcc />
          </PrivateRoute>
        ),
      },
      {
        path: "change-password",
        element: (
          <PrivateRoute>
            <ChangePassword />
          </PrivateRoute>
        ),
      },
      {
        path: "delete-acount",
        element: (
          <PrivateRoute>
            <DeleteAcount />
          </PrivateRoute>
        ),
      },
      {
        path: "add-review",
        element: (
          <PrivateRoute>
            <Review />
          </PrivateRoute>
        ),
      },
    ],
  },
]);

function App() {
  return (
    <div className="App">
      <RouterProvider router={router} />
    </div>
  );
}

export default App;
