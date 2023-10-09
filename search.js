const search1 = (nums, target) => {
    if(nums.length === 1 && nums[0] === target) return 0
    if (nums.length < 2) return -1
    return nums.findIndex((num) => num === target);
}

console.log(search1([4,5,6,7,0,1,2], 0));