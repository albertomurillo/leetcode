// https://leetcode.com/problems/group-anagrams

use crate::leetcode::Solution;
use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut anagrams: HashMap<[u8; 26], Vec<String>> = HashMap::new();

        for word in strs {
            let mut key = [0; 26];
            word.bytes().for_each(|c| key[(c - b'a') as usize] += 1);
            anagrams.entry(key).or_default().push(word);
        }

        anagrams.into_values().collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::vec_of_strings;

    fn sorted(input: Vec<Vec<String>>) -> Vec<Vec<String>> {
        let mut output = Vec::with_capacity(input.len());
        for v in input {
            let mut v = v.clone();
            v.sort();
            output.push(v);
        }
        output.sort();
        output
    }

    #[test]
    fn example_1() {
        let strs = vec_of_strings!["eat", "tea", "tan", "ate", "nat", "bat"];
        let want = vec![
            vec_of_strings!["bat"],
            vec_of_strings!["nat", "tan"],
            vec_of_strings!["ate", "eat", "tea"],
        ];
        let got: Vec<Vec<String>> = Solution::group_anagrams(strs);
        assert_eq!(sorted(got), sorted(want));
    }

    #[test]
    fn example_2() {
        let strs = vec_of_strings![""];
        let want = vec![vec_of_strings![""]];
        let got = Solution::group_anagrams(strs);
        assert_eq!(sorted(got), sorted(want));
    }

    #[test]
    fn example_3() {
        let strs = vec_of_strings!["a"];
        let want = vec![vec_of_strings!["a"]];
        let got = Solution::group_anagrams(strs);
        assert_eq!(sorted(got), sorted(want));
    }
}
