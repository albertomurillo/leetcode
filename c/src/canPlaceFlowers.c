// https://leetcode.com/problems/can-place-flowers

#include <stdbool.h>

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n)
{
    const int lastIndex = flowerbedSize - 1;
    for (int i = 0; i <= lastIndex;) {
        if (n == 0)
            return true;

        if (flowerbed[i]) {
            i += 2;
            continue;
        }

        if (i < lastIndex && flowerbed[i + 1]) {
            i += 3;
            continue;
        }

        if (i > 0 && flowerbed[i - 1]) {
            i++;
            continue;
        }

        n -= 1;
        i += 2;
    }

    return n <= 0;
}
