const productionFlag = process.env.NODE_ENV === 'production'
const productionSourceMap = !productionFlag
const cssSourceMap = !productionFlag
module.exports = {
  publicPath: productionFlag ? './' : '/',
  lintOnSave: false,
  filenameHashing: false,
  productionSourceMap,
  css: {
    sourceMap: cssSourceMap
  }
}
