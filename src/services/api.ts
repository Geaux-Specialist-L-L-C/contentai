// src/services/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  }
});

export const contentService = {
  getContent: async () => {
    const response = await api.get('/content');
    return response.data;
  },
  
  createContent: async (data: any) => {
    const response = await api.post('/content', data);
    return response.data;
  },

  searchByTags: async (tags: string[]) => {
    const response = await api.get(`/content/search?tags=${tags.join(',')}`);
    return response.data;
  }
};

export default api;