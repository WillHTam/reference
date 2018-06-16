import java.util.Arrays;  
import java.lang.Math;

public class PowerSet  
{
   public static void main(String[] args)
   {
      System.out.println(Arrays.toString(findPowerSet("abc")));
      System.out.println(Arrays.toString(findPowerSet("power")));
   }

   public static String[] findPowerSet(String input)
   {
      int inputLength = input.length();
      int powerSetSize = (int)Math.pow(2, inputLength);
      String[] result = new String[powerSetSize];

      for (int k = 0; k < powerSetSize; k++) 
      {
         String set = "";
         int binaryDigits = k;
         for (int j = 0; j < inputLength; j++)
         {
            if (binaryDigits % 2 == 1)
               set += input.charAt(j);
            binaryDigits >>= 1;
         }
         result[k] = set;
      }

      return result;
   }
}
