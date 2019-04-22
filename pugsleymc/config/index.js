// config/webenv.js
const path = require('path')
const DotEnv = require('dotenv')
module.exports = function (name) {
  const envPath = path.resolve(__dirname, `${name}.env`)
  console.log(envPath)
  var parsedEnv = DotEnv.config({path: envPath}).parsed
  if(parsedEnv == undefined) {
    parsedEnv = process.env
  }
  // console.log(parsedEnv)
  // Let's stringify our variables
  for (key in parsedEnv) {
    if (typeof parsedEnv[key] === 'string') {
      parsedEnv[key] = JSON.stringify(parsedEnv[key])
    }
  }
  console.log(parsedEnv)
  return parsedEnv
}