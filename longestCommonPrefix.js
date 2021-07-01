function longestCommonPrefix(strs) {
    if(strs.length === 0) return "";
    if(strs.length === 1) return strs[0];

    const commonPrefix = {};
    const longestCommonPrefix = {
        "maxValue": strs.length,
        "maxKey":""
    }
    let cell;

    for(let i=0; i<=strs.length-1;i++){
        cell = strs[i];
        while(cell){
            commonPrefix[cell] = (commonPrefix[cell] || 0) + 1
            if( commonPrefix[cell] >= longestCommonPrefix["maxValue"] && 
                cell.length > longestCommonPrefix["maxKey"]){
                longestCommonPrefix["maxValue"] = commonPrefix[cell];
                longestCommonPrefix["maxKey"] = cell;
            }
            cell = cell.slice(0, -1);
        }
    }

    return longestCommonPrefix["maxKey"];
}


console.log(longestCommonPrefix(["flower","flow","flight"]));
// console.log(longestCommonPrefix(["cir","car"]));
// console.log(longestCommonPrefix(["c"]));