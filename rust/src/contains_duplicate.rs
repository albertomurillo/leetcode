// https://leetcode.com/problems/contains-duplicate
use crate::leetcode::Solution;

use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut seen = HashSet::with_capacity(nums.len());
        for n in nums {
            match seen.get(&n) {
                Some(_) => return true,
                None => seen.insert(n),
            };
        }
        false
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let got = Solution::contains_duplicate(vec![1, 2, 3, 1]);
        assert_eq!(got, true);
    }

    #[test]
    fn example_2() {
        let got = Solution::contains_duplicate(vec![1, 2, 3, 4]);
        assert_eq!(got, false);
    }

    #[test]
    fn example_3() {
        let got = Solution::contains_duplicate(vec![1, 1, 1, 3, 3, 4, 3, 2, 4, 2]);
        assert_eq!(got, true);
    }
}
