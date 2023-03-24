mod expression;
mod models;

mod parse;

use std::mem;

use expression::expression::Expression;
use models::vars::VarValues;
use parse::check::{check_validity, Status};

pub fn result(expression: &str) {
    use Status::*;

    match check_validity(expression) {
        Ok => (),
        Unexpected(i, ch) => {
            let init_msg = format!("unexpected '{}' in \"", ch);
            let init_spaces = init_msg.len() + i;

            println!("{}{}\" at index {}", init_msg, expression, i);

            for _ in 0..init_spaces {
                print!(" ")
            }
            println!("^");
            return;
        }
        ExpectedAtEnd(s) => {
            let init_msg = format!("expected {} at end of \"{}", s, expression);

            println!("{}\"", init_msg);

            for _ in 0..init_msg.len() {
                print!(" ");
            }
            println!("^");
            return;
        }
        Msg(s) => {
            println!("{}", s);
            return;
        }
    }

    let (expr, var_values) = parse::parsing::parse(expression);

    display(expression, &expr, var_values)
}

fn display(original: &str, expression: &Expression, mut var_values: VarValues) {
    let mut name_lengths = vec![];

    for name in var_values.names() {
        name_lengths.push(name.len());
        print!("{} ", name)
    }

    let mut results: Vec<u8> = vec![];
    let mut pcnf_values = vec![];
    let mut pdnf_values = vec![];

    print!(" —  {}", original);
    println!("\n");

    let mut even = true;

    loop {
        for (space, value) in name_lengths.iter().zip(var_values.values()) {
            if value {
                print!("T");
            } else {
                print!("F");
            }
            for _ in 0..*space {
                print!(" ");
            }
        }

        if even {
            print!(" -  ")
        } else {
            print!(" —  ")
        };
        even = !even;

        if expression.evaluate(&var_values) {
            results.push(1);
            pdnf_values.push(var_values.values());
            print!("T");
        } else {
            results.push(0);
            pcnf_values.push(var_values.values());
            print!("F");
        }
        println!();

        if !var_values.advance() {
            break;
        }
    }

    println!();

    let pcnf = pcnf_values
        .clone()
        .into_iter()
        .fold(vec![], |mut acc, item| {
            let n = item.len();
            let mut word = String::new();

            word.push_str("(");
            for (i, value) in item.into_iter().enumerate() {
                let letter = var_values.names().nth(i).unwrap();
                if value {
                    word.push_str(letter.as_str());
                } else {
                    word.push_str(format!("!{}", letter.as_str()).as_str());
                }
                if i == n - 1 {
                    word.push_str(")")
                } else {
                    word.push_str("&");
                }
            }

            acc.push(word);

            acc
        })
        .join("|");
    let binary_pcnf = pcnf_values
        .clone()
        .into_iter()
        .fold(vec![], |mut acc, item| {
            for value in item {
                let byte: u8 = unsafe { mem::transmute(value) };
                acc.push(byte)
            }

            acc
        });

    println!("PCNF: {}", pcnf);
    println!("Binary PCNF: {:?}\n", binary_pcnf);

    let pdnf = pdnf_values
        .into_iter()
        .fold(vec![], |mut acc, item| {
            let n = item.len();
            let mut word = String::new();

            word.push_str("(");
            for (i, value) in item.into_iter().enumerate() {
                let letter = var_values.names().nth(i).unwrap();
                if value {
                    word.push_str(letter.as_str());
                } else {
                    word.push_str(letter.as_str());
                }
                if i == n - 1 {
                    word.push_str(")")
                } else {
                    word.push_str("|");
                }
            }

            acc.push(word);

            acc
        })
        .join("&");
    let binary_pdnf = pcnf_values
        .clone()
        .into_iter()
        .fold(vec![], |mut acc, item| {
            for value in item {
                let byte: u8 = unsafe { mem::transmute(value) };
                acc.push(byte)
            }

            acc
        });

    println!("PDNF: {}", pdnf);
    println!("Binary PDNF: {:?}\n", binary_pdnf);

    let index = results.into_iter().fold(0, |acc, digit| (acc << 1) + digit);
    println!("Index: {}", index)
}
