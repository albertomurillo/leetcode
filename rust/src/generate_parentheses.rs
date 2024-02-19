// https://leetcode.com/problems/generate-parentheses

use crate::leetcode::Solution;

impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let n = n as u32;
        let mut result = vec![];
        let mut stack = String::new();

        fn dfs(result: &mut Vec<String>, stack: &mut String, open: u32, closed: u32) {
            if open == 0 && closed == 0 {
                result.push(stack.clone());
                return;
            }

            if open > 0 {
                stack.push('(');
                dfs(result, stack, open - 1, closed);
                stack.pop();
            }

            if closed > open {
                stack.push(')');
                dfs(result, stack, open, closed - 1);
                stack.pop();
            }
        }
        dfs(&mut result, &mut stack, n, n);

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let want = vec!["((()))", "(()())", "(())()", "()(())", "()()()"];
        let got = Solution::generate_parenthesis(3);
        assert_eq!(got, want);
    }

    #[test]
    fn example_2() {
        let want = vec!["()"];
        let got = Solution::generate_parenthesis(1);
        assert_eq!(got, want);
    }
}
