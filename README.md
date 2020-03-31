# Five-day Leetcode Challange

All the Leetcode problems are selected from [60 LeetCode problems to solve for coding interview](https://medium.com/@koheiarai94/60-leetcode-questions-to-prepare-for-coding-interview-8abbb6af589e). This article is highly recommended by me if you want to do some pratice on data structure and algorithms. It collects 60 problems and sorts them based on core techniques.

## Day 1 - Dynamic Programming

Leetcode problem: [198. House Robber](https://leetcode.com/problems/house-robber/) - Easy

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

**Example 1**:  

```text
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

**Example 2**;  

```text
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
```

## Day 2 - Graph

Leetcode problem: [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) - Medium

Given a 2d grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1**:

```text
Input:
11110
11010
11000
00000

Output: 1
```

**Example 2**:

```text
Input:
11000
11000
00100
00011

Output: 3
```

## Day 3 - Sliding Window

Leetcode problem: [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) - Medium

Given an array of **n** positive integers and a positive integer **s**, find the minimal length of a **contiguous** subarray of which the sum ≥ **s**. If there isn't one, return 0 instead.

**Example:**:

```text
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
```

## Day 4 - Back tracking

Leetcode problem: [39. Combination Sum](https://leetcode.com/problems/combination-sum/) - Medium

Given a **set** of candidate numbers (`candidates`) (**without duplicates**) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

The same repeated number may be chosen from `candidates` unlimited number of times.

**Note:**

* All numbers (including target) will be positive integers.
* The solution set must not contain duplicate combinations.

**Example 1**:

```text
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```

**Example 2**:

```text
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```
