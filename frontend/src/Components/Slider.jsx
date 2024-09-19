import '../css/Slider.css';
function Slider() {
  return (
    <>
      <div id="carouselExample" className="carousel slide">
        <div className="carousel-inner">
          <div className="carousel-item active slider">
            <img
              src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQf_ZHWuxOWYpv-I69uQy6-R-78Oc3e531kVEMlRxoPYIszRW3KKRo-podXSxex5tmx0Uw&usqp=CAU"
              className="d-block w-100"
              alt="..."
            />
          </div>
          <div className="carousel-item">
            <img
              src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbOHJ0QI9JZqIQ_5FL3yu-0E60n_uG_pZEV0oHh2iSuyBNzDjq0Yr-E34TqjSZippacss&usqp=CAU"
              className="d-block w-100"
              alt="..."
            />
          </div>
          <div className="carousel-item">
            <img
              src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT62vn4AZhhXbfsHFbO1YiFcVjmLWto1Z3KMg&s"
              className="d-block w-100"
              alt="..."
            />
          </div>
        </div>
        <button
          className="carousel-control-prev"
          type="button"
          data-bs-target="#carouselExample"
          data-bs-slide="prev"
        >
          <span
            className="carousel-control-prev-icon"
            aria-hidden="true"
          ></span>
          <span className="visually-hidden">Previous</span>
        </button>
        <button
          className="carousel-control-next"
          type="button"
          data-bs-target="#carouselExample"
          data-bs-slide="next"
        >
          <span
            className="carousel-control-next-icon"
            aria-hidden="true"
          ></span>
          <span className="visually-hidden">Next</span>
        </button>
      </div>
    </>
  );
}
export default Slider;
