/* eslint-disable @typescript-eslint/no-var-requires */
/* global require __dirname module */

const path = require("path");
const webpack = require('webpack');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const {
    CleanWebpackPlugin
} = require('clean-webpack-plugin');
const FixStyleOnlyEntriesPlugin = require("webpack-fix-style-only-entries"); // Will be unecessary in Webpack 5, apparently
const TerserPlugin = require("terser-webpack-plugin");
const BundleTracker = require("webpack-bundle-tracker");
const assetsFolder = "./assets/";
const outputFolder = "../../../static/dist";

module.exports = {
    entry: {
        base: [
            assetsFolder + "css/basic.scss",
            assetsFolder + "css/style.css",
            assetsFolder + "js/contactform.js",
            assetsFolder + "lib/jquery/jquery-migrate.min.js",
            assetsFolder + "lib/easing/easing.min.js",
            assetsFolder + "lib/counterup/jquery.waypoints.min.js",
            assetsFolder + "lib/counterup/jquery.counterup.js",
            assetsFolder + "lib/lightbox/js/lightbox.min.js",
            assetsFolder + "js/basic.js",
            assetsFolder + "js/main.js",
        ],
    },
    output: {
        path: path.resolve(__dirname, outputFolder),
        filename: "[name]-[hash].js",
    },
    module: {
        rules: [{
                test: /\.tsx?$/,
                exclude: /node_modules/,
                loader: ["babel-loader", {
                    loader: "ts-loader",
                    options: {
                        transpileOnly: true
                    }
                }]
            }, {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: "babel-loader"
            }, {
                test: /\.(s*)css$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    {
                        loader: "css-loader",
                        options: {
                            sourceMap: true
                        }
                    },
                    {
                        loader: "sass-loader",
                        options: {
                            sourceMap: true,
                        }
                    },
                ]
            },
            {
                test: /\.(jpg|gif|webp|ico|tiff|bmp|png|woff|woff2|eot|ttf|svg)$/,
                loader: "file-loader",
                options: {
                    name: "[name]-[hash].[ext]"
                }
            }
        ],
    },
    resolve: {
        extensions: [".tsx", ".ts", ".js", ".jsx"],
        modules: [
          assetsFolder,
          'node_modules'
        ],
    },
    target: "web",
    plugins: [
        new CleanWebpackPlugin(),
        new BundleTracker({
            filename: "../webpack-stats.json"
        }),
        new FixStyleOnlyEntriesPlugin({
            silent: true
        }),
        new MiniCssExtractPlugin({
            filename: "[name]-[hash].css",
            chunkFilename: "[id].css"
        }),
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery'
        }),
    ],
    optimization: {
        minimizer: [
            new TerserPlugin({
                sourceMap: true,
                terserOptions: {
                    output: {
                        comments: false
                    }
                }
            })
        ],
    }
};
