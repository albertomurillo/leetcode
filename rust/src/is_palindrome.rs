// https://leetcode.com/problems/valid-palindrome
use crate::leetcode::Solution;

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let chars: Vec<char> = s
            .chars()
            .filter(|c| c.is_alphanumeric())
            .map(|c| c.to_lowercase().next().unwrap())
            .collect();

        let mut left = 0;
        let mut right = if chars.is_empty() { 0 } else { chars.len() - 1 };
        while left < right {
            if chars[left] != chars[right] {
                return false;
            }
            left += 1;
            right -= 1;
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let got = Solution::is_palindrome("A man, a plan, a canal: Panama".to_string());
        assert_eq!(got, true);
    }

    #[test]
    fn example_2() {
        let got = Solution::is_palindrome("race a car".to_string());
        assert_eq!(got, false);
    }

    #[test]
    fn example_3() {
        let got = Solution::is_palindrome(" ".to_string());
        assert_eq!(got, true);
    }
}
