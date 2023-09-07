//  https://leetcode.com/problems/two-sum/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include "lib/uthash.h"

struct map {
    int key;
    int val;
    UT_hash_handle hh;
};

int* twoSum(int* nums, int numsSize, int target, int* returnSize)
{
    int* result = calloc(*returnSize = 2, sizeof(int));

    struct map* seen = NULL;
    struct map* item;
    struct map* tmp;

    for (int i = 0; i < numsSize; i++) {
        int want = target - nums[i];

        HASH_FIND_INT(seen, &want, item);
        if (item != NULL) {
            result[0] = item->val;
            result[1] = i;
            break;
        }

        item = malloc(sizeof(struct map));
        item->key = nums[i];
        item->val = i;
        HASH_ADD_INT(seen, key, item);
    }

    HASH_ITER(hh, seen, item, tmp)
    {
        HASH_DEL(seen, item);
        free(item);
    }

    return result;
}
