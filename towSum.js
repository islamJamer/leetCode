function towSum(nums, target) {
    const hash = {}
    for (let val in nums)
        if (!(nums[val] in hash)) {
            hash[target - nums[val]] = val;
        } else {
            return [hash[nums[val]], val];
        }
    return 0;
}

console.log(towSum([3, 4, 3], 6));