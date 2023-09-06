// https://leetcode.com/problems/merge-strings-alternately

#include <stdlib.h>
#include <string.h>

char* mergeAlternately(char* word1, char* word2)
{
    size_t len_w1 = strlen(word1);
    size_t len_w2 = strlen(word2);

    char* buff = (char*)calloc((len_w1 + len_w2 + 1), sizeof(char));
    if (buff == NULL)
        exit(EXIT_FAILURE);

    size_t i = 0;
    size_t j = 0;
    size_t k = 0;
    while ((i < len_w1) && (j < len_w2)) {
        buff[k++] = word1[i++];
        buff[k++] = word2[j++];
    }
    memcpy(&buff[k], &word1[i], sizeof(char) * (len_w1 - i));
    memcpy(&buff[k], &word2[j], sizeof(char) * (len_w2 - j));

    return buff;
}
