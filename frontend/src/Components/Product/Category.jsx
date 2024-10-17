import { useEffect, useState } from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/pagination";
import "./Category.css";
import SwiperCore from "swiper";
import { Navigation, Pagination } from "swiper/modules";
import { Link } from "react-router-dom";
SwiperCore.use([Navigation, Pagination]);

function Category(props) {
  const category_id = props.category;
  console.log(props);
  console.log(category_id);
  const [categoryProducts, setCcategoryProducts] = useState([]);
  const api_url = "http://localhost:5000/api/products/categories";
  const theUrl = `${api_url}/${category_id}`;
  console.log(theUrl);

  useEffect(() => {
    fetch(`${api_url}/${category_id}`)
      .then((res) => res.json())
      .then((data) => setCcategoryProducts(data));
  }, []);

  return (
    <>
      <div className="containerr">
        <div className="card-wrapper">
          <Swiper
            spaceBetween={30}
            slidesPerView={3}
            navigation
            pagination={{ clickable: true }}
            breakpoints={{
              320: {
                slidesPerView: 1,
                spaceBetween: 10,
              },
              640: {
                slidesPerView: 2,
                spaceBetween: 20,
              },
              1024: {
                slidesPerView: 3,
                spaceBetween: 30,
              },
            }}
            onSlideChange={() => console.log("slide change")}
            onSwiper={(swiper) => console.log(swiper)}
          >
            {categoryProducts.map((product) => (
              <SwiperSlide key={product.id}>
                <div className="card-list">
                  <div className="card-item">
                    <Link
                      aria-current="page"
                      to={`/product/${product.id}`}
                      className="card-link"
                    >
                      <img
                        src={product.image}
                        alt={product.name}
                        className="card-image"
                      />
                      <div className="product_breif_info">
                        <h3 className="product_title">{product.name}</h3>
                        <p className="product_price">Price: {product.price}</p>
                        <button className="card-button">
                          <span className="material-icons arrow-icon">
                            arrow_forward_ios
                          </span>
                        </button>
                      </div>
                    </Link>
                  </div>
                </div>
              </SwiperSlide>
            ))}
          </Swiper>
        </div>
      </div>
    </>
  );
}

export default Category;
