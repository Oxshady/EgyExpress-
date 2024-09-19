import { useEffect, useState } from "react";
import Category from "./Category";
import "../css/CategroiesList.css";

function CategroiesList() {
  const [categories, setCategories] = useState([]);
  const api_url = "http://localhost:5000/api/categories";

  useEffect(() => {
    fetch(api_url)
      .then((res) => {
        if (!res.ok) {
          return res.text().then(text => { throw new Error(text) });
        }
        return res.json();
      })
      .then((data) => setCategories(data))
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  const handleClick = (category) => {
    console.log(category);
  };

  console.log(categories);

  return (
    <div className="categories">
      {categories.map((category) => (
        <div key={category.id}>
          <h1 className="big_title">{category.name}</h1>
          <hr />
          <Category category={category.id} />
        </div>
      ))}
    </div>
  );
}

export default CategroiesList;