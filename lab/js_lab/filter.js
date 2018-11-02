'use strict';
var click_filter = function() {
    function get_primes(arr) {
        return arr.filter(function(e, i, s) {
            let flag = true;
            if (e <= 1) {
                flag = false;
            } else {
                for (let l = i; l > 1; l--) {
                    if (e % l === 0) {
                        flag = false;
                        break;
                    }
                }
            }
            return flag;
        });
    }
    // 测试:
    var
        x,
        r,
        arr = [];
    for (x = 1; x < 100; x++) {
        arr.push(x);
    }
    r = get_primes(arr);
    if (r.toString() === [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97].toString()) {
        console.log('测试通过!');
    } else {
        console.log('测试失败: ' + r.toString());
    }
};

var r,
    arr = ['apple', 'strawberry', 'banana', 'pear', 'apple', 'orange', 'orange', 'strawberry'];

r = arr.filter(function(element, index, self) {
    return self.indexOf(element) === index;
});

console.log(r.toString());

//去除重复元素依靠的是indexOf总是返回第一个元素的位置， 后续的重复元素位置与indexOf返回的位置不相等， 因此被filter滤掉了。