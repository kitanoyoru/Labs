use super::downgrade::{downgrade_braces, downgrade_unary_not, downgrade_and, downgrade_or, dowgrade_implication, downgrade_biconditional};
use super::str_ops::{to_parts, extract_names};

use crate::vars::vars::VarValues;
use crate::expression::expression::Expression;

pub enum Parsing {
    String(String),
    SubList(Vec<Parsing>)
}

impl Parsing {
    pub fn string_eq(&self, other: &str) -> bool {
        if let Parsing::String(s) = self {
            return s.as_str() == other
        }

        false
    }
}

pub fn parse(from: &str) -> (Expression, VarValues) {
    let parts = to_parts(from);
    let vars = VarValues::new(&extract_names(&parts));

    let mut parsing: Vec<Parsing> = parts.into_iter().map(Parsing::String).collect();

    downgrade_braces(&mut parsing);
    downgrade_unary_not(&mut parsing);
    downgrade_and(&mut parsing);
    downgrade_or(&mut parsing);
    dowgrade_implication(&mut parsing);
    downgrade_biconditional(&mut parsing);

    let expression = Expression::from(parsing);

    (expression, vars)

    
}
