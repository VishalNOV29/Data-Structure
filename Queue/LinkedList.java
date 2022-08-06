class Queue {
    class Node {
        String data;
        Node next;

        public Node(String data) {
            this.data = data;
            this.next = null;
        }
    }

    Node head;

    public Queue(String data) {
        head = null;
    }
    
}