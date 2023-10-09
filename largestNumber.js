var largestNumber = function(nums) {
    const numStrs = nums.map(num => num.toString());
    
    numStrs.sort((a, b) => {
        const order1 = a + b; 
        const order2 = b + a; 
        return order2.localeCompare(order1); 
    });
    
    if (numStrs[0] === "0") return "0";

    return numStrs.join("");
};

// console.log(largestNumber([10,2]));
// console.log(largestNumber([3,30,34,5,9]));
console.log(largestNumber([432,43243]));