class MentalMath {
  public static void main(String args[])
    throws java.io.IOException {
    System.out.println("Mental Math Test!"); //DELETEME

    char ch;
    String sentence = "";
    ch = (char) System.in.read();

    do {
      sentence += ch;
    } while(ch != '.');

    System.out.println(ch);

  }
}