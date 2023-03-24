use libtruthtable::result;

fn main() {
    let expr = "((p => !q) & r) | (!r => q)";
    result(expr);
}
