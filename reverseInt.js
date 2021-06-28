function reverseInt(num) {
    if (!Number.isInteger(num)) return 0;
    if (num === 0) return 0;

    let n = num;
    let reverseNum = 0;
    num < 0 ? num = num * -1 : num;

    while (num != 0) {
        reverseNum = reverseNum * 10 + (num % 10)
        num = Math.floor(num / 10);
    }

    n < 0 ? reverseNum= -reverseNum : reverseNum =reverseNum;

    if(reverseNum> (Math.pow(2, 31) - 1))  return 0;
    if(reverseNum< Math.pow(-2, 31))  return 0;

    return reverseNum;
}

console.log(reverseInt(123))