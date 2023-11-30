function Shape() {
    this.x = 0;
    this.y = 0;
    this.draw = function () {
        console.log(`drawing shape at point: ${this.x},${this.y}`);
    };

    Object.defineProperty(this, 'origin', {
        get: function () {
            return { x: this.x, y: this.y };
        },
        set: function (value) {
            this.x = value.x;
            this.y = value.y;
        }
    })
}

Shape.prototype.toString = function () {
    return `Shape at: ${this.x},${this.y}`
}

let shape = new Shape();
shape.origin = { x: 1, y: 2 };
console.log(shape);
console.log(shape.toString());
console.log(shape.origin);