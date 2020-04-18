var expect = require("chai").expect;
var BufferQueue = require("../");

function filledBuffer (size, val) {
  var b = new Buffer(size);
  b.fill(val);
  return b;
}

describe("buffer-queue", function () {
  it("push() queues buffers and length() returns length", function () {
    var q = new BufferQueue();
    for (var i = 0; i < 5; i++) { q.push(filledBuffer((i+1)*1024, 1)); }
    expect(q.length()).to.be.equal(15 * 1024);
  });

  it("empty() empties the queue", function () {
    var q = new BufferQueue();
    for (var i = 0; i < 5; i++) { q.push(filledBuffer(i*1024, 1)); }
    q.empty();
    expect(q.length()).to.be.equal(0);
    q.push(new Buffer(10));
    expect(q.length()).to.be.equal(10);
  });

  it("drain() empties the queue and returns the buffer", function () {
    var q = new BufferQueue();
    for (var i = 0; i < 5; i++) { q.push(filledBuffer((i+1)*1024, 1)); }
    var d = q.drain();
    expect(q.length()).to.be.equal(0);
    expect(d.length).to.be.equal(15 * 1024);
  });

  it("shift(n) returns the first n bytes of the entire queue", function () {
    var q = new BufferQueue();
    for (var i = 1; i < 6; i++) { q.push(filledBuffer(i, i)); }
    var front = q.shift(3); // bytes
    expect(front.length).to.be.equal(3);
    expect(front[0]).to.be.equal(1);
    expect(front[1]).to.be.equal(2);
    expect(front[2]).to.be.equal(2);
    expect(q.length()).to.be.equal(12);
  });
});
