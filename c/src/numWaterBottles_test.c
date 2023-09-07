#include <assert.h>
#include <stdlib.h>

#include "numWaterBottles.c"

typedef struct test {
    int bottles;
    int exchange;
    int want;
} test;

int main(int argc, char* argv[])
{
    test tests[] = {
        { 9, 3, 13 },
        { 15, 4, 19 },
    };
    size_t len_tests = sizeof(tests) / sizeof(test);

    for (size_t i = 0; i < len_tests; i++) {
        test* t = &tests[i];
        int got = numWaterBottles(t->bottles, t->exchange);
        assert(got == t->want);
    }

    exit(EXIT_SUCCESS);
}
