    int removeDuplicates(vector<int>& nums) {
        
        int count = 0;
      
        
        for(int i = 1; i < nums.size(); ++i){
            
            if(nums[i] == nums[i-1]){
                
                nums.erase(nums.begin()+i);
                i--;
                
            
            }
            
            
        }
        return nums.size();
    }
