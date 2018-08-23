"use strict";

var s = "Hello";

function greet(name) {
	var Console=console;
	Console.log(s + "," + name + "!");
}
module.exports = greet;