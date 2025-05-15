class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int now = health;
        int befTime = 0;
        
        int t = bandage[0];
        int x = bandage[1];
        int y = bandage[2];
        
        for (int[] attack: attacks) {
            int time = attack[0];
            int restTime = time - befTime;

            now += (restTime / t) * (t * x + y) + restTime % t * x;
            now = Math.min(now, health);
            
            System.out.println(now);

            now -= attack[1];
            if (now <= 0)
                return -1;
            befTime = time + 1;
            
            System.out.println(now);
        }
        
        return now;
    }
}