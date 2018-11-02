'use strict';
// process.nextTick(function(){
//     console.log("nextTick callback!");
// });
process.on('exit',function(code){
    console.log("about to exit with code:"+code);
});
var data= getJSONync('http://example.com/ajax');
console.log('nextTick was set!');