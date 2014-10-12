class class_asd {
    public static void main1(String args[]){
	System.out.println("Nope");
    }
}
class wow extends class_asd{
    public static void main(String args[]){
	class_asd.main1();
	System.out.println("asdasdasd");
    }
}
