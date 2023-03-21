mod expression;
mod vars;

mod parse;
mod check_validity;

mod display;

mod simplify;

pub fn get_table(expresion: &str) {
    match check_validity(expression) {
        Ok => (),
        UnexpectedSymbol(i, ch) => ()
    }

    let (expr, var_val) = parse::parse(expression);

    display::display(expression, &expr, &var_val)
}