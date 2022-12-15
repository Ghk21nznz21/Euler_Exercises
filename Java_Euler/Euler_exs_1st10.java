import java.util.stream 

class run {
		public static void main(String [] args){
			int EU1 = Euler.euler1();
			int EU2 = Euler2.euler2();
			int [] lista_range= IntStream.rangeClosed(1, 10).toArray();
			int EU3 =Euler3.euler3(10,lista_range);
			System.out.println(EU1);
			System.out.println(EU2);
			
			}
}
class Euler{

	public static int euler1(){
		int sum=0;
		for (int i =0; i<1000; i++){
			if (i%3==0 || i%5==0 ){sum+=i; }
			}
		return sum;
		}
}

class Euler2{

	public static int euler2(){
		int a=0,b=1;
		int sum=0;
		while (b<=4000000){
			if(b%2==0){
				sum +=b;}
			int c= b, d= a+b;
			a=c;b=d;}
		return sum; 
	}
}
class Euler3{
	public static int euler3(int number, int[] lista){
		for(int i : lista){
			if(number%i==0){
				return i; } }
			return 0;	
		}
}


		

	
	



