class Loading {
    Loading(){
	int k = summer(1,2);
	System.out.println(k);
	double j = summer(0.65,0.67);
	System.out.println(j);
    }
    private int summer(int a, int b){
	return a+b;
    }
    private double summer(double a, double b){
	return a+b;
    }
}

class Ride {
    void aval(){
	System.out.println("aval = ride");
    }
}

class Riding extends Ride {
    Riding(){
	Ride ride1 = new Ride();
	aval();
    }
    void aval(){
	System.out.println("aval = riding");
    }
}
	
class LoadingRiding {
    public static void main(String args[]){
	Loading load = new Loading();
	Riding riding = new Riding();
	Ride ride = new Ride();
	ride.aval();
	riding.aval();
    }
}
