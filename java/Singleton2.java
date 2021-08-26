public class Singleton2 {

    private Singleton2() {}

    public static Singleton2 getSingleton() {
        return Singleton2.GetSingleton.singleton;
    }

    public void print() {
        System.out.println(this);
    }

    private static class GetSingleton {
        private static final Singleton2 singleton = new Singleton2();
    }

    public static void main(String[] args) {
        Singleton2.getSingleton().print();
        Singleton2.getSingleton().print();
        Singleton2.getSingleton().print();
        Singleton2.getSingleton().print();
        Singleton2.getSingleton().print();
    }

}