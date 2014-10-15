class deadlock {
    public static Object lock1 = new Object();
    public static Object lock2 = new Object();

    private static class ThreadDemo1 implements Runnable{
	private Thread t;
	private String tname;
	
	ThreadDemo1(String name){
	    tname = name;
	    System.out.println("Starting "+name+"...");
	}
    
	public void run() {
	    synchronized(lock1){
		try {
		    System.out.println("Holding lock1..");
		    Thread.sleep(50);
		} catch (InterruptedException e) {
		    System.out.println("Thread: "+tname+" interrupted.");
		}
		System.out.println("Thread 1 waiting fo rlock2..");
		synchronized(lock2){
		    System.out.println("Hoding lock 1 & 2");
		}
		System.out.println("Thread: "+tname+" exiting.");
	    }
	}
	public void start(){
	    System.out.println("Starting "+tname+".");
	    if (t == null){
		t = new Thread (this,tname);
		t.start();
	    }
	}
}

    private static class ThreadDemo2 implements Runnable{
	private Thread t;
	private String tname;
	
	ThreadDemo2(String name){
	    tname = name;
	    System.out.println("Starting "+name+"...");
	}
	
	public void run() {
	    synchronized(lock1){
		try {
		    System.out.println("Holding lock2..");
		    Thread.sleep(50);
		} catch (InterruptedException e) {
		    System.out.println("Thread: "+tname+" interrupted.");
		}
		System.out.println("Thread 2 waiting fo rlock1..");
		synchronized(lock2){
		    System.out.println("Holding lock 1 & 2");
		}
		System.out.println("Thread: "+tname+" exiting.");
	    }
	}
	
	public void start(){
	    System.out.println("Starting "+tname+".");
	    if (t == null){
		t = new Thread (this,tname);
		t.start();
	    }
	}
    }

    
    
    public static void main(String args[]){
	ThreadDemo1 td1 = new ThreadDemo1("one");
	td1.start();
	ThreadDemo2 td2 = new ThreadDemo2("two");
	td2.start();
    }
}
