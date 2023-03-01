/*
To practice different Algos, I use QuickSort to solve this problem. 
Although the worst case of qiucksort may exceed O(nlogn), it pass all of the test case on LC. 
*/
class Solution {
    public int[] sortArray(int[] nums) {
        quickSort(nums, 0, nums.length-1);
        
        return nums;
    }
    
    public void quickSort(int[] nums, int start, int end){
        if(start >= end) {
          return;  
        }
        
        int pivot = nums[(start + end)/2];
        int left = start;
        int right = end;
        
        while (left <= right) {
            while (left <= right && nums[left] < pivot ) {
                left++;
            }
        
            while (left <= right && nums[right] > pivot) {
                right--;
            }
            
            if(left <= right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                
                left++;
                right--;
            }
        }
        quickSort(nums, start, right);
        quickSort(nums, left, end);
    }
}