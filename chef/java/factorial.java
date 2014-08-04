import java.io.*;

class factorial{
    public static void main(String args[]) throws IOException{
	BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
	int c,num;
	int t = Integer.parseInt(stdin.readLine());
	for(int i=0;i<t;i++){
	    c = 0;
	    num = Integer.parseInt(stdin.readLine());
	    while(num >= 5){
		c += num/5;
		num /= 5;
	    }
	    System.out.println(c);
	}
    }
}
