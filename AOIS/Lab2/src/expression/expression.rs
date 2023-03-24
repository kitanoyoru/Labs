use crate::expression::functions::{and, biconditional, implication, not, or};
use crate::models::vars::VarValues;

pub enum BinaryOperationTypes {
    And,
    Or,
    Implication,
    Biconditional,
}

pub enum Expression {
    Variable(String),
    BinaryOperation(BinaryOperationTypes, Box<Expression>, Box<Expression>),
    NotUnaryOperation(Box<Expression>),
}

impl Expression {
    pub fn evaluate(&self, vals: &VarValues) -> bool {
        use BinaryOperationTypes::*;
        use Expression::*;

        match self {
            Variable(v) => vals.get_value(v),
            NotUnaryOperation(expr) => not(expr.evaluate(vals)),
            BinaryOperation(op, left, right) => {
                let func = match op {
                    And => and,
                    Or => or,
                    Implication => implication,
                    Biconditional => biconditional,
                };

                func(left.evaluate(vals), right.evaluate(vals))
            }
        }
    }
}
