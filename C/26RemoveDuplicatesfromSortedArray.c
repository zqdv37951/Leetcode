#include <stdbool.h>
#include <stdio.h>
// #define true 1
// #define FALSE 0
int removeDuplicates(int *nums, int numsSize)
{
    int index1 = 0;
    int index2 = 1;

    if (numsSize <= 0)
    {
        return numsSize;
    }
    if (nums[index1] == nums[index2])
    {
        if (index2 == numsSize - 1)
        {
            return index1 + 1;
        }
        index2++;
    }
    else
    {
        index1++;
        nums[index1] = nums[index2];
        if (index2 == (numsSize - 1))
        {
            return (index1 + 1);
        }
        else
        {
            index2++;
        }
    }
}
int main()
{
    int nums[] = {1, 1, 1, 2, 4, 5, 5, 6};
    int numsSize = 8;
    printf("Usernames are:  %d\n", removeDuplicates(nums, numsSize));
    return 0;
}
