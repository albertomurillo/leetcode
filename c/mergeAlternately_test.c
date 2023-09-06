#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "mergeAlternately.c"

typedef struct test {
    char* word1;
    char* word2;
    char* want;
} test;

int main(int argc, char* argv[])
{
    test tests[] = {
        { "abc", "pqr", "apbqcr" },
        { "ab", "pqrs", "apbqrs" },
        { "abcd", "pq", "apbqcd" },
    };
    size_t len_tests = sizeof(tests) / sizeof(test);

    for (size_t i = 0; i < len_tests; i++) {
        test* t = &tests[i];
        char* got = mergeAlternately(t->word1, t->word2);
        assert(strcmp(got, t->want) == 0);
        free(got);
    }

    exit(EXIT_SUCCESS);
}
