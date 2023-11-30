class Shape {
    constructor(origin) {
        this.origin = origin || { x: 0, y: 0 }
    }

    draw() {
        console.log('drawing a shape at:' + this.origin);
    }
}

let shape = new Shape({ x: 0, y: 0 });
console.log(shape);