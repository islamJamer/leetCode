



const convert = (s, numRows) => {
    if (s.length < 1) return '';
    if (s.length === 1) return s;
    if (numRows === 1) return s;

    const n = numRows
    const results = [];

    const cycleLen = 2*n - 2;
    const string = s.split('');
    const len = string.length

    for(let i=0; i<n; i++){
        for(let j=0; j+i < len; j+=cycleLen){
            
            results.push(string[i+j])

            if(i!==0 && i!==n-1){
                let sipling = j+cycleLen - i 
                if(sipling < len)
                    results.push(string[sipling])
            }

        }
    }
   
    return results.join('');
}

console.log(convert("PAYPALISHIRING", 4));
