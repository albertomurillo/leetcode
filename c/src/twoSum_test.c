#include <assert.h>
#include <stdlib.h>

#include "twoSum.c"

typedef struct test {
    int* nums;
    int nums_size;
    int target;
    int* want;
} test;

int cmpfunc(const void* a, const void* b)
{
    return (*(int*)a - *(int*)b);
}

int main(int argc, char* argv[])
{
    test tests[] = {
        { (int[]) { 2, 7, 11, 15 }, 4, 9, (int[]) { 0, 1 } },
        { (int[]) { 3, 2, 4 }, 3, 6, (int[]) { 1, 2 } },
        { (int[]) { 3, 3 }, 2, 6, (int[]) { 0, 1 } },
    };
    size_t len_tests = sizeof(tests) / sizeof(test);
    size_t len_got = 2;

    for (size_t i = 0; i < len_tests; i++) {
        test* t = &tests[i];
        int return_size;
        int* got = twoSum(t->nums, t->nums_size, t->target, &return_size);
        qsort(got, len_got, sizeof(int), cmpfunc);
        assert(memcmp(got, t->want, sizeof(int) * len_got) == 0);
        free(got);
    }

    exit(EXIT_SUCCESS);
}
