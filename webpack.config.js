const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const devMode = process.env.NODE_ENV !== 'production';

module.exports = {
  mode : devMode ? 'development' : 'production',
  // devtool: 'source-map',
  context: path.resolve(__dirname, 'src'),
  entry: {
    main: './main.js', 
    calendar: './calendar.js'
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'static/dist')
  },
  plugins: [
    new MiniCssExtractPlugin({
      // Options similar to the same options in webpackOptions.output
      // both options are optional
      filename: "[name].css",
      chunkFilename: "[id].css"
    })
  ],
  module: {
    rules: [
      {
        test: /\.s?[ac]ss$/,
        use: [
            MiniCssExtractPlugin.loader,
            { loader: 'css-loader', options: { url: false, sourceMap: true } },
            { loader: 'sass-loader', options: { sourceMap: true } }
        ],
      }
    ]
  }
};