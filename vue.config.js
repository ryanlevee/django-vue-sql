module.exports = {
	// publicPath: 'http://localhost:8080/',
	publicPath: 'static',
	outputDir: 'static/dist',
	indexPath: 'templates/_base_vue.html',

	configureWebpack: {
		devServer: {
			devMiddleware: {
				writeToDisk: true
			}
		}
	}
}

