/*
1. Record all roads in HashMap.
2. Start traversing by BFS from 1, and find all points which can be arrived
3. Find minimal Distance. 
*/
class Solution {
    public int minScore(int n, int[][] roads) {
        Map<Integer, Map<Integer, Integer>> graph = new HashMap<>();
        
        for (int[] road : roads) {
            int u = road[0];
            int v = road[1];
            int d = road[2];
            
            if(!graph.containsKey(u)) {
                HashMap<Integer, Integer> tempMap = new HashMap<>();
                tempMap.put(v, d);
                graph.put(u, tempMap);
            } else {
                graph.get(u).put(v, d);
            }
            
            if(!graph.containsKey(v)) {
                HashMap<Integer, Integer> tempMap = new HashMap<>();
                tempMap.put(u, d);
                graph.put(v, tempMap);
            } else {
                graph.get(v).put(u, d);
            }
        }
		
		// Start BFS
        int res = Integer.MAX_VALUE;
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> q = new LinkedList<>();
        q.offer(1);

        while (!q.isEmpty()) {
            int node = q.poll();
            for (Map.Entry<Integer, Integer> entry : graph.get(node).entrySet()) {
                int adj = entry.getKey();
                int score = entry.getValue();
                
                if (!visited.contains(adj)) {
                    q.offer(adj);
                    visited.add(adj);
                }
                
                res = Math.min(res, score);
            }
        }

        return res;
    }
}