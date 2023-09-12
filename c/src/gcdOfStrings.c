// https://leetcode.com/problems/greatest-common-divisor-of-strings/

#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

unsigned int gcd(const unsigned int a, const unsigned int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

char* gcdOfStrings(char* str1, char* str2)
{
    size_t len_str1 = strlen(str1);
    size_t len_str2 = strlen(str2);
    size_t len_s1_s2 = len_str1 + len_str2 + 1;

    // result = ""
    int n = gcd(len_str1, len_str2);
    char* result = (char*)calloc(n + 1, sizeof(char));
    if (result == NULL)
        return NULL;

    // if str1 + str2 != str2 + str1: return result
    char* s1_s2 = alloca(len_s1_s2 * sizeof(char));
    if (s1_s2 == NULL)
        return NULL;
    snprintf(s1_s2, len_s1_s2, "%s%s", str1, str2);
    if (memcmp(s1_s2, str2, len_str2) != 0) {
        return result;
    }
    if (memcmp(s1_s2 + len_str2 * sizeof(char), str1, len_str1) != 0) {
        return result;
    }

    // Return str1[:n]
    memcpy(result, str1, n * sizeof(char));
    return result;
}
