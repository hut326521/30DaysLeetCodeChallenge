/*
Easily solved by Double Linked list.
*/
class BrowserHistory {
    Node curNode;

    public BrowserHistory(String homepage) {
        curNode = new Node(homepage);
    }
    
    public void visit(String url) {
        curNode.next = new Node(url);
        curNode.next.prev = curNode;
        curNode = curNode.next;
    }
    
    public String back(int steps) {
        while (curNode.prev != null && steps > 0) {
            curNode = curNode.prev;
            steps--;
        }
        
        return curNode.mUrl;
    }
    
    public String forward(int steps) {
        while (curNode.next != null && steps > 0) {
            curNode = curNode.next;
            steps--;
        }
        
        return curNode.mUrl;
    }
}


class Node {
  Node prev;
  Node next;
  String mUrl;

  public Node(final String url) {
    mUrl = url;
  }
}