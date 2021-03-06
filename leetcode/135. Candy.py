# https://leetcode.com/problems/candy/description/

# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
#
# Example 1:
#
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:
#
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.


def main():
    n = int(input())
    rating_value = list(map(int, input().split(' ')))
    cnt = [1 for _ in range(n)]
    for i in range(1, n):
        if rating_value[i] > rating_value[i - 1]:
            cnt[i] = cnt[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if rating_value[i] > rating_value[i + 1] and cnt[i] < cnt[i + 1]:
            cnt[i] = cnt[i + 1] + 1
    return sum(cnt)


if __name__ == '__main__':
    result = main()
    print(result)
