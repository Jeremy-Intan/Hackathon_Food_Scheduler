import java.util.Date;

//import java.sql.Date;

public class getTime {

        Date dateInstance = new Date();
        int year = dateInstance.getYear()+1900;//Returns:the year represented by this date, minus 1900.
        int date = dateInstance.getDate();
        int month = dateInstance.getMonth();
        int day = dateInstance.getDay();
        int hours = dateInstance.getHours();
        int min = dateInstance.getMinutes();
        int sec = dateInstance.getSeconds();
      
}
