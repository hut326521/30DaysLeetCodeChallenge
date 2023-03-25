/*
BFS and count reverse road.
*/

class Solution {
    public int minReorder(int n, int[][] connections) {
        HashMap<Integer, LinkedList<Integer>> graph = new HashMap<>();
        Queue<Integer> q = new LinkedList<>();
        HashSet<Integer> visited = new HashSet<>();

        int ans = 0;

        for(int[] path : connections) {
            int aCity = path[0];
            int bCity = path[1];

            graph.computeIfAbsent(aCity, key -> new LinkedList<>()).add(bCity);
            graph.computeIfAbsent(bCity, key -> new LinkedList<>()).add(aCity * -1);
        }

        q.offer(0);

        while(!q.isEmpty()) {
            int curCity = q.poll();

            for(int adj : graph.get(curCity)) {
                if(!visited.contains(Math.abs(adj))) {
                    q.offer(Math.abs(adj));
                    if(adj > 0){
                        ans++;
                    }
                }
            }
            visited.add(curCity);
        }
        return ans;
    }
}
