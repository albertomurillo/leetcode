// https://leetcode.com/problems/valid-anagram

#include <stdbool.h>
#include <strings.h>

bool isAnagram(char* s, char* t)
{
    int seen[26] = { 0 };

    for (; *s != '\0'; s++)
        seen[*s - 'a']++;

    for (; *t != '\0'; t++)
        seen[*t - 'a']--;

    for (size_t i = 0; i < 26; i++) {
        if (seen[i] != 0)
            return false;
    }

    return true;
}
