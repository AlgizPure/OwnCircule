/**
 * Metro configuration
 * https://facebook.github.io/metro/docs/configuration
 */

const { getDefaultConfig, mergeConfig } = require('@react-native/metro-config');

const config = {};

module.exports = mergeConfig(getDefaultConfig(__dirname), config);
