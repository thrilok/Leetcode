import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

class Solution {
    public String smallestSubsequence(String s) {
        Set<Character> added = new HashSet<Character>();
        HashMap<Character, Integer> frequency= new HashMap<Character, Integer>();
        Stack<Character> result = new Stack<Character>();

        for (Character ch: s.toCharArray()){
            Integer value = frequency.get(ch);
            if (value == null){
                frequency.put(ch, 1);
            } else {
                frequency.put(ch, value+1);
            }
        }

        for (Character ch: s.toCharArray()){
            frequency.put(ch, frequency.get(ch)-1);
            if (added.contains(ch)){
                continue;
            }
            while (!result.isEmpty() && frequency.get(result.lastElement())> 0 && result.lastElement()> ch) {
                added.remove(result.pop());
            }
            added.add(ch);
            result.push(ch);
        }
        String finalResult = new String();
        while (!result.isEmpty()){
            finalResult = result.pop()+finalResult;
        }
        return finalResult;
    }
}