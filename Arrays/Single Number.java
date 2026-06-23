class Solution {
    public int singleNumber(int[] nums) {
        int s=1;
        for(int i=0;i<nums.length;i++){
            int c=0;
            for(int j=0;j<nums.length;j++){
                if(nums[i]==nums[j]){
                    c+=1;
                }
            }
            if(c==0||c==1){
                s=nums[i];
            }
        }
        return s;
    }
}
