use crate::expression::functions::{and, or, implication, biconditional, not};

use super::super::vars::vars::VarValues; // REFACTOR


pub enum BinaryOperationTypes {
    And,
    Or,
    Implication,
    Biconditional
}

pub enum UnaryOperationTypes {
    Not
}

pub enum Expression {
    Variable(String),
    BinaryOperation(BinaryOperationTypes, Box<Expression>, Box<Expression>),
    UnaryOperation(UnaryOperationTypes, Box<Expression>)
}

impl Expression {
    pub fn evaluate(&self, vals: &VarValues) -> bool {
        use Expression::*;
        use BinaryOperationTypes::*;
        use UnaryOperationTypes::*;

        match self {
            Variable(v) => vals.get_value(v),
            BinaryOperation(op, left, right) => {
                let func = match op {
                    And => and,
                    Or => or,
                    Implication => implication,
                    Biconditional => biconditional
                };

                func(left.evaluate(vals), right.evaluate(vals))
            },
            UnaryOperation(op, val) => {
                let func = match op {
                    Not => not
                };

                func(val.evaluate(vals))
            }
        }
    }
}