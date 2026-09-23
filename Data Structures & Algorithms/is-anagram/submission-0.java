class Solution {
   public boolean isAnagram(String s, String t) {
        Map<Character, Integer> first = new HashMap<>();
        Map<Character, Integer> second = new HashMap<>();

        for(char s1: s.toCharArray()){
            first.put(s1, first.getOrDefault(s1, 0) + 1 );
        }
        for(char s2: t.toCharArray()){
            second.put(s2, second.getOrDefault(s2, 0) + 1);
        }

        return first.equals(second);

    }
}
