/* eslint-disable @typescript-eslint/no-var-requires */
/* global require __dirname module */

const merge = require("webpack-merge");
const common = require("./webpack.common.js");
const pp = "http://localhost:8080/static/dist/";

module.exports = merge(common, {
    mode: "development",
    output: {
        publicPath: pp
    },
    devServer: {
        headers: { "Access-Control-Allow-Origin": "*" },
        contentBase: "./assets/dist",
        compress: true,
        port: 8080
    }
});