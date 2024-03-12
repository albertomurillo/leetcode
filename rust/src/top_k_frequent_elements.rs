// https://leetcode.com/problems/top-k-frequent-elements
use crate::leetcode::Solution;

use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();

        let mut counter: HashMap<i32, usize> = HashMap::with_capacity(n);
        for num in nums {
            *counter.entry(num).or_default() += 1;
        }

        let mut bucket = vec![vec![]; n + 1];
        for (num, count) in counter {
            bucket[count].push(num);
        }

        bucket
            .into_iter()
            .rev()
            .filter(|x| !x.is_empty())
            .flatten()
            .take(k as usize)
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let got = Solution::top_k_frequent(vec![1, 1, 1, 2, 2, 3], 2);
        assert_eq!(got, vec![1, 2]);
    }

    #[test]
    fn example_2() {
        let got = Solution::top_k_frequent(vec![1], 1);
        assert_eq!(got, vec![1]);
    }
}
