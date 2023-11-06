import Cookies from 'js-cookie';

export const setAccessTokenCookie = (accessToken) => {
  Cookies.set('access_token', accessToken, { path: '/', secure: true });
};

export const getAccessTokenCookie = () => {
  return Cookies.get('access_token');
};

export const removeAccessTokenCookie = () => {
  Cookies.remove('access_token');
};