/*
Check if edges are enough, then DFS.
*/
class Solution {
    Set<Integer> visited = new HashSet<>();
    HashMap<Integer, LinkedList<Integer>> graph = new HashMap<>();

    public int makeConnected(int n, int[][] connections) {
        if((n-1) > connections.length) {
            return -1;
        }

        for(int[] path : connections) {
            int pcA = path [0];
            int pcB = path[1];

            if(graph.containsKey(pcA)) {
                graph.get(pcA).add(pcB);
            } else {
                LinkedList<Integer> tempList = new LinkedList<>();
                tempList.add(pcB);
                graph.put(pcA, tempList);
            }

            if(graph.containsKey(pcB)) {
                graph.get(pcB).add(pcA);
            } else {
                LinkedList<Integer> tempList = new LinkedList<>();
                tempList.add(pcA);
                graph.put(pcB, tempList);
            }
        }

        // Cal amount of group
        int groupNum = 0;

        for(int i = 0; i < n; i++) {
            if(!visited.contains(i)) {
                groupNum++;
                dfs(i);
            }
        }

        return groupNum - 1;
    }

    void dfs(int n) {
        visited.add(n);
        
        if(graph.get(n) != null) {
            for(int curNode : graph.get(n)){
                if(!visited.contains(curNode)) {
                    dfs(curNode);
                }
            }
        }
    }
}