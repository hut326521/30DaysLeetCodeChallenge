/*
Step 1: Build a HashMap<Key: arrValue, Val: List of index which has same arrValue>
Step 2: Init a queue and offer init val(0)
Step 3: Run BFS(In every stage, there are 3 posible next step sides: index+1, index-1, all of the index which have same arrValue) 

Time complexity: O(N)
Space complexity: O(N)
*/
class Solution {
    public int minJumps(int[] arr) {
        if(arr.length == 1) {
            return 0;
        }
        HashMap<Integer,List<Integer>> mMap = new HashMap<>();
        int step = 0;
        
        for(int i = 0; i < arr.length; i++) {
            if(mMap.containsKey(arr[i])) {
                List<Integer> mTempList = new LinkedList<>();
                mTempList = mMap.get(arr[i]);
                mTempList.add(i);
                mMap.put(arr[i], mTempList);
            } else {
                List<Integer> mTempList = new LinkedList<>();
                mTempList.add(i);
                mMap.put(arr[i], mTempList);
 
            }
        }
        
        Queue<Integer> q = new LinkedList<>();
        q.offer(0);
        
        while(!q.isEmpty()) {
            step++;
            int size = q.size();
            
            for(int i = 0; i < size; i++) {
                int cur = q.poll();
                
                if((cur - 1) >= 0 && mMap.containsKey(arr[cur - 1])) {
                    q.offer(cur - 1);
                }
                
                if((cur + 1) < arr.length && mMap.containsKey(arr[cur + 1])) {
                    if((cur + 1) == (arr.length - 1)){
                        return step;
                    }
                    
                    q.offer(cur + 1);
                }
                
                if(mMap.containsKey(arr[cur])) {
                    for(int j : mMap.get(arr[cur])) {
                        if(j != cur) {
                            if(j == (arr.length - 1)){
                                return step;
                            }
                            q.offer(j);
                        }
                    }
                }
                mMap.remove(arr[cur]);
            }
        }
        return step;
    }
}