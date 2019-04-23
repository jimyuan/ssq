/**
 * 阶乘算法
 */
export const fact = num => {
  return num <= 1 ? 1 : num * fact(num - 1)
}

/**
 * 组合算法
 */
export const comb = (m, n) => {
  return fact(m) / fact(m - n) / fact(n)
}

const _getFlagArrs = (m, n = 1) => {
  if (n < 1 || m < n) return []

  // 先生成一个长度为 m 字符串，开头为 n 个 1， 例如“11100”
  let str = '1'.repeat(n) + '0'.repeat(m - n)
  let flag

  const keyStr = '10'
  // 1
  const resultArrs = [Array.from(str, x => Number(x))]

  while (str.indexOf(keyStr) > -1) {
    flag = str.indexOf(keyStr)
    // 2
    str = str.replace(keyStr, '01')
    // 3
    str = Array.from(str.slice(0, flag))
      .sort((a, b) => b - a)
      .join('') + str.slice(flag)
    // 4
    resultArrs.push(Array.from(str, x => Number(x)))
  }
  return resultArrs
}
/**
 * 获得指定数组的所有组合
 */
export const arrayCombine = (targetArr = [], count = 1) => {
  if (!Array.isArray(targetArr)) return []

  const resultArrs = []
  // 所有组合
  const flagArrs = _getFlagArrs(targetArr.length, count)
  while (flagArrs.length) {
    const flagArr = flagArrs.shift()
    resultArrs.push(targetArr.filter((_, idx) => flagArr[idx]))
  }
  return resultArrs
}
