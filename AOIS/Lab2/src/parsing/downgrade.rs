use std::ops::{RangeBounds, Bound};

use super::parsing::Parsing;

fn downgrade<R>(range: R, parsing: &mut Vec<Parsing>) where R: RangeBounds<usize> {
    let index = match range.start_bound() {
        Bound::Included(t) => *t,
        Bound::Unbounded => 0,
        _ => panic!("foo")
    };

    let sub: Vec<Parsing> = parsing.drain(range).collect();
    parsing.insert(index, Parsing::SubList(sub))
}

pub fn downgrade_braces(parsing: &mut Vec<Parsing>) {
    for sub in parsing.iter_mut() {
        if let Parsing::SubList(s) = sub {
            downgrade_braces(s)
        }
    }

    loop {
        let mut maybe_open = None;
        let mut maybe_close = None;

        for (i, sub) in parsing.iter().enumerate() {
            if sub.string_eq("(") {
                maybe_open = Some(i);
            } else if sub.string_eq(")") {
                maybe_close = Some(i);
                break;
            }
        }

        if maybe_open.is_none() {
            break;
        }

        let (first, last) = (maybe_open.unwrap(), maybe_close.unwrap());

        downgrade(first+1..last, parsing);

        parsing.remove(first);
        parsing.remove(first+1);
    }
}

pub fn downgrade_unary_not(parsing: &mut Vec<Parsing>) {
    for sub in parsing.iter_mut() {
        if let Parsing::SubList(s) = sub {
            downgrade_unary_not(s);
        }
    }

    loop {
        let maybe_index = parsing.iter().position(|x| x.string_eq("!"));
        if let Some(index) = maybe_index {
            let mut obliterated = false;
            if let Parsing::String(s) = &parsing[index + 1] {
                if s == "!" {
                    parsing.remove(index);
                    parsing.remove(index);
                    obliterated = true;
                }
            }

            if !obliterated {
                downgrade(index..index+2, parsing);
            }
        } else {
            break
        }            
    }
}

pub fn downgrade_and(parsing: &mut Vec<Parsing>) {
    downgrade_binary("&", parsing)
}

pub fn downgrade_or(parsing: &mut Vec<Parsing>) {
    downgrade_binary("|", parsing)
}

pub fn dowgrade_implication(parsing: &mut Vec<Parsing>) {
    downgrade_binary("=>", parsing)
}

pub fn downgrade_biconditional(parsing: &mut Vec<Parsing>) {
    downgrade_binary("<=>", parsing)
}

fn downgrade_binary(op: &str, parsing: &mut Vec<Parsing>) {
    for sub in parsing.iter_mut() {
        if let Parsing::SubList(s) = sub {
            downgrade_binary(op, parsing);
        }
    }

    loop {
        let maybe_index = parsing.iter().position(|x| x.string_eq(op));
        if let Some(index) = maybe_index {
            downgrade(index-1..index+2, parsing);
        } else {
            break;
        }
    }

}