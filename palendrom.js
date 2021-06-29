function palendrom(num) {
    if (!Number.isInteger(num)) return false;
    if (num === 0) return false;
    if (num < 0) return false;

    let n = num;
    let reverseNum = 0;
    num < 0 ? num = num * -1 : num;

    while (num != 0) {
        reverseNum = reverseNum * 10 + (num % 10)
        num = Math.floor(num / 10);
    }

    return n === reverseNum;
}

console.log(palendrom(121))