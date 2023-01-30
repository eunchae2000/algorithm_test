abstract class Pet{
    public abstract void talk();
}

class Dog extends Pet{
    public void talk(){
        System.out.println("멍멍");
    }
}

class Cat extends Pet{
    public void talk(){
        System.out.println("야옹");
    }
}

class Parrot extends Pet{
    public void talk(){
        System.out.println("안녀엉");
    }
}

public class test1{
    public static void main(String[] args) {
        Pet[] p = {new Dog(), new Cat(), new Parrot()};
        for(int i = 0; i<3; i++)
            p[i].talk();
    }
}

