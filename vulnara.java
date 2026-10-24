
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

public class PaymentService {

    private static final String PAYMENT_API_KEY =
            System.getenv("PAYMENT_API_KEY");

    public boolean checkPayment(Connection db, String email)
            throws Exception {

        // Vulnerability: SQL injection via String.format()
        String sql = String.format(
                "SELECT * FROM payments WHERE email = '%s'",
                email
        );

        Statement stmt = db.createStatement();
        ResultSet rs = stmt.executeQuery(sql);

        return rs.next();
    }
}
