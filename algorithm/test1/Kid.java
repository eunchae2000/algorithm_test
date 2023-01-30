
public class Kid {
    private Robot toy;

    public void setToy(Robot toy)
    {
        this.toy = toy;
    }

    public void play() {
        System.out.println(toy.toString());
    }
}