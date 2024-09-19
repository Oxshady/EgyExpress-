import "../css/Intro.css";
import { useNavigate } from "react-router-dom";
function Intro({ onShopNowClick }) {
    const navigate = useNavigate();
    const handleClinck = () =>{
        navigate('/about');
    }
  return (
    <div className="intro">
      <h1>EgyXpress</h1>
      <div className="welcome">
        <h2>Welcome! </h2>
        <p>Find everything you need here</p>
      </div>
      <div className="coll">
        <button className="colll button1" onClick={onShopNowClick}>
          Shop Now
        </button>
        <button className="colll button2" onClick={handleClinck}>About</button>
      </div>
    </div>
  );
}
export default Intro;
