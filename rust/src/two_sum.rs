// https://leetcode.com/problems/two-sum/
use crate::leetcode::Solution;

use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen = HashMap::with_capacity(nums.len());

        for (i, num) in nums.iter().enumerate() {
            let want = target - num;
            match seen.get(&want) {
                Some(v) => return vec![i as i32, *v as i32],
                None => seen.insert(num, i),
            };
        }

        vec![]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut got: Vec<i32> = Solution::two_sum(vec![2, 7, 11, 15], 9);
        got.sort();
        assert_eq!(got, vec![0, 1]);
    }

    #[test]
    fn example_2() {
        let mut got = Solution::two_sum(vec![3, 2, 4], 6);
        got.sort();
        assert_eq!(got, vec![1, 2]);
    }

    #[test]
    fn example_3() {
        let mut got = Solution::two_sum(vec![3, 3], 6);
        got.sort();
        assert_eq!(got, vec![0, 1]);
    }
}
