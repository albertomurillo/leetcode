#include <assert.h>
#include <stdlib.h>

#include "fib.c"

typedef struct test {
    int given;
    int want;
} test;

int main(int argc, char* argv[])
{
    test tests[] = {
        { 2, 1 },
        { 3, 2 },
        { 4, 3 },
    };
    size_t len_tests = sizeof(tests) / sizeof(test);

    for (size_t i = 0; i < len_tests; i++) {
        test* t = &tests[i];
        int got = fib(t->given);
        assert(got == t->want);
    }

    exit(EXIT_SUCCESS);
}
