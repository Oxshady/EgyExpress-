import ProductList from "../Components/Product/ProductList";
import Slider from "../Components/Slider";
import Intro from "../Components/Intro";
import "../css/Home.css";
import { useRef } from "react";
import CategroiesList from "../Components/Product/CategroiesList";
function Home() {
  const sliderRef = useRef(null);
  const scrollToSlider = () => {
    if (sliderRef.current) {
      sliderRef.current.scrollIntoView({ behavior: "smooth" });
    }
  };
  return (
    <>
      <div className="content">
        <Intro onShopNowClick={scrollToSlider} />
        <div ref={sliderRef}>
          <CategroiesList />
        </div>
      </div>
    </>
  );
  //<ProductList />
  //        <Slider />
}
export default Home;
