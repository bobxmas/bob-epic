const path = require('path')

function resolve (dir) {
    return path.join(__dirname, dir)
}

module.exports = {
    lintOnSave: false,
    devServer: {
        proxy: {
            '^/api': {
                target: 'http://172.30.1.18:80',
                // target: 'http://127.0.0.1:9000',
                changeOrigin: true,
                pathRewrite: {
                    ['^/api']: ''
                }
            }
        },
        port: 80,
        overlay: {
            warnings: false,
            errors: true
        }
    },
    configureWebpack: {
        resolve: {
            alias: {
                '@': resolve('src')
            }
        }
    },
    filenameHashing: false
};