
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

public class VulnerableService {

    // VULNERABILITY 1: Hardcoded API key
    private static final String API_KEY =
            "sk_test_1234567890abcdef123456";

    // VULNERABILITY 2: SQL Injection
    public static void getUser(Connection connection, String username)
            throws Exception {

        Statement statement = connection.createStatement();

        String query = "SELECT * FROM users WHERE username = '"
                + username + "'";

        ResultSet result = statement.executeQuery(query);

        while (result.next()) {
            System.out.println(result.getString("username"));
        }
    }
}
