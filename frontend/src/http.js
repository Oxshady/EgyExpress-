
export async function register(userData) {
  const response = await fetch("http://localhost:5000/api/signup", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(userData),
  });

  if (!response.ok) {
    throw new Error("Registration failed");
  }

  return response.json();
}

export async function fetchWithAuth(url, options = {}) {
  const token = localStorage.getItem("token");
  if (!token) {
    throw new Error("No token found");
  }
  console.log(token);
  console.log(options);
try {
  const response = await fetch(url, {
    ...options,
    headers: {
      ...options.headers,
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(options.body),
  });

  if(response.status === 401){
    const refreshToken = localStorage.getItem("refreshToken");
    if (!refreshToken) {
      throw new Error("No refresh token found");
    }
    const refreshRespone = await fetch("/auth/refresh",
      {
       method:"POST",
       headers:{
        "Content-Type":"application/json",
       },
       body:JSON.stringify({token: refreshToken}),
       } );
    if (!refreshRespone.ok) {
       throw new Error(`HTTP error! status: ${refreshRespone.status}`);
      }
      const refreshData = await refreshRespone.json();
      token = refreshData.token;
      localStorage.setItem("token", token);
      response = await fetch(url,{
        ...options,
        headers:{
          ...options.headers,
          Authorization: `Bearer ${token}`,
        },
      });
  }
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }

  return await response.json();
} catch (error) {
  console.error('Fertch Error', error);
  throw error;
}
}
export async function login(credentials) {
  const response = await fetch("http://localhost:5000/api/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(credentials),
  });

  if (!response.ok) {
    throw new Error("Login failed");
  }

  return response.json();
}
