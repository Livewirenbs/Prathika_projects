package project;
import java.awt.*;
import java.awt.event.*;
import java.sql.*;
import javax.swing.*;
public class Login extends Dashboard {
    static final String url = "jdbc:mysql://localhost:3306/ps";
    static final String user = "root";
    static final String pass = "ps@123";

    public static void homepage() {
    //‪‪C:\\Users\\ELCOT\\Downloads\\voting.jpeg
        JFrame f = new JFrame("Login");
        ImageIcon img = new ImageIcon("c:\\Users\\ELCOT\\Downloads\\Voting.jpeg");
        f.setContentPane(new JLabel(img));
        f.setLayout(null);
        JLabel heading = new JLabel("Cody Hub....");

        heading.setOpaque(false); // Transparent
        heading.setBounds(550, 150, 400, 50);
        heading.setFont(new Font("Arial", Font.BOLD | Font.ITALIC, 50));

        f.add(heading);

        Label l = new Label("Username:");
        l.setFont(new Font("italic", Font.BOLD, 40));
        l.setBounds(350, 250, 250, 50);
        f.add(l);
        TextField t = new TextField();
        t.setFont(new Font("italic", Font.BOLD, 40));
        t.setForeground(Color.blue);
        t.setBounds(650, 250, 250, 50);
        f.add(t);

        Label l1 = new Label("Password:");
        l1.setFont(new Font("italic", Font.BOLD, 40));
        l1.setBounds(350, 450, 250, 50);
        f.add(l1);

        JPasswordField t1 = new JPasswordField();
        t1.setFont(new Font("italic", Font.BOLD, 40));
        t1.setForeground(Color.blue);
        t1.setBounds(650, 450, 250, 50);
        f.add(t1);

        Button b = new Button("Login");
        b.setBackground(Color.GRAY);
        b.setFont(new Font("italic", Font.BOLD, 40));
        b.setBounds(370, 600, 250, 50);
        f.add(b);

        b.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String uname = t.getText();
                String pwd = new String(t1.getPassword());

                try {
                    Connection c = DriverManager.getConnection(url, user, pass);
                    PreparedStatement p = c.prepareStatement(
                            "SELECT * FROM detail WHERE username=? AND pass=?");
                    p.setString(1, uname);
                    p.setString(2, pwd);
                    ResultSet rs = p.executeQuery();

                    if (rs.next()) {
                        JOptionPane.showMessageDialog(f, "Login Successful");
                        f.dispose();
                      Login lo=new Login();  
                       lo.newpage();
                    } else {
                        JOptionPane.showMessageDialog(f, "Invalid username or password");
                    }

                } catch (Exception ex) {
                    JOptionPane.showMessageDialog(f, "Database Error");
                }
            }
        });

        Button b1 = new Button("Sign in");
        b1.setBackground(Color.RED);
        b1.setFont(new Font("italic", Font.BOLD, 40));
        b1.setBounds(630, 600, 250, 50);
        f.add(b1);

        b1.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String uname = t.getText();
                String pwd = new String(t1.getPassword());

                try {
                    Connection c = DriverManager.getConnection(url, user, pass);
                    PreparedStatement p = c.prepareStatement(
                            "INSERT INTO detail(username, pass) VALUES(?, ?)");
                    p.setString(1, uname);
                    p.setString(2, pwd);
                    p.executeUpdate();

                    JOptionPane.showMessageDialog(f, "Account created successfully");

                } catch (Exception ex) {
                    JOptionPane.showMessageDialog(f, "Error creating account");
                }
            }
        });

        f.setSize(1500, 900);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }

   
	public static void main(String[] args){
		homepage();
	}}