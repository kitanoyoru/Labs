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
            },
            '&' | '|' | '!' | '(' | ')' => {
                if !part.is_empty() {
                    parts.push(part);
                    part = String::new()
                }

                let mut p = String::new();
                p.push(ch);
                parts.push(p)
            },
            '<' => {
                if !part.is_empty() {
                    parts.push(part);
                    part = String::new()
                }

                part.push(ch)
            },
            '=' => {
                if last.unwrap() != '<' && !part.is_empty() {
                    parts.push(part);
                    part = String::new();
                }

                part.push(ch)
            },
            '>' => {
                part.push(ch);
                parts.push(part);
                part = String::new()
            },
            _ => panic!("foo")
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