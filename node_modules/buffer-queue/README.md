# buffer-queue

[![Build Status](http://img.shields.io/travis/jsantell/buffer-queue.svg?style=flat-square)](https://travis-ci.org/jsantell/buffer-queue)
[![Build Status](http://img.shields.io/npm/v/buffer-queue.svg?style=flat-square)](https://www.npmjs.org/package/buffer-queue)

A fast buffer store, for queueing up buffer chunks to later drain as a full buffer for streams. Faster than `Buffer.concat` on every chunk.

## Install

```
npm install buffer-queue
```

## Usage

Example of a transform stream that only writes downstream 1MB at a time, storing
up buffers in the buffer store.

```javascript
var Transform = require("stream").Transform;
var util = require("util");
var Store = require("buffer-queue");

/**
 * Transform stream that limits writes to 1MB at a time
 */
function ThrottleStream (limit) {
  this.limit = limit || 1024 * 1024;
  this.store = new Store();
  Transform.call(this);
}
util.inherits(ThrottleStream, Transform);

ThrottleStream.prototype._transform = function (chunk, enc, callback) {
  this.store.push(chunk);
  var data;

  // While we have more in our store than the limit, then push
  // out a chunk
  while (this.store.length() > this.limit && data = this.store.shift(this.limit)) {
    this.push(data);
  }
  callback();
};

ThrottleStream.prototype._flush = function (callback) {
  var data;
  while (data = this.store.shift(this.limit)) {
    this.push(data);
  }
  callback();
};
```

## API

### `BufferStore()`

Constructor for a buffer store.

#### `store.push(buffer)`

Pushes a buffer to the store.

#### `store.shift(n)`

Returns the first `n` bytes of the entire buffer store and removes from the store.

#### `store.empty()`

Empties the entire internal buffer store.

#### `store.length()`

Returns the length of the internal buffer store in bytes.

#### `store.drain()`

Empties and returns the internal buffer store. Use `store.empty()` if you are not interested in the return value.

## Testing

```
npm test
```

## License

MIT License, Copyright (c) 2015 Jordan Santell
