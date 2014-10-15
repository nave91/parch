import java.util.*;
import java.io.*;

class collectset {
    public static void main(String args[])
	throws IOException{
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	System.out.println("Give number:");
	int n = Integer.parseInt(br.readLine());
	String name[] = new String[n];
	for (int i=0;i<n;i++){
	    name[i] = br.readLine();
	}
	for(int i=0;i<name.length;i++){
	    System.out.println(name[i]);
	}
	List l  = Arrays.asList(name);
	System.out.println(l);
	Set s = new Set();
	s.addAll(l);
	System.out.println(l);
    }
}
