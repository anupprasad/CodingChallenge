import java.util.ArrayList;

public class SwordPuzzle {

	public static ArrayList<Integer> peeps=new ArrayList<Integer>();
	public static ArrayList<Integer> killed=new ArrayList<>();
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		initialize(1000, peeps);
	/*	kill(peeps, killed, 0);
		notKilled(peeps, killed);*/
		kill2(peeps,1);
	}
	
	public static void initialize(int n,ArrayList<Integer> peeps)
	{
		for(int i=0;i<n;i++)
		{
			peeps.add(i+1);
		}
	}
	
	public static void kill(ArrayList<Integer> peeps,ArrayList<Integer> killed,int start)
	{
		if(killed.size()==peeps.size()-1)
		{
			return;
		}
		
		for(;(start)<peeps.size();start=start+2)
		{
			
			if((start)+1<peeps.size() && (!killed.contains(peeps.get((start)+1))))
			{
			   killed.add(peeps.get((start%peeps.size())+1));
			}
		}
		
		kill(peeps,killed,(start-1)%peeps.size());
	}

	public static void notKilled(ArrayList<Integer> peeps,ArrayList<Integer> killed)
	{
		for(Integer i:peeps)
		{
			if(!killed.contains(i))
			{
				System.out.println("person Not killed "+i);
				break;
			}
		}
	}
	
	public static void kill2(ArrayList<Integer> peeps,int start)
	{
		
		ArrayList<Integer> alive=new ArrayList<>();
		if(start>peeps.size())
		{
			System.out.println("\n ############ Kutto Chyutiya Mat Banao #############");
			return;
		}
		if(peeps.size()==1)
		{
			System.out.println("\n******* And The Winner is "+peeps.get(0)+" ************");
			return;
		}
		boolean isKilled=false;
		int sword=start-1;
		if(sword<0)
		{
			sword=0;
		}
		int i=0;
		System.out.println("\n-------------------Killing Spree Begins Here -----------\n");
		while(sword<peeps.size())
		{
			isKilled=false;
			for( ;i<start-1;i++)
			{
				alive.add(peeps.get(i));
			}
			alive.add(peeps.get(sword));
			if((sword+1)<peeps.size())
			{
				isKilled=true;
				System.out.println("\n Person Killed "+peeps.get(sword+1)+" By "+peeps.get(sword)+"\n");
			}
			else
			{
				break;
			}
			sword=sword+2;
			
		}
		if(!isKilled)
		{
			alive.add(0, peeps.get(peeps.size()-1));
			alive.remove(alive.size()-1);
			
		}
		System.out.println("\n Peeps Alive are "+alive.toString()+" and Sword is with first person");
		
		kill2(alive,0);
	
	}
	
	
}
