import java.io.*; 
import java.util.*;
import java.lang.*;

class MusicDownloader { 
    public static void main(String[] args) 
    { 
        Scanner sc = new Scanner(System.in);

        System.out.print("what is the link? ");
        String link = sc.nextLine();

        System.out.print("what is the name of the song? ");
        String song_name = sc.nextLine();
        
        System.out.println(link + " " + song_name); 

        ProcessBuilder pb = new ProcessBuilder("/home/imax/yt-dlp/yt-dlp.sh", "https://www.youtube.com/watch?v=iNKiQfJO6jE");
        Process p = pb.start();

        BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String line = null;
        while ((line = reader.readLine()) != null)
        {
            System.out.println(line);
        }

    } 
} 