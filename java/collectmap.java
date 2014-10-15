import java.util.*;
import java.io.*;

class collectmap {
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
	Map<String,String> m = new HashMap<String,String>();
	
	for (int i=0;i<name.length;i++){
	    m.put(Integer.toString(i),name[i]);
	    }
	m.put("asdasd","asdasasd");
	Set s = m.keySet();
	for (String i: m.keySet()){
	    System.out.println(i+"- "+m.get(i));
	}
	//for (String i: m.keySet())
	//    System.out.println(i+'-'+m.get(i));
		
	//System.out.println(m);
    }
}
