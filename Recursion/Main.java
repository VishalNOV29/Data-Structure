class Main {
    static void run(int number) {
        if (number >= 0) {
            run(number - 1);
        }
        System.out.println("I am called for"+number);
    }

    public static void main(String[] args) {
        run(10);
    }

}