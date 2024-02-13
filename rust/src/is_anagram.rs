// https://leetcode.com/problems/valid-anagram
use crate::leetcode::Solution;

use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut map = HashMap::new();

        for c in s.chars() {
            map.entry(c).and_modify(|e| *e += 1).or_insert(1);
        }

        for c in t.chars() {
            map.entry(c).and_modify(|e| *e -= 1).or_insert(-1);
        }

        for val in map.into_values() {
            if val != 0 {
                return false;
            }
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let got = Solution::is_anagram("anagram".to_string(), "nagaram".to_string());
        assert_eq!(got, true);
    }

    #[test]
    fn example_2() {
        let got = Solution::is_anagram("rat".to_string(), "car".to_string());
        assert_eq!(got, false);
    }
}
