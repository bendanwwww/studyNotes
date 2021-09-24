public class GenericTest<T extends Object> {

    private T t;

    public GenericTest(T t) {
        this.t = t;
    }

    public T getT() {
        return t;
    }

    public static void main(String[] args) {
        GenericTest<? super RuntimeException> generic = new GenericTest<Exception>(new Exception());
        System.out.println(generic.getT().getClass());
    }
    
}