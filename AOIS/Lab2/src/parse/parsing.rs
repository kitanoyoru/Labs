use super::downgrade::{
    dowgrade_implication, downgrade_and, downgrade_biconditional, downgrade_braces, downgrade_or,
    downgrade_unary_not,
};

use crate::expression::expression::Expression;
use crate::models::vars::VarValues;

pub enum Parsing {
    String(String),
    SubList(Vec<Parsing>),
}

impl Parsing {
    pub fn string_eq(&self, other: &str) -> bool {
        if let Parsing::String(s) = self {
            return s.as_str() == other;
        }

        false
    }
}

pub fn to_parts(from: &str) -> Vec<String> {
    let mut parts = vec![];
    let mut part = String::new();
    let mut last: Option<char> = None;

    for ch in from.chars() {
        match ch {
            ' ' => (),
            'a'..='z' | 'A'..='Z' => {
                if let Some(l) = last {
                    if !l.is_alphabetic() && !part.is_empty() {
                        parts.push(part);
                        part = String::new();
                    }
                }

                part.push(ch)
            }
            '&' | '|' | '!' | '(' | ')' => {
                if !part.is_empty() {
                    parts.push(part);
                    part = String::new()
                }

                let mut p = String::new();
                p.push(ch);
                parts.push(p)
            }
            '<' => {
                if !part.is_empty() {
                    parts.push(part);
                    part = String::new()
                }

                part.push(ch)
            }
            '=' => {
                if last.unwrap() != '<' && !part.is_empty() {
                    parts.push(part);
                    part = String::new();
                }

                part.push(ch)
            }
            '>' => {
                part.push(ch);
                parts.push(part);
                part = String::new()
            }
            _ => panic!("foo"),
        }

        last = Some(ch)
    }

    if !part.is_empty() {
        parts.push(part)
    }

    parts
}

pub fn extract_names(parts: &[String]) -> Vec<String> {
    let mut vars = vec![];
    for part in parts {
        if part.chars().next().unwrap().is_alphabetic() {
            vars.push(part.clone());
        }
    }

    vars
}

pub fn to_expression(parsing: &Parsing) -> Expression {
    match parsing {
        Parsing::String(s) => Expression::Variable(s.clone()),
        Parsing::SubList(l) => match l.len() {
            1 => to_expression(&l[0]),
            2 => Expression::NotUnaryOperation(Box::new(to_expression(&l[1]))),
            3 => {
                if let Parsing::String(s) = &l[1] {
                    let left = Box::new(to_expression(&l[0]));
                    let right = Box::new(to_expression(&l[2]));

                    use crate::expression::expression::BinaryOperationTypes::*;

                    match s.as_str() {
                        "&" => Expression::BinaryOperation(And, left, right),
                        "|" => Expression::BinaryOperation(Or, left, right),
                        "=>" => Expression::BinaryOperation(Implication, left, right),
                        "<=>" => Expression::BinaryOperation(Biconditional, left, right),
                        _ => panic!("Unexpected operation"),
                    }
                } else {
                    unreachable!("Some internal error while parsing expression");
                }
            }
            _ => unreachable!("foo"),
        },
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

    let expression = to_expression(&Parsing::SubList(parsing));

    (expression, vars)
}
