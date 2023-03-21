
// Binary operations

pub fn and(left: bool, right: bool) -> bool {
    left && right
}

pub fn or(left: bool, right: bool) -> bool {
    left || right
}

pub fn implication(left: bool, right: bool) -> bool {
    !left || right
}

pub fn biconditional(left: bool, right: bool) -> bool {
    left == right
}

// Unary operations

pub fn not(value: bool) -> bool {
    !value
}