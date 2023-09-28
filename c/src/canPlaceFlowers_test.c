#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

#include "canPlaceFlowers.c"

typedef struct test {
    int* flowerbed;
    size_t flowerbedSize;
    int n;
    bool want;
} test;

int main(int argc, char* argv[])
{
    test tests[] = {
        { (int[]) { 1, 0, 0, 0, 1 }, 5, 1, true },
        { (int[]) { 1, 0, 0, 0, 1 }, 5, 2, false },
        { (int[]) { 0, 1, 1, 0, 0 }, 5, 1, true },
    };
    size_t len_tests = sizeof(tests) / sizeof(test);

    for (size_t i = 0; i < len_tests; i++) {
        test* t = &tests[i];
        bool got = canPlaceFlowers(t->flowerbed, t->flowerbedSize, t->n);
        assert(got == t->want);
    }

    exit(EXIT_SUCCESS);
}
