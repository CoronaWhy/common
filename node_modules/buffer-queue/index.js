/**
 * BufferQueue constructor.
 */
function BufferQueue () {
  this._buffers = [];
  this._buffersLength = 0;
}
module.exports = BufferQueue;

/**
 * Removes the first `n` bytes out of the queue
 * and returns them. If `n` is greater than the current
 * buffer size, return as much as possible.
 *
 * @param {Number} bytes
 * @return {Buffer}
 */

BufferQueue.prototype.shift = function (bytes) {
  // If trying to shift more space than the internal buffer has, cap it
  // at the current size of the queue.
  bytes = bytes > this._buffersLength ? this._buffersLength : bytes;

  var data = Buffer.concat(this._buffers, this._buffersLength);
  var front = data.slice(0, bytes);
  this.empty();
  this.push(data.slice(bytes));
  return front;
};

/**
 * Merges the buffer into the buffer queue.
 *
 * @param {Buffer} buffer
 */

BufferQueue.prototype.push = function (buffer) {
  this._buffers.push(buffer);
  this._buffersLength += buffer.length;
};

/**
 * Clears out the internal buffer queue.
 */
BufferQueue.prototype.empty = function () {
  this._buffers.length = 0;
  this._buffersLength = 0;
};

/**
 * Returns the size of all the queued buffers.
 */
BufferQueue.prototype.length = function () {
  return this._buffersLength;
};

/**
 * Returns the aggregate buffer and empties the internal queue.
 *
 * @return {Buffer}
 */
BufferQueue.prototype.drain = function () {
  var data = Buffer.concat(this._buffers, this.buffersLength);
  this._buffers.length = this._buffersLength = 0;
  return data;
};
