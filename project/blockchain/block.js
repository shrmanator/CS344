// https://www.youtube.com/watch?v=zVqczFZr124&ab_channel=SimplyExplained

const SHA256 = require('crypto-js/sha256');

class Block {
    // index: the index of this block on the chain
    // date_created: the date this block was created
    // data: all of the transaction details of this block
    // prevHash: string containing the hash of the prev Block.
    constructor(index, date_created, data, prevHash='') {
        this.index = index;
        this.date_created = date_created;
        this.data = {
            amount_transferred: 0,
            sender: '',
            receiver: ''
        };
        this.prevHash = prevHash;
        this.hash = this.calculateHash();
    };

    // Calculates the "hash function" of this Block and returns it as a String.
    calculateHash() {
        return SHA256(this.index + this.prevHash + this.date_created + JSON.stringify(this.data)).toString();
    }
}