use libtruthtable::result;

fn main() {
    let expr1 = "((p => !q) & r) <=> (!r => q)";
    result(expr1);
}
