class Solution {
    int ans = -1;
    HashSet<Integer> visited = new HashSet<>();
    int[] mEdges;
    
    public int longestCycle(int[] edges) {
        mEdges = edges;
        HashMap<Integer, Integer> localRecord = new HashMap<>();
        
        for(int n = 0; n < edges.length; n++) {
            if(!visited.contains(n)) {
                localRecord.clear();
                localRecord.put(n, 0);
                
                dfs(n, localRecord);
            }
            
            if(visited.size() > edges.length/2) {
                break;
            }
        }
        
        return ans;
    }
    
    void dfs(int n, HashMap<Integer, Integer> localRecord) {
        visited.add(n);
        
        if(mEdges[n] == -1) {
            return;
        }
        
        if(localRecord.containsKey(mEdges[n])) {
            ans = Math.max(ans, localRecord.get(n) - localRecord.get(mEdges[n]) + 1);
            
            return;
        }
        
        if(!visited.contains(mEdges[n])) {
            localRecord.put(mEdges[n], localRecord.get(n) + 1);
            dfs(mEdges[n], localRecord);
        }
    }
}