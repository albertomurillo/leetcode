#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "isAnagram.c"

typedef struct test {
    char* s;
    char* t;
    bool want;
} test;

int main(int argc, char* argv[])
{
    test tests[] = {
        { "anagram", "nagaram", true },
        { "rat", "car", false },
    };
    size_t len_tests = sizeof(tests) / sizeof(test);

    for (size_t i = 0; i < len_tests; i++) {
        test* t = &tests[i];
        bool got = isAnagram(t->s, t->t);
        assert(got == t->want);
    }

    exit(EXIT_SUCCESS);
}
