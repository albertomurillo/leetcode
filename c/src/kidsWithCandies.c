// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

#include <limits.h>
#include <stdbool.h>
#include <stddef.h>

bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize)
{
    bool* result = (bool*)malloc(candiesSize * sizeof(bool));
    if (result == NULL)
        return NULL;
    *returnSize = candiesSize;

    int max = INT_MIN;
    for (size_t i = 0; i < candiesSize; i++)
        max = candies[i] > max ? candies[i] : max;

    for (size_t i = 0; i < candiesSize; i++)
        result[i] = candies[i] + extraCandies >= max;

    return result;
}
