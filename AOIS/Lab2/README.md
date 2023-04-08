# AOIS Lab3


## Configuration

Change logic formala in **src/main.rs** right here:
```rust
fn main() {
    let expr = "((p => !q) & r) | (!r => q)";
    result(expr);
}
```

**Logic operations**

* & - *conjunction*
* | - *disjunction*
* => - *implication*
* <=> - *biconditial*


## Install deps and run 
```sh
# In root folder
cargo run . 
```



