class singleton {
    private static singleton instance = null;
    private singleton() {
    }
    
    public static singleton getInstance() {
	System.out.println("asdasd");
	if (instance == null) {
	    instance = new singleton();
	}
	return instance;
    }
}


class Main {
    public static void main(String args[]){
	singleton sin = singleton.getInstance();
	singleton sin 2= singleton.getInstance();
    }
}
