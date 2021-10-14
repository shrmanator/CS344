let dovBlock = require("block.js");
const SHA256 = require('crypto-js/sha256');

class MerkelTree {
    constructor(data) {
        this.data = data;
        this.chain = Array(8);
        this.chain[0] = this.getGenesisBlock();
        this.hash = "";
        this.chainSize = 1;
    }

    getGenesisBlock(block_instance) {
        block_instance.hash = generateHashValue();
        block_instance.data = "genesis block";
        return block_instance;
    }

    getHashValue() {
        return SHA256(this.data + this.blocks + this.hash).toString();  // returns a 64 char string.
    }

    rehashTree(merkleTree) {
        if (this.chainSize === 1)
            return this.chain[0];
        let newHashList = [];
        for (let i = 1; i < this.chainSize + 1; i + 2) {
            newHashList.push(hash2(this.chain[i]));
            newHashList.push(hash2(this.chain[i + 1]));
        }
        if (this.chainSize % 2 === 1) {
            newHashList.push(hash2(newHashList[newHashList.length - 1]), newHashList[newHashList.length - 1]);
        }
        return this.rehashTree(newHashList);
    }

    hash2(a, b) {
        a.hash = this.getHashValue();
        b.hash = this.getHashValue();
    }

    // A new_block can be any block that contains the following attributes:
    //
    addBlock(new_block) {


    }
}

let mtree = new MerkelTree(new dovBlock("1 dollar"));
