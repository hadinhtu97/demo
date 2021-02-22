var displayTree = tree => console.log(JSON.stringify(tree, null, 2));
function Node(value) {
    this.value = value;
    this.left = null;
    this.right = null;
}
function BinarySearchTree() {
    this.root = null

    this.add = (val) => {
        if (this.root == null) {
            this.root = new Node(val);
            return undefined
        } else {
            let current = this.root
            while (current) {
                if (val == current.value) {
                    return null
                } else if (val < current.value) {
                    if (current.left == null) {
                        let newNode = new Node(val);
                        current.left = newNode
                        return undefined
                    } else {
                        current = current.left
                    }
                } else if (val > current.value) {
                    if (current.right == null) {
                        let newNode = new Node(val)
                        current.right = newNode
                        return undefined
                    } else {
                        current = current.right
                    }
                }
            }
        }
    }

    this.findMax = () => {
        if (this.root == null) {
            return null
        } else {
            let current = this.root
            while (current.right) {
                current = current.right
            }
            return current.value
        }
    }
    this.findMin = () => {
        if (this.root == null) {
            return null
        } else {
            let current = this.root
            while (current.left) {
                current = current.left
            }
            return current.value
        }
    }

    this.isPresent = (val) => {
        if (this.root = null) {
            return false
        } else {
            let current = this.root
            while (current) {
                if (val == current.value) {
                    return true
                } else if (val < current.value) {
                    current = current.left
                } else if (val > current.value) {
                    current = current.right
                }
            }
            return false
        }
    }

    this.isBinarySearchTree = (tree) => {
        if (tree.root == null) {
            return null
        } else {
            let isBST = true;
            function checkNode(node) {
                if (node.left != null) {
                    if (node.left.value > node.value) {
                        return isBST = false
                    } else {
                        checkNode(node.left)
                    }
                }
                if (node.right != null) {
                    if (node.right.value < node.value) {
                        return isBST = false
                    } else {
                        checkNode(node.right)
                    }
                }
            }
            checkNode(tree.root)
            return isBST
        }
    }

}