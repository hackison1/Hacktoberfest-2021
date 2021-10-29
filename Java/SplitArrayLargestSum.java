/*
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.


Input: nums = [7,2,5,10,8], m = 2
Output: 18

*/

public class Solution {
    public int splitArray(int[] nums, int m) {
        long sum = 0;
        int max = 0;
        for(int num: nums){
            max = Math.max(max, num);
            sum += num;
        }
        return (int)binary(nums, m, sum, max);
    }
    
    private long binary(int[] nums, int m, long high, long low){
        long mid = 0;
        while(low < high){
            mid = (high + low)/2;
            if(valid(nums, m, mid)){
                //System.out.println(mid);
                high = mid;
            }else{
                low = mid + 1;
            }
        }
        return high;
    }
    
    private boolean valid(int[] nums, int m, long max){
        int cur = 0;
        int count = 1;
        for(int num: nums){
            cur += num;
            if(cur > max){
                cur = num;
                count++;
                if(count > m){
                    return false;
                }
            }
        }
        return true;
    }
}
