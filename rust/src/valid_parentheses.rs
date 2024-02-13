// https://leetcode.com/problems/valid-parentheses
use crate::leetcode::Solution;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();

        for c in s.chars() {
            match c {
                '(' => stack.push(')'),
                '[' => stack.push(']'),
                '{' => stack.push('}'),
                ')' | ']' | '}' => {
                    if Some(c) != stack.pop() {
                        return false;
                    }
                }
                _ => return false,
            };
        }

        stack.is_empty()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let got = Solution::is_valid("()".to_string());
        assert_eq!(got, true);
    }

    #[test]
    fn example_2() {
        let got = Solution::is_valid("()[]{}".to_string());
        assert_eq!(got, true);
    }

    #[test]
    fn example_3() {
        let got = Solution::is_valid("(]".to_string());
        assert_eq!(got, false);
    }
}
