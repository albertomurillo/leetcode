#include <assert.h>
#include <stdlib.h>
#include <string.h>

#include "kidsWithCandies.c"

typedef struct test {
    int* candies;
    int candiesSize;
    int extraCandies;
    bool* want;
} test;

int main(int argc, char* argv[])
{
    test tests[] = {
        { (int[]) { 2, 3, 5, 1, 3 }, 5, 3, (bool[]) { true, true, true, false, true } },
        { (int[]) { 4, 2, 1, 1, 2 }, 5, 1, (bool[]) { true, false, false, false, false } },
        { (int[]) { 12, 1, 12 }, 3, 10, (bool[]) { true, false, true } },
    };
    size_t len_tests = sizeof(tests) / sizeof(test);

    for (size_t i = 0; i < len_tests; i++) {
        test* t = &tests[i];
        int returnSize = 0;
        bool* got = kidsWithCandies(t->candies, t->candiesSize, t->extraCandies, &returnSize);
        assert(returnSize == t->candiesSize);
        assert(memcmp(got, t->want, sizeof(bool) * returnSize) == 0);
        free(got);
    }

    exit(EXIT_SUCCESS);
}
