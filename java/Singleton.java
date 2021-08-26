public class Singleton {

    private static Singleton singleton;

    private Singleton() {}

    public static Singleton getSingleton() {
        if (singleton == null) {
            synchronized(Singleton.class) {
                if (singleton == null) {
                    singleton = new Singleton();
                }
            }
        }
        return singleton;
    }

    public void print() {
        System.out.println(this);
    }

    public static void main(String[] args) {
        Singleton.getSingleton().print();
        Singleton.getSingleton().print();
        Singleton.getSingleton().print();
        Singleton.getSingleton().print();
        Singleton.getSingleton().print();
    }

}