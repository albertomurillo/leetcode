#include <assert.h>
#include <stdlib.h>
#include <string.h>

#include "gcdOfStrings.c"

typedef struct test {
    char* str1;
    char* str2;
    char* want;
} test;

int main(int argc, char* argv[])
{
    test tests[] = {
        { "ABCABC", "ABC", "ABC" },
        { "ABABAB", "ABAB", "AB" },
        { "LEET", "CODE", "" },
    };
    size_t len_tests = sizeof(tests) / sizeof(test);

    for (size_t i = 0; i < len_tests; i++) {
        test* t = &tests[i];
        char* got = gcdOfStrings(t->str1, t->str2);
        assert(strcmp(got, t->want) == 0);
        free(got);
    }

    exit(EXIT_SUCCESS);
}
