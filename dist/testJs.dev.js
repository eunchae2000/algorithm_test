"use strict";

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

var Queue =
/*#__PURE__*/
function () {
  function Queue() {
    _classCallCheck(this, Queue);

    this.queue = [];
  }

  _createClass(Queue, [{
    key: "enqueue",
    value: function enqueue(item) {
      this.queue(item);
    }
  }, {
    key: "dequeue",
    value: function dequeue() {
      return this.queue.shift();
    }
  }, {
    key: "isEmpty",
    value: function isEmpty() {
      return this.queue.length === 0;
    }
  }, {
    key: "front",
    value: function front() {
      return this.queue[0];
    }
  }, {
    key: "clear",
    value: function clear() {
      this.queue = [];
    }
  }, {
    key: "length",
    value: function length() {
      return this.queue.length;
    }
  }]);

  return Queue;
}();

var readline = require('readline');

var rl = readline.createInterface({
  input: process.stdin
});
rl.question('', function (input) {
  input = input.trim().split(' ');
  input = input.map(function (item) {
    return parseInt(item);
  });
  void answer(input);
  rl.close();
});

function answer(input) {
  var n = input[0];
  var k = input[1];
  var queue = new Queue();

  for (var i = 0; i < n; i++) {
    queue.enqueue(i);
  }

  var arr = [];

  for (var _i = 0; _i < n; _i++) {
    k = k % n;
    if (k === 0) k = n;

    for (var j = 0; j < k; j++) {
      var temp = queue.dequeue();
      if (j != k - 1) queue.enqueue(temp);else arr.push(temp);
    }
  }

  console.log("<".concat(arr.join(", "), ">"));
}