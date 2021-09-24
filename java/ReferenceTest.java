import java.lang.ref.WeakReference;

public class ReferenceTest {

    public static void main(String[] args) throws Exception {
        String referent = "abc";
        WeakReference weakReference = new WeakReference(referent);
        referent = null;
        // System.gc();
        // Thread.sleep(10000);
        System.out.println(weakReference.get());
    }
}