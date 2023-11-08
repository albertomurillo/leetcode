#include <assert.h>
#include <stdlib.h>

#include "findDuplicate.c"

typedef struct test {
    int* nums;
    int numsSize;
    int want;
} test;

int main(int argc, char* argv[])
{
    test tests[] = {
        { (int[]) { 1, 3, 4, 2, 2 }, 5, 2 },
        { (int[]) { 3, 1, 3, 4, 2 }, 5, 3 },
    };
    size_t len_tests = sizeof(tests) / sizeof(test);

    for (size_t i = 0; i < len_tests; i++) {
        test* t = &tests[i];
        int got = findDuplicate(t->nums, t->numsSize);
        assert(got == t->want);
    }

    exit(EXIT_SUCCESS);
}
