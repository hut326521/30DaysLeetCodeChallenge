// Use DFS to count size in a group.
// Count (n - size)*size for all group, then sum would be ans. 
class Solution {
    HashMap<Integer, LinkedList<Integer>> graph = new HashMap<>();
    HashSet<Integer> visited = new HashSet<>();
    int countNumInGroup = 0;
    double ans = 0L;
    
    public long countPairs(int n, int[][] edges) {
        // Build the map.
        
        if(edges != null) {
            for(int[] edge : edges) {
                int p1 = edge[0];
                int p2 = edge[1];
            
                graph.computeIfAbsent(p1, key -> new LinkedList<Integer>()).add(p2);
                graph.computeIfAbsent(p2, key -> new LinkedList<Integer>()).add(p1);
            }
        }
        
        for(int i = 0; i < n; i++) {
            if(!visited.contains(i)) {
                dfs(i);
                
                double tempAns = ((double)(n - countNumInGroup)*(double)countNumInGroup);
                ans += tempAns;
                countNumInGroup = 0;
            }
        }
        
        return (long)ans/2;
    }
    
    void dfs(int p) {
        countNumInGroup++;
        visited.add(p);
        
        if(!graph.containsKey(p)) {
            return;
        }
        
        for(int nextPoint : graph.get(p)) {
            if(!visited.contains(nextPoint)) {
                dfs(nextPoint);
            }
        }
    }
}