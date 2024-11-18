import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Cambia a la URL de tu backend

// Función para el login
export const login = async (username, password) => {
  try {
    const response = await axios.post(`${API_URL}/login`, { username, password });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Función para el perfil
export const fetchProfile = async (token) => {
  try {
    const response = await axios.post(
      `${API_URL}/profile`, 
      {}, 
      { headers: { Authorization: `Token ${token}` } }
    );
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};
