// https://leetcode.com/problems/evaluate-reverse-polish-notation

use crate::leetcode::Solution;

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack = vec![];
        for token in tokens {
            if let Ok(n) = token.parse() {
                stack.push(n);
                continue;
            }

            let (y, x) = (stack.pop().unwrap(), stack.pop().unwrap());
            match token.as_str() {
                "+" => stack.push(x + y),
                "-" => stack.push(x - y),
                "*" => stack.push(x * y),
                "/" => stack.push(x / y),
                _ => unreachable!(),
            }
        }

        stack.pop().unwrap()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let tokens = vec!["2", "1", "+", "3", "*"];
        let tokens = tokens.into_iter().map(|s: &str| s.to_string()).collect();
        let got = Solution::eval_rpn(tokens);
        assert_eq!(got, 9);
    }

    #[test]
    fn example_2() {
        let tokens = vec!["4", "13", "5", "/", "+"];
        let tokens = tokens.into_iter().map(|s| s.to_string()).collect();
        let got = Solution::eval_rpn(tokens);
        assert_eq!(got, 6);
    }

    #[test]
    fn example_3() {
        let tokens = vec![
            "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+",
        ];
        let tokens = tokens.into_iter().map(|s| s.to_string()).collect();
        let got = Solution::eval_rpn(tokens);
        assert_eq!(got, 22);
    }
}
