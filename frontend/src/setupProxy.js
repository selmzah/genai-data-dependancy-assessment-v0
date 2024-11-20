const { createProxyMiddleware } = require('http-proxy-middleware');

// Utiliser la variable d'environnement pour définir le target
const target = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000';

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: target,
      changeOrigin: true,
    })
  );
};
