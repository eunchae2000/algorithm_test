class Queue{
    constructor() {
        this.queue = []
    }
    enqueue(item) {
        this.queue(item)
    }
    dequeue() {
        return this.queue.shift()
    }
    isEmpty() {
        return this.queue.length === 0;
    }
    front() {
        return this.queue[0]
    }
    clear() {
        this.queue = []
    }
    length() {
        return this.queue.length
    }
}

function answer() {
    const n = 7
    var k = 3

    const queue = new Queue();
    for (let i = 0; i < n; i++){
        queue.enqueue(i)
    }

    const arr = []
    for (let i = 0; i < n; i++){
        k = k % n
        if (k === 0) k = n
        for (let j = 0; j < k; j++) {
            let temp = queue.dequeue();
            if (j != k - 1) queue.enqueue(temp);
            else arr.push(temp)
        }
    }

    console.log(`<${arr.join(", ")}>`)
}