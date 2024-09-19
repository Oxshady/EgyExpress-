import { Outlet } from "react-router-dom";
import Nav from "../Components/NavBar";
function RootPage() {
  return (
    <>
    <Nav/>
    <Outlet/>
    </>

  );
  //outlet is used to render chilren
}
export default RootPage;
