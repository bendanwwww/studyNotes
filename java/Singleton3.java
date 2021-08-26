public class Singleton3 {

    private Singleton3() {}

    public static Singleton getSingleton() {
        return Singleton.SINGLE;
    }

    enum Singleton {

        SINGLE;

        private Singleton() {}

        public void print() {
            System.out.println("enum eingle");
        }

    }

    public static void main(String[] args) {
        Singleton3.getSingleton().print();
        Singleton3.getSingleton().print();
        Singleton3.getSingleton().print();
        Singleton3.getSingleton().print();
        Singleton3.getSingleton().print();
    }

}