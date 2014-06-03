import java.io.*;

class enormous_input_java{
    public static void main(String argv[]) throws IOException{
	int in=0,n=0,k=0,count=0;
	while((in=System.in.read())!=' '){
	    n = 10*n+in -'0';
	}
	while((in=System.in.read())!='\n'){
		k = 10*k+in - '0';
	    }
	int[] arr = new int[n];
	for(int i=0; i<n; i++){
	    int temp = 0;
	    while((in=System.in.read())!='\n'){
		temp = 10*temp+in - '0';
	    }
	    if(temp%k==0){
		count += 1;
	    }
	}
	System.out.println(count);
    }
}
