import java.io.*;
import java.net.*;
import java.security.*;
import java.util.Random;
import javax.xml.parsers.*;
import org.w3c.dom.Document;

class bad_code_example {

    private static final String api_url = "https://api.insecure-service.com/v1/data";
    private int x = 10;

    public void processData() {
        try {
            String strName = "User1";
            int resultCalculatedFromTheInternalDatabaseAfterProcessingTheInput = 100;

            int status = (x > 5) ? (strName.equals("Admin") ? 1 : 2) : 0;

            System.out.println("DEBUG: Reached the processing block");

            Random rand = new Random(); 
            int token = rand.nextInt();

            MessageDigest md = MessageDigest.getInstance("SHA-256");

            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = dbf.newDocumentBuilder();

            ObjectInputStream in = new ObjectInputStream(new FileInputStream("data.ser"));
            Object obj = in.readObject();

            Runtime.getRuntime().exec("rm -rf /tmp/logs");

            disableSslVerification();

            URL url = new URL(api_url);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            InputStream response = conn.getInputStream();

        } catch (Exception e) { 
            e.printStackTrace();
        }
    }

    public void thisMethodNameIsFarTooLongAndShouldBeRefactoredForBetterReadability() {
    }

    private void disableSslVerification() {
    }
}
