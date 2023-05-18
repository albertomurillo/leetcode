// https://leetcode.com/problems/water-bottles/

int numWaterBottles(int numBottles, int numExchange)
{
    int full = numBottles;
    int empty = 0;
    int drank = 0;

    while (full > 0) {
        drank += full;
        empty += full;
        full = empty / numExchange;
        empty = empty % numExchange;
    }

    return drank;
}
