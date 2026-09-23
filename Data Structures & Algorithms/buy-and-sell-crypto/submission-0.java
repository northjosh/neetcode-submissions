class Solution {
     public int maxProfit(int[] prices) {
        int min = prices[0];
        int[] set = new int[prices.length];

        for (int i= 0; i < prices.length; i++) {
            if (prices[i] < min) {
                min = prices[i];
            }
            set[i] = (prices[i] - min);
        }
        Arrays.sort(set);

        return set[prices.length - 1]; // or set[prices.length -1]
    }
}
