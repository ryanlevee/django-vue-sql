module.exports = {
	publicPath: 'http://localhost:8080/',
	outputDir: '../static/dist',
	indexPath: '../../templates/_base_vue.html',

	configureWebpack: {
		devServer: {
			devMiddleware: {
				writeToDisk: true
			}
		}
	}
}

