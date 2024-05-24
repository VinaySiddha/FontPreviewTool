package internal;

class Outer {
    static int data =  59;
    static class inner{
        void show() {
            System.err.println("data" +data);
        }
    }
    public static void main(String args[]) {
        Outer.inner o = new Outer.inner();
        o.show();
    }
    
}
