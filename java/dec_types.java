class dec_types {
    public static void main(String args[]){
	String str1 = "Hi";
	String str2 = new String("Hi2");
	int num1 = 10;
	System.out.println(str1+str2+num1);
	int[] numarr1 = new int[3];
	int[] numarr2 = {1,2,3};
	int[] numarr3 = new int[]{1,2,3};
	//doesnt work
	// System.out.println(numarr1,numarr2,numarr3);
	for (int i=0; i<numarr1.length; i++){
	    System.out.print(numarr1[i]+",");
	}
    }
}
