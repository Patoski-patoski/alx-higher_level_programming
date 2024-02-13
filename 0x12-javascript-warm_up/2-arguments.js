#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('No argument');
} else if (process.argv[3] === undefined) {
  console.log('Argument found');
} else console.log('Arguments found');

//console.log (process.argv[2]);
for (var i = 0; i < process.argv.length; i++) {
	console.log (`length ${i}: ${process.argv[i]}`);
}
