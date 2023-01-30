public class test{
    public static void main(String[] args) {
        Pet[] p = {new Dog(), new Cat(), new Parrot()};
        for(int i = 0; i<3; i++)
            p[i].talk();
    }
}


