class Solution {
    public int getIntTime(String stringTime) {
        String[] times = stringTime.split(":");
        int m = Integer.parseInt(times[0]);
        int s = Integer.parseInt(times[1]);
        
        return m * 60 + s;
    }
    
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        int videoTotal = getIntTime(video_len);
        int time = getIntTime(pos);
        int openingStart = getIntTime(op_start);
        int openingEnd = getIntTime(op_end);
        
        if (openingStart <= time && time <= openingEnd)
            time = openingEnd;
        
        for (String command: commands) {
            if (command.equals("next")) {
                time = Math.min(videoTotal, time+10);
            } else if (command.equals("prev")) {
                time = Math.max(0, time-10);
            }
            
            if (openingStart <= time && time <= openingEnd)
                time = openingEnd;
        }
        
        int m = time / 60;
        int h = time % 60;
        
        return (m < 10 ? "0" + m : m) + ":" + (h < 10 ? "0" + h : h);
    }
}