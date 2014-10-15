class ThreadDemo implements Runnable{
    private Thread t;
    private String tname;
    
    ThreadDemo(String name){
	tname = name;
	System.out.println("Starting "+name+"...");
    }
    
    public void run() {
	try {
	    for(int i=0; i<5; i++){
		System.out.println("Thread: "+tname+
				   "value: "+i);
		Thread.sleep(50);
	    }
	} catch (InterruptedException e) {
	    System.out.println("Thread: "+tname+" interrupted.");
	}
	System.out.println("Thread: "+tname+" exiting.");
    }
    
    public void start(){
	System.out.println("Starting "+tname+".");
	if (t == null){
	    t = new Thread (this,tname);
	    t.start();
	}
    }
}



class threads {
    public static void main(String args[]){
	ThreadDemo td = new ThreadDemo("one");
	td.start();
	ThreadDemo td2 = new ThreadDemo("two");
	td2.start();
    }
}
