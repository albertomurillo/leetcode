// https://leetcode.com/problems/binary-search
use crate::leetcode::Solution;

use std::cmp::Ordering;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left = 0;
        let mut right = nums.len();

        while left < right {
            let mid = (left + right) / 2;
            match nums[mid].cmp(&target) {
                Ordering::Less => left = mid + 1,
                Ordering::Greater => right = mid,
                Ordering::Equal => return mid as i32,
            }
        }

        -1
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let got = Solution::search(vec![-1, 0, 3, 5, 9, 12], 9);
        assert_eq!(got, 4);
    }

    #[test]
    fn example_2() {
        let got = Solution::search(vec![-1, 0, 3, 5, 9, 12], 2);
        assert_eq!(got, -1);
    }

    #[test]
    fn example_3() {
        let got = Solution::search(vec![5], -5);
        assert_eq!(got, -1);
    }

    #[test]
    fn example_4() {
        let got = Solution::search(vec![5], 5);
        assert_eq!(got, 0);
    }
}
